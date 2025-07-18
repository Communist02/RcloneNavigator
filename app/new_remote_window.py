import os

from PySide6.QtCore import QRegularExpression, Qt
from PySide6.QtGui import QIcon, QIntValidator, QRegularExpressionValidator
from PySide6.QtWidgets import QCheckBox, QComboBox, QDialog, QLineEdit, QListWidgetItem, QMessageBox, QWidget
from app.main_window import QLabel
from app.rclone import Rclone
from app.views import new_remote_window
from app.views.upstream_widget import Ui_Upstream


class Upstream(QWidget):
    def __init__(self, index, parent=None):
        super().__init__(parent)
        self.ui = Ui_Upstream()
        self.ui.setupUi(self)

        self.index = index
        self.ui.label_number.setText(str(index + 1))
        self.ui.comboBox_attribute.setItemData(
            1, ':ro', Qt.ItemDataRole.ToolTipRole)
        self.ui.comboBox_attribute.setItemData(
            2, ':nc', Qt.ItemDataRole.ToolTipRole)
        tip = self.tr('New files are first created in the specified layer, then (if needed) moved to the target layer.\nThis is useful if the primary layer is slow or unreliable, but you want to temporarily store files elsewhere.')
        self.ui.comboBox_attribute.setItemData(
            3, ':writeback\n' + tip, Qt.ItemDataRole.ToolTipRole)

    def set_index(self, index: int):
        self.index = index
        self.ui.label_number.setText(str(index + 1))


