# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'application.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QButtonGroup, QDoubleSpinBox,
    QFrame, QHBoxLayout, QKeySequenceEdit, QLabel,
    QLayout, QRadioButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(486, 396)
        self.verticalLayoutWidget_4 = QWidget(Form)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(30, 10, 181, 371))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.left = QRadioButton(self.verticalLayoutWidget_4)
        self.mouseGroup = QButtonGroup(Form)
        self.mouseGroup.setObjectName(u"mouseGroup")
        self.mouseGroup.addButton(self.left)
        self.left.setObjectName(u"left")
        self.left.setChecked(True)

        self.horizontalLayout.addWidget(self.left)

        self.mid = QRadioButton(self.verticalLayoutWidget_4)
        self.mouseGroup.addButton(self.mid)
        self.mid.setObjectName(u"mid")

        self.horizontalLayout.addWidget(self.mid)

        self.right = QRadioButton(self.verticalLayoutWidget_4)
        self.mouseGroup.addButton(self.right)
        self.right.setObjectName(u"right")

        self.horizontalLayout.addWidget(self.right)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetFixedSize)
        self.click = QRadioButton(self.verticalLayoutWidget_4)
        self.click_form = QButtonGroup(Form)
        self.click_form.setObjectName(u"click_form")
        self.click_form.addButton(self.click)
        self.click.setObjectName(u"click")

        self.horizontalLayout_2.addWidget(self.click)

        self.break_time = QDoubleSpinBox(self.verticalLayoutWidget_4)
        self.break_time.setObjectName(u"break_time")
        self.break_time.setWrapping(False)
        self.break_time.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.break_time.setMinimum(0.010000000000000)

        self.horizontalLayout_2.addWidget(self.break_time)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.press = QRadioButton(self.verticalLayoutWidget_4)
        self.click_form.addButton(self.press)
        self.press.setObjectName(u"press")
        self.press.setChecked(True)

        self.verticalLayout.addWidget(self.press)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.mouse_hotkey_label = QLabel(self.verticalLayoutWidget_4)
        self.mouse_hotkey_label.setObjectName(u"mouse_hotkey_label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mouse_hotkey_label.sizePolicy().hasHeightForWidth())
        self.mouse_hotkey_label.setSizePolicy(sizePolicy)
        self.mouse_hotkey_label.setLayoutDirection(Qt.LeftToRight)
        self.mouse_hotkey_label.setAutoFillBackground(False)
        self.mouse_hotkey_label.setFrameShape(QFrame.StyledPanel)
        self.mouse_hotkey_label.setTextFormat(Qt.AutoText)
        self.mouse_hotkey_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.mouse_hotkey_label)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.mouse_start_label = QLabel(self.verticalLayoutWidget_4)
        self.mouse_start_label.setObjectName(u"mouse_start_label")

        self.horizontalLayout_3.addWidget(self.mouse_start_label)

        self.mouse_start_hotkey = QKeySequenceEdit(self.verticalLayoutWidget_4)
        self.mouse_start_hotkey.setObjectName(u"mouse_start_hotkey")

        self.horizontalLayout_3.addWidget(self.mouse_start_hotkey)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.mouse_end_label = QLabel(self.verticalLayoutWidget_4)
        self.mouse_end_label.setObjectName(u"mouse_end_label")

        self.horizontalLayout_5.addWidget(self.mouse_end_label)

        self.mouse_end_hotkey = QKeySequenceEdit(self.verticalLayoutWidget_4)
        self.mouse_end_hotkey.setObjectName(u"mouse_end_hotkey")

        self.horizontalLayout_5.addWidget(self.mouse_end_hotkey)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalLayoutWidget_5 = QWidget(Form)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(270, 10, 181, 371))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.keyboard_click = QRadioButton(self.verticalLayoutWidget_5)
        self.keyboard_click.setObjectName(u"keyboard_click")

        self.horizontalLayout_4.addWidget(self.keyboard_click)

        self.keyboard_break_time = QDoubleSpinBox(self.verticalLayoutWidget_5)
        self.keyboard_break_time.setObjectName(u"keyboard_break_time")
        self.keyboard_break_time.setWrapping(False)
        self.keyboard_break_time.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.keyboard_break_time.setMinimum(0.010000000000000)

        self.horizontalLayout_4.addWidget(self.keyboard_break_time)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.keyboard_press = QRadioButton(self.verticalLayoutWidget_5)
        self.keyboard_press.setObjectName(u"keyboard_press")
        self.keyboard_press.setChecked(True)

        self.verticalLayout_3.addWidget(self.keyboard_press)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.key_label = QLabel(self.verticalLayoutWidget_5)
        self.key_label.setObjectName(u"key_label")

        self.horizontalLayout_6.addWidget(self.key_label)

        self.keyboard_key = QKeySequenceEdit(self.verticalLayoutWidget_5)
        self.keyboard_key.setObjectName(u"keyboard_key")

        self.horizontalLayout_6.addWidget(self.keyboard_key)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.keyboard_hotkey_label = QLabel(self.verticalLayoutWidget_5)
        self.keyboard_hotkey_label.setObjectName(u"keyboard_hotkey_label")
        sizePolicy.setHeightForWidth(self.keyboard_hotkey_label.sizePolicy().hasHeightForWidth())
        self.keyboard_hotkey_label.setSizePolicy(sizePolicy)
        self.keyboard_hotkey_label.setLayoutDirection(Qt.LeftToRight)
        self.keyboard_hotkey_label.setAutoFillBackground(False)
        self.keyboard_hotkey_label.setFrameShape(QFrame.StyledPanel)
        self.keyboard_hotkey_label.setTextFormat(Qt.AutoText)
        self.keyboard_hotkey_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.keyboard_hotkey_label)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.keyboard_start_label = QLabel(self.verticalLayoutWidget_5)
        self.keyboard_start_label.setObjectName(u"keyboard_start_label")

        self.horizontalLayout_7.addWidget(self.keyboard_start_label)

        self.keyboard_start_hotkey = QKeySequenceEdit(self.verticalLayoutWidget_5)
        self.keyboard_start_hotkey.setObjectName(u"keyboard_start_hotkey")

        self.horizontalLayout_7.addWidget(self.keyboard_start_hotkey)


        self.verticalLayout_6.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.keyboard_end_label = QLabel(self.verticalLayoutWidget_5)
        self.keyboard_end_label.setObjectName(u"keyboard_end_label")

        self.horizontalLayout_8.addWidget(self.keyboard_end_label)

        self.keyboard_end_hotkey = QKeySequenceEdit(self.verticalLayoutWidget_5)
        self.keyboard_end_hotkey.setObjectName(u"keyboard_end_hotkey")

        self.horizontalLayout_8.addWidget(self.keyboard_end_hotkey)


        self.verticalLayout_6.addLayout(self.horizontalLayout_8)


        self.verticalLayout_5.addLayout(self.verticalLayout_6)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(230, -10, 20, 431))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u540e\u53f0\u6309\u952e", None))
        self.left.setText(QCoreApplication.translate("Form", u"\u5de6\u952e", None))
        self.mid.setText(QCoreApplication.translate("Form", u"\u4e2d\u952e", None))
        self.right.setText(QCoreApplication.translate("Form", u"\u53f3\u952e", None))
        self.click.setText(QCoreApplication.translate("Form", u"\u8fde\u70b9", None))
