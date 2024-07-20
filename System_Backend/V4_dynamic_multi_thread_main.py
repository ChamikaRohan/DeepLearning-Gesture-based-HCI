import sys
import cv2
import threading

sys.path.append('../2_Application_Actions')
from Orchestrator import orchestrator

sys.path.append('../1_Model_Binding')
from Gesture_prediction_func import predict_gesture
from Dynamic_gesture_prediction_func import predict_gesture_and_direction
from Utils.First_frame_getter import first_frame_getter

sys.path.append('../3_Intended_Gesture_Mapping')
from Intended_gesture_mapping_func import intended_gesture_map
from dynamic_intended_gesture_mapping_func import intended_gesture_and_direction_map

sys.path.append('../8_Dynamic_Gesture_Recognition')
from Dynamic_gesture_extender import combined_gesture_number_finder

sys.path.append('../5_Mode_Selector')
from Mode_selector import mode_selector
from Mode_engine import engine
from Mode_toggler import mode_toggler

sys.path.append('../6_Settings')
from Application_settings import ask_for_setting

sys.path.append('../8_Dynamic_Gesture_Recognition')
from Gesture_type_selector import gesture_type_selector
from Dynamic_mode_engine import dynamic_engine

sys.path.append('../9_Mobile_App')
from flask_server import run_flask_server

from collections import deque

model_path = "../1_Model_Binding/Media/10_gesture_model_25th_attempt.h5"
cap = cv2.VideoCapture(0)
first_gray = first_frame_getter(cap)

gesture_type = gesture_type_selector()
mode = mode_selector()

gesture_frames = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
direction_frames = deque()

def dynamic_main(cap, first_gray, gesture_type, mode,model_path, gesture_frames, direction_frames):
    if gesture_type == 1:
        for gesture in predict_gesture(cap, model_path, first_gray):
            if gesture == 's':
                choice = ask_for_setting()
                if choice == 1:
                    mode = mode_toggler(mode)
            else:
                print("Predicted Gesture:", gesture)
                intended_gesture = intended_gesture_map(gesture, gesture_frames)
                print("Intended Gesture:", intended_gesture)
                engine(mode, intended_gesture)
    else:
        for gesture, direction in predict_gesture_and_direction(cap, model_path, first_gray, gesture_type):
            if gesture == 's':
                choice = ask_for_setting()
                if choice == 1:
                    mode = mode_toggler(mode)
            else:
                # print("Predicted Gesture:", gesture)
                intended_gesture, intended_direction = intended_gesture_and_direction_map(gesture, direction,
                                                                                          gesture_frames,
                                                                                          direction_frames)
                print("Intended Gesture:", intended_gesture)
                print("Intended Direction:", intended_direction)
                intended_combined_gesture = combined_gesture_number_finder(intended_gesture, intended_direction)
                print(intended_combined_gesture)
                dynamic_engine(mode, intended_combined_gesture)

def main_thread():
    global cap, first_gray, gesture_type, mode,model_path, gesture_frames, direction_frames

    thread1 = threading.Thread(target=dynamic_main, args=(cap, first_gray, gesture_type, mode,model_path, gesture_frames, direction_frames))
    thread2 = threading.Thread(target=run_flask_server)

    #Start both threads
    thread1.start()
    thread2.start()

    #Wait for both threads to complete
    thread1.join()
    thread2.join()

    #Release the video capture object and close any open windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main_thread()