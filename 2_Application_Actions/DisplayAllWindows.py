import pygetwindow as gw

def display_all_windows():
    open_windows = gw.getAllTitles()
    return open_windows

if __name__ == "__main__":
    open_windows = display_all_windows()
    print("Opened Windows:")
    for window_title in open_windows:
        print(window_title)
