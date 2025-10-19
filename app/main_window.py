import asyncio
import tempfile
import json
import os
import shutil
import signal
import subprocess
import threading
import types
import sys

from PySide6.QtCore import QFileInfo, QMimeData, QPoint, QSettings, QSize, QTimer, QUrl, Qt
from PySide6.QtGui import QAction, QCloseEvent, QColorConstants, QCursor, QDesktopServices, QDrag, QDragEnterEvent, QIcon, QKeySequence, QPainter, QPixmap, QShortcut
from PySide6.QtWidgets import QApplication, QCheckBox, QDialog, QFileDialog, QFileIconProvider, QHBoxLayout, QInputDialog, QLabel, QMainWindow, QMenu, QMessageBox, QProgressBar, QPushButton, QSizePolicy, QSlider, QSpacerItem, QSystemTrayIcon, QTreeWidgetItem, QWidget
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from app.new_remote_window import NewRemoteWindow
from app.new_serve_window import NewServeWindow
from app.rclone import Rclone
from app.settings_window import SettingsWindow
from app.about_window import AboutWindow
from app.views import main_window

rc = Rclone()


class FileMonitorHandler(FileSystemEventHandler):
    def __init__(self, window, target_file: str):
        super().__init__()
        self.target_file = target_file
        self.window = window

    def on_created(self, event):
        if os.path.basename(event.src_path) == os.path.basename(self.target_file):
            self.window.download_path = event.src_path[:-
                                                       len(os.path.basename(self.target_file)) - 1]
            while True:
                try:
                    os.remove(event.src_path)
                    break
                except PermissionError:
                    pass
                except FileNotFoundError:
                    break


class Task(QMainWindow):
    last_index = 0

    def __init__(self, operation: str, source: str = '', destination: str = '', process: subprocess.Popen = None):
        self.operation = operation
        self.source = source
        self.destination = destination
        self.status = 'Running'
        self.size = ''
        self.full_size = 0
        self.progress = 0
        self.speed = ''
        self.estimated = ''
        self.process = process

        match operation:
            case 'Download' | 'Upload' | 'Opening':
                self.index = Task.last_index
                Task.last_index += 1
            case _:
                self.index = -1

    def stop(self):
        if os.name == 'nt':
            self.process.send_signal(signal.CTRL_BREAK_EVENT)
        else:
            self.process.terminate()

    def done(self):
        self.status = 'Done'
        self.progress = 100
        self.speed = '-'
        self.estimated = '-'

    def error(self):
        self.status = 'Error'

    def set_full_size(self, size: float):
        self.full_size = size

    def set_size(self, size: float):
        sizes = [self.tr('B'), self.tr('KB'), self.tr(
            'MB'), self.tr('GB'), self.tr('TB')]
        index = 0
        full_size = self.full_size

        for _ in range(4):
            if full_size >= 1024 or full_size == 0 and size >= 1024:
                full_size = round(float(full_size) / 1024, 2)
                size = round(float(size) / 1024, 2)
                index += 1

        if full_size > 0:
            self.size = f'{size} / {full_size} {sizes[index]}'
        else:
            self.size = f'{size} {sizes[index]}'

        if full_size != 0:
            self.progress = round((size / full_size) * 100)
        else:
            self.progress = 0

    def set_speed(self, speed: float):
        sizes = [self.tr('B/s'), self.tr('KB/s'), self.tr('MB/s'),
                 self.tr('GB/s'), self.tr('TB/s')]
        index = 0

        for _ in range(4):
            if speed >= 1024:
                speed = speed / 1024
                index += 1

        self.speed = f'{round(speed, 2)} {sizes[index]}'

    def set_estimated(self, estimated: str):
        self.estimated = estimated


class Serve():
    def __init__(self, protocol: str, path: str, address: str, user: str, password: str, read_only: bool, args: str, process: subprocess.Popen = None):
        self.protocol = protocol
        self.path = path
        self.address = address
        self.user = user
        self.password = password
        self.read_only = read_only
        self.process = process
        self.args = args

    def stop(self):
        if os.name == 'nt':
            self.process.send_signal(signal.CTRL_BREAK_EVENT)
        else:
            self.process.terminate()


class Process():
    def __init__(self, process: subprocess.Popen, data=None):
        self.process = process
        self.data = data

    def stop(self):
        if os.name == 'nt':
            self.process.send_signal(signal.CTRL_BREAK_EVENT)
        else:
            self.process.terminate()


class Mount():
    def __init__(self, remote: str, mount_point: str, process: subprocess.Popen = None):
        self.remote = remote
        self.mount_point = mount_point
        self.process = process

    def stop(self):
        if os.name == 'nt':
            self.process.send_signal(signal.CTRL_BREAK_EVENT)
        else:
            self.process.terminate()


