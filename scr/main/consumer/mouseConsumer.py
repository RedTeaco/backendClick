import threading
import time
from ctypes.wintypes import HWND
from dataclasses import dataclass
from typing import Optional

import mouseClick


@dataclass
class MouseEvent:
    button: str
    isClick: bool
    hwnd: HWND
    mouse_pos: Optional[tuple] = (940,480)
    breaktime: float = -1


class MouseConsumer(threading.Thread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue
        self.mouse_flag = True
        # mouse_lock 作为gui的逻辑处理，防止多次按下开始
        # self.mouse_lock = False

    def run(self):
        while True:
            msg: MouseEvent = self.queue.get()

            if isinstance(msg, str) and msg == 'exit':
                # 停止mouse_click
                self.mouse_flag = False

                # 停止mouse_down
                mouseClick.mouse_up(cache_msg.hwnd, cache_msg.mouse_pos[0], cache_msg.mouse_pos[1],
                                    cache_msg.button)
                break
            cache_msg: MouseEvent = msg
            print(f'Received message: {msg}\n')
            if not isinstance(msg, MouseEvent):
                raise TypeError(f'Expected Class<MouseEvent>, got {type(msg)}')

            # logic codes start
            if not msg.isClick:
                print(f"execute: mouse_down: \n hwnd:{msg.hwnd}, button: {msg.button}")
                mouseClick.mouse_down(msg.hwnd, msg.mouse_pos[0], msg.mouse_pos[1],
                                      msg.button)
            else:
                self.mouse_flag = True
                th = threading.Thread(target=self.mouse_click, args=[msg], name="mouse_click")
            # logic codes end
        print('Mouse Consumer thread exiting.\n')

    def mouse_click(self, msg: MouseEvent):
        # 当mouse_flag为True时,即可重复鼠标点击行为,当设为false时,即可停止
        while self.mouse_flag:
            mouseClick.mouse_click(msg.hwnd, msg.mouse_pos[0], msg.mouse_pos[1],
                                   msg.button)
            time.sleep(msg.breaktime)


def build_worker_pool(queue, size):
    _workers = []
    for _ in range(size):
        _worker = MouseConsumer(queue)
        _worker.start()
        _workers.append(_worker)
    return _workers


if __name__ == '__main__':
    from queue import Queue
    import win32gui

    queue = Queue()
    time.sleep(2)
    pos = win32gui.GetCursorPos()
    handle = win32gui.WindowFromPoint(pos)
    queue_list = [MouseEvent(button=mouseClick.MOUSE_LEFT, isClick=False, hwnd=handle),
                  MouseEvent(button=mouseClick.MOUSE_RIGHT, isClick=False, hwnd=handle)]
    _workers = build_worker_pool(queue, len(queue_list))

    for queue_mouse in queue_list:
        queue.put(queue_mouse)
    time.sleep(10)
    for _w in _workers:
        queue.put('exit')
    for _w in _workers:
        _w.join()
    print(f'Producer thread exit')
