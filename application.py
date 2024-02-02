import sys

from PySide6.QtWidgets import QApplication, QWidget

from application_ui import Ui_Form


def main():
    app = QApplication(sys.argv)
    window = QWidget()
    window.resize(480, 400)
    window.setFixedSize(480, 400)
    ui = Ui_Form()
    ui.setupUi(window)
    window.show()
    exit(app.exec())


if __name__ == '__main__':
    main()
