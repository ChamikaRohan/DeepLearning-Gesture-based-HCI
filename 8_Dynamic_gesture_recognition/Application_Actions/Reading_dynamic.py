import pyautogui

import sys

sys.path.append('../4_Voice_Assistance/Speech_to_read_control/Comment_control')
from Speech_to_comment_composer import speech_to_comment_composer

sys.path.append('../2_Application_Actions')
from Utils.Focus_on_window import focus_on_window

"""
Function to control reading and browsing functionalities

Gesture Mapping:
4: Scrolling down
0: Scrolling up
3: Zooming in
2: Zooming out
5: Toggle Full-Screen Mode
7: Add a comment
"""
def dynamic_control_reading(gesture):
    #Find and activate the movie player window
    window_titles =  [" - Microsoft​ Edge"]
    for title in window_titles:
        focus_on_window(title)
    if gesture == None:
        return
    elif gesture == 29:
        print("Scrolling down")
        pyautogui.scroll(-80)
        for _ in range(10):
            pyautogui.scroll(-50)
    elif gesture == 28:
        print("Scrolling up")
        pyautogui.scroll(80)
        for _ in range(10):
            pyautogui.scroll(50)
    elif gesture == 19:
        print("Zooming in")
        pyautogui.hotkey("ctrl", "+")
    elif gesture == 18:
        print("Zooming out")
        pyautogui.hotkey("ctrl", "_")
    elif gesture == 20:
        print("Toggling Full-Screen Mode")
        pyautogui.hotkey("f11")
    elif gesture == 7:
        print("Adding a comment")
        speech_to_comment_composer()




