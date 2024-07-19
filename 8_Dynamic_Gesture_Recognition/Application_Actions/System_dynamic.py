import pyautogui
from Utils.Focus_on_window import focus_on_window
from Utils.Powerpoint_mode_checker import is_fullscreen_mode
import time
import sys

sys.path.append('../4_Voice_Assistance/Speech_to_application')
from Speech_to_app_composer import speech_to_app_composer

"""
Function to control system functionalities

Gesture Mapping:
5: Taking a screenshot
3: Switch between applications
4: Increase System Volume
0: Decrease System Volume
2: Activate sleep mode
6: Open Task Manager
7: Trigger speech to application
"""
def dynamic_control_system(gesture):
    if gesture == None:
        return
    elif gesture == 32 or gesture == 33 or gesture == 30 or gesture == 31:
        print("Taking a screenshot")
        pyautogui.hotkey("winleft", "printscreen")
        time.sleep(1)
    elif gesture == 22 or gesture == 23:
        print("Switch between applications")
        pyautogui.keyDown('alt')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.keyUp('alt')
    elif gesture == 28:
        print("Increase System Volume")
        pyautogui.hotkey('volumeup')
        time.sleep(0.5)
    elif gesture == 29:
        print("Decrease System Volume")
        pyautogui.hotkey('volumedown')
        time.sleep(0.5)
    elif gesture == 42 or gesture == 43 or gesture == 44 or gesture == 44:
        print("Activate sleep mode")
        pyautogui.hotkey("winleft", "x")
        pyautogui.typewrite("u")
        pyautogui.typewrite("s")
    elif gesture == 34 or gesture == 35 or gesture == 36 or gesture == 37:
        print("Open Task Manager")
        pyautogui.hotkey("ctrl", "shift", "esc")
    elif gesture == 40 or gesture == 41 or gesture == 38 or gesture == 39:
        print("Trigger speech to application")
        speech_to_app_composer()

