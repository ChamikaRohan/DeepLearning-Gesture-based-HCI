import pyautogui
import time
import sys

sys.path.append('../2_Application_Actions')
from Utils.Focus_on_window import focus_on_window

def mobile_control_media_player(action):
    # Find and activate the movie player window
    window_titles = ["Movies", "VLC media player"]
    for title in window_titles:
        focus_on_window(title)
    if action == None:
        return
    elif action == 1 or action == 2:
        pyautogui.press("space")
        print("Play/Stop the movie")
    elif action == 4:
        pyautogui.keyDown('ctrl')
        pyautogui.press('left')
        pyautogui.keyUp('ctrl')
        print("Seeking Backward")
    elif action == 5:
        pyautogui.keyDown('ctrl')
        pyautogui.press('right')
        pyautogui.keyUp('ctrl')
        print("Seeking Forward")
    elif action == 6:
        pyautogui.scroll(1)
        print("Volume Increased")
    elif action == 7:
        pyautogui.scroll(-1)
        print("Volume Decreased")
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