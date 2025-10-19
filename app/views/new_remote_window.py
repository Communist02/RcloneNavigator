# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_remote_window.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialog, QDialogButtonBox, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QRadioButton, QScrollArea,
    QSizePolicy, QSpacerItem, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_NewRemoteWindow(object):
    def setupUi(self, NewRemoteWindow):
        if not NewRemoteWindow.objectName():
            NewRemoteWindow.setObjectName(u"NewRemoteWindow")
        NewRemoteWindow.resize(1080, 720)
        NewRemoteWindow.setModal(True)
        self.verticalLayout = QVBoxLayout(NewRemoteWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit_name = QLineEdit(NewRemoteWindow)
        self.lineEdit_name.setObjectName(u"lineEdit_name")

        self.verticalLayout.addWidget(self.lineEdit_name)

        self.tabWidget_mode = QTabWidget(NewRemoteWindow)
        self.tabWidget_mode.setObjectName(u"tabWidget_mode")
        self.tabWidget_mode.setDocumentMode(True)
        self.tab_simple = QWidget()
        self.tab_simple.setObjectName(u"tab_simple")
        self.horizontalLayout_10 = QHBoxLayout(self.tab_simple)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.listWidget_remotes = QListWidget(self.tab_simple)
        __qlistwidgetitem = QListWidgetItem(self.listWidget_remotes)
        __qlistwidgetitem.setText(u"FTP");
        __qlistwidgetitem1 = QListWidgetItem(self.listWidget_remotes)
        __qlistwidgetitem1.setText(u"SFTP");
        __qlistwidgetitem2 = QListWidgetItem(self.listWidget_remotes)
        __qlistwidgetitem2.setText(u"WebDAV");
        QListWidgetItem(self.listWidget_remotes)
        QListWidgetItem(self.listWidget_remotes)
        __qlistwidgetitem3 = QListWidgetItem(self.listWidget_remotes)
        __qlistwidgetitem3.setText(u"Microsoft OneDrive");
        QListWidgetItem(self.listWidget_remotes)
        __qlistwidgetitem4 = QListWidgetItem(self.listWidget_remotes)
        __qlistwidgetitem4.setText(u"HTTP");
        QListWidgetItem(self.listWidget_remotes)
        QListWidgetItem(self.listWidget_remotes)
        QListWidgetItem(self.listWidget_remotes)
        self.listWidget_remotes.setObjectName(u"listWidget_remotes")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_remotes.sizePolicy().hasHeightForWidth())
        self.listWidget_remotes.setSizePolicy(sizePolicy)

        self.horizontalLayout_10.addWidget(self.listWidget_remotes)

        self.tabWidget = QTabWidget(self.tab_simple)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setDocumentMode(True)
        self.tab_ftp = QWidget()
        self.tab_ftp.setObjectName(u"tab_ftp")
        self.verticalLayout_3 = QVBoxLayout(self.tab_ftp)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.tab_ftp)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.lineEdit_ftp_host = QLineEdit(self.tab_ftp)
        self.lineEdit_ftp_host.setObjectName(u"lineEdit_ftp_host")

        self.verticalLayout_4.addWidget(self.lineEdit_ftp_host)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_16 = QLabel(self.tab_ftp)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_5.addWidget(self.label_16)

        self.lineEdit_ftp_port = QLineEdit(self.tab_ftp)
        self.lineEdit_ftp_port.setObjectName(u"lineEdit_ftp_port")
        self.lineEdit_ftp_port.setText(u"21")

        self.verticalLayout_5.addWidget(self.lineEdit_ftp_port)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_4 = QLabel(self.tab_ftp)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_6.addWidget(self.label_4)

        self.lineEdit_ftp_login = QLineEdit(self.tab_ftp)
        self.lineEdit_ftp_login.setObjectName(u"lineEdit_ftp_login")

        self.verticalLayout_6.addWidget(self.lineEdit_ftp_login)


        self.horizontalLayout_4.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_5 = QLabel(self.tab_ftp)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_7.addWidget(self.label_5)

        self.lineEdit_ftp_password = QLineEdit(self.tab_ftp)
        self.lineEdit_ftp_password.setObjectName(u"lineEdit_ftp_password")
        self.lineEdit_ftp_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_7.addWidget(self.lineEdit_ftp_password)


        self.horizontalLayout_4.addLayout(self.verticalLayout_7)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.groupBox = QGroupBox(self.tab_ftp)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setTitle(u"FTPS")
        self.horizontalLayout_7 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.checkBox_ftp_tls = QCheckBox(self.groupBox)
        self.checkBox_ftp_tls.setObjectName(u"checkBox_ftp_tls")
        self.checkBox_ftp_tls.setText(u"TLS")

        self.horizontalLayout_7.addWidget(self.checkBox_ftp_tls)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)

        self.radioButton_ftp_false = QRadioButton(self.groupBox)
        self.radioButton_ftp_false.setObjectName(u"radioButton_ftp_false")
        self.radioButton_ftp_false.setEnabled(False)
        self.radioButton_ftp_false.setChecked(True)

        self.horizontalLayout_7.addWidget(self.radioButton_ftp_false)

        self.radioButton_ftp_true = QRadioButton(self.groupBox)
        self.radioButton_ftp_true.setObjectName(u"radioButton_ftp_true")
        self.radioButton_ftp_true.setEnabled(False)

        self.horizontalLayout_7.addWidget(self.radioButton_ftp_true)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.tabWidget.addTab(self.tab_ftp, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_ftp), u"FTP")
        self.tab_sftp = QWidget()
        self.tab_sftp.setObjectName(u"tab_sftp")
        self.verticalLayout_18 = QVBoxLayout(self.tab_sftp)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_14 = QLabel(self.tab_sftp)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_16.addWidget(self.label_14)

        self.lineEdit_sftp_host = QLineEdit(self.tab_sftp)
        self.lineEdit_sftp_host.setObjectName(u"lineEdit_sftp_host")

        self.verticalLayout_16.addWidget(self.lineEdit_sftp_host)


        self.horizontalLayout_9.addLayout(self.verticalLayout_16)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_15 = QLabel(self.tab_sftp)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_17.addWidget(self.label_15)

        self.lineEdit_sftp_port = QLineEdit(self.tab_sftp)
        self.lineEdit_sftp_port.setObjectName(u"lineEdit_sftp_port")
        self.lineEdit_sftp_port.setText(u"22")

        self.verticalLayout_17.addWidget(self.lineEdit_sftp_port)


        self.horizontalLayout_9.addLayout(self.verticalLayout_17)


        self.verticalLayout_18.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_12 = QLabel(self.tab_sftp)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_14.addWidget(self.label_12)

        self.lineEdit_sftp_login = QLineEdit(self.tab_sftp)
        self.lineEdit_sftp_login.setObjectName(u"lineEdit_sftp_login")

        self.verticalLayout_14.addWidget(self.lineEdit_sftp_login)


        self.horizontalLayout_6.addLayout(self.verticalLayout_14)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_13 = QLabel(self.tab_sftp)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_15.addWidget(self.label_13)

        self.lineEdit_sftp_password = QLineEdit(self.tab_sftp)
        self.lineEdit_sftp_password.setObjectName(u"lineEdit_sftp_password")
        self.lineEdit_sftp_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_15.addWidget(self.lineEdit_sftp_password)


        self.horizontalLayout_6.addLayout(self.verticalLayout_15)


        self.verticalLayout_18.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_7 = QSpacerItem(20, 246, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_7)

        self.tabWidget.addTab(self.tab_sftp, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_sftp), u"SFTP")
        self.tab_webdav = QWidget()
        self.tab_webdav.setObjectName(u"tab_webdav")
        self.verticalLayout_10 = QVBoxLayout(self.tab_webdav)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.tab_webdav)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_10.addWidget(self.label_7)

        self.lineEdit_webdav_url = QLineEdit(self.tab_webdav)
        self.lineEdit_webdav_url.setObjectName(u"lineEdit_webdav_url")

        self.verticalLayout_10.addWidget(self.lineEdit_webdav_url)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_8 = QLabel(self.tab_webdav)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_11.addWidget(self.label_8)

        self.lineEdit_webdav_login = QLineEdit(self.tab_webdav)
        self.lineEdit_webdav_login.setObjectName(u"lineEdit_webdav_login")

        self.verticalLayout_11.addWidget(self.lineEdit_webdav_login)


        self.horizontalLayout.addLayout(self.verticalLayout_11)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_9 = QLabel(self.tab_webdav)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_13.addWidget(self.label_9)

        self.lineEdit_webdav_password = QLineEdit(self.tab_webdav)
        self.lineEdit_webdav_password.setObjectName(u"lineEdit_webdav_password")
        self.lineEdit_webdav_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_13.addWidget(self.lineEdit_webdav_password)


        self.horizontalLayout.addLayout(self.verticalLayout_13)


        self.verticalLayout_10.addLayout(self.horizontalLayout)

        self.label_10 = QLabel(self.tab_webdav)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_10.addWidget(self.label_10)

        self.comboBox_webdav_vendor = QComboBox(self.tab_webdav)
        self.comboBox_webdav_vendor.addItem("")
        self.comboBox_webdav_vendor.addItem(u"Fastmail Files")
        self.comboBox_webdav_vendor.addItem(u"Nextcloud")
        self.comboBox_webdav_vendor.addItem(u"Owncloud")
        self.comboBox_webdav_vendor.addItem("")
        self.comboBox_webdav_vendor.addItem("")
        self.comboBox_webdav_vendor.addItem("")
        self.comboBox_webdav_vendor.setObjectName(u"comboBox_webdav_vendor")

        self.verticalLayout_10.addWidget(self.comboBox_webdav_vendor)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_5)

        self.tabWidget.addTab(self.tab_webdav, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_webdav), u"WebDAV")
        self.tab_google_drive = QWidget()
        self.tab_google_drive.setObjectName(u"tab_google_drive")
        self.verticalLayout_9 = QVBoxLayout(self.tab_google_drive)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.tab_google_drive)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setWordWrap(True)

        self.verticalLayout_9.addWidget(self.label_3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_3)

        self.tabWidget.addTab(self.tab_google_drive, "")
        self.tab_yandex_disk = QWidget()
        self.tab_yandex_disk.setObjectName(u"tab_yandex_disk")
        self.verticalLayout_8 = QVBoxLayout(self.tab_yandex_disk)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.tab_yandex_disk)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.label_6)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_4)

        self.tabWidget.addTab(self.tab_yandex_disk, "")
        self.tab_onedrive = QWidget()
        self.tab_onedrive.setObjectName(u"tab_onedrive")
        self.verticalLayout_12 = QVBoxLayout(self.tab_onedrive)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.tab_onedrive)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setWordWrap(True)

        self.verticalLayout_12.addWidget(self.label_11)

        self.line_2 = QFrame(self.tab_onedrive)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_12.addWidget(self.line_2)

        self.label_28 = QLabel(self.tab_onedrive)
        self.label_28.setObjectName(u"label_28")

        self.verticalLayout_12.addWidget(self.label_28)

        self.comboBox_onedrive_region = QComboBox(self.tab_onedrive)
        self.comboBox_onedrive_region.addItem("")
        self.comboBox_onedrive_region.addItem("")
        self.comboBox_onedrive_region.addItem("")
        self.comboBox_onedrive_region.setObjectName(u"comboBox_onedrive_region")

        self.verticalLayout_12.addWidget(self.comboBox_onedrive_region)

        self.label_29 = QLabel(self.tab_onedrive)
        self.label_29.setObjectName(u"label_29")

        self.verticalLayout_12.addWidget(self.label_29)

        self.comboBox_onedrive_type = QComboBox(self.tab_onedrive)
        self.comboBox_onedrive_type.addItem("")
        self.comboBox_onedrive_type.addItem("")
        self.comboBox_onedrive_type.addItem("")
        self.comboBox_onedrive_type.addItem("")
        self.comboBox_onedrive_type.addItem("")
        self.comboBox_onedrive_type.addItem("")
        self.comboBox_onedrive_type.addItem("")
        self.comboBox_onedrive_type.setObjectName(u"comboBox_onedrive_type")

        self.verticalLayout_12.addWidget(self.comboBox_onedrive_type)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_6)

        self.tabWidget.addTab(self.tab_onedrive, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_onedrive), u"Microsoft OneDrive")
        self.tab_mailru = QWidget()
        self.tab_mailru.setObjectName(u"tab_mailru")
        self.verticalLayout_25 = QVBoxLayout(self.tab_mailru)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_24 = QLabel(self.tab_mailru)
        self.label_24.setObjectName(u"label_24")

        self.verticalLayout_23.addWidget(self.label_24)

        self.lineEdit_mailru_login = QLineEdit(self.tab_mailru)
        self.lineEdit_mailru_login.setObjectName(u"lineEdit_mailru_login")

        self.verticalLayout_23.addWidget(self.lineEdit_mailru_login)


        self.horizontalLayout_3.addLayout(self.verticalLayout_23)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_25 = QLabel(self.tab_mailru)
        self.label_25.setObjectName(u"label_25")

        self.verticalLayout_24.addWidget(self.label_25)

        self.lineEdit_mailru_password = QLineEdit(self.tab_mailru)
        self.lineEdit_mailru_password.setObjectName(u"lineEdit_mailru_password")
        self.lineEdit_mailru_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_24.addWidget(self.lineEdit_mailru_password)


        self.horizontalLayout_3.addLayout(self.verticalLayout_24)


        self.verticalLayout_25.addLayout(self.horizontalLayout_3)

        self.label_26 = QLabel(self.tab_mailru)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setWordWrap(True)

        self.verticalLayout_25.addWidget(self.label_26)

        self.label_27 = QLabel(self.tab_mailru)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setText(u"<a href=\"https://id.mail.ru/security\">https://id.mail.ru/security</a>")
        self.label_27.setTextFormat(Qt.TextFormat.RichText)
        self.label_27.setOpenExternalLinks(True)
        self.label_27.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)

        self.verticalLayout_25.addWidget(self.label_27)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_25.addItem(self.verticalSpacer_10)

        self.tabWidget.addTab(self.tab_mailru, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_mailru), u"Mail.ru Cloud")
        self.tab_http = QWidget()
        self.tab_http.setObjectName(u"tab_http")
        self.verticalLayout_2 = QVBoxLayout(self.tab_http)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.tab_http)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.lineEdit_url = QLineEdit(self.tab_http)
        self.lineEdit_url.setObjectName(u"lineEdit_url")
        self.lineEdit_url.setText(u"http://127.0.0.1:8000/")

        self.verticalLayout_2.addWidget(self.lineEdit_url)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.tab_http, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_http), u"HTTP")
        self.tab_local = QWidget()
        self.tab_local.setObjectName(u"tab_local")
        self.tabWidget.addTab(self.tab_local, "")
        self.tab_alias = QWidget()
        self.tab_alias.setObjectName(u"tab_alias")
        self.verticalLayout_19 = QVBoxLayout(self.tab_alias)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.tab_alias)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setWordWrap(True)

        self.verticalLayout_19.addWidget(self.label_17)

        self.line = QFrame(self.tab_alias)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_19.addWidget(self.line)

        self.label_18 = QLabel(self.tab_alias)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_19.addWidget(self.label_18)

        self.lineEdit_alias_path = QLineEdit(self.tab_alias)
        self.lineEdit_alias_path.setObjectName(u"lineEdit_alias_path")

        self.verticalLayout_19.addWidget(self.lineEdit_alias_path)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_8)

        self.tabWidget.addTab(self.tab_alias, "")
        self.tab_union = QWidget()
        self.tab_union.setObjectName(u"tab_union")
        self.verticalLayout_20 = QVBoxLayout(self.tab_union)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.pushButton_union_add = QPushButton(self.tab_union)
        self.pushButton_union_add.setObjectName(u"pushButton_union_add")

        self.verticalLayout_20.addWidget(self.pushButton_union_add)

        self.scrollArea = QScrollArea(self.tab_union)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 800, 566))
        self.verticalLayout_21 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_union_container = QVBoxLayout()
        self.verticalLayout_union_container.setObjectName(u"verticalLayout_union_container")

        self.verticalLayout_21.addLayout(self.verticalLayout_union_container)

        self.groupBox_union_policies = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_union_policies.setObjectName(u"groupBox_union_policies")
        self.verticalLayout_22 = QVBoxLayout(self.groupBox_union_policies)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_21 = QLabel(self.groupBox_union_policies)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_22.addWidget(self.label_21)

        self.comboBox_2 = QComboBox(self.groupBox_union_policies)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToMinimumContentsLengthWithIcon)

        self.verticalLayout_22.addWidget(self.comboBox_2)

        self.label_22 = QLabel(self.groupBox_union_policies)
        self.label_22.setObjectName(u"label_22")

        self.verticalLayout_22.addWidget(self.label_22)

        self.comboBox_3 = QComboBox(self.groupBox_union_policies)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToMinimumContentsLengthWithIcon)

        self.verticalLayout_22.addWidget(self.comboBox_3)

        self.label_23 = QLabel(self.groupBox_union_policies)
        self.label_23.setObjectName(u"label_23")

        self.verticalLayout_22.addWidget(self.label_23)

        self.comboBox_4 = QComboBox(self.groupBox_union_policies)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToMinimumContentsLengthWithIcon)

        self.verticalLayout_22.addWidget(self.comboBox_4)


        self.verticalLayout_21.addWidget(self.groupBox_union_policies)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_9)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_20.addWidget(self.scrollArea)

        self.tabWidget.addTab(self.tab_union, "")

        self.horizontalLayout_10.addWidget(self.tabWidget)

        self.tabWidget_mode.addTab(self.tab_simple, "")
        self.tab_advanced = QWidget()
        self.tab_advanced.setObjectName(u"tab_advanced")
        self.horizontalLayout_8 = QHBoxLayout(self.tab_advanced)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.listWidget_advanced = QListWidget(self.tab_advanced)
        self.listWidget_advanced.setObjectName(u"listWidget_advanced")
        sizePolicy.setHeightForWidth(self.listWidget_advanced.sizePolicy().hasHeightForWidth())
        self.listWidget_advanced.setSizePolicy(sizePolicy)
        self.listWidget_advanced.setSortingEnabled(True)

        self.horizontalLayout_8.addWidget(self.listWidget_advanced)

        self.scrollArea_advance = QScrollArea(self.tab_advanced)
        self.scrollArea_advance.setObjectName(u"scrollArea_advance")
        self.scrollArea_advance.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea_advance.setWidgetResizable(True)
        self.scrollAreaWidgetContents_advance = QWidget()
        self.scrollAreaWidgetContents_advance.setObjectName(u"scrollAreaWidgetContents_advance")
        self.scrollAreaWidgetContents_advance.setGeometry(QRect(0, 0, 98, 164))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollAreaWidgetContents_advance.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_advance.setSizePolicy(sizePolicy1)
        self.verticalLayout_27 = QVBoxLayout(self.scrollAreaWidgetContents_advance)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.groupBox_required = QGroupBox(self.scrollAreaWidgetContents_advance)
        self.groupBox_required.setObjectName(u"groupBox_required")
        self.verticalLayout_26 = QVBoxLayout(self.groupBox_required)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")

        self.verticalLayout_27.addWidget(self.groupBox_required)

        self.groupBox_not_required = QGroupBox(self.scrollAreaWidgetContents_advance)
        self.groupBox_not_required.setObjectName(u"groupBox_not_required")
        self.verticalLayout_29 = QVBoxLayout(self.groupBox_not_required)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")

        self.verticalLayout_27.addWidget(self.groupBox_not_required)

        self.groupBox_advanced = QGroupBox(self.scrollAreaWidgetContents_advance)
        self.groupBox_advanced.setObjectName(u"groupBox_advanced")
        self.groupBox_advanced.setFlat(True)
        self.groupBox_advanced.setCheckable(True)
        self.groupBox_advanced.setChecked(False)
        self.verticalLayout_28 = QVBoxLayout(self.groupBox_advanced)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")

        self.verticalLayout_27.addWidget(self.groupBox_advanced)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_27.addItem(self.verticalSpacer_11)

        self.scrollArea_advance.setWidget(self.scrollAreaWidgetContents_advance)

        self.horizontalLayout_8.addWidget(self.scrollArea_advance)

        self.tabWidget_mode.addTab(self.tab_advanced, "")

        self.verticalLayout.addWidget(self.tabWidget_mode)

        self.buttonBox = QDialogButtonBox(NewRemoteWindow)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(NewRemoteWindow)
        self.buttonBox.rejected.connect(NewRemoteWindow.reject)

        self.tabWidget_mode.setCurrentIndex(0)
        self.listWidget_remotes.setCurrentRow(-1)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(NewRemoteWindow)
    # setupUi

    def retranslateUi(self, NewRemoteWindow):
        NewRemoteWindow.setWindowTitle(QCoreApplication.translate("NewRemoteWindow", u"New remote", None))
        self.lineEdit_name.setText("")
        self.lineEdit_name.setPlaceholderText(QCoreApplication.translate("NewRemoteWindow", u"Enter name for new remote", None))

        __sortingEnabled = self.listWidget_remotes.isSortingEnabled()
        self.listWidget_remotes.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget_remotes.item(3)
        ___qlistwidgetitem.setText(QCoreApplication.translate("NewRemoteWindow", u"Google Drive", None));
        ___qlistwidgetitem1 = self.listWidget_remotes.item(4)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("NewRemoteWindow", u"Yandex Disk", None));
        ___qlistwidgetitem2 = self.listWidget_remotes.item(6)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("NewRemoteWindow", u"Mail.ru Cloud", None));
        ___qlistwidgetitem3 = self.listWidget_remotes.item(8)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("NewRemoteWindow", u"Local", None));
        ___qlistwidgetitem4 = self.listWidget_remotes.item(9)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("NewRemoteWindow", u"Alias", None));
        ___qlistwidgetitem5 = self.listWidget_remotes.item(10)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("NewRemoteWindow", u"Union", None));
        self.listWidget_remotes.setSortingEnabled(__sortingEnabled)

        self.label_2.setText(QCoreApplication.translate("NewRemoteWindow", u"Host", None))
        self.label_16.setText(QCoreApplication.translate("NewRemoteWindow", u"Port", None))
        self.label_4.setText(QCoreApplication.translate("NewRemoteWindow", u"Login", None))
        self.label_5.setText(QCoreApplication.translate("NewRemoteWindow", u"Password", None))
        self.radioButton_ftp_false.setText(QCoreApplication.translate("NewRemoteWindow", u"Implict", None))
        self.radioButton_ftp_true.setText(QCoreApplication.translate("NewRemoteWindow", u"Explict", None))
        self.label_14.setText(QCoreApplication.translate("NewRemoteWindow", u"Host", None))
        self.label_15.setText(QCoreApplication.translate("NewRemoteWindow", u"Port", None))
        self.label_12.setText(QCoreApplication.translate("NewRemoteWindow", u"Login", None))
        self.label_13.setText(QCoreApplication.translate("NewRemoteWindow", u"Password", None))
        self.label_7.setText(QCoreApplication.translate("NewRemoteWindow", u"URL", None))
        self.label_8.setText(QCoreApplication.translate("NewRemoteWindow", u"Login", None))
        self.label_9.setText(QCoreApplication.translate("NewRemoteWindow", u"Password", None))
        self.label_10.setText(QCoreApplication.translate("NewRemoteWindow", u"Option vendor", None))
        self.comboBox_webdav_vendor.setItemText(0, QCoreApplication.translate("NewRemoteWindow", u"Other site/service or software", None))
        self.comboBox_webdav_vendor.setItemText(4, QCoreApplication.translate("NewRemoteWindow", u"Sharepoint Online, authenticated by Microsoft account", None))
        self.comboBox_webdav_vendor.setItemText(5, QCoreApplication.translate("NewRemoteWindow", u"Sharepoint with NTLM authentication, usually self-hosted or on-premises", None))
        self.comboBox_webdav_vendor.setItemText(6, QCoreApplication.translate("NewRemoteWindow", u"rclone WebDAV server to serve a remote over HTTP via the WebDAV protocol", None))

        self.label_3.setText(QCoreApplication.translate("NewRemoteWindow", u"By pressing the OK button your browser will open and you will be needed to authenticate in Google Drive", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_google_drive), QCoreApplication.translate("NewRemoteWindow", u"Google Drive", None))
        self.label_6.setText(QCoreApplication.translate("NewRemoteWindow", u"By pressing the OK button your browser will open and you will be needed to authenticate in Yandex Disk", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_yandex_disk), QCoreApplication.translate("NewRemoteWindow", u"Yandex Disk", None))
        self.label_11.setText(QCoreApplication.translate("NewRemoteWindow", u"By pressing the OK button your browser will open and you will be needed to authenticate in Microsoft OneDrive", None))
        self.label_28.setText(QCoreApplication.translate("NewRemoteWindow", u"Region", None))
        self.comboBox_onedrive_region.setItemText(0, QCoreApplication.translate("NewRemoteWindow", u"Microsoft Cloud Global", None))
        self.comboBox_onedrive_region.setItemText(1, QCoreApplication.translate("NewRemoteWindow", u"Microsoft Cloud for US Government", None))
        self.comboBox_onedrive_region.setItemText(2, QCoreApplication.translate("NewRemoteWindow", u"Azure and Office 365 operated by Vnet Group in China", None))

        self.label_29.setText(QCoreApplication.translate("NewRemoteWindow", u"Type of connection", None))
        self.comboBox_onedrive_type.setItemText(0, QCoreApplication.translate("NewRemoteWindow", u"OneDrive Personal or Business", None))
        self.comboBox_onedrive_type.setItemText(1, QCoreApplication.translate("NewRemoteWindow", u"Root Sharepoint site", None))
        self.comboBox_onedrive_type.setItemText(2, QCoreApplication.translate("NewRemoteWindow", u"Sharepoint site name or URL", None))
        self.comboBox_onedrive_type.setItemText(3, QCoreApplication.translate("NewRemoteWindow", u"Search for a Sharepoint site", None))
        self.comboBox_onedrive_type.setItemText(4, QCoreApplication.translate("NewRemoteWindow", u"Type in driveID (advanced)", None))
        self.comboBox_onedrive_type.setItemText(5, QCoreApplication.translate("NewRemoteWindow", u"Type in SiteID (advanced)", None))
        self.comboBox_onedrive_type.setItemText(6, QCoreApplication.translate("NewRemoteWindow", u"Sharepoint server-relative path (advanced)", None))

        self.label_24.setText(QCoreApplication.translate("NewRemoteWindow", u"Login", None))
        self.label_25.setText(QCoreApplication.translate("NewRemoteWindow", u"Password", None))
        self.label_26.setText(QCoreApplication.translate("NewRemoteWindow", u"To add Mail.ru you will need to generate a password for external applications in the Mail.ru web control panel. Select \"Full access to Mail. Cloud, Calendar (All Protocols)\". You can generate the password in this url", None))
        self.label.setText(QCoreApplication.translate("NewRemoteWindow", u"URL", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_local), QCoreApplication.translate("NewRemoteWindow", u"Local", None))
        self.label_17.setText(QCoreApplication.translate("NewRemoteWindow", u"Set a new name for a remote or path", None))
        self.label_18.setText(QCoreApplication.translate("NewRemoteWindow", u"Remote or path to alias", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_alias_path.setToolTip(QCoreApplication.translate("NewRemoteWindow", u"Can be \"myremote:path/to/dir\", \"myremote:bucket\", \"myremote:\" or \"/local/path\"", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_alias_path.setPlaceholderText(QCoreApplication.translate("NewRemoteWindow", u"Can be \"myremote:path/to/dir\", \"myremote:bucket\", \"myremote:\" or \"/local/path\"", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_alias), QCoreApplication.translate("NewRemoteWindow", u"Alias", None))
        self.pushButton_union_add.setText(QCoreApplication.translate("NewRemoteWindow", u"Add upstream", None))
        self.groupBox_union_policies.setTitle(QCoreApplication.translate("NewRemoteWindow", u"Behavior / Policies", None))
        self.label_21.setText(QCoreApplication.translate("NewRemoteWindow", u"Action policy (writing existing file)", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("NewRemoteWindow", u"epall (existing path, all): apply to all found", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("NewRemoteWindow", u"all (same as epall)", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("NewRemoteWindow", u"epff (existing path, first found): act on the first one found, by the time upstreams reply, where the relative path exists", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("NewRemoteWindow", u"eplfs (existing path, least free space)", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("NewRemoteWindow", u"eplus (existing path, least used space)", None))
        self.comboBox_2.setItemText(5, QCoreApplication.translate("NewRemoteWindow", u"eplno (existing path, least number of objects)", None))
        self.comboBox_2.setItemText(6, QCoreApplication.translate("NewRemoteWindow", u"epmfs (existing path, most free space)", None))
        self.comboBox_2.setItemText(7, QCoreApplication.translate("NewRemoteWindow", u"eprand (existing path, random)", None))
        self.comboBox_2.setItemText(8, QCoreApplication.translate("NewRemoteWindow", u"ff (first found): same as epff", None))
        self.comboBox_2.setItemText(9, QCoreApplication.translate("NewRemoteWindow", u"lfs (least free space)", None))
        self.comboBox_2.setItemText(10, QCoreApplication.translate("NewRemoteWindow", u"lus (least used space)", None))
        self.comboBox_2.setItemText(11, QCoreApplication.translate("NewRemoteWindow", u"lno (least number of objects)", None))
        self.comboBox_2.setItemText(12, QCoreApplication.translate("NewRemoteWindow", u"mfs (most free space)", None))
        self.comboBox_2.setItemText(13, QCoreApplication.translate("NewRemoteWindow", u"newest", None))
        self.comboBox_2.setItemText(14, QCoreApplication.translate("NewRemoteWindow", u"rand (random)", None))

        self.label_22.setText(QCoreApplication.translate("NewRemoteWindow", u"Create policy (create non-existing file)", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("NewRemoteWindow", u"epmfs (existing path, most free space): of all the upstreams on which the relative path exists choose the one with the most free space", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("NewRemoteWindow", u"all (act on all upstreams)", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("NewRemoteWindow", u"epff (existing path, first found): act on the first one found, by the time upstreams reply, where the relative path exists", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("NewRemoteWindow", u"epall (existing path, all): act on all upstreams where the relative path exists", None))
        self.comboBox_3.setItemText(4, QCoreApplication.translate("NewRemoteWindow", u"eplfs (existing path, least free space)", None))
        self.comboBox_3.setItemText(5, QCoreApplication.translate("NewRemoteWindow", u"eplus (existing path, least used space)", None))
        self.comboBox_3.setItemText(6, QCoreApplication.translate("NewRemoteWindow", u"eplno (existing path, least number of objects)", None))
        self.comboBox_3.setItemText(7, QCoreApplication.translate("NewRemoteWindow", u"eprand (existing path, random)", None))
        self.comboBox_3.setItemText(8, QCoreApplication.translate("NewRemoteWindow", u"ff (first found): act on the first one found by the time upstreams reply", None))
        self.comboBox_3.setItemText(9, QCoreApplication.translate("NewRemoteWindow", u"lfs (least free space)", None))
        self.comboBox_3.setItemText(10, QCoreApplication.translate("NewRemoteWindow", u"lus (least used space)", None))
        self.comboBox_3.setItemText(11, QCoreApplication.translate("NewRemoteWindow", u"lno (least number of objects)", None))
        self.comboBox_3.setItemText(12, QCoreApplication.translate("NewRemoteWindow", u"mfs (most free space)", None))
        self.comboBox_3.setItemText(13, QCoreApplication.translate("NewRemoteWindow", u"newest", None))
        self.comboBox_3.setItemText(14, QCoreApplication.translate("NewRemoteWindow", u"rand (random)", None))

        self.label_23.setText(QCoreApplication.translate("NewRemoteWindow", u"Search policy (reading and listing file)", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("NewRemoteWindow", u"ff (first found): same as epff", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("NewRemoteWindow", u"all (same as epall)", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("NewRemoteWindow", u"epff (existing path, first found): act on the first one found, by the time upstreams reply, where the relative path exists", None))
        self.comboBox_4.setItemText(3, QCoreApplication.translate("NewRemoteWindow", u"epall (existing path, all): given this order configured, act on the first one found where the relative path exists", None))
        self.comboBox_4.setItemText(4, QCoreApplication.translate("NewRemoteWindow", u"eplfs (existing path, least free space)", None))
        self.comboBox_4.setItemText(5, QCoreApplication.translate("NewRemoteWindow", u"eplus (existing path, least used space)", None))
        self.comboBox_4.setItemText(6, QCoreApplication.translate("NewRemoteWindow", u"eplno (existing path, least number of objects)", None))
        self.comboBox_4.setItemText(7, QCoreApplication.translate("NewRemoteWindow", u"epmfs (existing path, most free space)", None))
        self.comboBox_4.setItemText(8, QCoreApplication.translate("NewRemoteWindow", u"eprand (existing path, random)", None))
        self.comboBox_4.setItemText(9, QCoreApplication.translate("NewRemoteWindow", u"lfs (least free space)", None))
        self.comboBox_4.setItemText(10, QCoreApplication.translate("NewRemoteWindow", u"lus (least used space)", None))
        self.comboBox_4.setItemText(11, QCoreApplication.translate("NewRemoteWindow", u"lno (least number of objects)", None))
        self.comboBox_4.setItemText(12, QCoreApplication.translate("NewRemoteWindow", u"mfs (most free space)", None))
        self.comboBox_4.setItemText(13, QCoreApplication.translate("NewRemoteWindow", u"newest", None))
        self.comboBox_4.setItemText(14, QCoreApplication.translate("NewRemoteWindow", u"rand (random)", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_union), QCoreApplication.translate("NewRemoteWindow", u"Union", None))
        self.tabWidget_mode.setTabText(self.tabWidget_mode.indexOf(self.tab_simple), QCoreApplication.translate("NewRemoteWindow", u"Simple", None))
        self.groupBox_required.setTitle(QCoreApplication.translate("NewRemoteWindow", u"Required", None))
        self.groupBox_not_required.setTitle(QCoreApplication.translate("NewRemoteWindow", u"Not required", None))
        self.groupBox_advanced.setTitle(QCoreApplication.translate("NewRemoteWindow", u"Advanced", None))
        self.tabWidget_mode.setTabText(self.tabWidget_mode.indexOf(self.tab_advanced), QCoreApplication.translate("NewRemoteWindow", u"Advanced", None))
    # retranslateUi

