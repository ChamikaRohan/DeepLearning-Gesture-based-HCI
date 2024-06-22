import win32gui

"""
Function to search for the correct window title
"""

def window_title_matcher(user_given_custom_window_titles):
    def callback(hwnd, hwnd_list):
        if win32gui.IsWindowVisible(hwnd):
            window_title = win32gui.GetWindowText(hwnd)
            for target_title in user_given_custom_window_titles:
                if target_title.lower() in window_title.lower():
                    hwnd_list.append((hwnd, window_title))

    hwnd_list = []
    win32gui.EnumWindows(callback, hwnd_list)

    hwnd_list.sort(key=lambda x: len(x[1]), reverse=True)
    print(hwnd_list[0][1] if hwnd_list else None)
    return hwnd_list[0][1] if hwnd_list else None


"""
print(window_title_matcher(["photoshop", "hero"]))
"""
