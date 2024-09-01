import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QIcon

import Tray_rc
from Tray import Ui_MainWindow as Ui_MinimizeTray

from SystemTrayChange import n_value

#Switching to different bars (Hand appears:hand=1, not =0)
def show_pages(self,hand):
    if(hand ==1):
        self.ui.stackedWidget.setCurrentIndex(n_value)
    else:
        self.ui.stackedWidget.setCurrentIndex(7)
        

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
        show_pages(self,1)

    # Code to connect another window
    def open_main_window(self):
        from UI_main import MainWindow
        if self.main_window is None:
            self.main_window = MainWindow()

        self.main_window.show()
        self.close()

    # Move to the logo bar
    def show_page_one(self):
        self.ui.stackedWidget.setCurrentIndex(7)


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
