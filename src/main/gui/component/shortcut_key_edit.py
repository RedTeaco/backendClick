from PySide6.QtCore import Qt
from PySide6.QtGui import QKeyEvent, QKeySequence

from PySide6.QtWidgets import QLineEdit


class ShortcutKeyEdit(QLineEdit):
    def keyPressEvent(self, event: QKeyEvent):

        key = event.key()
        if key is Qt.Key.Key_unknown:
            return

        if key == Qt.Key.Key_CapsLock or key == Qt.Key.Key_Escape:
            return

        if (key == Qt.Key.Key_Control or
                key == Qt.Key.Key_Shift or
                key == Qt.Key.Key_Space or
                key == Qt.Key.Key_Alt or
                key == Qt.Key.Key_Return or
                key == Qt.Key.Key_Tab or
                key == Qt.Key.Key_Enter):
            # 部分单独的系统按键直接返回
            match key:
                case Qt.Key.Key_Control:
                    self.setText("CTRL")
                case Qt.Key.Key_Shift:
                    self.setText("SHIFT")
                case Qt.Key.Key_Alt:
                    self.setText("ALT")
                case Qt.Key.Key_Enter:
                    self.setText("ENTER")
                case Qt.Key.Key_Return:
                    self.setText("RETURN")
                case Qt.Key.Key_Tab:
                    self.setText("TAB")
                case Qt.Key.Key_Space:
                    self.setText("SPACE")
            return
        modifier = event.modifiers()
        if modifier and modifier == Qt.Modifier.SHIFT:
            self.setText("shift")
            return
        if modifier and modifier == Qt.Modifier.CTRL:
            self.setText("ctrl")
            return
        if modifier and modifier == Qt.Modifier.ALT:
            self.setText("alt")
            return

        self.setText(QKeySequence(key).toString().upper())
        return


