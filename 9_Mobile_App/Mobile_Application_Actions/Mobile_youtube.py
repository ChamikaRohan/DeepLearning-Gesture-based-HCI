import pyautogui
import time
import sys

sys.path.append('../2_Application_Actions')
from Utils.Focus_on_window import focus_on_window

def mobile_control_youtube(action):
    window_titles = ["YouTube - Google Chrome"]
    for title in window_titles:
        focus_on_window(title)
    if action == None:
        return
    elif action == 1 or action == 2:
        print("Play/Pause video")
        pyautogui.click(x=0, y=600)
        pyautogui.press('space')
    elif action == 4:
        print("Decrease System Volume")
        pyautogui.hotkey('volumedown')
    elif action == 5:
        print("Increase System Volume")
        pyautogui.hotkey('volumeup')
    elif action == 6:
        print("Scrolling up")
        pyautogui.click(x=0, y=700)
        pyautogui.scroll(80)
        for _ in range(10):
            pyautogui.scroll(50)
    elif action == 7:
        print("Scrolling down")
        pyautogui.click(x=0, y=700)
        pyautogui.scroll(-80)
        for _ in range(10):
            pyautogui.scroll(-50)
    elif action == 10:
        print("Select video")
        pyautogui.click(x=800, y=600)
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