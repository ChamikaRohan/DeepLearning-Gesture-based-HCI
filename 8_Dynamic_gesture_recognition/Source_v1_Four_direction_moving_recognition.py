import cv2
import mediapipe as mp

def dynamic_action_finder(cap):
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
    mp_drawing = mp.solutions.drawing_utils

    prev_landmarks = None

    while True:
        # Read the frame from the webcam
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.flip(frame, 1)  # Flip the frame horizontally for a later selfie-view display
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame and detect hands
        result = hands.process(frame_rgb)

        if result.multi_hand_landmarks:
            moving = False
            direction = None
            for hand_landmarks in result.multi_hand_landmarks:
                if prev_landmarks is not None:
                    # Compare current landmarks with previous ones
                    prev_x = prev_landmarks[0].x
                    prev_y = prev_landmarks[0].y
                    curr_x = hand_landmarks.landmark[0].x
                    curr_y = hand_landmarks.landmark[0].y

                    # Calculate the difference in x and y coordinates
                    dx = curr_x - prev_x
                    dy = curr_y - prev_y

                    # Determine the direction based on the sign of dx and dy
                    if abs(dx) > abs(dy):
                        if dx > 0:
                            direction = "Right"
                        else:
                            direction = "Left"
                    else:
                        if dy > 0:
                            direction = "Down"
                        else:
                            direction = "Up"

                    # Check if there's significant movement
                    if abs(dx) > 0.06 or abs(dy) > 0.06:
                        moving = True

                prev_landmarks = hand_landmarks.landmark

                # Draw landmarks on the frame
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            if moving:
                print(f"Yes, moving {direction}")
            else:
                print("No")
        else:
            print("No")
            prev_landmarks = None

"""
cap = cv2.VideoCapture(0)
dynamic_action_finder(cap)
"""