import speech_recognition as sr
import sys

sys.path.append('../7_Sound_manipulating')
from Mp3_player import mp3_player

def speech_to_text(timeout=5):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        mp3_player('..\Assets\Sounds\pick_up.mp3')
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=timeout)
        except sr.WaitTimeoutError:
            print("Timeout occurred while waiting for speech to start. Please speak louder or move closer to the microphone.")
            return None

    try:
        text = recognizer.recognize_google(audio)
        mp3_player('..\Assets\Sounds\pick_down.mp3')
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        return None
    except sr.RequestError as e:
        print("Sorry, I couldn't request results from Google Speech Recognition service; {0}".format(e))
        return None
