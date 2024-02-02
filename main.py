import sys
from ctypes import windll

import keyboard
import win32gui
import keyboardClick
import mouseClick

if __name__ == '__main__':
    if not windll.shell32.IsUserAnAdmin():
        # 不是管理员就提权
        windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, __file__, None, 1)
        sys.exit()
    else:
        # 按下k获取窗口句柄
        print("按下K开始捕获窗口句柄")
        keyboard.wait('k')
        pos = win32gui.GetCursorPos()
        handle = win32gui.WindowFromPoint(pos)
        print("捕获窗口句柄完成,窗口名:%s" % win32gui.GetWindowText(handle))
        keyboard.add_hotkey('f8', keyboardClick.key_down, args=(handle, 'f'))
        keyboard.add_hotkey('f7', keyboardClick.key_up, args=(handle, 'f'))  # f7暂停
        keyboard.add_hotkey('shift+f8', mouseClick.mouse_down, args=(handle, 960, 540, mouseClick.MOUSE_LEFT))
        keyboard.add_hotkey('shift+f7', mouseClick.mouse_up, args=(handle, 960, 540, mouseClick.MOUSE_LEFT))
        keyboard.wait('f9')
        keyboardClick.key_up(handle, 'f')
        mouseClick.mouse_up(handle,960, 540,mouseClick.MOUSE_LEFT)
