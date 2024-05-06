import pyautogui
from Utils.Focus_on_window import focus_on_window
from Utils.Powerpoint_mode_checker import is_fullscreen_mode
import time

"""
Function to control reading and browsing functionalities

Gesture Mapping:
4: Scrolling down
0: Scrolling up
3: Zooming in
2: Zooming out
"""
def control_reading(gesture):
    #Find and activae the movie player window
    window_titles = ["Microsoft Edge", "Word", "Google Chrome"]
    for title in window_titles:
        focus_on_window(title)
    if gesture == None:
        return
    elif gesture == 4:
        print("Scrolling down")
        pyautogui.scroll(-80)
        for _ in range(10):
            pyautogui.scroll(-50)
    elif gesture == 0:
        print("Scrolling up")
        pyautogui.scroll(80)
        for _ in range(10):
            pyautogui.scroll(50)
    elif gesture == 3:
        print("Zooming in")
        pyautogui.keyDown('ctrl')
        pyautogui.press('+')
        pyautogui.keyUp('ctrl')
    elif gesture == 2:
        print("Zooming out")
        pyautogui.keyDown('ctrl')
        pyautogui.press('-')
        pyautogui.keyUp('ctrl')



