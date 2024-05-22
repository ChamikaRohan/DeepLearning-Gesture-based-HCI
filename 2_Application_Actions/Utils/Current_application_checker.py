import time

import cv2
import win32gui
import win32process
import psutil
import pygetwindow as gw
from URL_Reader import URL_origin_finder

model_path = "../1_Model_Binding/Media/6_gesture_model_9th_attempt_part_3_without_pretrained.h5"
cap = cv2.VideoCapture(0)

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
    while True:
        active_pid = get_active_window_pid()
        if active_pid:
            process_name = get_process_name(active_pid)
            if process_name == 'vlc.exe' or process_name == 'ApplicationFrameHost.exe':
                application = 0
                break;
            elif process_name == 'POWERPNT.EXE':
                application = 3
                break;
            elif process_name == 'msedge.exe' or process_name == 'WINWORD.EXE':
                application = 2
                break;
            elif process_name == 'chrome.exe':
                if URL_origin_finder() == 'youtube':
                    application = 4
                    break;
                elif URL_origin_finder() == 'canva':
                    application = 3
                    break;
                else:
                    application = 2
                    break;
            else:
                application = 1
                break;
    print(f"Active Application: {process_name} -> {application}")
    return application

