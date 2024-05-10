import time

import pyautogui
import pygetwindow
import pyperclip

def URL_reader():
    # Get the URL of the active tab using pyautogui
    pyautogui.hotkey('ctrl', 'l')  # Focus the address bar
    pyautogui.hotkey('ctrl', 'c')  # Copy the URL
    pyautogui.press('tab')
    return pyperclip.paste()

def URL_origin_finder():
    URL = URL_reader()
    # Check if the URL contains "youtube.com"
    if "youtube.com" in URL:
        return "youtube"
    else:
        return None