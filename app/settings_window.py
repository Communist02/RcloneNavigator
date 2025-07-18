import os
import sys

from PySide6.QtCore import QLocale, QSettings, QTranslator, Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QDialog, QStyleFactory
from app.palettes import palettes
from app.views import settings_window

if os.name == 'nt':
    import winreg


class SettingsWindow(QDialog):
    def __init__(self):
        super(SettingsWindow, self).__init__()
        self.ui = settings_window.Ui_SettingsWindow()
        self.ui.setupUi(self)

        self.settings = QSettings('Rclone Navigator', 'Rclone Navigator')

        self.setWindowIcon(
            QIcon(os.path.dirname(__file__) + '/resources/' + 'favicon.ico'))

        styles = QStyleFactory.keys()
        for i in range(len(styles)):
            styles[i] = styles[i].lower()
        self.ui.comboBox_style.addItems(styles)
        self.ui.comboBox_style.setCurrentText(
            self.settings.value('style', self.style().name()))

        palettes_list: list = list(palettes.keys())
        # if self.ui.comboBox_style.currentText() != 'fusion' and self.ui.comboBox_style.currentText() != 'windows':
        for i in range(len(palettes_list)):
            palettes_list[i] = palettes_list[i].replace(
                ' Dark', '').replace(' Light', '')

        unique_list = []
        for palette in palettes_list:
            if palette not in unique_list:
                unique_list.append(palette)

        languages = set()
        languages.add('en')
        languages.add('auto')
        self.translations_dir = os.path.join(
            os.path.dirname(__file__), os.pardir, 'translations')

        for file_name in os.listdir(self.translations_dir):
            if file_name.endswith('.qm'):
                lang_code = file_name[:-3].replace('qtbase_', '')
                languages.add(lang_code)
        self.ui.comboBox_language.addItems(sorted(list(languages)))

        self.ui.comboBox_palette.addItems(unique_list)
        self.ui.comboBox_palette.setCurrentText(
            self.settings.value('palette', 'System'))
        self.ui.comboBox_language.setCurrentText(
            self.settings.value('language', 'auto'))
        self.ui.checkBox_tray.setChecked(
            bool(self.settings.value('minimize_to_tray', False)))

        if os.name != 'nt':
            self.ui.checkBox_autorun.hide()
        else:
            self.ui.checkBox_autorun.setChecked(
                self.check_autorun('Rclone Navigator'))
            self.ui.checkBox_autorun.checkStateChanged.connect(
                lambda value: self.autorun(value, 'Rclone Navigator'))

        self.ui.buttonBox.accepted.connect(self.ok)

    def check_autorun(self, app_name: str):
        if os.name == 'nt':
            key = winreg.HKEY_CURRENT_USER
            reg_path = r'Software\\Microsoft\\Windows\\CurrentVersion\\Run'
            try:
                with winreg.OpenKey(key, reg_path, 0, winreg.KEY_READ) as reg_key:
                    try:
                        winreg.QueryValueEx(reg_key, app_name)
                        return True
                    except FileNotFoundError:
                        return False
            except Exception as e:
                print(f'Error checking autorun: {e}')
                return False

    def autorun(self, is_add: bool, app_name: str):
        if os.name == 'nt':
            if is_add:
                key = winreg.HKEY_CURRENT_USER
                reg_path = r'Software\\Microsoft\\Windows\\CurrentVersion\\Run'

                try:
                    with winreg.OpenKey(key, reg_path, 0, winreg.KEY_SET_VALUE) as reg_key:
                        path = sys.argv[0]
                        file_name = os.path.basename(path)
                        path = os.path.dirname(path) + os.sep
                        if file_name == 'rclone_explorer.exe' and os.path.exists(path + 'rclone_explorer_no_console.exe'):
                            winreg.SetValueEx(
                                reg_key, app_name, 0, winreg.REG_SZ, f'"{path}rclone_explorer_no_console.exe" --minimized')
                except Exception as e:
                    print(f'Error: {e}')
            else:
                key = winreg.HKEY_CURRENT_USER
                reg_path = r'Software\\Microsoft\\Windows\\CurrentVersion\\Run'

                try:
                    with winreg.OpenKey(key, reg_path, 0, winreg.KEY_SET_VALUE) as reg_key:
                        winreg.DeleteValue(reg_key, app_name)
                except WindowsError as e:
                    if e.errno == 2:  # Value doesn't exist
                        print(f'Startup entry not found: {app_name}')
                    else:
                        print(f'Error removing from startup: {e}')
                except Exception as e:
                    print(f'Error: {e}')

    def ok(self):
        QApplication.setStyle(self.ui.comboBox_style.currentText())
        palette = self.ui.comboBox_palette.currentText()
        if QApplication.styleHints().colorScheme() == Qt.ColorScheme.Light:
            palette += ' Light'
        else:
            palette += ' Dark'
        QApplication.setPalette(palettes.get(palette, palettes['System']))

        self.settings.setValue('style', self.ui.comboBox_style.currentText())
        self.settings.setValue(
            'palette', self.ui.comboBox_palette.currentText())
        self.settings.setValue(
            'language', self.ui.comboBox_language.currentText())
        self.settings.setValue(
            'minimize_to_tray', self.ui.checkBox_tray.isChecked())

        self.autorun(self.ui.checkBox_autorun.isChecked(), 'Rclone Navigator')

        qt_translator = QTranslator()
        translator = QTranslator()
        lang_code = self.ui.comboBox_language.currentText()
        if lang_code == 'auto':
            lang_code = QLocale.system().name()
        if qt_translator.load(f'qtbase_{lang_code}.qm', self.translations_dir):
            QApplication.installTranslator(qt_translator)
        else:
            QApplication.removeTranslator(qt_translator)
        if translator.load(lang_code + '.qm', self.translations_dir):
            QApplication.installTranslator(translator)
        else:
            QApplication.removeTranslator(translator)
        self.ui.retranslateUi(self)
        QApplication.installTranslator(translator)