class NewRemoteWindow(QDialog):
    def __init__(self, edit_mode: bool = False, remote_name: str = None):
        super(NewRemoteWindow, self).__init__()
        self.ui = new_remote_window.Ui_NewRemoteWindow()
        self.ui.setupUi(self)

        rc = Rclone()
        self.providers = rc.providers()
        self.remote = {}
        self.edit_mode = edit_mode
        self.upstreams = []

        self.setWindowIcon(
            QIcon(os.path.dirname(__file__) + '/resources/' + 'favicon.ico'))
        self.ui.tabWidget.tabBar().hide()

        self.ui.buttonBox.accepted.connect(
            lambda: self.new_remote(remote_name))
        self.ui.checkBox_ftp_tls.clicked.connect(self.set_view_ftp_tls_option)
        self.ui.pushButton_union_add.clicked.connect(self.add_upstream)

        self.ui.listWidget_remotes.currentRowChanged.connect(
            self.ui.tabWidget.setCurrentIndex)
        self.ui.listWidget_advanced.currentItemChanged.connect(
            self.remote_view)

        reg_exp = QRegularExpression('[a-zA-ZА-Яа-яЁё0-9_\\.\\-\\+@\\* ]*$')
        validator = QRegularExpressionValidator(reg_exp)
        self.ui.lineEdit_name.setValidator(validator)
        self.ui.groupBox_union_policies.hide()

        if edit_mode:
            self.setWindowTitle(self.tr('Edit') + ' ' + remote_name[:-1])
            config = rc.config('dump')
            remote_type = config[remote_name[:-1]]['type']
            self.ui.lineEdit_name.setText(remote_name[:-1])
            self.ui.tabWidget_mode.tabBar().hide()
            self.ui.tabWidget_mode.setCurrentIndex(1)
            self.ui.listWidget_advanced.hide()
            self.ui.listWidget_advanced.setSortingEnabled(False)

        for provider in self.providers:
            item = QListWidgetItem(f'{provider['Description']}')
            item.setToolTip(provider['Name'])
            self.ui.listWidget_advanced.addItem(item)
            if edit_mode and remote_type == provider['Name']:
                self.remote = config[remote_name[:-1]]
                self.ui.listWidget_advanced.setCurrentRow(
                    self.ui.listWidget_advanced.count() - 1)
                break

        if not edit_mode:
            self.ui.listWidget_advanced.setCurrentRow(0)

    def set_view_ftp_tls_option(self, value):
        self.ui.radioButton_ftp_false.setEnabled(value)
        self.ui.radioButton_ftp_true.setEnabled(value)

    def add_upstream(self):
        upstream = Upstream(len(self.upstreams))
        self.ui.verticalLayout_union_container.addWidget(upstream)
        self.upstreams.append(
            {'widget': upstream, 'remote': '', 'attribute': ''})
        upstream.destroyed.connect(
            lambda: self.delete_upstream(upstream.index))
        upstream.ui.lineEdit_remote.textChanged.connect(
            lambda text: self.upstreams[upstream.index].__setitem__('remote', text))
        upstream.ui.toolButton_up.clicked.connect(
            lambda: self.up_upstream(upstream.index))
        upstream.ui.toolButton_down.clicked.connect(
            lambda: self.down_upstream(upstream.index))
        upstream.ui.comboBox_attribute.currentIndexChanged.connect(
            lambda index: self.upstreams[upstream.index].__setitem__('attribute', ['', ':ro', ':nc', ':writeback'][index]))

    def delete_upstream(self, index):
        self.upstreams.pop(index)
        for i in range(len(self.upstreams)):
            self.upstreams[i]['widget'].set_index(i)

    def up_upstream(self, index):
        if index > 0:
            self.upstreams[index -
                           1], self.upstreams[index] = self.upstreams[index], self.upstreams[index - 1]
            self.ui.verticalLayout_union_container.insertWidget(
                index, self.upstreams[index]['widget'])
            self.upstreams[index]['widget'].set_index(index)
            self.upstreams[index - 1]['widget'].set_index(index - 1)

    def down_upstream(self, index):
        if index < len(self.upstreams) - 1:
            self.upstreams[index +
                           1], self.upstreams[index] = self.upstreams[index], self.upstreams[index + 1]
            self.ui.verticalLayout_union_container.insertWidget(
                index, self.upstreams[index]['widget'])
            self.upstreams[index]['widget'].set_index(index)
            self.upstreams[index + 1]['widget'].set_index(index + 1)

    def remote_view(self, item):
        provider: dict[str, dict] = list(
            filter(lambda x: x['Name'] == item.toolTip(), self.providers))[0]

        if not self.edit_mode:
            self.remote = {'type': provider['Name']}

        is_required_show = False
        is_not_required_show = False
        is_advanced_show = False

        for i in range(self.ui.groupBox_advanced.layout().count()):
            self.ui.groupBox_advanced.layout().itemAt(i).widget().deleteLater()
        for i in range(self.ui.groupBox_required.layout().count()):
            self.ui.groupBox_required.layout().itemAt(i).widget().deleteLater()
        for i in range(self.ui.groupBox_not_required.layout().count()):
            self.ui.groupBox_not_required.layout().itemAt(i).widget().deleteLater()

        def toggle_content(value):
            for child in self.ui.groupBox_advanced.children():
                if isinstance(child, QWidget):
                    child.setVisible(value)
            if value:
                self.ui.groupBox_advanced.setFocus()

        self.ui.groupBox_advanced.toggled.connect(toggle_content)

        options = []
        for option in provider['Options']:
            if option['Name'] in options:
                continue
            options.append(option['Name'])
            label_help = QLabel(option['Help'], wordWrap=True)
            label_help.setEnabled(False)

            if option['Advanced']:
                is_advanced_show = True
                layout = self.ui.groupBox_advanced.layout()
            elif option['Required']:
                is_required_show = True
                layout = self.ui.groupBox_required.layout()
                if not self.edit_mode:
                    self.remote[option['Name']] = option['Default']
            else:
                is_not_required_show = True
                layout = self.ui.groupBox_not_required.layout()

            if option['Type'] != 'bool':
                layout.addWidget(QLabel(option['Name']))
                layout.addWidget(label_help)

            match option['Type']:
                case 'string' | 'SpaceSepList':
                    if not option.get('Examples', False):
                        if option['Type'] == 'SpaceSepList' and option['Default'] is not None:
                            s = ''
                            for string in option['Default']:
                                s += f'{string} '
                            widget = QLineEdit(s.strip())
                        else:
                            widget = QLineEdit(option['Default'])
                        if option['IsPassword']:
                            widget.setEchoMode(QLineEdit.EchoMode.Password)
                        widget.textChanged.connect(
                            lambda text, name=option['Name']: self.remote.__setitem__(name, text))
                        if self.edit_mode and option['Name'] in self.remote and not option['IsPassword']:
                            widget.setText(self.remote[option['Name']])
                    else:
                        widget = QComboBox(editable=True)
                        for example in option['Examples']:
                            widget.addItem(example['Value'])
                            widget.setItemData(
                                widget.count() - 1, example['Help'], Qt.ItemDataRole.ToolTipRole)
                        widget.editTextChanged.connect(
                            lambda text, name=option['Name']: self.remote.__setitem__(name, text))
                        if self.edit_mode and option['Name'] in self.remote:
                            widget.setCurrentText(self.remote[option['Name']])
                        else:
                            if option['Type'] == 'SpaceSepList':
                                s = ''
                                for string in option['Default']:
                                    s += f'"{string}" '
                                widget.setCurrentText(s.lstrip())
                            else:
                                widget.setCurrentText(option['Default'])
                    layout.addWidget(widget)
                case 'int':
                    line_edit = QLineEdit(str(option['Default']))
                    line_edit.setValidator(QIntValidator())
                    layout.addWidget(line_edit)
                    line_edit.textChanged.connect(
                        lambda text, name=option['Name']: self.remote.__setitem__(name, text))
                    if self.edit_mode and option['Name'] in self.remote:
                        line_edit.setText(str(self.remote[option['Name']]))
                case 'bool':
                    checkbox = QCheckBox()
                    checkbox.setText(option['Name'])
                    layout.addWidget(checkbox)
                    layout.addWidget(label_help)
                    checkbox.toggled.connect(
                        lambda value, name=option['Name']: self.remote.__setitem__(name, value))
                    if self.edit_mode and option['Name'] in self.remote:
                        checkbox.setChecked(bool(self.remote[option['Name']]))
                    else:
                        checkbox.setChecked(option['Default'])

        self.ui.groupBox_required.setVisible(is_required_show)
        self.ui.groupBox_not_required.setVisible(is_not_required_show)
        self.ui.groupBox_advanced.setVisible(is_advanced_show)
        if not self.ui.groupBox_advanced.isChecked():
            toggle_content(False)

    def new_remote(self, remote_name_delete: str = None):
        name = self.ui.lineEdit_name.text().strip()
        rc = Rclone()

        if name != '':
            if remote_name_delete is not None and remote_name_delete != name:
                rc.config('delete', f'"{remote_name_delete[:-1]}"')
            if self.ui.tabWidget_mode.currentIndex() == 0:
                match self.ui.tabWidget.currentWidget().objectName():
                    case 'tab_google_drive':
                        rc.create_remote(
                            name, remote_type='drive')
                        self.close()
                    case 'tab_yandex_disk':
                        rc.create_remote(
                            name, remote_type='yandex')
                        self.close()
                    case 'tab_ftp':
                        if self.ui.checkBox_ftp_tls.isChecked():
                            explicit_tls = str(
                                self.ui.radioButton_ftp_true.isChecked()).lower()
                        else:
                            explicit_tls = 'false'
                        rc.create_remote(name,
                                         remote_type='ftp',
                                         host=self.ui.lineEdit_ftp_host.text().strip(),
                                         port=self.ui.lineEdit_ftp_port.text().strip(),
                                         user=self.ui.lineEdit_ftp_login.text().strip(),
                                         tls=str(
                                             self.ui.checkBox_ftp_tls.isChecked()).lower(),
                                         explicit_tls=explicit_tls
                                         )
                        if self.ui.lineEdit_ftp_password.text().strip() != '':
                            rc.config('password', name, 'pass',
                                      self.ui.lineEdit_ftp_password.text().strip())
                        self.close()
                    case 'tab_webdav':
                        vendor = ['other', 'fastmail', 'nextcloud', 'owncloud', 'sharepoint',
                                  'sharepoint-ntlm', 'rclone'][self.ui.comboBox_webdav_vendor.currentIndex()]
                        rc.create_remote(name,
                                         remote_type='webdav',
                                         url=self.ui.lineEdit_webdav_url.text().strip(),
                                         user=self.ui.lineEdit_webdav_login.text().strip(),
                                         vendor=vendor
                                         )
                        if self.ui.lineEdit_webdav_password.text().strip() != '':
                            rc.config('password', name, 'pass',
                                      self.ui.lineEdit_webdav_password.text().strip())
                        self.close()
                    case 'tab_http':
                        rc.create_remote(
                            name, remote_type='http', url=self.ui.lineEdit_url.text().strip())
                        self.close()
                    case 'tab_local':
                        rc.create_remote(
                            name, remote_type='local')
                        self.close()
                    case 'tab_onedrive':
                        region = [
                            'global', 'us', 'cn'][self.ui.comboBox_onedrive_region.currentIndex()]
                        config_type = ['onedrive', 'sharepoint', 'url', 'search', 'driveid',
                                       'siteid', 'path'][self.ui.comboBox_onedrive_type.currentIndex()]
                        rc.create_remote(
                            name, remote_type='onedrive', region=region, config_type=config_type)
                        self.close()
                    case 'tab_mailru':
                        rc.create_remote(name, remote_type='mailru',
                                         user=self.ui.lineEdit_mailru_login.text().strip())
                        if self.ui.lineEdit_mailru_password.text().strip() != '':
                            rc.config('password', name, 'pass',
                                      self.ui.lineEdit_mailru_password.text().strip())
                        self.close()
                    case 'tab_sftp':
                        rc.create_remote(name,
                                         remote_type='sftp',
                                         host=self.ui.lineEdit_sftp_host.text().strip(),
                                         port=self.ui.lineEdit_sftp_port.text().strip(),
                                         user=self.ui.lineEdit_sftp_login.text().strip()
                                         )
                        if self.ui.lineEdit_sftp_password.text().strip() != '':
                            rc.config('password', name, 'pass',
                                      self.ui.lineEdit_sftp_password.text().strip())
                        self.close()
                    case 'tab_alias':
                        rc.create_remote(
                            name, remote_type='alias', remote=self.ui.lineEdit_alias_path.text().strip())
                        self.close()
                    case 'tab_union':
                        upstreams = ''
                        for upstream in self.upstreams:
                            upstreams += f'\\"{upstream['remote']}'
                            if upstream['attribute'] != '':
                                upstreams += f'{upstream['attribute']}\\" '
                            else:
                                upstreams += '\\" '
                        rc.create_remote(
                            name, remote_type='union', upstreams=upstreams)
                        self.close()
            else:
                arg = ''
                for key, value in self.remote.items():
                    if key != 'type':
                        match value:
                            case str():
                                arg += f'{key}="{value.replace('"', '\\"')}" '
                            case int():
                                arg += f'{key}={value} '
                            case bool():
                                arg += f'{key}={str(value).lower()} '
                rc.create_remote(name, self.remote['type'], arg)
                self.close()
        else:
            QMessageBox.warning(self, self.tr('Enter name'),
                                self.tr('Enter name for new remote') + '!')
