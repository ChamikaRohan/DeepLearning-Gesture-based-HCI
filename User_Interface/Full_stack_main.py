import sys
import threading
from PyQt6.QtWidgets import QApplication
from UI_main import MainWindow

sys.path.append('../System_Backend')
from backend_funcs import main_thread as backend_main_thread

class BackendThread(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        backend_main_thread()  # Run the backend function

class MainThread(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        # Start the backend thread
        backend_thread = BackendThread()
        backend_thread.start()

        # Start the PyQt application
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()

        # Wait for the backend thread to complete


        # Run the application event loop
        sys.exit(app.exec())

        backend_thread.join()

if __name__ == "__main__":
    main_thread = MainThread()
    main_thread.start()
