# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_window.ui'
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
    QDialog, QDialogButtonBox, QHBoxLayout, QLabel,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        if not SettingsWindow.objectName():
            SettingsWindow.setObjectName(u"SettingsWindow")
        SettingsWindow.resize(400, 300)
        SettingsWindow.setModal(True)
        self.verticalLayout = QVBoxLayout(SettingsWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(SettingsWindow)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.comboBox_language = QComboBox(SettingsWindow)
        self.comboBox_language.setObjectName(u"comboBox_language")

        self.horizontalLayout_3.addWidget(self.comboBox_language)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(SettingsWindow)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.comboBox_style = QComboBox(SettingsWindow)
        self.comboBox_style.setObjectName(u"comboBox_style")

        self.horizontalLayout.addWidget(self.comboBox_style)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(SettingsWindow)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.comboBox_palette = QComboBox(SettingsWindow)
        self.comboBox_palette.setObjectName(u"comboBox_palette")

        self.horizontalLayout_2.addWidget(self.comboBox_palette)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(SettingsWindow)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.spinBox_depth = QSpinBox(SettingsWindow)
        self.spinBox_depth.setObjectName(u"spinBox_depth")
        self.spinBox_depth.setMinimum(1)

        self.horizontalLayout_4.addWidget(self.spinBox_depth)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.checkBox_tray = QCheckBox(SettingsWindow)
        self.checkBox_tray.setObjectName(u"checkBox_tray")

        self.verticalLayout.addWidget(self.checkBox_tray)

        self.checkBox_autorun = QCheckBox(SettingsWindow)
        self.checkBox_autorun.setObjectName(u"checkBox_autorun")

        self.verticalLayout.addWidget(self.checkBox_autorun)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(SettingsWindow)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(SettingsWindow)
        self.buttonBox.accepted.connect(SettingsWindow.accept)
        self.buttonBox.rejected.connect(SettingsWindow.reject)

        QMetaObject.connectSlotsByName(SettingsWindow)
    # setupUi

    def retranslateUi(self, SettingsWindow):
        SettingsWindow.setWindowTitle(QCoreApplication.translate("SettingsWindow", u"Settings", None))
        self.label_3.setText(QCoreApplication.translate("SettingsWindow", u"Language (restart required)", None))
        self.label.setText(QCoreApplication.translate("SettingsWindow", u"Style", None))
        self.label_2.setText(QCoreApplication.translate("SettingsWindow", u"Palette", None))
        self.label_4.setText(QCoreApplication.translate("SettingsWindow", u"Path depth", None))
        self.checkBox_tray.setText(QCoreApplication.translate("SettingsWindow", u"Minimize to tray instead of closing the application", None))
        self.checkBox_autorun.setText(QCoreApplication.translate("SettingsWindow", u"Launch at user login", None))
    # retranslateUi

