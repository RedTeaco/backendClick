import threading
import time
from ctypes.wintypes import HWND
from dataclasses import dataclass
from typing import Optional

from PySide6.QtCore import qDebug

from api import mouse_api


@dataclass
class MouseEvent:
    button: str
    isClick: bool
    hwnd: HWND
    mouse_pos: Optional[tuple] = (940,480)
    breaktime: float = 0.01


class MouseConsumer(threading.Thread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue
        self.mouse_flag = True

    def run(self):
        while True:
            msg: MouseEvent = self.queue.get()

            if isinstance(msg, str) and msg == 'exit':
                # 停止mouse_click
                self.mouse_flag = False

                # 停止mouse_down
                mouse_api.mouse_up(cache_msg.hwnd, cache_msg.mouse_pos[0], cache_msg.mouse_pos[1],
                                    cache_msg.button)
                break
            cache_msg: MouseEvent = msg

            qDebug(f"Mouse Consumer Received :{msg}")

            if not isinstance(msg, MouseEvent):
                raise TypeError(f'Expected Class<MouseEvent>, got {type(msg)}')

            # logic codes start
            if not msg.isClick:
                mouse_api.mouse_down(msg.hwnd, msg.mouse_pos[0], msg.mouse_pos[1],
                                      msg.button)
            else:
                self.mouse_flag = True
                th = threading.Thread(target=self.mouse_click, args=[msg], name="mouse_click")
                th.start()
            # logic codes end

    def mouse_click(self, msg: MouseEvent):
        # 当mouse_flag为True时,即可重复鼠标点击行为,当设为false时,即可停止
        while self.mouse_flag:
            mouse_api.mouse_click(msg.hwnd, msg.mouse_pos[0], msg.mouse_pos[1],
                                   msg.button)
            time.sleep(float(msg.breaktime))