# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'keyboard_event_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt)
from PySide6.QtWidgets import (QAbstractSpinBox, QDialogButtonBox, QDoubleSpinBox, QHBoxLayout, QLabel,
                               QRadioButton, QSizePolicy, QVBoxLayout, QWidget)

from gui.component import ShortcutKeyEdit


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(300, 200)
        Dialog.setModal(True)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(40, 150, 211, 23))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(51, 45, 191, 91))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.shortcut_key_edit = ShortcutKeyEdit(self.verticalLayoutWidget)
        self.shortcut_key_edit.setObjectName(u"shortcut_key_edit")

        self.horizontalLayout_3.addWidget(self.shortcut_key_edit)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.is_tap_btn = QRadioButton(self.verticalLayoutWidget)
        self.is_tap_btn.setObjectName(u"is_tap_btn")

        self.horizontalLayout_2.addWidget(self.is_tap_btn)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.break_time_box = QDoubleSpinBox(self.verticalLayoutWidget)
        self.break_time_box.setObjectName(u"break_time_box")
        self.break_time_box.setEnabled(False)
        self.break_time_box.setMinimumSize(QSize(75, 0))
        self.break_time_box.setMouseTracking(True)
        self.break_time_box.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.break_time_box.setMinimum(0.010000000000000)

        self.horizontalLayout.addWidget(self.break_time_box)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.is_tap_btn.toggled.connect(self.break_time_box.setEnabled)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u952e\u76d8\u4e8b\u4ef6\u6dfb\u52a0", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u952e\u76d8\u6309\u952e", None))
        self.is_tap_btn.setText(QCoreApplication.translate("Dialog", u"\u8fde\u6309", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u95f4\u9694\u65f6\u95f4", None))
        self.break_time_box.setSuffix(QCoreApplication.translate("Dialog", u"\u79d2", None))
    # retranslateUi