#if QT_CONFIG(tooltip)
        self.break_time.setToolTip(QCoreApplication.translate("Form", u"\u95f4\u9694\u65f6\u95f4", None))
#endif // QT_CONFIG(tooltip)
        self.break_time.setPrefix("")
        self.break_time.setSuffix(QCoreApplication.translate("Form", u"\u79d2", None))
        self.press.setText(QCoreApplication.translate("Form", u"\u957f\u6309", None))
        self.mouse_hotkey_label.setText(QCoreApplication.translate("Form", u"\u9f20\u6807\u64cd\u4f5c\u5feb\u6377\u952e", None))
        self.mouse_start_label.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb:", None))
        self.mouse_start_hotkey.setKeySequence(QCoreApplication.translate("Form", u"Shift+F8", None))
        self.mouse_end_label.setText(QCoreApplication.translate("Form", u"\u7ed3\u675f:", None))
        self.mouse_end_hotkey.setKeySequence(QCoreApplication.translate("Form", u"Shift+F7", None))
        self.keyboard_click.setText(QCoreApplication.translate("Form", u"\u8fde\u6309", None))
#if QT_CONFIG(tooltip)
        self.keyboard_break_time.setToolTip(QCoreApplication.translate("Form", u"\u95f4\u9694\u65f6\u95f4", None))
#endif // QT_CONFIG(tooltip)
        self.keyboard_break_time.setPrefix("")
        self.keyboard_break_time.setSuffix(QCoreApplication.translate("Form", u"\u79d2", None))
        self.keyboard_press.setText(QCoreApplication.translate("Form", u"\u957f\u6309", None))
        self.key_label.setText(QCoreApplication.translate("Form", u"\u6309\u952e:", None))
        self.keyboard_hotkey_label.setText(QCoreApplication.translate("Form", u"\u952e\u76d8\u64cd\u4f5c\u5feb\u6377\u952e", None))
        self.keyboard_start_label.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb:", None))
        self.keyboard_start_hotkey.setKeySequence(QCoreApplication.translate("Form", u"F8", None))
        self.keyboard_end_label.setText(QCoreApplication.translate("Form", u"\u7ed3\u675f:", None))
        self.keyboard_end_hotkey.setKeySequence(QCoreApplication.translate("Form", u"F7", None))
    # retranslateUi

