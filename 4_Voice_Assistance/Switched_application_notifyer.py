from Text_to_speech_generator import text_to_speech

def speak_application(gesture):
    # Dictionary mapping option numbers to application names
    applications = {
        0: "media player",
        2: "system",
        3: "reading",
        4: "presentation",
        5: "youtube",
        6: "zoom",
        7: "custom application"
    }

    # Convert the selected option to speech
    if gesture in applications:
        text_to_speech(f"Switched to {applications[gesture]} control.")
    else:
        text_to_speech("Invalid option.")