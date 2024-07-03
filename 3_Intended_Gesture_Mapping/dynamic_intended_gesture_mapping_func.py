def intended_gesture_and_direction_map(predicted_class, predicted_direction, gesture_frames, direction_frames):
    if predicted_class is not None:
        gesture_frames[predicted_class] += 1
    direction_frames.append(predicted_direction)

    if len(direction_frames) > 5:
        direction_frames.popleft()

    # Check for intended gesture
    intended_gesture = None
    for gesture, count in gesture_frames.items():
        if count == 5:
            intended_gesture = gesture
            break

    if intended_gesture is not None:
        # Reset counts to 0 for all gestures
        for gesture in gesture_frames:
            gesture_frames[gesture] = 0

    # Determine the most frequent direction in the last 5 frames
    if intended_gesture is None:
        intended_direction = None
    else:
        direction_counts = {dir: direction_frames.count(dir) for dir in set(direction_frames)}
        if direction_counts.get("Static", 0) == 5:
            intended_direction = "Static"
        else:
            non_static_directions = {k: v for k, v in direction_counts.items() if k != "Static"}
            intended_direction = max(non_static_directions, key=non_static_directions.get) if non_static_directions else "Static"

    return intended_gesture, intended_direction