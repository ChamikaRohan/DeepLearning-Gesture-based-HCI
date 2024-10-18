import win32gui
import win32con
import win32api
import pywintypes

def is_fullscreen_mode():
    try:
        # Get the size of the primary display
        screen_width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
        screen_height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)

        # Get the size of the currently active window
        hwnd = win32gui.GetForegroundWindow()
        if hwnd == 0:
            print("No active window found.")
            return False

        rect = win32gui.GetWindowRect(hwnd)
        window_width = rect[2] - rect[0]
        window_height = rect[3] - rect[1]

        # Compare the window size with the screen size
        return window_width == screen_width and window_height == screen_height
    except pywintypes.error as e:
        print(f"Failed to get window rect: {e}")
        return False
