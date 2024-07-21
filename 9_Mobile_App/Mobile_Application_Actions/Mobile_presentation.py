import pyautogui
import time
import sys

sys.path.append('../2_Application_Actions')
from Utils.Focus_on_window import focus_on_window

def mobile_control_presentation(action):
    # Find and activate the movie player window
    window_titles = ["PowerPoint"]
    for title in window_titles:
        focus_on_window(title)
    if action == None:
        return
    elif action == 1:
        print("Slide Show Mode On")
        pyautogui.press("f5")
        time.sleep(1)
    elif action == 2:
        print("Slide Show Mode Off")
        pyautogui.press("esc")
    elif action == 4:
        print("Switch to Previous Slide")
        pyautogui.hotkey("left")
    elif action == 5:
        print("Switch to Next Slide")
        pyautogui.hotkey("right")
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