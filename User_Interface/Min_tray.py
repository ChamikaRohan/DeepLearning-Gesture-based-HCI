import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QTimer

import Tray_rc
from Tray import Ui_MainWindow as Ui_MinimizeTray

from SystemTrayChange import TraySelection

sys.path.append('../10_Storage_and_utils')
from Payload import Payload

class MinimizeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MinimizeTray()
        self.ui.setupUi(self)

        # Hide the title bar
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        # Make the window draggable
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.dragPosition = None

        # Connect buttons to their respective slots
        self.ui.Close.clicked.connect(self.close)
        self.ui.Maximize.clicked.connect(self.open_main_window)
        self.main_window = None

        # Set the window icon
        self.setWindowIcon(QIcon('SystemTray/logo.png'))
        
        #Calling the system bar
        self.show_pages()

    # Code to connect another window
    def open_main_window(self):
        from UI_main import MainWindow
        if self.main_window is None:
            self.main_window = MainWindow()

        self.main_window.show()
        self.close()

    def show_pages(self):
        # Initial
        self.ui.stackedWidget.setCurrentIndex(7)
        # after 2s
        payload = Payload()
        gesture_type = payload.get_gesture_type()
        mode = payload.get_mode()
        QTimer.singleShot(2000, lambda: self.change_to_desired_tray(self.give_desired_tray_num(gesture_type, mode, 5)))

    def give_desired_tray_num(self, gesture_type, mode, application):
        return TraySelection(gesture_type, mode, application)

    def change_to_desired_tray(self, key):
        self.ui.stackedWidget.setCurrentIndex(key)

    # Code to window Draggable
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.dragPosition = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.MouseButton.LeftButton:
            if self.dragPosition is not None:
                self.move(event.globalPosition().toPoint() - self.dragPosition)
                event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.dragPosition = None
            event.accept()

# Execute App
if __name__ =="__main__":
    app = QApplication(sys.argv)
    window = MinimizeWindow()
    window.show()
    sys.exit(app.exec())
