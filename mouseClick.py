import time
from ctypes import windll, byref, c_char_p
from ctypes.wintypes import HWND, POINT

import win32api, win32con, win32gui

MOUSE_LEFT = "鼠标左键"
MOUSE_MID = "鼠标中键"
MOUSE_RIGHT = "鼠标右键"
WHEEL_DELTA = 120
mouse_dict_down = {"鼠标左键": win32con.WM_LBUTTONDOWN, "鼠标中键": win32con.WM_MBUTTONDOWN,
                   "鼠标右键": win32con.WM_RBUTTONDOWN}
mouse_dict_up = {"鼠标左键": win32con.WM_LBUTTONUP, "鼠标中键": win32con.WM_MBUTTONUP,
                 "鼠标右键": win32con.WM_RBUTTONUP}
PostMessageW = windll.user32.PostMessageW
ClientToScreen = windll.user32.ClientToScreen


def move_to(handle: HWND, x: int, y: int) -> None:
    """
    移动鼠标到坐标(x,y)
    :param handle: 窗口句柄
    :param x: 横坐标
    :param y: 纵坐标
    :return:
    """
    PostMessageW(handle, win32con.WM_MOUSEMOVE, 0, y << 16 | x)


def mouse_down(handle: HWND, x: int = 960, y: int = 540, button=MOUSE_LEFT) -> None:
    """
    在坐标(x,y)处按下鼠标
    :param handle: 窗口句柄
    :param x: 横坐标
    :param y: 纵坐标
    :param button: 左键|中键|右键
    :return:
    """
    print("按下%s" % button)
    wparam = 0
    lparam = y << 16 | x
    PostMessageW(handle, mouse_dict_down[button], wparam, lparam)


def mouse_move(dx, dy):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, dx, dy, 0, 0)


def mouse_up(handle: HWND, x: int = 960, y: int = 540, button=MOUSE_LEFT):
    """
    在坐标(x,y)处松开鼠标
    :param handle: 窗口句柄
    :param x: 横坐标
    :param y: 纵坐标
    :param button: 左键|中键|右键
    :return:
    """
    print("松开%s" % button)
    wparam = 0
    lparam = y << 16 | x
    PostMessageW(handle, mouse_dict_up[button], wparam, lparam)


def mouse_click(handle: HWND, x, y, button=MOUSE_LEFT):
    mouse_down(handle, x, y, button)
    mouse_up(handle, x, y, button)


def scroll(handle: HWND, delta: int, x: int, y: int) -> None:
    """
    在鼠标(x,y)处滚动鼠标滚轮
    :param handle: 窗口句柄
    :param delta: +：向上，-：向下
    :param x: 横坐标
    :param y: 纵坐标
    :return:
    """
    move_to(handle, x, y)
    wparam = delta << 16
    p = POINT(x, y)
    ClientToScreen(handle, byref(p))
    lparam = p.y << 16 | p.x
    PostMessageW(handle, win32con.WM_MOUSEWHEEL, wparam, lparam)
