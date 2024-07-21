import pyautogui
import time
import sys

sys.path.append('../2_Application_Actions')
from Utils.Focus_on_window import focus_on_window

def mobile_control_system(action):
    if action == None:
        return
    elif action == 1 or action == 2:
        print("Toggling Full-Screen Mode")
        pyautogui.hotkey("f11")
    elif action == 5:
        print("Switch between applications")
        pyautogui.keyDown('alt')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.keyUp('alt')
    elif action == 6:
        print("Increase System Volume")
        pyautogui.hotkey('volumeup')
    elif action == 7:
        print("Decrease System Volume")
        pyautogui.hotkey('volumedown')
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