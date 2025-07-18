import os
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialog, QFileDialog

import app.main_window as main_window
from app.views import new_serve_window


class NewServeWindow(QDialog):
    def __init__(self, parent=None, protocol: str = '', path: str = '', user: str = '', password: str = '', address: str = '', read_only: bool = False, args: str = ''):
        super(NewServeWindow, self).__init__()
        self.ui = new_serve_window.Ui_NewServeWindow()
        self.ui.setupUi(self)

        self.parent: main_window.MainWindow = parent

        self.setWindowIcon(
            QIcon(os.path.dirname(__file__) + '/resources/' + 'favicon.ico'))

        self.ui.buttonBox.accepted.connect(self.new_serve)
        self.ui.button_select_dir.clicked.connect(self.select_dir)
        self.ui.checkBox_use_ram.toggled.connect(self.use_ram)

        match protocol:
            case 'ftp':
                self.ui.radioButton_ftp.setChecked(True)
            case 'dnla':
                self.ui.radioButton_dnla.setChecked(True)
            case 'http':
                self.ui.radioButton_http.setChecked(True)
            case 'webdav':
                self.ui.radioButton_webdav.setChecked(True)
            case 'sftp':
                self.ui.radioButton_sftp.setChecked(True)
            case 's3':
                self.ui.radioButton_s3.setChecked(True)
        self.ui.lineEdit_path.setText(path)
        self.ui.lineEdit_username.setText(user)
        self.ui.lineEdit_password.setText(password)
        self.ui.lineEdit_address.setText(address)
        self.ui.checkBox_read_only.setChecked(read_only)
        if path == ':memory:':
            self.ui.checkBox_use_ram.setChecked(True)
        self.ui.lineEdit_args.setText(args)

    def select_dir(self):
        path = QFileDialog.getExistingDirectory()
        if path is not None and path != '':
            self.ui.lineEdit_path.setText(path)

    def use_ram(self, value):
        if value:
            self.ui.lineEdit_path.setText(':memory:')
            self.ui.lineEdit_path.setEnabled(False)
            self.ui.button_select_dir.setEnabled(False)
        else:
            self.ui.lineEdit_path.setEnabled(True)
            self.ui.button_select_dir.setEnabled(True)

    def new_serve(self):
        path = self.ui.lineEdit_path.text()
        user = self.ui.lineEdit_username.text()
        password = self.ui.lineEdit_password.text()
        address = self.ui.lineEdit_address.text()
        read_only = self.ui.checkBox_read_only.isChecked()
        args = self.ui.lineEdit_args.text()
        if self.ui.radioButton_ftp.isChecked():
            protocol = 'ftp'
            if address.strip() == '':
                address = 'localhost:2121'
        elif self.ui.radioButton_dnla.isChecked():
            protocol = 'dnla'
            if address.strip() == '':
                address = ':7879'
        elif self.ui.radioButton_http.isChecked():
            protocol = 'http'
            read_only = True
            if address.strip() == '':
                address = '127.0.0.1:8080'
        elif self.ui.radioButton_webdav.isChecked():
            protocol = 'webdav'
            if address.strip() == '':
                address = 'http://127.0.0.1:8080'
        elif self.ui.radioButton_sftp.isChecked():
            protocol = 'sftp'
            if not user or not password:
                args += '--no-auth'
            if address.strip() == '':
                address = 'localhost:2022'
        elif self.ui.radioButton_s3.isChecked():
            protocol = 's3'
            if address.strip() == '':
                address = 'http://127.0.0.1:8080'

        self.parent.create_serve(protocol, path, user,
                                 password, address, read_only, args=args)
        self.accept()
