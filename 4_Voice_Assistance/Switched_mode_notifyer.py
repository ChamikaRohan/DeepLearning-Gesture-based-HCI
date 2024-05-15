from Text_to_speech_generator import text_to_speech
def speak_mode(mode):
    if mode == 1:
        text_to_speech("Switched to manual mode.")
    elif mode == 2:
        text_to_speech("Switched to auto mode.")