# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'upstream_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QSizePolicy, QSpacerItem,
    QToolButton, QVBoxLayout, QWidget)

class Ui_Upstream(object):
    def setupUi(self, Upstream):
        if not Upstream.objectName():
            Upstream.setObjectName(u"Upstream")
        Upstream.resize(342, 134)
        self.verticalLayout = QVBoxLayout(Upstream)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Upstream)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(4, 2, 4, 4)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_number = QLabel(self.frame)
        self.label_number.setObjectName(u"label_number")
        self.label_number.setText(u"Number")

        self.horizontalLayout_5.addWidget(self.label_number)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.toolButton_down = QToolButton(self.frame)
        self.toolButton_down.setObjectName(u"toolButton_down")
        self.toolButton_down.setText(u"Down")
        self.toolButton_down.setArrowType(Qt.ArrowType.DownArrow)

        self.horizontalLayout_5.addWidget(self.toolButton_down)

        self.toolButton_up = QToolButton(self.frame)
        self.toolButton_up.setObjectName(u"toolButton_up")
        self.toolButton_up.setText(u"Up")
        self.toolButton_up.setArrowType(Qt.ArrowType.UpArrow)

        self.horizontalLayout_5.addWidget(self.toolButton_up)

        self.toolButton_delete = QToolButton(self.frame)
        self.toolButton_delete.setObjectName(u"toolButton_delete")
        self.toolButton_delete.setText(u"Delete")
        icon = QIcon(QIcon.fromTheme(u"edit-delete"))
        self.toolButton_delete.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.toolButton_delete)


        self.verticalLayout_30.addLayout(self.horizontalLayout_5)

        self.label_19 = QLabel(self.frame)
        self.label_19.setObjectName(u"label_19")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)

        self.verticalLayout_30.addWidget(self.label_19)

        self.lineEdit_remote = QLineEdit(self.frame)
        self.lineEdit_remote.setObjectName(u"lineEdit_remote")

        self.verticalLayout_30.addWidget(self.lineEdit_remote)

        self.label_20 = QLabel(self.frame)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_30.addWidget(self.label_20)

        self.comboBox_attribute = QComboBox(self.frame)
        self.comboBox_attribute.addItem("")
        self.comboBox_attribute.addItem("")
        self.comboBox_attribute.addItem("")
        self.comboBox_attribute.addItem("")
        self.comboBox_attribute.setObjectName(u"comboBox_attribute")

        self.verticalLayout_30.addWidget(self.comboBox_attribute)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Upstream)
        self.toolButton_delete.clicked.connect(Upstream.deleteLater)

        QMetaObject.connectSlotsByName(Upstream)
    # setupUi

    def retranslateUi(self, Upstream):
        self.label_19.setText(QCoreApplication.translate("Upstream", u"Remote", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_remote.setToolTip(QCoreApplication.translate("Upstream", u"Can be \"myremote:path/to/dir\", \"myremote:bucket\", \"myremote:\" or \"/local/path\"", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_remote.setPlaceholderText(QCoreApplication.translate("Upstream", u"Can be \"myremote:path/to/dir\", \"myremote:bucket\", \"myremote:\" or \"/local/path\"", None))
        self.label_20.setText(QCoreApplication.translate("Upstream", u"Attribute", None))
        self.comboBox_attribute.setItemText(0, QCoreApplication.translate("Upstream", u"None", None))
        self.comboBox_attribute.setItemText(1, QCoreApplication.translate("Upstream", u"Files will only be read from here and never written", None))
        self.comboBox_attribute.setItemText(2, QCoreApplication.translate("Upstream", u"New files or directories won't be created here", None))
        self.comboBox_attribute.setItemText(3, QCoreApplication.translate("Upstream", u"Files found in different remotes will be written back here", None))

        pass
    # retranslateUi