class MainWindow(QMainWindow):
    download_path: str = ''
    remotes_paths = {}
    files: list = []
    current_remote: str = ''
    temp_dir: str = ''
    tree: list = []
    cache: dict = {}
    tasks: list[Task] = []
    scale: int
    copy_files: list = []
    history: dict = {}
    serve: list[Serve] = []
    mount: list[Mount] = []
    processes: list[Process] = []
    settings = QSettings('Rclone Navigator', 'Rclone Navigator')

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = main_window.Ui_MainWindow()
        self.ui.setupUi(self)

        self.search_process_is_running: int = 0

        self.setWindowIcon(
            QIcon(os.path.dirname(__file__) + '/resources/' + 'favicon.ico'))

        self.ui.treeWidget_files.header().resizeSection(0, 300)
        self.ui.treeWidget_files.header().resizeSection(1, 80)
        self.ui.treeWidget_files.header().resizeSection(2, 120)
        self.ui.treeWidget_search.header().resizeSection(0, 300)
        self.ui.treeWidget_search.header().resizeSection(1, 80)
        self.ui.treeWidget_search.header().resizeSection(2, 120)

        self.ui.treeWidget_files.header().setSortIndicator(0, Qt.SortOrder.AscendingOrder)
        self.ui.treeWidget_remotes.header().setSortIndicator(
            0, Qt.SortOrder.AscendingOrder)
        self.ui.treeWidget_remotes.setIconSize(QSize(28, 28))
        self.ui.dock_tasks.hide()
        self.ui.lineEdit_input_path.hide()

        if QApplication.style().name().lower() == 'windows11':
            self.ui.path_list_frame.setStyleSheet(
                'QPushButton {background-color: rgba(255, 255, 255, 0);font-weight: bold;}QLabel {font-weight: bold;}')

        def close():
            self.hide()
            self.close()

        self.ui.action_exit.triggered.connect(close)
        self.ui.action_new_remote.triggered.connect(
            self.open_new_remote_window)
        self.ui.action_new_serve.triggered.connect(self.open_new_serve_window)
        self.ui.action_list_remotes.triggered.connect(self.open_list_remotes)
        self.ui.action_settings.triggered.connect(self.open_settings_window)
        self.ui.action_about_qt.triggered.connect(
            lambda: QMessageBox.aboutQt(self))
        self.ui.action_about.triggered.connect(lambda: AboutWindow().exec())
        self.ui.action_show_tasks.triggered.connect(self.ui.dock_tasks.show)
        self.ui.action_config_rclone.triggered.connect(self.open_terminal)

        self.ui.treeWidget_remotes.itemClicked.connect(self.open_remote)
        self.ui.treeWidget_files.itemDoubleClicked.connect(
            lambda item: self.open_item(item.data(0, Qt.ItemDataRole.UserRole)['remote'], item.data(0, Qt.ItemDataRole.UserRole)['path'], item.data(0, Qt.ItemDataRole.UserRole)['name'], item.data(0, Qt.ItemDataRole.UserRole)['is_dir']))
        self.ui.treeWidget_search.itemDoubleClicked.connect(
            lambda item: self.open_item(item.data(0, Qt.ItemDataRole.UserRole)['remote'], item.data(0, Qt.ItemDataRole.UserRole)['path'], item.data(0, Qt.ItemDataRole.UserRole)['name'], item.data(0, Qt.ItemDataRole.UserRole)['is_dir']))
        self.ui.treeWidget_tasks.itemDoubleClicked.connect(self.open_task_dir)

        self.ui.button_exit_dir.clicked.connect(self.exit_folder)
        self.ui.button_update.clicked.connect(lambda: asyncio.ensure_future(
            self.update_dir(self.current_remote, self.remotes_paths.setdefault(self.current_remote, ''))))
        self.ui.button_prev_history.clicked.connect(self.prev_history)
        self.ui.button_next_history.clicked.connect(self.next_history)
        self.ui.button_new_serve.clicked.connect(self.open_new_serve_window)
        self.ui.button_search.clicked.connect(
            lambda: asyncio.ensure_future(self.search()))
        self.ui.lineEdit_search.editingFinished.connect(
            lambda: asyncio.ensure_future(self.search()))
        self.ui.button_mount.clicked.connect(lambda: self.mount_remote(
            self.ui.comboBox_remote.currentText(), type=self.ui.comboBox_remote.currentData(Qt.ItemDataRole.UserRole), mount_point=self.ui.comboBox_mount_point.currentText()))
        self.ui.pushButton_input_path.clicked.connect(self.start_input_path)
        self.ui.pushButton_explorer_search.clicked.connect(self.click_search)
        self.ui.lineEdit_input_path.editingFinished.connect(
            self.enter_input_path)

        if os.name == "nt":
            self.ui.toolButton_mount_point.hide()
        else:
            self.ui.toolButton_mount_point.clicked.connect(self.mount_point)

        self.ui.treeWidget_files.startDrag = self.start_drag
        self.ui.treeWidget_search.startDrag = self.start_drag

        self.ui.treeWidget_files.customContextMenuRequested.connect(
            self.show_context_menu_tree)
        self.ui.treeWidget_search.customContextMenuRequested.connect(
            self.show_context_menu_tree_search)
        self.ui.treeWidget_remotes.customContextMenuRequested.connect(
            self.show_context_menu_remote)
        self.ui.treeWidget_serve.customContextMenuRequested.connect(
            self.show_context_menu_serve)
        self.ui.treeWidget_mount.customContextMenuRequested.connect(
            self.show_context_menu_mount)
        self.ui.treeWidget_tasks.customContextMenuRequested.connect(
            self.show_context_menu_task)

        statusbar_widget = QWidget()
        h_layout = QHBoxLayout(statusbar_widget)
        h_layout.setContentsMargins(0, 0, 9, 0)

        self.slider_scale: QSlider = QSlider(statusbar_widget)
        self.slider_scale.setFixedWidth(128)
        self.slider_scale.setMinimum(0)
        self.slider_scale.setMaximum(16)
        self.slider_scale.setValue(2)
        self.slider_scale.setOrientation(Qt.Orientation.Horizontal)
        self.slider_scale.valueChanged.connect(self.set_scale)

        self.layout_free_size = QLabel('', statusbar_widget)
        h_layout.addItem(QSpacerItem(
            0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        h_layout.addWidget(self.layout_free_size)
        h_layout.addWidget(QLabel(self.tr('Scale') + ':', statusbar_widget))
        h_layout.addWidget(self.slider_scale)
        self.ui.statusbar.addPermanentWidget(statusbar_widget)

        self.timer = QTimer(interval=500)
        self.timer.timeout.connect(self.timer_update)
        self.timer.start()

        if os.name == 'nt':
            self.timer_drive_check = QTimer(interval=5000)
            self.timer_drive_check.timeout.connect(self.check_free_drives)
            self.timer_drive_check.start()

        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(self.windowIcon())
        self.tray_icon.setContextMenu(self.context_menu_tray_icon())
        self.tray_icon.activated.connect(self.tray_icon_activated)
        self.tray_icon.show()

        self.ui.splitter_serve.setSizes([500, 100])
        self.ui.splitter_mount.setSizes([500, 100])

        self.shortcuts()
        self.recovery_ui()
        if rc.rclone == None:
            QMessageBox.critical(self, self.tr('This program requires the rclone library'), self.tr('System Requirements\nTo function correctly, this application depends on rclone. Please ensure that rclone is installed and configured on your computer before running the program.\n\nInstallation Instructions:\n1) Visit the official rclone website: https://rclone.org/downloads/\n2) Download and install the version for your operating system (Windows, macOS, Linux).'))
            self.close()
        self.update_remotes()
        QTimer.singleShot(1, self.recovery_mount)
        QTimer.singleShot(1, self.recovery_serve)

        if os.name == 'nt':
            self.check_free_drives()
        else:
            self.start_file_monitor()

    def tray_icon_activated(self, reason: QSystemTrayIcon.ActivationReason):
        match reason:
            case QSystemTrayIcon.ActivationReason.Trigger:
                self.show()
                self.activateWindow()

    def timer_update(self):
        if self.download_path != '':
            self.download_file(self.copy_files, self.download_path)
            self.download_path = ''

        for i in range(len(self.tasks)):
            if i >= self.ui.treeWidget_tasks.topLevelItemCount():
                item = QTreeWidgetItem()
                match self.tasks[i].operation:
                    case 'Download':
                        item.setIcon(0, QIcon.fromTheme('emblem-downloads'))
                    case 'Upload':
                        item.setIcon(0, QIcon.fromTheme('go-up'))
                    case 'Opening':
                        item.setIcon(0, QIcon.fromTheme('document-open'))
                    case 'Mount':
                        item.setIcon(0, QIcon.fromTheme('drive-harddisk'))
                    case 'Delete':
                        item.setIcon(0, QIcon.fromTheme('edit-delete'))
                self.ui.treeWidget_tasks.addTopLevelItem(item)
                self.ui.dock_tasks.show()
            else:
                item = self.ui.treeWidget_tasks.topLevelItem(i)

            match self.tasks[i].operation:
                case 'Download':
                    item.setText(0, self.tr('Download', 'noun'))
                case 'Upload':
                    item.setText(0, self.tr('Upload'))
                case 'Opening':
                    item.setText(0, self.tr('Opening'))
                case 'Delete':
                    item.setText(0, self.tr('Delete'))
                case _:
                    item.setText(0, self.tasks[i].operation)

            item.setText(1, self.tasks[i].source)
            item.setText(2, self.tasks[i].destination)

            match self.tasks[i].status:
                case 'Done':
                    item.setText(3, self.tr('Done'))
                case 'Running':
                    item.setText(3, self.tr('Running'))
                case 'Error':
                    item.setText(3, self.tr('Error'))
                case _:
                    item.setText(3, self.tasks[i].status)

            item.setText(4, self.tasks[i].size)
            self.ui.treeWidget_tasks.setItemWidget(
                item, 5, QProgressBar(value=self.tasks[i].progress))
            item.setText(6, self.tasks[i].speed)
            item.setText(7, self.tasks[i].estimated)

    def closeEvent(self, event: QCloseEvent):
        settings = QSettings('Rclone Navigator', 'Rclone Navigator')
        if self.isVisible() and str(settings.value('minimize_to_tray', False)) in ['true', 'True']:
            event.ignore()
            self.hide()
        else:
            if self.temp_dir != '':
                shutil.rmtree(self.temp_dir)
            event.accept()
            for serve in self.serve:
                serve.stop()
            for mount in self.mount:
                mount.stop()
            for process in self.processes:
                process.stop()
            for task in self.tasks:
                if task.process is not None:
                    task.stop()
            try:
                for observer in self.observers:
                    observer.stop()
            except AttributeError:
                pass
            if os.name == 'nt':
                os._exit(0)
            else:
                sys.exit(0)

    def start_file_monitor(self):
        if self.temp_dir == '':
            self.temp_dir = tempfile.mkdtemp(prefix='rclone_explorer_')
        open(self.temp_dir + os.sep + '.rclone_explorer_file_temp', 'a').close()

        handler = FileMonitorHandler(self, '.rclone_explorer_file_temp')

        if os.name == 'nt':
            self.observers = []

            for drive in self.drives:
                observer = Observer()
                observer.schedule(handler, drive + '\\', recursive=True)
                try:
                    observer.start()
                    self.observers.append(observer)
                except PermissionError:
                    pass
        else:
            observer = Observer()
            observer.schedule(handler, os.path.expanduser('~'), recursive=True)
            observer_thread = threading.Thread(target=observer.start)
            observer_thread.daemon = True
            observer_thread.start()

    def check_free_drives(self):
        if os.name == 'nt':
            all_drives = set(d + ':' for d in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
            occupied_drives = [
                d + ':' for d in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if os.path.exists(d + ':')]
            try:
                self.drives
            except AttributeError:
                self.drives = []
            if occupied_drives != self.drives:
                try:
                    for observer in self.observers:
                        observer.stop()
                except AttributeError:
                    pass
                self.drives = occupied_drives
                self.start_file_monitor()
                free_drives = sorted(
                    all_drives - set(occupied_drives), reverse=True)
                self.ui.comboBox_mount_point.clear()
                self.ui.comboBox_mount_point.addItems(free_drives)

    async def search(self):
        remote_name = self.ui.comboBox_search.currentText()
        text = self.ui.lineEdit_search.text()

        self.search_process_is_running += 1
        search_process_is_running = self.search_process_is_running

        self.ui.statusbar.showMessage(self.tr('Search in') + ' ' + remote_name)
        self.ui.treeWidget_search.clear()
        process = rc.search(remote_name, 20)

        loop = asyncio.get_running_loop()

        while True:
            line = await loop.run_in_executor(None, process.stdout.readline)
            if not line or search_process_is_running != self.search_process_is_running:
                break
            line = line.decode()

            if len(line) > 10:
                line = json.loads(line.replace(',\n', ''))
                sizes = [self.tr('B'), self.tr('KB'), self.tr(
                    'MB'), self.tr('GB'), self.tr('TB')]
                index = 0
                size = line['Size']
                name = line['Name']
                modified = line['ModTime']
                is_dir = line['IsDir']
                type = line['MimeType']
                path = remote_name + line['Path']

                if is_dir:
                    size = ''
                else:
                    for _ in range(4):
                        if size >= 1024:
                            size = round(float(size) / 1024, 2)
                            index += 1
                    size = f'{size} {sizes[index]}'

                modified = modified.replace(
                    'T', ' ').replace('Z', ' ').split('.')[0]
                file = {'name': name, 'size': size, 'modified': modified,
                        'path': path, 'is_dir': is_dir, 'type': type}

                if file['name'].lower().rfind(text.lower()) != -1:
                    item = QTreeWidgetItem(
                        [file['name'], file['size'], file['modified'], file['type'], file['path']])
                    item.setTextAlignment(
                        1, Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignCenter)
                    item.setSizeHint(0, QSize(0, self.scale))

                    if file['is_dir']:
                        icon = QFileIconProvider().icon(QFileIconProvider().IconType.Folder)
                        item.setIcon(0, icon)
                    else:
                        file_info = QFileInfo(file['name'])
                        icon = QFileIconProvider().icon(file_info)
                        if icon.isNull():
                            file_info = QFileInfo('file')
                            icon = QFileIconProvider().icon(file_info)
                        item.setIcon(0, icon)
                    item.setData(0, Qt.ItemDataRole.UserRole, {
                                 'name': file['name'], 'remote': remote_name, 'path': line['Path'], 'is_dir': file['is_dir']})
                    self.ui.treeWidget_search.addTopLevelItem(item)

        if search_process_is_running == self.search_process_is_running:
            self.ui.statusbar.showMessage('')

    async def update_free_size(self, remote_name: str, clear: bool = False):
        if clear:
            self.layout_free_size.setText('')
        process = rc.about(remote_name)
        self.processes.append(Process(process))
        loop = asyncio.get_running_loop()
        size, error = await loop.run_in_executor(None, process.communicate)
        if error:
            print(error)

        if size:
            size = json.loads(size)
            free = size.get('free', None)
            total = size.get('total', None)

            sizes = [self.tr('B'), self.tr('KB'), self.tr(
                'MB'), self.tr('GB'), self.tr('TB')]

            index_free = 0
            if free is not None:
                for _ in range(4):
                    if free >= 1024:
                        free = round(float(free) / 1024, 2)
                        index_free += 1
                free_text = self.tr('Free') + f': {free} {sizes[index_free]}'
            else:
                free_text = ''

            if total is not None:
                index_total = 0
                for _ in range(4):
                    if total >= 1024:
                        total = round(float(total) / 1024, 2)
                        index_total += 1
                total_text = self.tr('Total') + \
                    f': {total} {sizes[index_total]}'
            else:
                total_text = ''

            if total_text != '':
                self.layout_free_size.setText(
                    f'{total_text} | {free_text}    ')
            else:
                self.layout_free_size.setText(f'{free_text}    ')

    def set_scale(self, index: int):
        sizes = [16, 20, 32, 48, 64, 80, 96, 112, 128,
                 144, 160, 176, 192, 208, 224, 240, 256]
        sizes_icon = [16, 16, 32, 48, 64, 80, 96, 112,
                      128, 144, 160, 176, 192, 208, 224, 240, 256]
        value = sizes[index]
        self.scale = value
        if index == 2 or index == 3:
            self.scale += 2
        elif index > 3:
            self.scale += 4
        self.slider_scale.setToolTip(f'{value}px')

        self.ui.treeWidget_files.setIconSize(
            QSize(sizes_icon[index], sizes_icon[index]))
        self.ui.treeWidget_search.setIconSize(
            QSize(sizes_icon[index], sizes_icon[index]))

        for i in range(self.ui.treeWidget_files.topLevelItemCount()):
            item = self.ui.treeWidget_files.topLevelItem(i)
            item.setSizeHint(0, QSize(0, self.scale))

        for i in range(self.ui.treeWidget_search.topLevelItemCount()):
            item = self.ui.treeWidget_search.topLevelItem(i)
            item.setSizeHint(0, QSize(0, self.scale))

        settings = QSettings('Rclone Navigator', 'Rclone Navigator')
        settings.setValue('scale', index)

    def recovery_ui(self):
        settings = QSettings('Rclone Navigator', 'Rclone Navigator')
        index = int(settings.value('scale', 2))
        self.set_scale(index)
        self.slider_scale.setValue(index)

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls() and event.mimeData().text() != '.rclone_explorer_file_temp':
            event.accept()

    def dropEvent(self, event):
        destination_remote = self.current_remote
        destination_path = self.remotes_paths[self.current_remote]

        for url in event.mimeData().urls():
            source_path = url.toLocalFile()
            if os.path.isfile(source_path) or os.path.isdir(source_path):
                asyncio.ensure_future(self.upload_file(
                    source_path, destination_remote, destination_path))

    def start_drag(self, supportedActions):
        match self.ui.tabWidget.currentIndex():
            case 0:
                items = self.ui.treeWidget_files.selectedItems()
                if self.ui.treeWidget_files.currentColumn() != 0:
                    return
            case 1:
                items = self.ui.treeWidget_search.selectedItems()
                if self.ui.treeWidget_search.currentColumn() != 0:
                    return

        if items is None or len(items) == 0:
            return

        self.download_path = ''

        if self.temp_dir == '':
            self.temp_dir = tempfile.mkdtemp(prefix='rclone_explorer_')
        open(self.temp_dir + os.sep + '.rclone_explorer_file_temp', 'a').close()

        mime_data = QMimeData()
        mime_data.setText('.rclone_explorer_file_temp')
        url = QUrl.fromLocalFile(
            self.temp_dir + os.sep + '.rclone_explorer_file_temp')
        mime_data.setUrls([url])

        drag: QDrag = QDrag(self)
        drag.setMimeData(mime_data)

        match len(items):
            case 1 | 2 | 3 | 4:
                icon_size = 64
                pixmap_size = 132
            case 5 | 6 | 7 | 8 | 9:
                icon_size = 48
                pixmap_size = 150
            case 10 | 11 | 12 | 13 | 14 | 15 | 16:
                icon_size = 32
                pixmap_size = 136
            case _:
                icon_size = 16
                pixmap_size = 144

        pixmap = QPixmap(QSize(pixmap_size, pixmap_size))
        pixmap.fill(QColorConstants.Transparent)
        painter = QPainter(pixmap)

        i = 0
        is_i_max = False
        j = 0
        self.copy_files = []
        for item in items:
            self.copy_files.append(item.data(0, Qt.ItemDataRole.UserRole))

            painter.drawPixmap(i, j, item.icon(
                0).pixmap(QSize(icon_size, icon_size)).scaled(icon_size, icon_size))
            if j < pixmap_size:
                i += icon_size + 2
                if i >= pixmap_size:
                    j += icon_size + 2
                    i = 0
                    is_i_max = True
        painter.end()

        if is_i_max:
            i = pixmap_size

        drag.setPixmap(pixmap)
        drag.setHotSpot(QPoint(i / 2, -9))
        drag.exec(Qt.DropAction.CopyAction)

    def start_input_path(self):
        if self.current_remote != '':
            self.ui.lineEdit_input_path.setText(
                self.current_remote + self.remotes_paths[self.current_remote])
            self.ui.scrollArea_explorer.hide()
            self.ui.lineEdit_input_path.show()
            self.ui.lineEdit_input_path.setFocus()

    def enter_input_path(self):
        is_focused = self.ui.lineEdit_input_path.hasFocus()
        self.ui.scrollArea_explorer.show()
        self.ui.lineEdit_input_path.hide()

        index = self.ui.lineEdit_input_path.text().find(':')

        if index != -1 and is_focused:
            remote_name = self.ui.lineEdit_input_path.text()[:index + 1]
            path = self.ui.lineEdit_input_path.text()[index + 1:]

            asyncio.ensure_future(self.open_dir(remote_name, path))

    def click_search(self):
        if self.current_remote != '':
            self.ui.comboBox_search.setCurrentIndex(self.ui.comboBox_search.findText(
                self.current_remote, Qt.MatchFlag.MatchCaseSensitive))
            self.ui.comboBox_search.setCurrentText(
                self.current_remote + self.remotes_paths[self.current_remote])
            self.ui.tabWidget.setCurrentIndex(1)

    def prev_history(self):
        if self.current_remote in self.history.keys():
            if self.history[self.current_remote][1] > 0:
                self.history[self.current_remote][1] -= 1
                asyncio.ensure_future(self.open_dir(
                    self.current_remote, self.history[self.current_remote][0][self.history[self.current_remote][1]]))
                self.ui.button_next_history.setEnabled(True)
            if self.history[self.current_remote][1] < 1:
                self.ui.button_prev_history.setEnabled(False)

    def next_history(self):
        if self.current_remote in self.history.keys() and self.history[self.current_remote][1] < len(self.history[self.current_remote][0]) - 1:
            self.history[self.current_remote][1] += 1
            self.ui.button_prev_history.setEnabled(True)
            if self.history[self.current_remote][1] == len(self.history[self.current_remote][0]) - 1:
                self.ui.button_next_history.setEnabled(False)
            asyncio.ensure_future(self.open_dir(
                self.current_remote, self.history[self.current_remote][0][self.history[self.current_remote][1]]))

    def update_history(self):
        if self.current_remote in self.history.keys():
            if self.history[self.current_remote][0][self.history[self.current_remote][1]] != self.remotes_paths[self.current_remote]:
                self.history[self.current_remote][1] += 1
                self.history[self.current_remote][0] = self.history[self.current_remote][0][:self.history[self.current_remote][1]]
                self.history[self.current_remote][0].append(
                    self.remotes_paths[self.current_remote])
        else:
            self.history[self.current_remote] = [
                [self.remotes_paths[self.current_remote]], 0]

        if self.history[self.current_remote][1] > 0:
            self.ui.button_prev_history.setEnabled(True)
        else:
            self.ui.button_prev_history.setEnabled(False)

        if self.history[self.current_remote][1] < len(self.history[self.current_remote][0]) - 1:
            self.ui.button_next_history.setEnabled(True)
        else:
            self.ui.button_next_history.setEnabled(False)

    def open_terminal(self):
        if os.name == 'nt':
            subprocess.Popen('start rclone config', shell=True)
        else:
            terminal_commands = {
                'gnome-terminal': ['gnome-terminal', '--', 'rclone', 'config'],
                'konsole': ['konsole', '-e', 'rclone', 'config'],
                'xterm': ['xterm', '-e', 'rclone', 'config'],
                'terminator': ['terminator', '-e', 'rclone config'],
                'xfce4-terminal': ['xfce4-terminal', '-x', 'rclone', 'config'],
                'lxterminal': ['lxterminal', '-e', 'rclone', 'config'],
                'mate-terminal': ['mate-terminal', '-x', 'rclone', 'config'],
                'tilix': ['tilix', '-e', 'rclone', 'config'],
                'kitty': ['kitty', 'rclone', 'config'],
                'alacritty': ['alacritty', '-e', 'rclone', 'config'],
                'urxvt': ['urxvt', '-e', 'rclone', 'config'],
                'termite': ['termite', '-e', 'rclone config'],
                'st': ['st', '-e', 'rclone', 'config'],
                'roxterm': ['roxterm', '-e', 'rclone config'],
                'sakura': ['sakura', '-e', 'rclone config'],
                'eterm': ['eterm', '-e', 'rclone config'],
                'deepin-terminal': ['deepin-terminal', '-e', 'rclone config'],
                'qterminal': ['qterminal', '-e', 'rclone config'],
                'terminology': ['terminology', '-e', 'rclone config'],
                'guake': ['guake', '-e', 'rclone config'],
                'tilda': ['tilda', '-e', 'rclone config'],
                'yakuake': ['yakuake', '-e', 'rclone config']
            }

            for term, cmd in terminal_commands.items():
                if shutil.which(term):
                    try:
                        subprocess.Popen(cmd)
                        print(f'Launched in: {term}')
                        break
                    except:
                        continue
                else:
                    print(f'{term} not found')

    def update_remotes(self):
        remotes = rc.listremotes(True)
        remotes.sort(key=lambda x: x['name'].lower())
        self.ui.treeWidget_remotes.clear()
        self.ui.comboBox_search.clear()
        self.ui.comboBox_remote.clear()
        settings = QSettings('Rclone Navigator', 'Rclone Navigator')
        for remote in remotes:
            item = QTreeWidgetItem([remote['name'] + ':', remote['type']])
            item.setSizeHint(0, QSize(0, 32))
            if (QApplication.styleHints().colorScheme() == Qt.ColorScheme.Light and (len(settings.value('palette', 'System')) > 4 and (settings.value('palette', 'System')[-4:].lower() != 'dark'))) or QApplication.style().name() == 'windowsvista' or (len(settings.value('palette', 'System')) > 5 and (settings.value('palette', 'System')[-5:].lower() == 'light')):
                inv = ''
            else:
                inv = '_inv'

            path = f'{os.path.dirname(__file__)}/resources/images/'

            file = path + f'{remote['type']}{inv}.png'
            if not os.path.isfile(file):
                file = path + f'unknown{inv}.png'
            item.setIcon(0, QPixmap(file))
            self.ui.treeWidget_remotes.addTopLevelItem(item)
            self.ui.comboBox_search.addItem(
                QPixmap(file), remote['name'] + ':')
            self.ui.comboBox_remote.addItem(
                QPixmap(file), remote['name'] + ':', remote['type'])

    async def upload_file(self, source_path: str, destination_remote: str, destination_path: str):
        destination_path_original = destination_path
        is_dir = await rc.is_dir(source_path)
        if is_dir:
            base_name = os.path.basename(source_path).split(':')[-1]
            if len(destination_path) > 0 and destination_path[-1] != '/':
                destination_path += f'/{base_name}'
            else:
                destination_path += f'{base_name}'

        process = rc.copy(
            source_path, f'{destination_remote}{destination_path}')
        task = Task(operation='Upload', source=source_path,
                    destination=f'{destination_remote}{destination_path_original}', process=process)
        self.tasks.append(task)

        await self.copy(task)
        await self.update_dir(destination_remote, destination_path_original)
        if destination_remote == self.current_remote:
            await self.update_free_size(destination_remote)

    async def copy(self, task: Task):
        loop = asyncio.get_running_loop()

        while True:
            line = await loop.run_in_executor(None, task.process.stdout.readline)
            if not line:
                break
            line = line.decode()

            s: str = line
            if 'ETA' in s:
                s = s.split('Transferred:')[1]
                s = s.strip()
                s = s.replace(',', '')
                # print(s)  # 66.996 MiB / 81.884 MiB 82% 5.003 MiB/s ETA 2s
                current_size = float(s.split(' ')[0])
                size_unit = s.split(' ')[1]
                full_size = float(s.split(' ')[3])
                size_unit_full_size = s.split(' ')[4]
                speed = float(s.split(' ')[6])
                size_unit_speed = s.split(' ')[7]
                estimated = s.split(' ')[9]

                match size_unit:
                    case 'KiB':
                        current_size *= 1024
                    case 'MiB':
                        current_size *= 1048576
                    case 'GiB':
                        current_size *= 1073741824
                    case 'TiB':
                        current_size *= 1099511627776

                match size_unit_full_size:
                    case 'KiB':
                        full_size *= 1024
                    case 'MiB':
                        full_size *= 1048576
                    case 'GiB':
                        full_size *= 1073741824
                    case 'TiB':
                        full_size *= 1099511627776

                match size_unit_speed:
                    case 'KiB/s':
                        speed *= 1024
                    case 'MiB/s':
                        speed *= 1048576
                    case 'GiB/s':
                        speed *= 1073741824
                    case 'TiB/s':
                        speed *= 1099511627776

                task.set_size(current_size)
                task.set_full_size(full_size)
                task.set_speed(speed)
                task.set_estimated(estimated)
                if full_size != 0 and current_size == full_size:
                    break

        out, error = task.process.communicate()
        if not error:
            task.done()
        elif error.decode() != '^C':
            task.error()
            self.error_output(
                self.tr('An error occurred when copying a file or directory'), error.decode())

    def error_output(self, message: str, error: str = None):
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.setWindowTitle(self.tr('Error'))
        msg_box.setText(message)
        if error:
            msg_box.setDetailedText(error)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.show()

    def notice_output(self, message: str, text: str = None):
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle(self.tr('Notice'))
        msg_box.setText(message)
        if text:
            msg_box.setDetailedText(text)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.show()

    def open_new_remote_window(self):
        open_win = NewRemoteWindow()
        open_win.exec()
        self.update_remotes()

    def open_new_serve_window(self):
        open_win = NewServeWindow(self)
        open_win.exec()

    def open_list_remotes(self):
        self.ui.treeWidget_remotes.setVisible(
            not self.ui.treeWidget_remotes.isVisible())

    def open_settings_window(self):
        open_win = SettingsWindow()
        open_win.exec()

    def clear_cache(self, remote_name: str, path: str):
        if remote_name in self.cache and path in self.cache[remote_name]:
            del self.cache[remote_name][path]

    async def open_dir(self, remote_name: str, path_dir: str = '', update=False):
        self.current_remote = remote_name
        self.remotes_paths[remote_name] = path_dir

        self.update_history()

        if path_dir != '':
            self.ui.button_exit_dir.setEnabled(True)
        else:
            self.ui.button_exit_dir.setEnabled(False)

        for i in range(self.ui.path_list.count()):
            self.ui.path_list.itemAt(i).widget().deleteLater()

        button = QPushButton(remote_name[:-1])
        button.setSizePolicy(QSizePolicy.Policy.Fixed,
                             QSizePolicy.Policy.Expanding)
        button.setFlat(True)
        button.setIcon(self.ui.treeWidget_remotes.findItems(
            remote_name, Qt.MatchFlag.MatchCaseSensitive)[0].icon(0))
        button.clicked.connect(lambda t, remote_name=remote_name: asyncio.ensure_future(
            self.open_dir(remote_name)))
        self.ui.path_list.addWidget(button)
        arrow_label = QLabel(':')
        arrow_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ui.path_list.addWidget(arrow_label)

        temp_path = ''
        count = 0
        for name in path_dir.split('/'):
            count += 1
            temp_path += name + '/'
            if name != '' or count > 1:
                if count > 1:
                    arrow_label = QLabel('/')
                    arrow_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    self.ui.path_list.addWidget(arrow_label)
                button = QPushButton(name)
                button.setSizePolicy(
                    QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
                button.setFlat(True)
                button.clicked.connect(
                    lambda t, a=self.current_remote, b=temp_path[:-1]: asyncio.ensure_future(self.open_dir(a, b)))
                self.ui.path_list.addWidget(button)

        if update:
            self.ui.statusbar.showMessage(
                self.tr('Updating') + ' ' + remote_name + path_dir)
            depth = 1
        else:
            self.ui.statusbar.showMessage(
                self.tr('Opening') + ' ' + remote_name + path_dir)
            depth = int(self.settings.value('path_depth', 1))
            
        if not update:
            depth = int(self.settings.value('path_depth', 1))
        
        while True:
            if remote_name in self.cache and path_dir in self.cache[remote_name] and not update:
                tree = self.cache[remote_name][path_dir]
                update = True
                self.ui.statusbar.showMessage(
                    self.tr('Updating') + ' ' + remote_name + path_dir)
            else:
                if not update:
                    self.ui.treeWidget_files.clear()
                update = False
                process = rc.lsjson(f'{remote_name}{path_dir}', depth)
                self.processes.append(Process(process, remote_name + path_dir))
                loop = asyncio.get_running_loop()
                tree_rclone, error = await loop.run_in_executor(None, process.communicate)
                tree_rclone = json.loads(tree_rclone)
                if error:
                    print(error.decode())
                self.ui.statusbar.showMessage('')

                tree = []
                directories = {}
                for i in range(len(tree_rclone)):
                    sizes = [self.tr('B'), self.tr('KB'), self.tr(
                        'MB'), self.tr('GB'), self.tr('TB')]
                    index = 0
                    size = tree_rclone[i]['Size']
                    name = tree_rclone[i]['Name']
                    modified = tree_rclone[i]['ModTime']
                    is_dir = tree_rclone[i]['IsDir']
                    type_file = tree_rclone[i]['MimeType']
                    path = tree_rclone[i]['Path']

                    if is_dir:
                        size = ''
                    else:
                        for _ in range(4):
                            if size >= 1024:
                                size = round(float(size) / 1024, 2)
                                index += 1
                        size = f'{size} {sizes[index]}'

                    is_depth_1 = len(path.split('/')) == 1
                    if path_dir != '' and path_dir[-1] != '/':
                        path = path_dir + '/' + tree_rclone[i]['Path']
                    else:
                        path = path_dir + tree_rclone[i]['Path']
                    if is_depth_1:
                        modified = modified.replace(
                            'T', ' ').replace('Z', ' ').split('.')[0]
                        tree.append({'name': name, 'size': size, 'modified': modified,
                                    'path': path, 'is_dir': is_dir, 'type': type_file})
                    else:
                        path_directory = path[:path.rindex('/')]
                        if path_directory in directories:
                            directories[path_directory].append({'name': name, 'size': size, 'modified': modified,
                                                                'path': path, 'is_dir': is_dir, 'type': type_file})
                        else:
                            directories[path_directory] = [{'name': name, 'size': size, 'modified': modified,
                                                            'path': path, 'is_dir': is_dir, 'type': type_file}]

                for path, tree_path in directories.items():
                    if remote_name in self.cache:
                        self.cache[remote_name][path] = tree_path
                    else:
                        self.cache[remote_name] = {path: tree_path}

                if remote_name in self.cache:
                    self.cache[remote_name][path_dir] = tree
                else:
                    self.cache[remote_name] = {path_dir: tree}

            if f'{self.current_remote}{self.remotes_paths[self.current_remote]}' == f'{remote_name}{path_dir}':
                def lt(self, other_item) -> bool:
                    column = self.treeWidget().sortColumn()
                    if self.text(3) == 'inode/directory' and other_item.text(3) != 'inode/directory':
                        return True
                    elif other_item.text(3) == 'inode/directory' and self.text(3) != 'inode/directory':
                        return False
                    return self.text(column).lower() < other_item.text(column).lower()

                self.ui.treeWidget_files.clear()
                for file in tree:
                    item = QTreeWidgetItem(
                        [file['name'], file['size'], file['modified'], file['type']])
                    item.setTextAlignment(
                        1, Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignCenter)
                    item.setSizeHint(0, QSize(0, self.scale))
                    item.__lt__ = types.MethodType(lt, item)

                    if file['is_dir']:
                        icon = QFileIconProvider().icon(QFileIconProvider().IconType.Folder)
                        item.setIcon(0, icon)
                    else:
                        file_info = QFileInfo(file['name'])
                        icon = QFileIconProvider().icon(file_info)
                        if icon.isNull():
                            file_info = QFileInfo('file')
                            icon = QFileIconProvider().icon(file_info)
                        item.setIcon(0, icon)
                    item.setData(0, Qt.ItemDataRole.UserRole, {
                                 'name': file['name'], 'remote': remote_name, 'path': file['path'], 'is_dir': file['is_dir']})
                    self.ui.treeWidget_files.addTopLevelItem(item)

            if not update:
                break

    def open_remote(self, item: QTreeWidgetItem):
        for i in range(self.ui.path_list.count()):
            self.ui.path_list.itemAt(i).widget().deleteLater()
        if item.text(0) not in self.remotes_paths.keys():
            self.remotes_paths[item.text(0)] = ''
        asyncio.ensure_future(self.open_dir(
            item.text(0), self.remotes_paths[item.text(0)]))
        asyncio.ensure_future(self.update_free_size(item.text(0), True))

    async def open_file(self, remote: str, file_path: str, file_name: str, is_with: bool = False):
        if self.temp_dir == '':
            self.temp_dir = tempfile.mkdtemp(prefix='rclone_explorer_')
        process = rc.copy(remote + file_path, self.temp_dir)
        task = Task(operation='Opening', source=remote + file_path,
                    destination=self.temp_dir, process=process)
        self.tasks.append(task)
        await self.copy(task)

        if not is_with:
            QDesktopServices.openUrl(QUrl.fromLocalFile(
                self.temp_dir + '/' + file_name))
        else:
            if os.name == 'nt':
                subprocess.run(
                    ['rundll32', 'shell32.dll,OpenAs_RunDLL', self.temp_dir + '\\' + file_name])
            else:
                QDesktopServices.openUrl(QUrl.fromLocalFile(
                    self.temp_dir + '/' + file_name))

    def open_item(self, remote: str, file_path: str, file_name: str, is_dir: bool, is_with: bool = False):
        if remote:
            if is_dir:
                asyncio.ensure_future(self.open_dir(
                    remote, file_path))
            else:
                asyncio.ensure_future(self.open_file(
                    remote, file_path, file_name, is_with))

    def download_file(self, list_files: list[dict], download_path: str = None):
        if download_path is None:
            download_path = QFileDialog.getExistingDirectory()
        if download_path is not None and download_path != '':
            for file in list_files:
                base_name = file.get(
                    'name', file['path'].split(':')[-1].split('/')[-1])
                file_path = file['path']
                source_remote = file['remote']

                if not file['is_dir']:
                    process = rc.copy(source_remote + file_path, download_path)
                else:
                    if len(download_path) > 0 and download_path[-1] != '/' and download_path[-1] != '\\':
                        process = rc.copy(
                            f'{source_remote}{file_path}', f'{download_path}/{base_name}')
                    else:
                        process = rc.copy(
                            f'{source_remote}{file_path}', f'{download_path}{base_name}')

                task = Task(
                    operation='Download', source=f'{source_remote}{file_path}', destination=download_path, process=process)
                self.tasks.append(task)
                asyncio.ensure_future(self.copy(task))

    def mount_point(self):
        path = QFileDialog.getExistingDirectory()
        if path is not None and path != '':
            self.ui.comboBox_mount_point.setCurrentText(path)

    def mount_remote(self, remote: str, type: str = '', mount_point: str = '', is_remember: bool = False):
        remote = remote.strip()
        mount_point = mount_point.strip()
        i = 0
        while i < len(self.mount):
            if self.mount[i].remote == remote or self.mount[i].mount_point == mount_point and mount_point not in ['', '*']:
                self.mount[i].stop()
                del self.mount[i]
                items = self.ui.treeWidget_mount.findItems(
                    remote, Qt.MatchFlag.MatchCaseSensitive) + self.ui.treeWidget_mount.findItems(mount_point, Qt.MatchFlag.MatchCaseSensitive, 2)
                for item in items:
                    self.remember_mount(Qt.CheckState.Unchecked, item.text(0))
                    self.ui.treeWidget_mount.takeTopLevelItem(
                        self.ui.treeWidget_mount.indexOfTopLevelItem(item))
            else:
                i += 1

        if os.name == 'nt':
            if mount_point.strip() == '':
                mount_point = '*'
            if type in ['local', 'alias']:
                process = rc.mount(remote, mount_point, '--links')
            else:
                process = rc.mount(remote, mount_point,
                                   '--network-mode --links')
        else:
            if mount_point.strip() == '':
                mount_point = f'{os.path.expanduser('~')}/Clouds/{remote.split(':')[0]}'
                if not os.path.isdir(f'{os.path.expanduser('~')}/Clouds'):
                    os.mkdir(f'{os.path.expanduser('~')}/Clouds')
                if not os.path.isdir(mount_point):
                    os.mkdir(mount_point)

            process = rc.mount(remote, mount_point)

        self.mount.append(Mount(remote, mount_point, process=process))
        item = QTreeWidgetItem([remote, type, mount_point])
        self.ui.treeWidget_mount.addTopLevelItem(item)
        checkbox = QCheckBox()
        checkbox.setChecked(is_remember)
        checkbox.checkStateChanged.connect(lambda check_state, remote=remote, type=type,
                                           mount_point=mount_point: self.remember_mount(check_state, remote, type, mount_point))
        self.ui.treeWidget_mount.setItemWidget(item, 3, checkbox)
        asyncio.ensure_future(self.check_process(
            process, 'mount', text=f'{remote} {type} {mount_point}'))

    def remember_mount(self, check_state: Qt.CheckState, remote: str, type: str = '', mount_point: str = ''):
        settings = QSettings('Rclone Navigator', 'Rclone Navigator')
        mount: dict = settings.value('mount', {})
        if check_state == Qt.CheckState.Checked:
            mount[remote] = {'remote': remote,
                             'type': type, 'mount_point': mount_point}
        else:
            mount.pop(remote, None)
        settings.setValue('mount', mount)

    def recovery_mount(self):
        settings = QSettings('Rclone Navigator', 'Rclone Navigator')
        mount: dict = settings.value('mount', {})
        for key, value in mount.items():
            self.mount_remote(key, value['type'], value['mount_point'], True)

    def create_serve(self, protocol: str, path: str, user: str, password: str, address: str, read_only: bool = False, args: str = '', is_remember: bool = False):
        if protocol == 'sftp' and not (user and password):
            if (not user or not password) and '--no-auth' not in args:
                args += ' --no-auth'
        args = args.strip().replace('  ', ' ')
        process: subprocess.Popen = rc.serve(
            protocol, path, user, password, address, read_only, args)

        self.serve.append(Serve(protocol, path, address, user,
                          password, read_only, args, process=process))
        item = QTreeWidgetItem(
            [protocol, path, address, user, password, '+' if read_only else '-'])
        self.ui.treeWidget_serve.addTopLevelItem(item)
        checkbox = QCheckBox()
        checkbox.setChecked(is_remember)
        checkbox.checkStateChanged.connect(lambda check_state, protocol=protocol, path=path, address=address, user=user, password=password,
                                           read_only=read_only: self.remember_serve(check_state, protocol, path, user, password, address, read_only, args))
        self.ui.treeWidget_serve.setItemWidget(item, 6, checkbox)
        asyncio.ensure_future(self.check_process(process, 'serve', text=f'{protocol} {path}'.strip(
        ) + '\n' + self.tr('An error occurred while the serve was running')))

    def remember_serve(self, check_state: Qt.CheckState, protocol: str, path: str, user: str, password: str = '', address: str = '', read_only: bool = False, args: str = ''):
        settings = QSettings('Rclone Navigator', 'Rclone Navigator')
        serve: dict = settings.value('serve', {})
        if check_state == Qt.CheckState.Checked:
            serve[protocol + path + user] = {'protocol': protocol, 'path': path,
                                             'user': user, 'password': password, 'address': address, 'read_only': read_only, 'args': args}
        else:
            serve.pop(protocol + path + user, None)
        settings.setValue('serve', serve)

    def recovery_serve(self):
        settings = QSettings('Rclone Navigator', 'Rclone Navigator')
        serve: dict = settings.value('serve', {})
        for value in serve.values():
            self.create_serve(value['protocol'], value['path'], value['user'],
                              value['password'], value['address'], read_only=value['read_only'], args=value['args'], is_remember=True)

    async def check_process(self, process: subprocess.Popen, type: str, text: str = '', is_stderr: bool = True):
        loop = asyncio.get_running_loop()
        while True:
            if is_stderr:
                output = await loop.run_in_executor(None, process.stderr.readline)
            else:
                output = await loop.run_in_executor(None, process.stdout.readline)
            if output and output.decode() != '^C':
                if type == 'mount':
                    scrollbar = self.ui.plainTextEdit_mount.verticalScrollBar()
                    is_bottom = scrollbar.value() == scrollbar.maximum()
                    self.ui.plainTextEdit_mount.appendPlainText(
                        output.decode().strip())
                    if is_bottom:
                        scrollbar.setValue(scrollbar.maximum())
                elif type == 'serve':
                    scrollbar = self.ui.plainTextEdit_serve.verticalScrollBar()
                    is_bottom = scrollbar.value() == scrollbar.maximum()
                    self.ui.plainTextEdit_serve.appendPlainText(
                        output.decode().strip())
                    if is_bottom:
                        scrollbar.setValue(scrollbar.maximum())
                if 'CRITICAL' in output.decode():
                    self.error_output(text, output.decode())
            if process.poll() is not None:
                break

    def copy_file(self, files: dict):
        self.copy_files = []
        for file in files:
            self.copy_files.append(file)

        if self.temp_dir == '':
            self.temp_dir = tempfile.mkdtemp(prefix='rclone_explorer_')
        open(self.temp_dir + os.sep + '.rclone_explorer_file_temp', 'a').close()

        clipboard = QApplication.clipboard()
        mime_data = QMimeData()
        mime_data.setText('.rclone_explorer_file_temp')
        url = QUrl.fromLocalFile(
            self.temp_dir + os.sep + '.rclone_explorer_file_temp')
        mime_data.setUrls([url])
        clipboard.setMimeData(mime_data)

    def delete_files(self, files: list[dict]):
        current_remote = self.current_remote

        if len(files) == 1:
            question = self.tr(
                'Are you sure you want to delete') + ' ' + files[0]['name'] + ' ?'
        else:
            question = self.tr('Are you sure you want to delete') + \
                ' ' + str(len(files)) + ' ' + self.tr('files') + ' ?'

        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Question)
        msg_box.setWindowTitle(self.tr('Delete'))
        msg_box.setText(question)
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        async def delete(button):
            if msg_box.buttonRole(button) == QMessageBox.YesRole:
                for file in files:
                    file_path = file['remote'] + file['path']

                    task = Task(operation='Delete', source=file_path)
                    self.tasks.append(task)

                    if file['is_dir']:
                        error = await rc.purge(file_path)
                    else:
                        error = await rc.deletefile(file_path)
                    if not error:
                        task.done()

                        # Explorer
                        items = self.ui.treeWidget_files.findItems(
                            file['name'], Qt.MatchFlag.MatchCaseSensitive)
                        if len(items) > 0 and items[0].data(0, Qt.ItemDataRole.UserRole)['remote'] == file['remote'] and items[0].data(0, Qt.ItemDataRole.UserRole)['path'] == file['path']:
                            items[0].setHidden(True)

                        # Search
                        items = self.ui.treeWidget_search.findItems(
                            file['name'], Qt.MatchFlag.MatchCaseSensitive)
                        if len(items) > 0 and items[0].data(0, Qt.ItemDataRole.UserRole)['remote'] == file['remote'] and items[0].data(0, Qt.ItemDataRole.UserRole)['path'] == file['path']:
                            items[0].setHidden(True)
                    else:
                        task.error()
                        self.error_output(
                            self.tr('An error occurred when deleting a file or directory'), error)
                if current_remote == self.current_remote:
                    await self.update_free_size(current_remote)

        msg_box.buttonClicked.connect(
            lambda button: asyncio.ensure_future(delete(button)))
        msg_box.show()

    async def update_dir(self, remote_name: str, path: str):
        if remote_name != '':
            self.clear_cache(remote_name, path)

            if f'{remote_name}{path}' == f'{self.current_remote}{self.remotes_paths[self.current_remote]}':
                await self.open_dir(remote_name, path, update=True)

    def paste_file(self):
        clipboard = QApplication.clipboard()

        destination_remote = self.current_remote
        destination_path = self.remotes_paths[self.current_remote]

        if clipboard.mimeData().text() == '.rclone_explorer_file_temp':
            for file in self.copy_files:
                asyncio.ensure_future(self.upload_file(
                    file['remote'] + file['path'], destination_remote, destination_path))
        else:
            for url in clipboard.mimeData().urls():
                source_path = url.toLocalFile()
                asyncio.ensure_future(self.upload_file(
                    source_path, destination_remote, destination_path))

    def exit_folder(self):
        if self.current_remote != '' and self.remotes_paths[self.current_remote] != '':
            self.update_history()
            path_dir = f'{self.remotes_paths[self.current_remote]}'
            path = '/'.join(path_dir.split('/')[:-1])
            asyncio.ensure_future(self.open_dir(self.current_remote, path))

    async def new_folder(self):
        input_dialog = QInputDialog(self)
        input_dialog.setWindowTitle(self.tr("New Folder"))
        input_dialog.setLabelText(self.tr("Enter folder name:"))
        input_dialog.setTextValue(self.tr("New Folder"))
        input_dialog.setModal(True)
        input_dialog.show()

        destination_remote = self.current_remote
        destination_path = self.remotes_paths[self.current_remote]

        async def create_folder():
            folder_name = input_dialog.textValue().strip()
            if destination_path != '':
                folder_path = f'{destination_remote}{destination_path}/{folder_name.strip()}'
            else:
                folder_path = f'{destination_remote}{destination_path}{folder_name.strip()}'
            error = await rc.mkdir(folder_path)
            if error:
                self.error_output(
                    self.tr('An error occurred when creating a new directory'), error)
            await self.update_dir(destination_remote, destination_path)

        input_dialog.accepted.connect(
            lambda: asyncio.ensure_future(create_folder()))

    async def rename_file(self, file_name: str):
        input_dialog = QInputDialog(self)
        input_dialog.setWindowTitle(self.tr("Rename"))
        input_dialog.setLabelText(self.tr("Enter new name:"))
        input_dialog.setTextValue(file_name)
        input_dialog.setModal(True)
        input_dialog.show()

        destination_remote = self.current_remote
        destination_path = self.remotes_paths[self.current_remote]

        async def rename():
            new_file_name = input_dialog.textValue().strip()
            if new_file_name.strip() != '':
                if destination_path != '':
                    new_file_path = f'{destination_remote}{destination_path}/{new_file_name.strip()}'
                    old_file_path = f'{destination_remote}{destination_path}/{file_name}'
                else:
                    new_file_path = f'{destination_remote}{destination_path}{new_file_name.strip()}'
                    old_file_path = f'{destination_remote}{destination_path}{file_name}'
                await rc.moveto(old_file_path, new_file_path)
                await self.update_dir(destination_remote, destination_path)

        input_dialog.accepted.connect(
            lambda: asyncio.ensure_future(rename()))

    def delete_remote(self, name: str):
        rc.config('delete', f'"{name[:-1]}"')
        self.update_remotes()

    def edit_remote(self, name: str):
        open_win = NewRemoteWindow(edit_mode=True, remote_name=name)
        open_win.setModal(True)
        open_win.exec()
        self.update_remotes()

    def open_task_dir(self, item: QTreeWidgetItem):
        if os.name == 'nt':
            os.startfile(item.text(2))
        else:
            subprocess.call(['xdg-open', item.text(2)])

    def shortcuts(self):
        def delete():
            selected = self.ui.treeWidget_files.selectedItems()
            selected_files = []
            for item in selected:
                selected_files.append(item.data(0, Qt.ItemDataRole.UserRole))
            if len(selected) > 0:
                self.delete_files(selected_files)

        def delete_search():
            selected = self.ui.treeWidget_search.selectedItems()
            selected_files = []
            for item in selected:
                selected_files.append(item.data(0, Qt.ItemDataRole.UserRole))
            if len(selected) > 0:
                self.delete_files(selected_files)

        def copy():
            selected = self.ui.treeWidget_files.selectedItems()
            selected_files = []
            for item in selected:
                selected_files.append(item.data(0, Qt.ItemDataRole.UserRole))
            if len(selected) > 0:
                self.copy_file(selected_files)

        self.delete_shortcut = QShortcut(
            QKeySequence("Del"), self.ui.treeWidget_files)
        self.delete_shortcut.activated.connect(delete)

        self.delete_shortcut_search = QShortcut(
            QKeySequence("Del"), self.ui.treeWidget_search)
        self.delete_shortcut_search.activated.connect(delete_search)

        self.copy_shortcut = QShortcut(
            QKeySequence("Ctrl+C"), self.ui.treeWidget_files)
        self.copy_shortcut.activated.connect(
            lambda: self.copy_files(self.ui.treeWidget_files.selectedItems()))

        self.copy_shortcut = QShortcut(
            QKeySequence("Ctrl+C"), self.ui.treeWidget_search)
        self.copy_shortcut.activated.connect(copy)

        self.paste_shortcut = QShortcut(
            QKeySequence("Ctrl+V"), self.ui.treeWidget_files)
        self.paste_shortcut.activated.connect(self.paste_file)

        def rename():
            selected = self.ui.treeWidget_files.selectedItems()
            if len(selected) > 0:
                asyncio.ensure_future(self.rename_file(selected[0].text(0)))

        self.rename_shortcut = QShortcut(
            QKeySequence("F2"), self.ui.treeWidget_files)
        self.rename_shortcut.activated.connect(rename)

        self.update_shortcut = QShortcut(
            QKeySequence("F5"), self.ui.treeWidget_files)
        self.update_shortcut.activated.connect(lambda: asyncio.ensure_future(
            self.update_dir(self.current_remote, self.remotes_paths.setdefault(self.current_remote, ''))))

        self.new_folder_shortcut = QShortcut(
            QKeySequence("F7"), self.ui.treeWidget_files)
        self.new_folder_shortcut.activated.connect(
            lambda: asyncio.ensure_future(self.new_folder()))

    def show_context_menu_tree(self, point):
        selected = self.ui.treeWidget_files.selectedItems()
        selected_files = []
        for item in selected:
            selected_files.append(item.data(0, Qt.ItemDataRole.UserRole))

        menu = QMenu()

        if self.current_remote != '':
            if len(selected) < 1:
                action = QAction(self)
                action.setText(self.tr('Paste'))
                action.setIcon(QIcon.fromTheme('edit-paste'))
                action.triggered.connect(self.paste_file)
                action.setShortcut(QKeySequence('Ctrl+V'))
                menu.addAction(action)

                action = QAction(self)
                action.setText(self.tr('New Folder'))
                action.setIcon(QIcon.fromTheme('folder-new'))
                action.triggered.connect(
                    lambda: asyncio.ensure_future(self.new_folder()))
                action.setShortcut(QKeySequence('F7'))
                menu.addAction(action)
            else:
                item = self.ui.treeWidget_files.itemAt(point)
                file_name = item.data(0, Qt.ItemDataRole.UserRole)['name']
                is_dir = item.data(0, Qt.ItemDataRole.UserRole)['is_dir']
                remote = item.data(0, Qt.ItemDataRole.UserRole)['remote']
                file_path = item.data(0, Qt.ItemDataRole.UserRole)['path']

                action = QAction(self)
                action.setText(self.tr('Open'))
                action.setIcon(item.icon(0))
                action.triggered.connect(
                    lambda: self.open_item(remote, file_path, file_name, is_dir))
                menu.addAction(action)

                if not is_dir and os.name == 'nt':
                    action = QAction(self)
                    action.setText(self.tr('Open With...'))
                    action.setIcon(QIcon.fromTheme('document-open'))
                    action.triggered.connect(
                        lambda: self.open_item(remote, file_path, file_name, is_dir, True))
                    menu.addAction(action)

                if is_dir:
                    def mount():
                        self.ui.comboBox_remote.setCurrentIndex(
                            self.ui.comboBox_remote.findText(remote, Qt.MatchFlag.MatchCaseSensitive))
                        self.ui.comboBox_remote.setCurrentText(
                            remote + file_path)
                        self.ui.tabWidget.setCurrentIndex(3)

                    menu.addSeparator()

                    action = QAction(self)
                    action.setText(self.tr('Mount', 'verb'))
                    action.setIcon(QIcon.fromTheme('drive-harddisk'))
                    action.triggered.connect(mount)
                    menu.addAction(action)

                action = QAction(self)
                action.setText(self.tr('Download'))
                action.setIcon(QIcon.fromTheme('emblem-downloads'))
                action.triggered.connect(
                    lambda: self.download_file(selected_files))
                menu.addAction(action)

                menu.addSeparator()

                action = QAction(self)
                action.setText(self.tr('Copy'))
                action.setIcon(QIcon.fromTheme('edit-copy'))
                action.triggered.connect(
                    lambda: self.copy_file(selected_files))
                action.setShortcut(QKeySequence('Ctrl+C'))
                menu.addAction(action)

                action = QAction(self)
                action.setText(self.tr('Paste'))
                action.setIcon(QIcon.fromTheme('edit-paste'))
                action.triggered.connect(self.paste_file)
                action.setShortcut(QKeySequence('Ctrl+V'))
                menu.addAction(action)

                menu.addSeparator()

                action = QAction(self)
                action.setText(self.tr('Rename'))
                action.setIcon(QIcon.fromTheme('format-text-italic'))
                action.triggered.connect(lambda: asyncio.ensure_future(
                    self.rename_file(file_name)))
                action.setShortcut(QKeySequence('F2'))
                menu.addAction(action)

                action = QAction(self)
                action.setText(self.tr('Delete'))
                action.setIcon(QIcon.fromTheme('edit-delete'))
                action.triggered.connect(
                    lambda: self.delete_files(selected_files))
                action.setShortcut(QKeySequence('Del'))
                menu.addAction(action)

                menu.addSeparator()

                action = QAction(self)
                action.setText(self.tr('New Folder'))
                action.setIcon(QIcon.fromTheme('folder-new'))
                action.triggered.connect(
                    lambda: asyncio.ensure_future(self.new_folder()))
                action.setShortcut(QKeySequence('F7'))
                menu.addAction(action)

        menu.exec(QCursor.pos())

    def show_context_menu_tree_search(self, point):
        selected = self.ui.treeWidget_search.selectedItems()
        selected_files = []
        for item in selected:
            selected_files.append(item.data(0, Qt.ItemDataRole.UserRole))

        if len(selected) == 0:
            return

        item = self.ui.treeWidget_search.itemAt(point)
        file_name = item.data(0, Qt.ItemDataRole.UserRole)['name']
        is_dir = item.data(0, Qt.ItemDataRole.UserRole)['is_dir']
        remote = item.data(0, Qt.ItemDataRole.UserRole)['remote']
        file_path = item.data(0, Qt.ItemDataRole.UserRole)['path']

        async def show():
            path = file_path[0:-len(file_name)]
            self.ui.tabWidget.setCurrentIndex(0)

            self.ui.treeWidget_remotes.clearSelection()
            items = self.ui.treeWidget_remotes.findItems(
                remote, Qt.MatchFlag.MatchCaseSensitive)
            items[0].setSelected(True)

            await self.open_dir(remote, path)
            items = self.ui.treeWidget_files.findItems(
                file_name, Qt.MatchFlag.MatchCaseSensitive)
            items[0].setSelected(True)

        menu = QMenu()

        action = QAction(self)
        action.setText(self.tr('Open file location'))
        action.setIcon(QIcon.fromTheme('system-file-manager'))
        action.triggered.connect(lambda: asyncio.ensure_future(show()))
        menu.addAction(action)

        if not is_dir:
            menu.addSeparator()

            action = QAction(self)
            action.setText(self.tr('Open'))
            action.setIcon(item.icon(0))
            action.triggered.connect(
                lambda: self.open_item(remote, file_path, file_name, is_dir))
            menu.addAction(action)
        else:
            def mount():
                self.ui.comboBox_remote.setCurrentIndex(
                    self.ui.comboBox_remote.findText(remote, Qt.MatchFlag.MatchCaseSensitive))
                self.ui.comboBox_remote.setCurrentText(remote + file_path)
                self.ui.tabWidget.setCurrentIndex(3)

            menu.addSeparator()

            action = QAction(self)
            action.setText(self.tr('Mount', 'verb'))
            action.setIcon(QIcon.fromTheme('drive-harddisk'))
            action.triggered.connect(mount)
            menu.addAction(action)

        if not is_dir and os.name == 'nt':
            action = QAction(self)
            action.setText(self.tr('Open With...'))
            action.setIcon(QIcon.fromTheme('document-open'))
            action.triggered.connect(
                lambda: self.open_item(remote, file_path, file_name, is_dir, True))
            menu.addAction(action)

        menu.addSeparator()

        action = QAction(self)
        action.setText(self.tr('Download'))
        action.setIcon(QIcon.fromTheme('emblem-downloads'))
        action.triggered.connect(
            lambda: self.download_file(selected_files))
        menu.addAction(action)

        menu.addSeparator()

        action = QAction(self)
        action.setText(self.tr('Copy'))
        action.setIcon(QIcon.fromTheme('edit-copy'))
        action.triggered.connect(lambda: self.copy_files(selected))
        action.setShortcut(QKeySequence('Ctrl+C'))
        menu.addAction(action)

        action = QAction(self)
        action.setText(self.tr('Delete'))
        action.setIcon(QIcon.fromTheme('edit-delete'))
        action.triggered.connect(
            lambda: self.delete_files(selected_files))
        action.setShortcut(QKeySequence('Del'))
        menu.addAction(action)

        menu.exec(QCursor.pos())

    def show_context_menu_remote(self, point):
        index = self.ui.treeWidget_remotes.indexAt(point)

        if not index.isValid():
            return

        item = self.ui.treeWidget_remotes.itemAt(point)

        menu = QMenu()

        action = QAction(self)
        action.setText(self.tr('Open'))
        action.setIcon(QIcon.fromTheme('folder-open'))
        action.triggered.connect(lambda: self.open_remote(item))
        menu.addAction(action)

        action = QAction(self)
        action.setText(self.tr('Edit'))
        action.setIcon(QIcon.fromTheme('applications-development'))
        action.triggered.connect(lambda: self.edit_remote(item.text(0)))
        menu.addAction(action)

        def mount():
            self.ui.comboBox_remote.setCurrentIndex(
                self.ui.comboBox_remote.findText(item.text(0), Qt.MatchFlag.MatchCaseSensitive))
            self.ui.comboBox_remote.setCurrentText(item.text(0))
            self.ui.tabWidget.setCurrentIndex(3)

        action = QAction(self)
        action.setText(self.tr('Mount', 'verb'))
        action.setIcon(QIcon.fromTheme('drive-harddisk'))
        action.triggered.connect(mount)
        menu.addAction(action)

        action = QAction(self)
        action.setText(self.tr('Delete'))
        action.setIcon(QIcon.fromTheme('edit-delete'))
        action.triggered.connect(lambda: self.delete_remote(item.text(0)))
        menu.addAction(action)

        menu.exec(QCursor.pos())

    def show_context_menu_serve(self, point):
        index = self.ui.treeWidget_serve.indexAt(point)
        menu = QMenu()
        item = self.ui.treeWidget_serve.itemAt(point)

        def stop_serve(index: int):
            self.serve[index].stop()
            self.remember_serve(
                Qt.CheckState.Unchecked, self.serve[index].protocol, self.serve[index].path, self.serve[index].user)
            self.ui.treeWidget_serve.takeTopLevelItem(index)
            del self.serve[index]

        def edit_serve(index: int):
            if (NewServeWindow(self, item.text(0), item.text(1), item.text(3), item.text(4), item.text(2), item.text(5) == '+', self.serve[index].args).exec()) == QDialog.Accepted:
                stop_serve(index)

        if index.isValid():
            action = QAction(self)
            action.setText(self.tr('Stop'))
            action.triggered.connect(lambda: stop_serve(index.row()))
            menu.addAction(action)

            action = QAction(self)
            action.setText(self.tr('Edit'))
            action.triggered.connect(lambda: edit_serve(index.row()))
            menu.addAction(action)

        menu.exec(QCursor.pos())

    def show_context_menu_mount(self, point):
        index = self.ui.treeWidget_mount.indexAt(point)
        menu = QMenu()
        item = self.ui.treeWidget_mount.itemAt(point)

        def stop_mount(index: int):
            self.mount[index].stop()
            self.remember_mount(Qt.CheckState.Unchecked, item.text(0))
            self.ui.treeWidget_mount.takeTopLevelItem(index)
            del self.mount[index]

        if index.isValid():
            action = QAction(self)
            action.setText(self.tr('Stop'))
            action.triggered.connect(lambda: stop_mount(index.row()))
            menu.addAction(action)

        menu.exec(QCursor.pos())

    def show_context_menu_task(self, point):
        index = self.ui.treeWidget_tasks.indexAt(point)
        menu = QMenu()

        def clear_tasks():
            for i in range(len(self.tasks)):
                if self.tasks[i].status == 'Done' or self.tasks[i].status == 'Error':
                    self.ui.treeWidget_tasks.topLevelItem(i).setHidden(True)

        def cancel_task(index: int):
            self.tasks[index].stop()
            self.ui.treeWidget_tasks.topLevelItem(index).setHidden(True)
            self.tasks[index].status = 'Stop'

        if not index.isValid():
            action = QAction(self)
            action.setText(self.tr('Clear Completed'))
            action.setIcon(QIcon.fromTheme('edit-clear'))
            action.triggered.connect(clear_tasks)
            menu.addAction(action)
        else:
            item = self.ui.treeWidget_tasks.itemAt(point)

            if item.text(0) in [self.tr('Download', 'noun'), self.tr('Upload'), self.tr('Opening')]:
                action = QAction(self)
                action.setText(self.tr('Open Folder'))
                action.setIcon(QIcon.fromTheme('folder-open'))
                action.triggered.connect(lambda: self.open_task_dir(item))
                menu.addAction(action)

            if item.text(3) == self.tr('Done'):
                action = QAction(self)
                action.setText(self.tr('Clear Task'))
                action.setIcon(QIcon.fromTheme('edit-clear'))
                action.triggered.connect(
                    lambda: self.ui.treeWidget_tasks.topLevelItem(index.row()).setHidden(True))
                menu.addAction(action)

            if item.text(0) in [self.tr('Download', 'noun'), self.tr('Upload'), self.tr('Opening')] and item.text(3) != self.tr('Done'):
                action = QAction(self)
                action.setText(self.tr('Сancel'))
                action.setIcon(QIcon.fromTheme('media-playback-stop'))
                action.triggered.connect(lambda: cancel_task(index.row()))
                menu.addAction(action)

            action = QAction(self)
            action.setText(self.tr('Clear Completed'))
            action.setIcon(QIcon.fromTheme('edit-clear'))
            action.triggered.connect(clear_tasks)
            menu.addAction(action)

        menu.exec(QCursor.pos())

    def context_menu_tray_icon(self):
        menu = QMenu()

        def open():
            self.show()
            self.activateWindow()

        def close():
            self.hide()
            self.close()

        action = QAction(self)
        action.setText(self.tr('Open'))
        action.setIcon(self.windowIcon())
        action.triggered.connect(open)
        menu.addAction(action)

        menu.addSeparator()
        menu.addAction(self.ui.action_new_remote)
        menu.addAction(self.ui.action_new_serve)
        menu.addSeparator()
        menu.addAction(self.ui.action_settings)
        menu.addSeparator()

        action = QAction(self)
        action.setText(self.tr('Exit'))
        action.setIcon(QIcon.fromTheme('application-exit'))
        action.triggered.connect(close)
        menu.addAction(action)

        return menu
