import pyautogui
import time
import webbrowser
import sys

sys.path.append('../2_Application_Actions')
from Utils.Focus_on_window import focus_on_window
from Utils.Powerpoint_mode_checker import is_fullscreen_mode
from Utils.URL_Reader import URL_origin_finder

sys.path.append('../4_Voice_Assistance')
from Speech_to_text_generator import speech_to_text
from Text_to_speech_generator import text_to_speech

"""
Function to control reading and browsing functionalities

Gesture Mapping:
4: Scrolling down
0: Scrolling up
3: Zooming in
2: Zooming out
"""
def dynamic_control_youtube(gesture):
    #Find and activate the YouTube-Google Chrome window
    window_titles = ["YouTube - Google Chrome"]
    for title in window_titles:
        focus_on_window(title)
    if gesture == None:
        return
    elif gesture == 29:
        print("Scrolling down")
        pyautogui.click(x=0, y=700)
        pyautogui.scroll(-80)
        for _ in range(10):
            pyautogui.scroll(-50)
    elif gesture == 28:
        print("Scrolling up")
        pyautogui.click(x=0, y=700)
        pyautogui.scroll(80)
        for _ in range(10):
            pyautogui.scroll(50)
    elif gesture == 22 or gesture == 23 or gesture == 24 or gesture == 25:
        print("Search Youtube")
        pyautogui.click(x=800, y=190)
        pyautogui.hotkey("ctrl", "a")
        pyautogui.hotkey('backspace')
        text = speech_to_text()
        print(text)
        if text is None:
            text_to_speech("I could't hear what you said. Please try again!")
            print("Speech recognition failed. Please try again...")
        else:
            print("Typing '{}' into the search bar".format(text))
            pyautogui.typewrite(text, interval=0.1)
            pyautogui.press('enter')
            time.sleep(2)
    elif gesture == 18 or gesture == 19:
        print("Select video")
        pyautogui.click(x=800, y=600)
        time.sleep(1)
    elif gesture == 32 or gesture == 33:
        print("Activate full-screen mode")
        pyautogui.click(x=0, y=600)
        pyautogui.press('f')
        time.sleep(1)
    elif gesture == 21 or gesture == 20:
        print("Play/Pause video")
        pyautogui.click(x=0, y=600)
        pyautogui.press('space')
        time.sleep(1)
    elif gesture == 40 or gesture == 41 or gesture == 38 or gesture == 39:
        print("Goto homes page")
        pyautogui.click(x=215, y=190)
        time.sleep(1)



