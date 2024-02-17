import os.path
import sys
import threading
import time

import keyboard
import win32gui
from PySide6.QtCore import QSettings
from PySide6.QtGui import QKeySequence
from PySide6.QtWidgets import QApplication, QWidget, QInputDialog

import keyboardClick
import mouseClick
from application_ui import Ui_Form


class Application:
    def __init__(self):
        self.window = None
        self.mouse_key = [mouseClick.MOUSE_LEFT, mouseClick.MOUSE_MID, mouseClick.MOUSE_RIGHT]
        self.ui = Ui_Form()
        self.app_data = QSettings('config.ini', QSettings.IniFormat)
        self.handle = None
        self.mouse_flag = True
        self.keyboard_flag = True
        self.mouse_pos = ()
        self.mouse_lock = False
        self.keyboard_lock = False
        if not os.path.exists('config.ini'):
            self.app_data.setValue('Common/capture_hotkey', 'k')
            self.app_data.beginGroup('Mouse')
            self.app_data.setValue('mouse_key', mouseClick.MOUSE_LEFT)
            self.app_data.setValue('click_type', 0)
            self.app_data.setValue('break_time', 0.01)
            self.app_data.setValue('start_hotkey', 'f8')
            self.app_data.setValue('stop_hotkey', 'f7')
            self.app_data.endGroup()
            self.app_data.beginGroup('Keyboard')
            self.app_data.setValue('key', 'F')
            self.app_data.setValue('press_type', 0)
            self.app_data.setValue('break_time', 0.01)
            self.app_data.setValue('start_hotkey', 'shift+f8')
            self.app_data.setValue('stop_hotkey', 'shift+f7')
            self.app_data.endGroup()
            self.app_data.sync()

    def main(self):
        app = QApplication(sys.argv)
        self.window = QWidget()
        self.window.resize(480, 400)
        self.window.setFixedSize(480, 400)  # 限制窗口大小
        self.ui.setupUi(self.window)
        self.set_button_id()
        self.read_config()
        self.app_listener()
        self.window.show()
        exit(app.exec())

    def read_config(self):
        """
        Read config
        :return:
        """
        mouse = {mouseClick.MOUSE_LEFT: self.ui.left, mouseClick.MOUSE_MID: self.ui.mid,
                 mouseClick.MOUSE_RIGHT: self.ui.right}
        app_data = self.app_data
        self.ui.mouse_start_hotkey.setKeySequence(QKeySequence.fromString(app_data.value('Mouse/start_hotkey')))
        self.ui.mouse_end_hotkey.setKeySequence(QKeySequence.fromString(app_data.value('Mouse/stop_hotkey')))
        mouse[app_data.value("Mouse/mouse_key")].setChecked(True)
        self.ui.click_form.buttons()[app_data.value("Mouse/click_type", type=int)].setChecked(True)
        self.ui.break_time.setDisabled(bool(app_data.value("Mouse/click_type", type=int)))
        self.ui.break_time.setValue(app_data.value("Mouse/break_time", type=float))
        self.ui.catch_window_hotkey.setKeySequence(QKeySequence.fromString(app_data.value('Common/capture_hotkey')))
        self.ui.keyboard_key.setKeySequence(QKeySequence.fromString(app_data.value('Keyboard/key')))
        self.ui.keyboard_break_time.setValue(app_data.value("Keyboard/break_time", type=float))
        self.ui.keyboardGroup.buttons()[app_data.value("Keyboard/press_type", type=int)].setChecked(True)
        self.ui.keyboard_break_time.setDisabled(bool(app_data.value("Keyboard/press_type", type=int)))
        self.ui.keyboard_start_hotkey.setKeySequence(QKeySequence.fromString(app_data.value('Keyboard/start_hotkey')))
        self.ui.keyboard_end_hotkey.setKeySequence(QKeySequence.fromString(app_data.value('Keyboard/stop_hotkey')))

        keyboard.add_hotkey(app_data.value("Common/capture_hotkey"), self.handle_capture)  # 捕捉窗口句柄快捷键

        keyboard.add_hotkey(app_data.value("Mouse/start_hotkey"), self.mouse_start)  # 鼠标开始快捷键
        keyboard.add_hotkey(app_data.value("Mouse/stop_hotkey"), self.mouse_stop)  # 鼠标停止快捷键

        keyboard.add_hotkey(app_data.value("Keyboard/start_hotkey"), self.keyboard_start)  # 键盘开始快捷键
        keyboard.add_hotkey(app_data.value("Keyboard/stop_hotkey"), self.keyboard_stop)  # 键盘停止快捷键

    def set_button_id(self):
        mouse_group = self.ui.mouseGroup
        mouse_click = self.ui.click_form
        keyboard_click = self.ui.keyboardGroup
        id1 = 0
        for button in mouse_group.buttons():
            mouse_group.setId(button, id1)
            id1 += 1
        id2 = 0
        for button in mouse_click.buttons():
            mouse_click.setId(button, id2)
            id2 += 1
        id3 = 0
        for button in keyboard_click.buttons():
            keyboard_click.setId(button, id3)
            id3 += 1

    def app_listener(self):
        self.ui.catch_window_hotkey.editingFinished.connect(self.set_handle_caputre_hotkey)  # 改动捕获窗口句柄热键槽函数连接
        # 改动鼠标点击按键槽函数连接 左键|中键|右键
        self.ui.left.clicked.connect(self.set_mouse_type)
        self.ui.mid.clicked.connect(self.set_mouse_type)
        self.ui.right.clicked.connect(self.set_mouse_type)

        self.ui.click.clicked[bool].connect(self.ui.break_time.setEnabled)  # 改动鼠标使用方式为连点槽函数连接
        self.ui.click.clicked.connect(self.set_mouse_click_type)
        self.ui.press.clicked[bool].connect(self.ui.break_time.setDisabled)  # 改动鼠标使用方式为长按槽函数连接
        self.ui.press.clicked.connect(self.set_mouse_click_type)

        self.ui.break_time.editingFinished.connect(self.set_break_time)  # 改动鼠标连点间隔时间槽函数连接

        self.ui.mouse_start_hotkey.editingFinished.connect(self.set_mouse_start_hotkey)  # 改动鼠标开始热键槽函数链接
        self.ui.mouse_end_hotkey.editingFinished.connect(self.set_mouse_stop_hotkey)  # 改动鼠标结束热键槽函数连接

        self.ui.keyboard_start_hotkey.editingFinished.connect(self.set_keyboard_start_hotkey)  # 改动键盘开始热键槽函数连接
        self.ui.keyboard_end_hotkey.editingFinished.connect(self.set_keyboard_stop_hotkey)  # 改动键盘停止热键槽函数连接

        self.ui.keyboard_key.editingFinished.connect(self.set_keyboard_key)  # 改动键盘按键槽函数连接

        self.ui.keyboard_click.clicked[bool].connect(self.ui.keyboard_break_time.setEnabled)  # 改动键盘使用方式为连点槽函数连接
        self.ui.keyboard_click.clicked.connect(self.set_keyboard_click_type)
        self.ui.keyboard_press.clicked[bool].connect(self.ui.keyboard_break_time.setDisabled)  # 改动键盘使用方式为长按槽函数连接
        self.ui.keyboard_press.clicked.connect(self.set_keyboard_click_type)
        self.ui.keyboard_break_time.editingFinished.connect(self.set_keyboard_break_time)  # 改动键盘连点间隔时间槽函数连接
        self.ui.specButton.clicked.connect(self.set_sys_key)  # 特殊快捷键选择

    # -----------------------窗口句柄捕获函数-start--------------------------#
    def handle_capture(self):
        """
        捕捉窗口句柄
        :return:
        """
        pos = win32gui.GetCursorPos()
        self.handle = win32gui.WindowFromPoint(pos)
        self.ui.window_name.setText(win32gui.GetWindowText(self.handle))

    def set_handle_caputre_hotkey(self, key: str) -> None:
        """
        更改捕捉窗口句柄的快捷键
        :param key: 快捷键
        :return:
        """
        keyboard.remove_hotkey(self.app_data.value("Common/capture_hotkey"))
        keyboard.add_hotkey(key, self.handle_capture)
        self.app_data.setValue("Common/capture_hotkey", key)
        self.app_data.sync()

    # -----------------------窗口句柄捕获函数-end--------------------------#

    # -----------------------鼠标操作函数-start--------------------------#
    def set_mouse_type(self):
        """
        设置鼠标按键 左键|中键|右键
        :return:
        """
        mouse_type_id = self.ui.mouseGroup.checkedId()
        self.app_data.setValue("Mouse/mouse_key", self.mouse_key[mouse_type_id])
        self.app_data.sync()

    def set_mouse_click_type(self):
        """
        设置鼠标按键形式 长按|连点
        :return:
        """
        mouse_type = self.ui.click_form.checkedId()
        self.app_data.setValue("Mouse/click_type", mouse_type)
        self.app_data.sync()

    def set_mouse_start_hotkey(self):
        """
        更改鼠标开始快捷键
        :return:
        """
        mouse_click_hotkey = QKeySequence.listToString(self.ui.mouse_start_hotkey.keySequence()).lower()
        keyboard.remove_hotkey(self.app_data.value("Mouse/start_hotkey"))
        keyboard.add_hotkey(mouse_click_hotkey, self.mouse_start)
        self.app_data.setValue("Mouse/start_hotkey", mouse_click_hotkey)
        self.app_data.sync()

    def set_mouse_stop_hotkey(self):
        """
        更改鼠标结束快捷键
        :return:
        """
        mouse_click_hotkey = QKeySequence.listToString(self.ui.mouse_start_hotkey.keySequence()).lower()
        keyboard.remove_hotkey(self.app_data.value("Mouse/stop_hotkey"))
        keyboard.add_hotkey(mouse_click_hotkey, self.mouse_stop)
        self.app_data.setValue("Mouse/stop_hotkey", mouse_click_hotkey)
        self.app_data.sync()

    def set_break_time(self):
        """设置鼠标连点间隔时间"""
        break_time = self.ui.break_time.value()
        self.app_data.setValue("Mouse/break_time", break_time)
        self.app_data.sync()

    def mouse_start(self):
        """
        鼠标操作开始函数
        :return:
        """
        if self.mouse_lock:
            return
        self.mouse_lock = True
        self.mouse_pos = win32gui.GetCursorPos()
        if self.ui.press.isChecked():
            mouseClick.mouse_down(self.handle, self.mouse_pos[0], self.mouse_pos[1],
                                  self.mouse_key[self.ui.mouseGroup.checkedId()])
        else:
            self.mouse_flag = True
            th = threading.Thread(target=self.mouse_click, name="mouse_click")
            th.start()

    def mouse_click(self):
        while self.mouse_flag:
            mouseClick.mouse_click(self.handle, self.mouse_pos[0], self.mouse_pos[1],
                                   self.mouse_key[self.ui.mouseGroup.checkedId()])
            time.sleep(self.ui.break_time.value())

    def mouse_stop(self):
        """
        鼠标操作停止函数
        :return:
        """
        self.mouse_lock = False
        if self.ui.press.isChecked():
            mouseClick.mouse_up(self.handle, self.mouse_pos[0], self.mouse_pos[1],
                                self.mouse_key[self.ui.mouseGroup.checkedId()])
        else:
            self.mouse_flag = False

    # -----------------------鼠标操作函数-end--------------------------#

    # -----------------------键盘操作函数-start--------------------------#
    def set_sys_key(self):
        """
        sign: specButton_clicked
        设置Shift/Ctrl等无法单独设置的快捷键
        :return:
        """
        keys = ('shift', 'ctrl', 'alt')
        key, ok = QInputDialog.getItem(self.window, "select specific key", '特殊按键列表', keys, 0, False)
        if ok and key:
            self.ui.keyboard_key.setKeySequence(str(key))
            self.set_keyboard_key()

    def set_keyboard_start_hotkey(self):
        keyboard_click_hotkey = QKeySequence.listToString(self.ui.keyboard_start_hotkey.keySequence()).lower()
        keyboard.remove_hotkey(self.app_data.value("Keyboard/start_hotkey"))
        keyboard.add_hotkey(keyboard_click_hotkey, self.keyboard_start)
        self.app_data.setValue("Keyboard/start_hotkey", keyboard_click_hotkey)
        self.app_data.sync()

    def set_keyboard_stop_hotkey(self):
        keyboard_click_hotkey = QKeySequence.listToString(self.ui.keyboard_end_hotkey.keySequence()).lower()
        keyboard.remove_hotkey(self.app_data.value("Keyboard/stop_hotkey"))
        keyboard.add_hotkey(keyboard_click_hotkey, self.keyboard_stop)
        self.app_data.setValue("Keyboard/stop_hotkey", keyboard_click_hotkey)
        self.app_data.sync()

    def set_keyboard_break_time(self):
        """设置键盘连点间隔时间"""
        break_time = self.ui.keyboard_break_time.value()
        self.app_data.setValue("Keyboard/break_time", break_time)
        self.app_data.sync()

    def set_keyboard_key(self):
        key = QKeySequence.listToString(self.ui.keyboard_key.keySequence()).lower()
        self.app_data.setValue("Keyboard/key", key)
        self.app_data.sync()

    def set_keyboard_click_type(self):
        """
        设置键盘按键形式 长按|连点
        :return:
        """
        keyboard_type = self.ui.keyboardGroup.checkedId()
        self.app_data.setValue("Keyboard/press_type", keyboard_type)
        self.app_data.sync()

    def keyboard_start(self):
        if self.keyboard_lock:
            return
        self.keyboard_lock = True
        if self.ui.keyboard_press.isChecked():
            # 获取快捷键框中的按键并转换为小写字符串
            keyboardClick.key_down(self.handle, QKeySequence.listToString(self.ui.keyboard_key.keySequence()).lower())
        else:
            self.keyboard_flag = True
            th = threading.Thread(target=self.keyboard_click, name="keyboard_start")
            th.start()

    def keyboard_click(self):
        while self.keyboard_flag:
            keyboardClick.key_down(self.handle, QKeySequence.listToString(self.ui.keyboard_key.keySequence()).lower())
            time.sleep(self.ui.keyboard_break_time.value())

    def keyboard_stop(self):
        self.keyboard_lock = False
        if self.ui.keyboard_press.isChecked():
            keyboardClick.key_up(self.handle, QKeySequence.listToString(self.ui.keyboard_key.keySequence()).lower())
        else:
            self.keyboard_flag = False

    # -----------------------键盘操作函数-end--------------------------#


if __name__ == '__main__':
    app = Application()
    app.main()
