import subprocess
from Words_finder import specific_words_finder

def text_to_application_mapper(input_string):
    application_mapping = {
        "word": r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE",
        "powerpoint": r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE",
        "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "notepad": r"C:\Windows\System32\notepad.exe",
        "calculator": r"C:\Windows\System32\calc.exe",
        "photoshop": r"D:\Adobe Phototshop 2023\Adobe Photoshop 2023\Photoshop.exe",
        "visual Studio Code": r"C:\Users\YourUsername\AppData\Local\Programs\Microsoft VS Code\Code.exe",
        "zoom": r"C:\Users\M\AppData\Roaming\Zoom\bin\Zoom.exe"  # Example path to Zoom
    }
    input_string_lower = input_string.lower()
    for app_name, app_command in application_mapping.items():
        if specific_words_finder(input_string_lower, [app_name]):
            try:
                subprocess.Popen(app_command)
                print(f"Opening {app_name}")
            except Exception as e:
                print(f"Failed to open {app_name}: {e}")


"""
input_string = "I need to open powerpoint"
text_to_application_mapper(input_string)
"""



