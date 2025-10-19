# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about_window.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QLabel, QPlainTextEdit, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_AboutWindow(object):
    def setupUi(self, AboutWindow):
        if not AboutWindow.objectName():
            AboutWindow.setObjectName(u"AboutWindow")
        AboutWindow.resize(360, 240)
        self.verticalLayout = QVBoxLayout(AboutWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(AboutWindow)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setText(u"Rclone Navigator")

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(AboutWindow)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.label_4 = QLabel(AboutWindow)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setText(u"<html><head/><body><p><a href=\"https://github.com/Communist02/RcloneExplorer\"><span style=\" text-decoration: underline; color:#fb9d8b;\">https://github.com/Communist02/RcloneNavigator</span></a></p></body></html>")
        self.label_4.setTextFormat(Qt.TextFormat.RichText)
        self.label_4.setOpenExternalLinks(True)
        self.label_4.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)

        self.verticalLayout.addWidget(self.label_4)

        self.plainTextEdit = QPlainTextEdit(AboutWindow)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.plainTextEdit)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(AboutWindow)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.buttonBox = QDialogButtonBox(AboutWindow)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Ok)

        self.horizontalLayout.addWidget(self.buttonBox)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(AboutWindow)
        self.buttonBox.accepted.connect(AboutWindow.accept)
        self.buttonBox.rejected.connect(AboutWindow.reject)

        QMetaObject.connectSlotsByName(AboutWindow)
    # setupUi

    def retranslateUi(self, AboutWindow):
        AboutWindow.setWindowTitle(QCoreApplication.translate("AboutWindow", u"About", None))
        self.label_2.setText(QCoreApplication.translate("AboutWindow", u"The program for managing files in cloud storage", None))
        self.label_3.setText(QCoreApplication.translate("AboutWindow", u"Copyright \u00a9 2025 Denis Mazur", None))
    # retranslateUi

