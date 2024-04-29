#consecutive_frames = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
def intended_gesture_map(predicted_class, consecutive_frames):
    print("What intended func got...")
    print(predicted_class)
    if predicted_class == 0:
        consecutive_frames[0] += 1
    else:
        consecutive_frames[0] = 0

    if predicted_class == 1:
        consecutive_frames[1] += 1
    else:
        consecutive_frames[1] = 0

    if predicted_class == 2:
        consecutive_frames[2] += 1
    else:
        consecutive_frames[2] = 0

    if predicted_class == 3:
        consecutive_frames[3] += 1
    else:
        consecutive_frames[3] = 0

    if predicted_class == 4:
        consecutive_frames[4] += 1
    else:
        consecutive_frames[4] = 0

    for gesture, count in consecutive_frames.items():
        if count == 3:
            print("Inteded............")
            print(gesture)
            return gesture
