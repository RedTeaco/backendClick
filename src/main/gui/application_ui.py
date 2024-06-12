# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'application.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            Qt)
from PySide6.QtWidgets import (QFrame, QHBoxLayout,
                               QKeySequenceEdit, QLabel, QLayout, QListWidget,
                               QPushButton, QSizePolicy, QSpacerItem,
                               QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(640, 480)
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 10, 641, 471))
        self.verticalLayout_7 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setSizeConstraint(QLayout.SetFixedSize)
        self.horizontalLayout_12.setContentsMargins(-1, -1, -1, 10)
        self.horizontalSpacer = QSpacerItem(40, 1, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setSizeConstraint(QLayout.SetFixedSize)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setSizeConstraint(QLayout.SetFixedSize)
        self.catch_window_label = QLabel(self.verticalLayoutWidget)
        self.catch_window_label.setObjectName(u"catch_window_label")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.catch_window_label.sizePolicy().hasHeightForWidth())
        self.catch_window_label.setSizePolicy(sizePolicy)

        self.horizontalLayout_10.addWidget(self.catch_window_label)

        self.catch_window_hotkey = QKeySequenceEdit(self.verticalLayoutWidget)
        self.catch_window_hotkey.setObjectName(u"catch_window_hotkey")
        self.catch_window_hotkey.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout_10.addWidget(self.catch_window_hotkey)


        self.verticalLayout_8.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setSizeConstraint(QLayout.SetFixedSize)
        self.window_name_label = QLabel(self.verticalLayoutWidget)
        self.window_name_label.setObjectName(u"window_name_label")
        sizePolicy.setHeightForWidth(self.window_name_label.sizePolicy().hasHeightForWidth())
        self.window_name_label.setSizePolicy(sizePolicy)

        self.horizontalLayout_11.addWidget(self.window_name_label)

        self.window_name = QLabel(self.verticalLayoutWidget)
        self.window_name.setObjectName(u"window_name")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.window_name.sizePolicy().hasHeightForWidth())
        self.window_name.setSizePolicy(sizePolicy1)
        self.window_name.setScaledContents(False)

        self.horizontalLayout_11.addWidget(self.window_name)


        self.verticalLayout_8.addLayout(self.horizontalLayout_11)


        self.horizontalLayout_12.addLayout(self.verticalLayout_8)

        self.horizontalSpacer_2 = QSpacerItem(40, 1, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_2)


        self.verticalLayout_7.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_4.setContentsMargins(20, 0, 20, 20)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, -1, -1)
        self.add_mel_button = QPushButton(self.verticalLayoutWidget)
        self.add_mel_button.setObjectName(u"add_mel_button")

        self.horizontalLayout.addWidget(self.add_mel_button)

        self.remove_mel_button = QPushButton(self.verticalLayoutWidget)
        self.remove_mel_button.setObjectName(u"remove_mel_button")

        self.horizontalLayout.addWidget(self.remove_mel_button)

        self.clear_mel_button = QPushButton(self.verticalLayoutWidget)
        self.clear_mel_button.setObjectName(u"clear_mel_button")

        self.horizontalLayout.addWidget(self.clear_mel_button)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.mouse_event_list = QListWidget(self.verticalLayoutWidget)
        self.mouse_event_list.setObjectName(u"mouse_event_list")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mouse_event_list.sizePolicy().hasHeightForWidth())
        self.mouse_event_list.setSizePolicy(sizePolicy2)

        self.verticalLayout_4.addWidget(self.mouse_event_list)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.mouse_hotkey_label = QLabel(self.verticalLayoutWidget)
        self.mouse_hotkey_label.setObjectName(u"mouse_hotkey_label")
        sizePolicy1.setHeightForWidth(self.mouse_hotkey_label.sizePolicy().hasHeightForWidth())
        self.mouse_hotkey_label.setSizePolicy(sizePolicy1)
        self.mouse_hotkey_label.setLayoutDirection(Qt.LeftToRight)
        self.mouse_hotkey_label.setAutoFillBackground(False)
        self.mouse_hotkey_label.setFrameShape(QFrame.StyledPanel)
        self.mouse_hotkey_label.setTextFormat(Qt.AutoText)
        self.mouse_hotkey_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.mouse_hotkey_label)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.mouse_start_label = QLabel(self.verticalLayoutWidget)
        self.mouse_start_label.setObjectName(u"mouse_start_label")

        self.horizontalLayout_3.addWidget(self.mouse_start_label)

        self.mouse_start_hotkey = QKeySequenceEdit(self.verticalLayoutWidget)
        self.mouse_start_hotkey.setObjectName(u"mouse_start_hotkey")
        sizePolicy.setHeightForWidth(self.mouse_start_hotkey.sizePolicy().hasHeightForWidth())
        self.mouse_start_hotkey.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.mouse_start_hotkey)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)

        self.mouse_stop_label = QLabel(self.verticalLayoutWidget)
        self.mouse_stop_label.setObjectName(u"mouse_stop_label")

        self.horizontalLayout_5.addWidget(self.mouse_stop_label)

        self.mouse_stop_hotkey = QKeySequenceEdit(self.verticalLayoutWidget)
        self.mouse_stop_hotkey.setObjectName(u"mouse_stop_hotkey")
        sizePolicy.setHeightForWidth(self.mouse_stop_hotkey.sizePolicy().hasHeightForWidth())
        self.mouse_stop_hotkey.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.mouse_stop_hotkey)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)


        self.horizontalLayout_9.addLayout(self.verticalLayout_4)

        self.line = QFrame(self.verticalLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_9.addWidget(self.line)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(20, 0, 20, 20)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.add_kel_btn = QPushButton(self.verticalLayoutWidget)
        self.add_kel_btn.setObjectName(u"add_kel_btn")

        self.horizontalLayout_6.addWidget(self.add_kel_btn)

        self.remove_kel_btn = QPushButton(self.verticalLayoutWidget)
        self.remove_kel_btn.setObjectName(u"remove_kel_btn")

        self.horizontalLayout_6.addWidget(self.remove_kel_btn)

        self.clear_kel_btn = QPushButton(self.verticalLayoutWidget)
        self.clear_kel_btn.setObjectName(u"clear_kel_btn")

        self.horizontalLayout_6.addWidget(self.clear_kel_btn)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

        self.keyboard_event_list = QListWidget(self.verticalLayoutWidget)
        self.keyboard_event_list.setObjectName(u"keyboard_event_list")
        sizePolicy2.setHeightForWidth(self.keyboard_event_list.sizePolicy().hasHeightForWidth())
        self.keyboard_event_list.setSizePolicy(sizePolicy2)

        self.verticalLayout_5.addWidget(self.keyboard_event_list)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.keyboard_hotkey_label = QLabel(self.verticalLayoutWidget)
        self.keyboard_hotkey_label.setObjectName(u"keyboard_hotkey_label")
        sizePolicy1.setHeightForWidth(self.keyboard_hotkey_label.sizePolicy().hasHeightForWidth())
        self.keyboard_hotkey_label.setSizePolicy(sizePolicy1)
        self.keyboard_hotkey_label.setLayoutDirection(Qt.LeftToRight)
        self.keyboard_hotkey_label.setAutoFillBackground(False)
        self.keyboard_hotkey_label.setFrameShape(QFrame.StyledPanel)
        self.keyboard_hotkey_label.setTextFormat(Qt.AutoText)
        self.keyboard_hotkey_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.keyboard_hotkey_label)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_9)

        self.keyboard_start_label = QLabel(self.verticalLayoutWidget)
        self.keyboard_start_label.setObjectName(u"keyboard_start_label")

        self.horizontalLayout_7.addWidget(self.keyboard_start_label)

        self.keyboard_start_hotkey = QKeySequenceEdit(self.verticalLayoutWidget)
        self.keyboard_start_hotkey.setObjectName(u"keyboard_start_hotkey")

        self.horizontalLayout_7.addWidget(self.keyboard_start_hotkey)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_10)


        self.verticalLayout_6.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_11)

        self.keyboard_stop_label = QLabel(self.verticalLayoutWidget)
        self.keyboard_stop_label.setObjectName(u"keyboard_stop_label")

        self.horizontalLayout_8.addWidget(self.keyboard_stop_label)

        self.keyboard_stop_hotkey = QKeySequenceEdit(self.verticalLayoutWidget)
        self.keyboard_stop_hotkey.setObjectName(u"keyboard_stop_hotkey")

        self.horizontalLayout_8.addWidget(self.keyboard_stop_hotkey)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_12)


        self.verticalLayout_6.addLayout(self.horizontalLayout_8)


        self.verticalLayout_5.addLayout(self.verticalLayout_6)


        self.horizontalLayout_9.addLayout(self.verticalLayout_5)


        self.verticalLayout_7.addLayout(self.horizontalLayout_9)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u540e\u53f0\u6309\u952e", None))
        self.catch_window_label.setText(QCoreApplication.translate("Form", u"\u7a97\u53e3\u6355\u83b7", None))
        self.window_name_label.setText(QCoreApplication.translate("Form", u"\u7a97\u53e3\u540d\uff1a", None))
        self.window_name.setText("")
