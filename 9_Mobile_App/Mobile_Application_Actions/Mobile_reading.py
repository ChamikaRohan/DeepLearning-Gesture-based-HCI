import pyautogui
import time
import sys

sys.path.append('../2_Application_Actions')
from Utils.Focus_on_window import focus_on_window

def mobile_control_reading(action):
    # Find and activate the movie player window
    window_titles = [" - Microsoft​ Edge"]
    for title in window_titles:
        focus_on_window(title)
    if action == None:
        return
    elif action == 1 or action == 2:
        print("Toggling Full-Screen Mode")
        pyautogui.hotkey("f11")
    elif action == 4:
        print("Zooming out")
        pyautogui.hotkey("ctrl", "_")
    elif action == 5:
        print("Zooming in")
        pyautogui.hotkey("ctrl", "+")
    elif action == 6:
        print("Scrolling up")
        pyautogui.scroll(80)
        for _ in range(10):
            pyautogui.scroll(50)
    elif action == 7:
        print("Scrolling down")
        pyautogui.scroll(-80)
        for _ in range(10):
            pyautogui.scroll(-50)
    elif action == 9:
        print("Minimize Current Application")
        pyautogui.hotkey('alt', 'space', 'n')
    elif action == 8:
        print("Close Current Application")
        pyautogui.hotkey('alt', 'f4')
    elif action == 3:
        print("Activate sleep mode")
        pyautogui.hotkey("winleft", "x")
        pyautogui.typewrite("u")
        pyautogui.typewrite("s")