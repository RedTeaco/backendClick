import os.path
import sys
from dataclasses import dataclass
from queue import Queue
from typing import List

import keyboard
import win32gui
from PySide6.QtCore import QSettings, Qt, qDebug
from PySide6.QtGui import QKeySequence
from PySide6.QtWidgets import QApplication, QWidget, QListWidgetItem, QDialog

from api import mouse_api
from consumer.keyboard_consumer import KeyboardConsumer, KeyboardEvent
from consumer.mouse_consumer import MouseConsumer, MouseEvent
from gui import mouse_event_dialog_ui, keyboard_event_dialog_ui
from gui.application_ui import Ui_Form


@dataclass
class mouse_event_data:
    button: str
    is_click: bool
    break_time: float = 0.01

    def toString(self):
        if self.is_click:
            return f"按键:{self.button}\t连点:是\t间隔时间:{self.break_time}秒"
        else:
            return f"按键:{self.button}\t连点:否"

    @staticmethod
    def fromString(string: str):
        split_string_list: list = string.split(":", 3)
        print(split_string_list)
        if split_string_list[2][0] == "是":

            return mouse_event_data(
                button=split_string_list[1][:4],
                is_click=True,
                break_time=split_string_list[3][:-1]
            )
        else:
            return mouse_event_data(
                button=split_string_list[1][:4],
                is_click=False
            )


@dataclass
class keyboard_event_data:
    key: str
    is_tap: bool
    break_time: float = 0.01

    def toString(self):
        if self.is_tap:
            return f"按键:{self.key}\t连按:是\t间隔时间:{self.break_time}秒"
        else:
            return f"按键:{self.key}\t连点:否"

    @staticmethod
    def fromString(string: str):
        split_string_list: list = string.strip().split(":", 3)
        print(split_string_list)
        if split_string_list[2][0] == "是":
            return keyboard_event_data(
                key=split_string_list[1][:-3],
                is_tap=True,
                break_time=split_string_list[3][:-1]
            )
        else:
            return keyboard_event_data(
                key=split_string_list[1][:-3],
                is_tap=False
            )


