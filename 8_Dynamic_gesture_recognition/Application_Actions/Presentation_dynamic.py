import time
import sys

import pyautogui
sys.path.append('../2_Application_Actions')
from Utils.Focus_on_window import focus_on_window

"""
Function to control presentation slides

Gesture Mapping:
4: Go to previous slide (left)
3: Go to next slide (right)
0: Enter slide show mode
5: Exit slide show mode
"""
def dynamic_control_presentation(gesture):
    #Find and activate the presentation window
    window_titles = ["PowerPoint"]
    for title in window_titles:
        focus_on_window(title)
    if gesture == None:
        return
    elif gesture == 32 or gesture == 33:
        print("Slide Show Mode On")
        pyautogui.press("f5")
        time.sleep(1)
    elif gesture == 21 or gesture == 20:
        print("Slide Show Mode Off")
        pyautogui.press("esc")
    elif gesture == 22:
        print("Switch to Next Slide")
        pyautogui.hotkey("right")
        time.sleep(0.5)
    elif gesture == 23:
        print("Switch to Previous Slide")
        pyautogui.hotkey("left")
        time.sleep(0.5)

