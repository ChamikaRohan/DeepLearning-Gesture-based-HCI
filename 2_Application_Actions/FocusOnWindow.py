import pygetwindow as gw
import time

"""
Function to focus on a window with the provided title
"""

import pygetwindow as gw

def focus_on_window(window_title):
    windows = gw.getWindowsWithTitle(window_title)
    if not windows:
        return

    for window in windows:
        try:
            if not window.isActive:
                window.activate()
            if not window.isMaximized:
                window.maximize()
        except gw.PyGetWindowException as e:
            print(f"Error occurred: {e}")

"""
window_titles = ["VLC media player"]
for title in window_titles:
    focus_on_window(title)
"""



