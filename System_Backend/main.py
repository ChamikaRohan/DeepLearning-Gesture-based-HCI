import sys
import cv2

sys.path.append('../2_Application_Actions')
from Orchestrator import orchestrator

sys.path.append('../1_Model_Binding')
from Gesture_prediction_func import predict_gesture

sys.path.append('../3_Intended_Gesture_Mapping')
from Intended_gesture_mapping_func import intended_gesture_map

model_path = "../1_Model_Binding/Media/5_gesture_model_8thattempt.h5"
cap = cv2.VideoCapture(0)

 # Initialize the consecutive frames
consecutive_frames = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
for gesture in predict_gesture(cap, model_path):
    orchestrator(intended_gesture_map(gesture,consecutive_frames))