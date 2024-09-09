import cv2
import numpy as np

def auto_first_frame_setter(difference, min_area=20, max_area=200, max_noise_contours=200, max_white_pixels=50000):
    contours, _ = cv2.findContours(difference, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    noise_contour_count = 0
    total_white_pixels = np.sum(difference == 255)  # Count all white pixels (value 255)

    for contour in contours:
        area = cv2.contourArea(contour)
        if min_area < area < max_area:
            noise_contour_count += 1

    return noise_contour_count > max_noise_contours or total_white_pixels > max_white_pixels