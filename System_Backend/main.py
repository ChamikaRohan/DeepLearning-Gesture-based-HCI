import sys
import cv2

sys.path.append('../2_Application_Actions')
from Orchestrator import orchestrator

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

model_path = "../1_Model_Binding/Media/9_gesture_model_23th_attempt.h5"
cap = cv2.VideoCapture(0)
first_gray = first_frame_getter(cap)

mode = mode_selector()

consecutive_frames = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6:0, 7: 0, 8: 0}
for gesture in predict_gesture(cap, model_path, first_gray):
    if gesture == 's':
        choice = ask_for_setting()
        if choice == 1:
            mode=  mode_toggler(mode)
    else:
        print("Predicted Gesture:", gesture)
        intended_gesture = intended_gesture_map(gesture,consecutive_frames)
        print("Intended Gesture:", intended_gesture)
        engine(mode, intended_gesture)

