import threading
import time
from ctypes.wintypes import HWND
from dataclasses import dataclass

from PySide6.QtCore import qDebug

from api import keyboard_api


@dataclass
class KeyboardEvent:
    key: str
    isTap: bool
    hwnd: HWND
    breaktime: float = 0.01


class KeyboardConsumer(threading.Thread):
    def __init__(self, queue):
        super().__init__()
        # 任务队列
        self.queue = queue
        # 当键盘事件需要连按时,flag作为继续连按的标志,设置为False时即可停止连按
        self.keyboard_flag = True

    def run(self):
        while True:
            msg: KeyboardEvent = self.queue.get()

            if isinstance(msg, str) and msg == 'exit':
                # 停止keyboard_tap
                self.keyboard_flag = False
                # 停止keyboard_pressed
                keyboard_api.key_up(cache_msg.hwnd, cache_msg.key)
                break
            cache_msg: KeyboardEvent = msg
            qDebug(f"Keyboard Consumer Received :{msg}")
            if not isinstance(cache_msg, KeyboardEvent):
                raise TypeError(f'Expected Class<KeyboardEvent>, got {type(cache_msg)}')

            # logic codes start
            #长按时
            if not msg.isTap:
                keyboard_api.key_down(msg.hwnd, msg.key)
            else:
                self.keyboard_flag = True
                th = threading.Thread(target=self.keyboard_tap, args=(msg,), name='keyboard_tap')
                th.start()
            # logic codes end

    def keyboard_tap(self, msg: KeyboardEvent):
        # 当keyboard_flag 为True时，即可重复鼠标点击行为,当设为false时,即可停止
        raw_break_time = float(msg.breaktime)
        break_time = raw_break_time - 0.05 if raw_break_time > 0.15 else 0.05
        while self.keyboard_flag:
            keyboard_api.key_down(msg.hwnd, msg.key)
            time.sleep(0.05)
            keyboard_api.key_up(msg.hwnd, msg.key)
            time.sleep(break_time)