#if QT_CONFIG(tooltip)
        self.add_mel_button.setToolTip(QCoreApplication.translate("Form", u"\u6dfb\u52a0\u9f20\u6807\u4e8b\u4ef6", None))
#endif // QT_CONFIG(tooltip)
        self.add_mel_button.setText(QCoreApplication.translate("Form", u"\u6dfb\u52a0", None))
#if QT_CONFIG(tooltip)
        self.remove_mel_button.setToolTip(QCoreApplication.translate("Form", u"\u5220\u9664\u9f20\u6807\u4e8b\u4ef6", None))
#endif // QT_CONFIG(tooltip)
        self.remove_mel_button.setText(QCoreApplication.translate("Form", u"\u5220\u9664", None))
#if QT_CONFIG(tooltip)
        self.clear_mel_button.setToolTip(QCoreApplication.translate("Form", u"\u6e05\u7a7a\u9f20\u6807\u4e8b\u4ef6\u5217\u8868", None))
#endif // QT_CONFIG(tooltip)
        self.clear_mel_button.setText(QCoreApplication.translate("Form", u"\u6e05\u7a7a", None))
        self.mouse_hotkey_label.setText(QCoreApplication.translate("Form", u"\u9f20\u6807\u64cd\u4f5c\u5feb\u6377\u952e", None))
        self.mouse_start_label.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb:", None))
        self.mouse_stop_label.setText(QCoreApplication.translate("Form", u"\u7ed3\u675f:", None))
