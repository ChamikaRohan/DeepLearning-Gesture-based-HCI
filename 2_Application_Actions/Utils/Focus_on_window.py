import pygetwindow as gw
import time
import pygetwindow as gw
from Utils.Powerpoint_mode_checker import is_fullscreen_mode

"""
Function to focus on a window with the provided title
"""
def focus_on_window(window_title):
    windows = gw.getWindowsWithTitle(window_title)
    if not windows:
        return
    for window in windows:
        try:
            if not window.isMaximized:
                print("called maximized")
                window.maximize()
            if not is_fullscreen_mode():
                print("pwrpont full screen")
                if not window.isActive:
                    print("called active")
                    window.activate()
        except gw.PyGetWindowException as e:
            print(f"Error occurred: {e}")

"""
import winsound
time.sleep(2)
winsound.Beep(1000, 1000)


window_titles = ["PowerPoint"]
for title in window_titles:
    focus_on_window(title)
"""





