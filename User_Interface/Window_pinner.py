import cv2

def window_pinner(window_name):

    cv2.namedWindow(window_name, cv2.WINDOW_GUI_NORMAL)
    cv2.setWindowProperty(window_name, cv2.WND_PROP_TOPMOST, 1.0)  # Set to 1.0 for True
