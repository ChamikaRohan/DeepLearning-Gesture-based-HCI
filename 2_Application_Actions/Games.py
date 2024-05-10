import pyautogui
from Utils.Focus_on_window import focus_on_window
from Utils.Powerpoint_mode_checker import is_fullscreen_mode
import time

"""
Function to control game functionalities

Gesture Mapping:
4: Moving up
0: Moving down
3: Moving left
2: Moving right
"""
def control_games(gesture):
    #Find and activae the movie player window
    window_titles =  ["Google Chrome"]
    for title in window_titles:
        focus_on_window(title)
    if gesture == None:
        return
    elif gesture == 3:
        print("Press right")
        pyautogui.press('right')
    elif gesture == 2:
        print("Press left")
        pyautogui.press('left')
    elif gesture == 0:
        print("Press Up")
        pyautogui.press('down')
    elif gesture == 4:
        print("Press Up")
        pyautogui.press('up')
