# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mouse_event_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt)
from PySide6.QtWidgets import (QAbstractSpinBox, QComboBox,
                               QDialogButtonBox, QDoubleSpinBox, QHBoxLayout,
                               QLabel, QRadioButton, QVBoxLayout,
                               QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setWindowModality(Qt.ApplicationModal)
        Dialog.resize(300, 200)
        Dialog.setModal(True)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(40, 150, 211, 23))
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 10, 231, 131))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.mouse_btn_box = QComboBox(self.verticalLayoutWidget)
        self.mouse_btn_box.addItem("")
        self.mouse_btn_box.addItem("")
        self.mouse_btn_box.addItem("")
        self.mouse_btn_box.setObjectName(u"mouse_btn_box")
        self.mouse_btn_box.setMinimumSize(QSize(100, 0))
        self.mouse_btn_box.setMaxVisibleItems(3)
        self.mouse_btn_box.setMaxCount(3)

        self.horizontalLayout_2.addWidget(self.mouse_btn_box)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.is_click_btn = QRadioButton(self.verticalLayoutWidget)
        self.is_click_btn.setObjectName(u"is_click_btn")

        self.horizontalLayout_3.addWidget(self.is_click_btn)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.break_time_box = QDoubleSpinBox(self.verticalLayoutWidget)
        self.break_time_box.setObjectName(u"break_time_box")
        self.break_time_box.setEnabled(False)
        self.break_time_box.setMinimumSize(QSize(75, 0))
        self.break_time_box.setMouseTracking(True)
        self.break_time_box.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.break_time_box.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.break_time_box.setMinimum(0.010000000000000)

        self.horizontalLayout_4.addWidget(self.break_time_box)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_4)


        self.horizontalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Dialog)
        self.is_click_btn.toggled.connect(self.break_time_box.setEnabled)

        self.mouse_btn_box.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u9f20\u6807\u4e8b\u4ef6\u6dfb\u52a0", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u9f20\u6807\u6309\u952e", None))
        self.mouse_btn_box.setItemText(0, QCoreApplication.translate("Dialog", u"\u9f20\u6807\u5de6\u952e", None))
        self.mouse_btn_box.setItemText(1, QCoreApplication.translate("Dialog", u"\u9f20\u6807\u4e2d\u952e", None))
        self.mouse_btn_box.setItemText(2, QCoreApplication.translate("Dialog", u"\u9f20\u6807\u53f3\u952e", None))

        self.mouse_btn_box.setCurrentText(QCoreApplication.translate("Dialog", u"\u9f20\u6807\u5de6\u952e", None))
        self.is_click_btn.setText(QCoreApplication.translate("Dialog", u"\u8fde\u70b9", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u95f4\u9694\u65f6\u95f4", None))
        self.break_time_box.setSuffix(QCoreApplication.translate("Dialog", u"\u79d2", None))
    # retranslateUi