class AppLogic:
    def __init__(self, config_file_path: str = 'config.ini'):
        self.window = None
        self.mouse_button = [mouse_api.MOUSE_LEFT, mouse_api.MOUSE_MID, mouse_api.MOUSE_RIGHT]
        self.ui = Ui_Form()
        self.app_data = QSettings(config_file_path, QSettings.IniFormat)
        self.handle = None

        self.mouse_workers: List[MouseConsumer] = []
        self.mouse_lock = False
        self.mouse_pos = ()
        self.mouse_list = []
        self.mouse_queue = Queue()

        self.keyboard_workers: List[KeyboardConsumer] = []
        self.keyboard_lock = False
        self.keyboard_list = []
        self.keyboard_queue = Queue()

        # init config file
        if not os.path.exists(config_file_path):
            self.app_data.setValue('Common/capture_hotkey', 'k')
            self.app_data.beginGroup('Mouse')
            self.app_data.setValue('mouse_list', self.mouse_list)
            self.app_data.setValue('start_hotkey', 'f8')
            self.app_data.setValue('stop_hotkey', 'f7')
            self.app_data.endGroup()
            self.app_data.beginGroup('Keyboard')
            self.app_data.setValue('keyboard_list', self.keyboard_list)
            self.app_data.setValue('start_hotkey', 'shift+f8')
            self.app_data.setValue('stop_hotkey', 'shift+f7')
            self.app_data.endGroup()
            self.app_data.sync()

    def main(self):
        bk_click = QApplication(sys.argv)
        self.window = QWidget()
        self.window.setFixedSize(self.window.size())
        self.ui.setupUi(self.window)
        self.read_config()
        self.app_listener()
        self.window.show()
        sys.exit(bk_click.exec())

    def read_config(self):
        """
        将Config文件中的设置读取并应用于GUI
        :return:
        """
        app_data = self.app_data
        self.ui.mouse_start_hotkey.setKeySequence(QKeySequence.fromString(app_data.value('Mouse/start_hotkey')))
        self.ui.mouse_stop_hotkey.setKeySequence(QKeySequence.fromString(app_data.value('Mouse/stop_hotkey')))

        if app_data.value('Mouse/mouse_list'):
            # 当配置文件中只存入了一个元素(event)时，value()返回值为str,当存入了多个元素时,value()返回值为列表
            mouse_events = [app_data.value('Mouse/mouse_list')] if type(
                app_data.value('Mouse/mouse_list')) is str else app_data.value('Mouse/mouse_list')
            for mouse_event in mouse_events:
                mouse_event_item = QListWidgetItem()
                mouse_event_item.setText(mouse_event)
                mouse_event_item.setData(Qt.UserRole, mouse_event)
                self.ui.mouse_event_list.addItem(mouse_event_item)

        if app_data.value('Keyboard/keyboard_list'):
            # 当配置文件中只存入了一个元素(event)时，value()返回值为str,当存入了多个元素时,value()返回值为列表
            keyboard_events = [app_data.value('Keyboard/keyboard_list')] if type(
                app_data.value('Keyboard/keyboard_list')) is str else app_data.value('Keyboard/keyboard_list')
            for keyboard_event in keyboard_events:
                keyboard_event_item = QListWidgetItem()
                keyboard_event_item.setText(keyboard_event)
                keyboard_event_item.setData(Qt.UserRole, keyboard_event)
                self.ui.keyboard_event_list.addItem(keyboard_event_item)

        self.ui.catch_window_hotkey.setKeySequence(QKeySequence.fromString(app_data.value('Common/capture_hotkey')))

        self.ui.keyboard_start_hotkey.setKeySequence(QKeySequence.fromString(app_data.value('Keyboard/start_hotkey')))
        self.ui.keyboard_stop_hotkey.setKeySequence(QKeySequence.fromString(app_data.value('Keyboard/stop_hotkey')))
        keyboard.add_hotkey(app_data.value("Common/capture_hotkey"), self.handle_capture)  # 捕捉窗口句柄快捷键

        keyboard.add_hotkey(app_data.value("Mouse/start_hotkey"), self.mouse_start)  # 鼠标开始快捷键
        keyboard.add_hotkey(app_data.value("Mouse/stop_hotkey"), self.mouse_stop)  # 鼠标停止快捷键

        keyboard.add_hotkey(app_data.value("Keyboard/start_hotkey"), self.keyboard_start)  # 键盘开始快捷键
        keyboard.add_hotkey(app_data.value("Keyboard/stop_hotkey"), self.keyboard_stop)  # 键盘停止快捷键

    def app_listener(self):
        """
        添加槽函数连接
        """
        self.ui.catch_window_hotkey.editingFinished.connect(self.set_handle_capture_hotkey)
        # 改动 捕获窗口句柄 热键 槽函数连接
        self.ui.lockWindow.clicked.connect(self.lock_btn_click)
        # 锁定窗口按钮

        self.ui.mouse_start_hotkey.editingFinished.connect(self.set_mouse_start_hotkey)
        # 改动 鼠标事件开始 热键 槽函数连接
        self.ui.mouse_stop_hotkey.editingFinished.connect(self.set_mouse_stop_hotkey)
        # 改动 鼠标事件停止 热键 槽函数连接
        self.ui.add_mel_button.clicked.connect(self.mouse_event_dialog)
        # 添加鼠标事件按钮
        self.ui.remove_mel_button.clicked.connect(self.remove_mouse_event)
        # 删除鼠标事件按钮
        self.ui.clear_mel_button.clicked.connect(self.clear_mouse_event)
        # 清空鼠标事件列表按钮

        self.ui.keyboard_start_hotkey.editingFinished.connect(self.set_keyboard_start_hotkey)
        # 改动 键盘事件开始 热键 槽函数连接
        self.ui.keyboard_stop_hotkey.editingFinished.connect(self.set_keyboard_stop_hotkey)
        self.ui.add_kel_btn.clicked.connect(self.keyboard_event_dialog)
        # 添加键盘事件按钮
        self.ui.remove_kel_btn.clicked.connect(self.remove_keyboard_event)
        # 删除键盘事件按钮
        self.ui.clear_kel_btn.clicked.connect(self.clear_keyboard_event)
        # 清空键盘事件列表按钮

    # ------------窗口句柄捕获函数-start------------#
    def handle_capture(self):
        """
        捕捉窗口句柄
        :return:
        """
        self.mouse_pos = win32gui.GetCursorPos()
        self.handle = win32gui.WindowFromPoint(self.mouse_pos)
        self.ui.window_name.setText(win32gui.GetWindowText(self.handle))

    def set_handle_capture_hotkey(self, key: str) -> None:
        """
        更改捕捉窗口句柄的快捷键
        :param key: 快捷键
        :return:
        """
        keyboard.remove_hotkey(self.app_data.value("Common/capture_hotkey"))
        keyboard.add_hotkey(key, self.handle_capture)
        self.app_data.setValue("Common/capture_hotkey", key)
        self.app_data.sync()

    def lock_btn_click(self):
        if self.ui.lockWindow.isChecked():
            keyboard.remove_hotkey(self.app_data.value("Common/capture_hotkey"))
        else:
            keyboard.add_hotkey(self.app_data.value("Common/capture_hotkey"),self.handle_capture)

    # ------------窗口句柄捕获函数-end------------#

    # ------------鼠标操作函数-start------------#

    def mouse_event_dialog(self):
        """
        在"鼠标操作栏"中的"添加"按钮按下时触发
        弹出对话框
        添加鼠标事件,例如: 鼠标左键,长按
        :return:
        """

        def add_mouse_event():
            """
            添加鼠标事件
            :return:
            """
            event: mouse_event_data = mouse_event_data(
                button=self.mouse_button[dialog.mouse_btn_box.currentIndex()],
                is_click=dialog.is_click_btn.isChecked(),
                break_time=dialog.break_time_box.value()
            )

            # 检查mouse_event_list中是否已存在该选项
            if self.ui.mouse_event_list.findItems(event.toString(), Qt.MatchExactly):
                return

            mouse_event = QListWidgetItem()
            mouse_event.setText(event.toString())
            mouse_event.setData(Qt.UserRole, event.toString())
            self.ui.mouse_event_list.addItem(mouse_event)

        dialog_window = QDialog()
        dialog = mouse_event_dialog_ui.Ui_Dialog()
        dialog.setupUi(dialog_window)
        dialog.buttonBox.accepted.connect(add_mouse_event)
        dialog.buttonBox.accepted.connect(dialog_window.close)
        dialog.buttonBox.rejected.connect(dialog_window.close)
        dialog_window.show()
        dialog_window.exec()

    def remove_mouse_event(self):
        """
        将选中的鼠标事件从列表中删除
        :return:
        """
        self.ui.mouse_event_list.takeItem(self.ui.mouse_event_list.currentRow())

    def clear_mouse_event(self):
        """
        清空鼠标事件列表
        :return:
        """
        self.ui.mouse_event_list.clear()

    def set_mouse_start_hotkey(self):
        """
        设置/更改 鼠标事件 开始 快捷键
        :return:
        """
        mouse_click_hotkey = QKeySequence.listToString(self.ui.mouse_start_hotkey.keySequence()).lower()
        # 先将默认设置中的热键删除
        keyboard.remove_hotkey(self.app_data.value("Mouse/start_hotkey"))
        # 再添加新设置的热键
        keyboard.add_hotkey(mouse_click_hotkey, self.mouse_start)
        self.app_data.setValue("Mouse/start_hotkey", mouse_click_hotkey)
        self.app_data.sync()

    def set_mouse_stop_hotkey(self):
        """
        设置/更改 鼠标事件 停止 快捷键
        :return:
        """
        mouse_click_hotkey = QKeySequence.listToString(self.ui.mouse_stop_hotkey.keySequence()).lower()
        # 先将默认设置中的热键删除
        keyboard.remove_hotkey(self.app_data.value("Mouse/stop_hotkey"))
        # 再添加新设置的热键
        keyboard.add_hotkey(mouse_click_hotkey, self.mouse_stop)
        self.app_data.setValue("Mouse/stop_hotkey", mouse_click_hotkey)
        self.app_data.sync()

    def mouse_start(self):
        """
        鼠标操作开始函数
        :return:
        """

        def build_worker_pool(queue, size):
            """
            创建工作线程,用于多线程并发
            :param queue: 队列
            :param size: 队列大小(并发大小)
            :return:
            """
            _workers = []
            for _ in range(size):
                _worker = MouseConsumer(queue)
                _worker.start()
                _workers.append(_worker)
            return _workers

        mouse_events = self.sync_mouse_event_list()
        self.mouse_queue = Queue()
        self.mouse_workers = build_worker_pool(self.mouse_queue, len(mouse_events))
        for mouse_event_str in mouse_events:
            mouse_event = mouse_event_data.fromString(mouse_event_str)
            qDebug(f"鼠标事件:{mouse_event}")
            self.mouse_queue.put(MouseEvent(mouse_event.button, mouse_event.is_click,
                                            self.handle, self.mouse_pos, mouse_event.break_time))

    def mouse_stop(self):
        """
        鼠标操作停止函数
        :return:
        """
        for _ in self.mouse_workers:
            self.mouse_queue.put('exit')
        for worker in self.mouse_workers:
            worker.join()

    def sync_mouse_event_list(self):
        """
        将鼠标事件列表中的所有事件写入到配置文件中
        :return:
        """
        mouse_events = []
        for i in range(self.ui.mouse_event_list.count()):
            mouse_event = self.ui.mouse_event_list.item(i).data(Qt.UserRole)
            mouse_events.append(mouse_event)
        self.app_data.setValue('Mouse/mouse_list', mouse_events)
        self.app_data.sync()
        return mouse_events

    # ------------鼠标操作函数-end------------#
    # ------------键盘操作函数-start------------#
    def keyboard_event_dialog(self):
        """
        在"键盘操作栏"中的"添加"按钮按下时触发
        弹出对话框
        添加键盘事件
        :return:
        """

        def add_keyboard_event():
            """
            添加键盘事件
            :return:
            """
            event: keyboard_event_data = keyboard_event_data(
                key=dialog.shortcut_key_edit.text(),
                is_tap=dialog.is_tap_btn.isChecked(),
                break_time=dialog.break_time_box.value()
            )

            # 检查keyboard_event_list中是否已存在该选项
            if self.ui.keyboard_event_list.findItems(event.toString(), Qt.MatchExactly):
                return

            keyboard_event = QListWidgetItem()
            keyboard_event.setText(event.toString())
            keyboard_event.setData(Qt.UserRole, event.toString())
            self.ui.keyboard_event_list.addItem(keyboard_event)

        dialog_window = QDialog()
        dialog = keyboard_event_dialog_ui.Ui_Dialog()
        dialog.setupUi(dialog_window)
        dialog.buttonBox.accepted.connect(add_keyboard_event)
        dialog_window.show()
        dialog_window.exec()

    def remove_keyboard_event(self):
        """
        将选中的键盘事件从列表中删除
        :return:
        """
        self.ui.keyboard_event_list.takeItem(self.ui.keyboard_event_list.currentRow())

    def clear_keyboard_event(self):
        """
        清空键盘事件列表
        :return:
        """
        self.ui.keyboard_event_list.clear()

    def set_keyboard_start_hotkey(self):
        """
        设置/更改 键盘事件 开始 快捷键
        :return:
        """
        keyboard_start_hotkey = QKeySequence.listToString(self.ui.keyboard_start_hotkey.keySequence()).lower()
        # 现将默认设置中注册的热键删除
        keyboard.remove_hotkey(self.app_data.value("Keyboard/start_hotkey"))
        # 再添加新设置的热键
        keyboard.add_hotkey(keyboard_start_hotkey, self.keyboard_start)
        self.app_data.setValue("Keyboard/start_hotkey", keyboard_start_hotkey)
        self.app_data.sync()

    def set_keyboard_stop_hotkey(self):
        """
        设置/更改 鼠标事件 停止 快捷键
        :return:
        """
        keyboard_stop_hotkey = QKeySequence.listToString(self.ui.keyboard_stop_hotkey.keySequence()).lower()
        # 先将默认设置中的热键删除
        keyboard.remove_hotkey(self.app_data.value("Keyboard/stop_hotkey"))
        # 再添加新设置的热键
        keyboard.add_hotkey(keyboard_stop_hotkey, self.mouse_stop)
        self.app_data.setValue("Keyboard/stop_hotkey", keyboard_stop_hotkey)
        self.app_data.sync()

    def keyboard_start(self):
        """
        键盘操作开始函数
        :return:
        """

        def build_worker_pool(queue, size):
            """
            创建工作线程，用于多线程并发
            :param queue: 任务队列
            :param size: 队列大小(并发数量)
            :return:
            """
            _workers = []
            for _ in range(size):
                _worker = KeyboardConsumer(queue)
                _worker.start()
                _workers.append(_worker)
            return _workers

        keyboard_events = self.sync_keyboard_event_list()
        self.keyboard_queue = Queue()
        self.keyboard_workers = build_worker_pool(self.keyboard_queue, len(keyboard_events))
        for keyboard_event_str in keyboard_events:
            qDebug(f"键盘事件:{keyboard_event_str}")
            keyboard_event = keyboard_event_data.fromString(keyboard_event_str)
            self.keyboard_queue.put(KeyboardEvent(keyboard_event.key, keyboard_event.is_tap,
                                                  self.handle, keyboard_event.break_time))

    def keyboard_stop(self):
        """
        键盘操作停止函数
        :return:
        """
        for _ in self.keyboard_workers:
            self.keyboard_queue.put('exit')
        for worker in self.keyboard_workers:
            worker.join()

    def sync_keyboard_event_list(self):
        """
        将键盘事件列表中的所有事件写入到配置文件中
        :return:
        """
        keyboard_events = []
        for i in range(self.ui.keyboard_event_list.count()):
            keyboard_event = self.ui.keyboard_event_list.item(i).data(Qt.UserRole)
            keyboard_events.append(keyboard_event)
        self.app_data.setValue('Keyboard/keyboard_list', keyboard_events)
        self.app_data.sync()
        return keyboard_events
    # ------------键盘操作函数-end------------#
