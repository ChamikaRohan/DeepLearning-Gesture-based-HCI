import pygetwindow as gw

"""
Function to focus on a window with the provided title
"""
def focus_on_window(window_title):
    windows = gw.getWindowsWithTitle(window_title)
    if windows == []:
        return
    if len(windows) > 1:
        window = windows[1]
        if isinstance(window_title, tuple):
            window.maximize()
        else:
            window.maximize()
    else:
        window = windows[0]
        window.maximize()


"""
window_titles = ["VLC"]
for title in window_titles:
    focus_on_window(title)
"""


