import pyautogui
import time
import sys

sys.path.append('../2_Application_Actions')
from Utils.Focus_on_window import focus_on_window

def mobile_control_zoom(action):
    window_titles = ["Zoom Meeting"]
    for title in window_titles:
        focus_on_window(title)
    if action == None:
        return
    elif action == 1:
        pyautogui.hotkey("alt", "a")
        print("Mute/Unmute Microphone")
    elif action == 2:
        pyautogui.hotkey("alt", "s")
        pyautogui.press("enter")
        print("Start/Stop Screen Share")
    elif action == 4:
        print("Decrease System Volume")
        pyautogui.hotkey('volumedown')
    elif action == 5:
        print("Increase System Volume")
        pyautogui.hotkey('volumeup')
    elif action == 10:
        pyautogui.hotkey("alt", "q")
        pyautogui.press("enter")
        print("Leave Meeting")
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