#if QT_CONFIG(tooltip)
        self.add_kel_btn.setToolTip(QCoreApplication.translate("Form", u"\u6dfb\u52a0\u952e\u76d8\u4e8b\u4ef6", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.add_kel_btn.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.add_kel_btn.setText(QCoreApplication.translate("Form", u"\u6dfb\u52a0", None))
#if QT_CONFIG(tooltip)
        self.remove_kel_btn.setToolTip(QCoreApplication.translate("Form", u"\u5220\u9664\u952e\u76d8\u4e8b\u4ef6", None))
#endif // QT_CONFIG(tooltip)
        self.remove_kel_btn.setText(QCoreApplication.translate("Form", u"\u5220\u9664", None))
#if QT_CONFIG(tooltip)
        self.clear_kel_btn.setToolTip(QCoreApplication.translate("Form", u"\u6e05\u7a7a\u952e\u76d8\u4e8b\u4ef6\u5217\u8868", None))
#endif // QT_CONFIG(tooltip)
        self.clear_kel_btn.setText(QCoreApplication.translate("Form", u"\u6e05\u7a7a", None))
        self.keyboard_hotkey_label.setText(QCoreApplication.translate("Form", u"\u952e\u76d8\u64cd\u4f5c\u5feb\u6377\u952e", None))
        self.keyboard_start_label.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb:", None))
        self.keyboard_stop_label.setText(QCoreApplication.translate("Form", u"\u7ed3\u675f:", None))
    # retranslateUi

