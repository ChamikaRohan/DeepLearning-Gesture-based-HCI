from Text_to_speech_generator import text_to_speech

def dynamic_speak_application(gesture):
    # Dictionary mapping option numbers to application names
    applications = {
        0: "media player",
        10: "media player",
        11: "media player",
        12: "media player",
        13: "media player",

        2: "system",
        18: "system",
        19: "system",
        20: "system",
        21: "system",

        3: "reading",
        22: "reading",
        23: "reading",
        24: "reading",
        25: "reading",

        4: "presentation",
        26: "presentation",
        27: "presentation",
        28: "presentation",
        29: "presentation",

        5: "youtube",
        30: "youtube",
        31: "youtube",
        32: "youtube",
        33: "youtube",

        6: "zoom",
        34: "zoom",
        35: "zoom",
        36: "zoom",
        37: "zoom",
    }

    # Convert the selected option to speech
    if gesture in applications:
        text_to_speech(f"Switched to {applications[gesture]} control.")
    else:
        text_to_speech("Invalid option.")