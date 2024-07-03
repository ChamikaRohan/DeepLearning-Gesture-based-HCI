"""
gesture_frames = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
direction_frames = deque()

cap = cv2.VideoCapture(0)
update_first_frame = False
first_gray = first_frame_getter(cap)
model_path = "Media/10_gesture_model_25th_attempt.h5"
for gesture, direction in predict_gesture_and_direction(cap, model_path, first_gray):
    if gesture is None:
        print("No gesture detected.")
    else:
        print("Predicted Gesture:", gesture)
        print("Predicted Direction:", direction)
        intended_gesture, intended_direction = intended_gesture_and_direction_map(gesture, direction, gesture_frames, direction_frames)
        print("Intended :", intended_gesture, intended_direction)

"""