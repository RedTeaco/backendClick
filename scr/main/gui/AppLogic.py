import os.path
import sys
from dataclasses import dataclass
from queue import Queue
from typing import List

import keyboard
import mouseClick
import win32gui
from PySide6.QtCore import QSettings, Qt
from PySide6.QtGui import QKeySequence
from PySide6.QtWidgets import QApplication, QWidget, QListWidgetItem, QDialog

from main.consumer.mouseConsumer import MouseConsumer, MouseEvent
from main.gui import mouse_event_dialog_ui
from main.gui.application_ui import Ui_Form


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
                break_time=split_string_list[3][:-1],
            )
        else:
            return mouse_event_data(
                button=split_string_list[1][:4],
                is_click=False,
            )


class AppLogic:
    def __init__(self, config_file_path: str = 'config.ini'):
        self.window = None
        self.mouse_button = [mouseClick.MOUSE_LEFT, mouseClick.MOUSE_MID, mouseClick.MOUSE_RIGHT]
        self.ui = Ui_Form()
        self.app_data = QSettings(config_file_path, QSettings.IniFormat)
        self.handle = None

        self.mouse_workers:List[MouseConsumer] = []
        self.mouse_lock = False
        self.mouse_pos = ()
        self.mouse_list = []
        self.mouse_queue = Queue()

        self.keyboard_lock = False
        self.keyboard_list = []

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
            mouse_events = [].append(app_data.value('Mouse/mouse_list')) if type(app_data.value('Mouse/mouse_list')) is str else app_data.value('Mouse/mouse_list')
            for mouse_event in mouse_events:
                mouse_event_item = QListWidgetItem()
                mouse_event_item.setText(mouse_event)
                mouse_event_item.setData(Qt.UserRole, mouse_event)
                self.ui.mouse_event_list.addItem(mouse_event_item)

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
        self.ui.add_mel_button.clicked.connect(self.mouse_event_dialog)
        self.ui.remove_mel_button.clicked.connect(self.remove_mouse_event)
        self.ui.clear_mel_button.clicked.connect(self.clear_mouse_event)

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
        item = self.ui.mouse_event_list.takeItem(self.ui.mouse_event_list.currentRow())

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
            print(mouse_event)
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
    def keyboard_start(self):
        pass

    def keyboard_stop(self):
        pass
    # ------------键盘操作函数-end------------#


if __name__ == '__main__':
    app = AppLogic()
    app.main()
