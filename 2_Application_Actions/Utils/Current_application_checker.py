import os
import sys
import win32process
import psutil
import pygetwindow as gw
from URL_Reader import URL_origin_finder

sys.path.append('../../2_Application_Actions')
from Custom.Load_gesture_map import load_gesture_map

sys.path.append('../10_Storage_and_utils')
from Payload import Payload

application = None

def get_active_window_pid():
    active_window = gw.getActiveWindow()
    pid = None
    if active_window is not None:
        hwnd = active_window._hWnd
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
    return pid

def get_process_name(pid):
    process = psutil.Process(pid)
    return process.name() if process.is_running() else None

def get_active_application():
    global application

    payload = Payload()
    folder_path = payload.get_custom_config_path()
    file_path = os.path.join(folder_path, 'custom_configs.json')
    custom_config = load_gesture_map(file_path)
    user_given_custom_window_titles = custom_config.get("custom_window_title", [])

    while True:
        active_pid = get_active_window_pid()
        if active_pid:
            process_name = get_process_name(active_pid)
            print(process_name)
            if process_name == 'vlc.exe' or process_name == 'ApplicationFrameHost.exe':
                application = 0
                break
            elif process_name == 'POWERPNT.EXE':
                application = 3
                break
            elif process_name == 'msedge.exe':
                application = 2
                break
            elif process_name == 'chrome.exe':
                if URL_origin_finder() == 'youtube':
                    application = 4
                    break
            elif process_name == 'Zoom.exe':
                application = 5
                break
            elif any(title.lower() in process_name.lower() for title in user_given_custom_window_titles):
                application = 6
                print("Matched custom title!")
                break
            else:
                application = 1
                break;
    print(f"Active Application: {process_name} -> {application}")
    return application

"""
import time
time.sleep(2)
get_active_application()
"""
