import win32gui
import win32con
import win32api

def is_fullscreen_mode():
    # Get the size of the primary display
    screen_width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
    screen_height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)

    # Get the size of the PowerPoint window
    hwnd = win32gui.GetForegroundWindow()
    rect = win32gui.GetWindowRect(hwnd)
    window_width = rect[2] - rect[0]
    window_height = rect[3] - rect[1]

    # Compare the window size with the screen size
    return window_width == screen_width and window_height == screen_height