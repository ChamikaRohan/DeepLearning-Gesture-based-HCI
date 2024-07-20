import sys
import cv2
import threading  # Import threading module for multi-threading
import time

# Importing necessary modules and functions from other files
sys.path.append('../2_Application_Actions')
from Orchestrator import orchestrator
from Custom.Save_gesture_map import save_gesture_map
from Custom.Load_gesture_map import load_gesture_map

sys.path.append('../1_Model_Binding')
from Gesture_prediction_func import predict_gesture
from Utils.First_frame_getter import first_frame_getter

sys.path.append('../3_Intended_Gesture_Mapping')
from Intended_gesture_mapping_func import intended_gesture_map

sys.path.append('../5_Mode_Selector')
from Mode_selector import mode_selector
from Mode_engine import engine
from Mode_toggler import mode_toggler

sys.path.append('../6_Settings')
from Application_settings import ask_for_setting


def gesture_recognition_thread(cap, model_path):
    try:
        first_gray = first_frame_getter(cap)
        mode = mode_selector()

        consecutive_frames = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

        for gesture in predict_gesture(cap, model_path, first_gray):
            if gesture == 's':
                choice = ask_for_setting()
                if choice == 1:
                    mode = mode_toggler(mode)
            else:
                print("Predicted Gesture:", gesture)
                intended_gesture = intended_gesture_map(gesture, consecutive_frames)
                print("Intended Gesture:", intended_gesture)
                engine(mode, intended_gesture)

    except Exception as e:
        print(f"Error in gesture recognition thread: {str(e)}")



gesture_map = {
    0: "space",    # Play/Stop the movie
    1: "up",       # Example: Increase volume
    2: "down",     # Example: Decrease volume
    3: "right",    # Example: Seek forward
    4: "left",     # Example: Seek backward
    5: "enter",    # Example: Full screen
    6: "esc",      # Example: Exit full screen
    7: "m",        # Example: Mute/Unmute
    8: "p",        # Example: Pause
    9: "s"         # Example: Stop
}
def print_hello():
    while(True):
        time.sleep(1)
        path = input("Enter your input path: ")
        save_gesture_map(path, gesture_map)
        load_gesture_map(path);


# Main program starts here
if __name__ == "__main__":
    model_path = "../1_Model_Binding/Media/10_gesture_model_25th_attempt.h5"
    cap = cv2.VideoCapture(0)

    # Create two threads for concurrent execution
    thread1 = threading.Thread(target=gesture_recognition_thread, args=(cap, model_path))
    thread2 = threading.Thread(target=print_hello)

    # Start both threads
    thread1.start()
    thread2.start()

    # Wait for both threads to complete
    thread1.join()
    thread2.join()

    # Release the video capture object and close any open windows
    cap.release()
    cv2.destroyAllWindows()
