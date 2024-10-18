import pygetwindow as gw
import time
import pygetwindow as gw
import sys

# sys.path.append('../../2_Application_Actions')
from Utils.Powerpoint_mode_checker import is_fullscreen_mode

"""
Function to focus on a window with the provided title
"""


def focus_on_window(window_title):
    windows = gw.getWindowsWithTitle(window_title)
    if not windows:
        print(f"No windows found with title: {window_title}")
        return
    for window in windows:
        try:
            # Check if the window is still valid before proceeding
            if not window._hWnd:
                print(f"Invalid window handle for {window_title}.")
                continue

            if not window.isMaximized:
                print("Maximizing window")
                window.maximize()

            if not is_fullscreen_mode():
                print("Window not in fullscreen mode, activating...")
                if not window.isActive:
                    window.activate()
        except gw.PyGetWindowException as e:
            print(f"Error occurred: {e}")
        except pywintypes.error as e:
            print(f"pywintypes error: {e}")
        except Exception as e:
            print(f"Unexpected error occurred: {e}")

# import winsound
# time.sleep(2)
# winsound.Beep(1000, 1000)
#
#
# window_titles = ["VLC media player"]
# for title in window_titles:
#     focus_on_window(title)






