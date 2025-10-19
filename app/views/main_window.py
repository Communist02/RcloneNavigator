# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDockWidget,
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPlainTextEdit, QPushButton, QScrollArea, QSizePolicy,
    QSplitter, QStatusBar, QTabWidget, QToolButton,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 800)
        MainWindow.setWindowTitle(u"Rclone Navigator")
        self.action_new_remote = QAction(MainWindow)
        self.action_new_remote.setObjectName(u"action_new_remote")
        icon = QIcon(QIcon.fromTheme(u"system-file-manager"))
        self.action_new_remote.setIcon(icon)
        self.action_exit = QAction(MainWindow)
        self.action_exit.setObjectName(u"action_exit")
        icon1 = QIcon(QIcon.fromTheme(u"application-exit"))
        self.action_exit.setIcon(icon1)
        self.action_about = QAction(MainWindow)
        self.action_about.setObjectName(u"action_about")
        icon2 = QIcon(QIcon.fromTheme(u"help-about"))
        self.action_about.setIcon(icon2)
        self.action_list_remotes = QAction(MainWindow)
        self.action_list_remotes.setObjectName(u"action_list_remotes")
        self.action_list_remotes.setCheckable(True)
        self.action_list_remotes.setChecked(True)
        self.action_new_serve = QAction(MainWindow)
        self.action_new_serve.setObjectName(u"action_new_serve")
        icon3 = QIcon(QIcon.fromTheme(u"applications-internet"))
        self.action_new_serve.setIcon(icon3)
        self.action_settings = QAction(MainWindow)
        self.action_settings.setObjectName(u"action_settings")
        icon4 = QIcon(QIcon.fromTheme(u"applications-development"))
        self.action_settings.setIcon(icon4)
        self.action_show_tasks = QAction(MainWindow)
        self.action_show_tasks.setObjectName(u"action_show_tasks")
        self.action_config_rclone = QAction(MainWindow)
        self.action_config_rclone.setObjectName(u"action_config_rclone")
        self.action_about_qt = QAction(MainWindow)
        self.action_about_qt.setObjectName(u"action_about_qt")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setDocumentMode(True)
        self.tab_explorer = QWidget()
        self.tab_explorer.setObjectName(u"tab_explorer")
        self.verticalLayout_3 = QVBoxLayout(self.tab_explorer)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, -1, 0, 6)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.button_prev_history = QPushButton(self.tab_explorer)
        self.button_prev_history.setObjectName(u"button_prev_history")
        self.button_prev_history.setEnabled(False)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_prev_history.sizePolicy().hasHeightForWidth())
        self.button_prev_history.setSizePolicy(sizePolicy)
        self.button_prev_history.setMinimumSize(QSize(34, 34))
        self.button_prev_history.setMaximumSize(QSize(34, 34))
        icon5 = QIcon(QIcon.fromTheme(u"go-previous"))
        self.button_prev_history.setIcon(icon5)
        self.button_prev_history.setFlat(True)

        self.horizontalLayout.addWidget(self.button_prev_history)

        self.button_next_history = QPushButton(self.tab_explorer)
        self.button_next_history.setObjectName(u"button_next_history")
        self.button_next_history.setEnabled(False)
        sizePolicy.setHeightForWidth(self.button_next_history.sizePolicy().hasHeightForWidth())
        self.button_next_history.setSizePolicy(sizePolicy)
        self.button_next_history.setMinimumSize(QSize(34, 34))
        self.button_next_history.setMaximumSize(QSize(34, 34))
        icon6 = QIcon(QIcon.fromTheme(u"go-next"))
        self.button_next_history.setIcon(icon6)
        self.button_next_history.setFlat(True)

        self.horizontalLayout.addWidget(self.button_next_history)

        self.button_exit_dir = QPushButton(self.tab_explorer)
        self.button_exit_dir.setObjectName(u"button_exit_dir")
        self.button_exit_dir.setEnabled(False)
        sizePolicy.setHeightForWidth(self.button_exit_dir.sizePolicy().hasHeightForWidth())
        self.button_exit_dir.setSizePolicy(sizePolicy)
        self.button_exit_dir.setMinimumSize(QSize(34, 34))
        self.button_exit_dir.setMaximumSize(QSize(34, 34))
        icon7 = QIcon(QIcon.fromTheme(u"go-up"))
        self.button_exit_dir.setIcon(icon7)
        self.button_exit_dir.setFlat(True)

        self.horizontalLayout.addWidget(self.button_exit_dir)

        self.button_update = QPushButton(self.tab_explorer)
        self.button_update.setObjectName(u"button_update")
        self.button_update.setMinimumSize(QSize(34, 34))
        self.button_update.setMaximumSize(QSize(34, 34))
        icon8 = QIcon(QIcon.fromTheme(u"view-refresh"))
        self.button_update.setIcon(icon8)
        self.button_update.setFlat(True)

        self.horizontalLayout.addWidget(self.button_update)

        self.scrollArea_explorer = QScrollArea(self.tab_explorer)
        self.scrollArea_explorer.setObjectName(u"scrollArea_explorer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollArea_explorer.sizePolicy().hasHeightForWidth())
        self.scrollArea_explorer.setSizePolicy(sizePolicy1)
        self.scrollArea_explorer.setMaximumSize(QSize(16777215, 34))
        self.scrollArea_explorer.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea_explorer.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea_explorer.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 527, 34))
        self.horizontalLayout_4 = QHBoxLayout(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.path_list_frame = QFrame(self.scrollAreaWidgetContents_3)
        self.path_list_frame.setObjectName(u"path_list_frame")
        sizePolicy1.setHeightForWidth(self.path_list_frame.sizePolicy().hasHeightForWidth())
        self.path_list_frame.setSizePolicy(sizePolicy1)
        self.path_list_frame.setMinimumSize(QSize(0, 34))
        self.path_list_frame.setMaximumSize(QSize(16777215, 34))
        self.path_list_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.horizontalLayout_3 = QHBoxLayout(self.path_list_frame)
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.path_list = QHBoxLayout()
        self.path_list.setSpacing(0)
        self.path_list.setObjectName(u"path_list")

        self.horizontalLayout_3.addLayout(self.path_list)

        self.pushButton_input_path = QPushButton(self.path_list_frame)
        self.pushButton_input_path.setObjectName(u"pushButton_input_path")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_input_path.sizePolicy().hasHeightForWidth())
        self.pushButton_input_path.setSizePolicy(sizePolicy2)
        self.pushButton_input_path.setText(u"")
        self.pushButton_input_path.setFlat(True)

        self.horizontalLayout_3.addWidget(self.pushButton_input_path)


        self.horizontalLayout_4.addWidget(self.path_list_frame)

        self.scrollArea_explorer.setWidget(self.scrollAreaWidgetContents_3)

        self.horizontalLayout.addWidget(self.scrollArea_explorer)

        self.lineEdit_input_path = QLineEdit(self.tab_explorer)
        self.lineEdit_input_path.setObjectName(u"lineEdit_input_path")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lineEdit_input_path.sizePolicy().hasHeightForWidth())
        self.lineEdit_input_path.setSizePolicy(sizePolicy3)
        self.lineEdit_input_path.setClearButtonEnabled(True)

        self.horizontalLayout.addWidget(self.lineEdit_input_path)

        self.pushButton_explorer_search = QPushButton(self.tab_explorer)
        self.pushButton_explorer_search.setObjectName(u"pushButton_explorer_search")
        self.pushButton_explorer_search.setMinimumSize(QSize(34, 34))
        self.pushButton_explorer_search.setMaximumSize(QSize(34, 34))
        icon9 = QIcon(QIcon.fromTheme(u"edit-find"))
        self.pushButton_explorer_search.setIcon(icon9)
        self.pushButton_explorer_search.setFlat(True)

        self.horizontalLayout.addWidget(self.pushButton_explorer_search)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.treeWidget_remotes = QTreeWidget(self.tab_explorer)
        self.treeWidget_remotes.setObjectName(u"treeWidget_remotes")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.treeWidget_remotes.sizePolicy().hasHeightForWidth())
        self.treeWidget_remotes.setSizePolicy(sizePolicy4)
        self.treeWidget_remotes.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.treeWidget_remotes.setRootIsDecorated(False)
        self.treeWidget_remotes.setSortingEnabled(True)

        self.horizontalLayout_2.addWidget(self.treeWidget_remotes)

        self.treeWidget_files = QTreeWidget(self.tab_explorer)
        self.treeWidget_files.setObjectName(u"treeWidget_files")
        self.treeWidget_files.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.treeWidget_files.setDragEnabled(True)
        self.treeWidget_files.setDragDropMode(QAbstractItemView.DragDropMode.DragOnly)
        self.treeWidget_files.setDefaultDropAction(Qt.DropAction.CopyAction)
        self.treeWidget_files.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.treeWidget_files.setRootIsDecorated(False)
        self.treeWidget_files.setSortingEnabled(True)

        self.horizontalLayout_2.addWidget(self.treeWidget_files)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.tabWidget.addTab(self.tab_explorer, icon, "")
        self.tab_search = QWidget()
        self.tab_search.setObjectName(u"tab_search")
        self.verticalLayout_4 = QVBoxLayout(self.tab_search)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.splitter_search = QSplitter(self.tab_search)
        self.splitter_search.setObjectName(u"splitter_search")
        self.splitter_search.setOrientation(Qt.Orientation.Horizontal)
        self.splitter_search.setChildrenCollapsible(False)
        self.lineEdit_search = QLineEdit(self.splitter_search)
        self.lineEdit_search.setObjectName(u"lineEdit_search")
        self.splitter_search.addWidget(self.lineEdit_search)
        self.comboBox_search = QComboBox(self.splitter_search)
        self.comboBox_search.setObjectName(u"comboBox_search")
        self.comboBox_search.setEditable(True)
        self.splitter_search.addWidget(self.comboBox_search)

        self.horizontalLayout_5.addWidget(self.splitter_search)

        self.button_search = QPushButton(self.tab_search)
        self.button_search.setObjectName(u"button_search")

        self.horizontalLayout_5.addWidget(self.button_search)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.treeWidget_search = QTreeWidget(self.tab_search)
        self.treeWidget_search.setObjectName(u"treeWidget_search")
        self.treeWidget_search.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.treeWidget_search.setDragEnabled(True)
        self.treeWidget_search.setDragDropMode(QAbstractItemView.DragDropMode.DragOnly)
        self.treeWidget_search.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.treeWidget_search.setRootIsDecorated(False)

        self.verticalLayout_4.addWidget(self.treeWidget_search)

        self.tabWidget.addTab(self.tab_search, icon9, "")
        self.tab_serve = QWidget()
        self.tab_serve.setObjectName(u"tab_serve")
        self.verticalLayout_6 = QVBoxLayout(self.tab_serve)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, -1, 0, -1)
        self.button_new_serve = QPushButton(self.tab_serve)
        self.button_new_serve.setObjectName(u"button_new_serve")

        self.verticalLayout_6.addWidget(self.button_new_serve)

        self.splitter_serve = QSplitter(self.tab_serve)
        self.splitter_serve.setObjectName(u"splitter_serve")
        self.splitter_serve.setOrientation(Qt.Orientation.Vertical)
        self.treeWidget_serve = QTreeWidget(self.splitter_serve)
        self.treeWidget_serve.setObjectName(u"treeWidget_serve")
        self.treeWidget_serve.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.treeWidget_serve.setRootIsDecorated(False)
        self.splitter_serve.addWidget(self.treeWidget_serve)
        self.plainTextEdit_serve = QPlainTextEdit(self.splitter_serve)
        self.plainTextEdit_serve.setObjectName(u"plainTextEdit_serve")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.plainTextEdit_serve.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_serve.setSizePolicy(sizePolicy5)
        self.plainTextEdit_serve.setReadOnly(True)
        self.splitter_serve.addWidget(self.plainTextEdit_serve)

        self.verticalLayout_6.addWidget(self.splitter_serve)

        self.tabWidget.addTab(self.tab_serve, icon3, "")
        self.tab_mount = QWidget()
        self.tab_mount.setObjectName(u"tab_mount")
        self.verticalLayout_7 = QVBoxLayout(self.tab_mount)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label = QLabel(self.tab_mount)
        self.label.setObjectName(u"label")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy6)

        self.horizontalLayout_6.addWidget(self.label)

        self.comboBox_remote = QComboBox(self.tab_mount)
        self.comboBox_remote.setObjectName(u"comboBox_remote")
        sizePolicy1.setHeightForWidth(self.comboBox_remote.sizePolicy().hasHeightForWidth())
        self.comboBox_remote.setSizePolicy(sizePolicy1)
        self.comboBox_remote.setEditable(True)

        self.horizontalLayout_6.addWidget(self.comboBox_remote)

        self.label_2 = QLabel(self.tab_mount)
        self.label_2.setObjectName(u"label_2")
        sizePolicy6.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy6)

        self.horizontalLayout_6.addWidget(self.label_2)

        self.comboBox_mount_point = QComboBox(self.tab_mount)
        self.comboBox_mount_point.setObjectName(u"comboBox_mount_point")
        sizePolicy1.setHeightForWidth(self.comboBox_mount_point.sizePolicy().hasHeightForWidth())
        self.comboBox_mount_point.setSizePolicy(sizePolicy1)
        self.comboBox_mount_point.setEditable(True)

        self.horizontalLayout_6.addWidget(self.comboBox_mount_point)

        self.toolButton_mount_point = QToolButton(self.tab_mount)
        self.toolButton_mount_point.setObjectName(u"toolButton_mount_point")
        self.toolButton_mount_point.setText(u"...")

        self.horizontalLayout_6.addWidget(self.toolButton_mount_point)

        self.button_mount = QPushButton(self.tab_mount)
        self.button_mount.setObjectName(u"button_mount")
        sizePolicy.setHeightForWidth(self.button_mount.sizePolicy().hasHeightForWidth())
        self.button_mount.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.button_mount)


        self.verticalLayout_7.addLayout(self.horizontalLayout_6)

        self.splitter_mount = QSplitter(self.tab_mount)
        self.splitter_mount.setObjectName(u"splitter_mount")
        self.splitter_mount.setOrientation(Qt.Orientation.Vertical)
        self.treeWidget_mount = QTreeWidget(self.splitter_mount)
        self.treeWidget_mount.setObjectName(u"treeWidget_mount")
        self.treeWidget_mount.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.treeWidget_mount.setRootIsDecorated(False)
        self.splitter_mount.addWidget(self.treeWidget_mount)
        self.plainTextEdit_mount = QPlainTextEdit(self.splitter_mount)
        self.plainTextEdit_mount.setObjectName(u"plainTextEdit_mount")
        sizePolicy5.setHeightForWidth(self.plainTextEdit_mount.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_mount.setSizePolicy(sizePolicy5)
        self.plainTextEdit_mount.setReadOnly(True)
        self.splitter_mount.addWidget(self.plainTextEdit_mount)

        self.verticalLayout_7.addWidget(self.splitter_mount)

        icon10 = QIcon(QIcon.fromTheme(u"drive-harddisk"))
        self.tabWidget.addTab(self.tab_mount, icon10, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1280, 23))
        self.menuClient = QMenu(self.menubar)
        self.menuClient.setObjectName(u"menuClient")
        self.menuOther = QMenu(self.menubar)
        self.menuOther.setObjectName(u"menuOther")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setSizeGripEnabled(False)
        MainWindow.setStatusBar(self.statusbar)
        self.dock_tasks = QDockWidget(MainWindow)
        self.dock_tasks.setObjectName(u"dock_tasks")
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout_2 = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.treeWidget_tasks = QTreeWidget(self.dockWidgetContents)
        self.treeWidget_tasks.setObjectName(u"treeWidget_tasks")
        self.treeWidget_tasks.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.treeWidget_tasks.setRootIsDecorated(False)

        self.verticalLayout_2.addWidget(self.treeWidget_tasks)

        self.dock_tasks.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, self.dock_tasks)

        self.menubar.addAction(self.menuClient.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuOther.menuAction())
        self.menuClient.addAction(self.action_new_remote)
        self.menuClient.addAction(self.action_new_serve)
        self.menuClient.addSeparator()
        self.menuClient.addAction(self.action_config_rclone)
        self.menuClient.addAction(self.action_settings)
        self.menuClient.addSeparator()
        self.menuClient.addAction(self.action_exit)
        self.menuOther.addAction(self.action_about_qt)
        self.menuOther.addAction(self.action_about)
        self.menuView.addAction(self.action_show_tasks)
        self.menuView.addAction(self.action_list_remotes)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.action_new_remote.setText(QCoreApplication.translate("MainWindow", u"New remote", None))
        self.action_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.action_about.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.action_list_remotes.setText(QCoreApplication.translate("MainWindow", u"List remotes", None))
        self.action_new_serve.setText(QCoreApplication.translate("MainWindow", u"New serve", None))
        self.action_settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.action_show_tasks.setText(QCoreApplication.translate("MainWindow", u"Show tasks", None))
        self.action_config_rclone.setText(QCoreApplication.translate("MainWindow", u"Config Rclone", None))
        self.action_about_qt.setText(QCoreApplication.translate("MainWindow", u"About Qt", None))
        self.button_prev_history.setText("")
        self.button_next_history.setText("")
        self.button_exit_dir.setText("")
        self.pushButton_explorer_search.setText("")
        ___qtreewidgetitem = self.treeWidget_remotes.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtreewidgetitem1 = self.treeWidget_files.headerItem()
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("MainWindow", u"Modified", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"Size", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"Name", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_explorer), QCoreApplication.translate("MainWindow", u"Explorer", None))
        self.lineEdit_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.button_search.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        ___qtreewidgetitem2 = self.treeWidget_search.headerItem()
        ___qtreewidgetitem2.setText(4, QCoreApplication.translate("MainWindow", u"Path", None));
        ___qtreewidgetitem2.setText(3, QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtreewidgetitem2.setText(2, QCoreApplication.translate("MainWindow", u"Modified", None));
        ___qtreewidgetitem2.setText(1, QCoreApplication.translate("MainWindow", u"Size", None));
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"Name", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_search), QCoreApplication.translate("MainWindow", u"Search", None))
        self.button_new_serve.setText(QCoreApplication.translate("MainWindow", u"New serve", None))
        ___qtreewidgetitem3 = self.treeWidget_serve.headerItem()
        ___qtreewidgetitem3.setText(6, QCoreApplication.translate("MainWindow", u"Remember", None));
        ___qtreewidgetitem3.setText(5, QCoreApplication.translate("MainWindow", u"Read-only", None));
        ___qtreewidgetitem3.setText(4, QCoreApplication.translate("MainWindow", u"Password", None));
        ___qtreewidgetitem3.setText(3, QCoreApplication.translate("MainWindow", u"Username", None));
        ___qtreewidgetitem3.setText(2, QCoreApplication.translate("MainWindow", u"Address", None));
        ___qtreewidgetitem3.setText(1, QCoreApplication.translate("MainWindow", u"Path", None));
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"Protocol", None));
        self.plainTextEdit_serve.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Logs", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_serve), QCoreApplication.translate("MainWindow", u"Serve", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Remote path", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Mount point", None))
        self.button_mount.setText(QCoreApplication.translate("MainWindow", u"Mount", u"verb"))
        ___qtreewidgetitem4 = self.treeWidget_mount.headerItem()
        ___qtreewidgetitem4.setText(3, QCoreApplication.translate("MainWindow", u"Remember", None));
        ___qtreewidgetitem4.setText(2, QCoreApplication.translate("MainWindow", u"Mount point", None));
        ___qtreewidgetitem4.setText(1, QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("MainWindow", u"Remote", None));
        self.plainTextEdit_mount.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Logs", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_mount), QCoreApplication.translate("MainWindow", u"Mount", None))
        self.menuClient.setTitle(QCoreApplication.translate("MainWindow", u"Client", None))
        self.menuOther.setTitle(QCoreApplication.translate("MainWindow", u"Other", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        ___qtreewidgetitem5 = self.treeWidget_tasks.headerItem()
        ___qtreewidgetitem5.setText(7, QCoreApplication.translate("MainWindow", u"Estimated", None));
        ___qtreewidgetitem5.setText(6, QCoreApplication.translate("MainWindow", u"Speed", None));
        ___qtreewidgetitem5.setText(5, QCoreApplication.translate("MainWindow", u"Progress", None));
        ___qtreewidgetitem5.setText(4, QCoreApplication.translate("MainWindow", u"Size", None));
        ___qtreewidgetitem5.setText(3, QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtreewidgetitem5.setText(2, QCoreApplication.translate("MainWindow", u"Destination", None));
        ___qtreewidgetitem5.setText(1, QCoreApplication.translate("MainWindow", u"Source", None));
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("MainWindow", u"Operation", None));
        pass
    # retranslateUi

