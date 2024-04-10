#Manual substraction

import cv2
import numpy as np

#Input
cap = cv2.VideoCapture(0)

_, first_frame = cap.read()
first_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
first_gray = cv2.GaussianBlur(first_gray, (5, 5), 0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (first_frame.shape[1], first_frame.shape[0]))

while True:
    _, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #cv2.imshow("Grayq frame", gray_frame)
    gray_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)

    difference = cv2.absdiff(first_gray, gray_frame)
    _, difference = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)

    #contours, _ = cv2.findContours(difference, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #contour_img = np.zeros_like(frame)

    #for contour in contours:
     #   area = cv2.contourArea(contour)
      #  if area > 100:  # Exampleqqq threshold for contour area
       #     cv2.drawContours(contour_img, [contour], 0, (0, 255, 0), 2)qq

    cv2.imshow("First frame", first_frame)
    cv2.imshow("Frame", frame)
    cv2.imshow("difference", difference)
    #cv2.imshow("Contours", contour_img)

    # Check for key press and break loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    key = cv2.waitKey(30)
    if key == 27:
        break
cap.release()
out.release()
cv2.destroyAllWindows()

