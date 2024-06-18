import cv2

def is_noisy(difference, min_area=20, max_area=200):
    contours, _ = cv2.findContours(difference, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    noise_count = 0
    for contour in contours:
        area = cv2.contourArea(contour)
        if min_area < area < max_area:
            noise_count += 1
    return noise_count > 35