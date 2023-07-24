import cv2
import numpy as np

from rotate_image import rotate_image


def deskew(image):

    # Step 2: Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Step 3: Apply Canny edge detection
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)

    # Step 4: Apply Hough Line Transform
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 100)

    # Step 5: Filter horizontal lines
    horizontal_lines = []
    for line in lines:
        for rho, theta in line:
            angle_degrees = theta * 180 / np.pi
            if 85 <= angle_degrees <= 95 or 265 <= angle_degrees <= 275:  # Threshold for horizontal lines
                horizontal_lines.append(line)

    # Step 6: Inspect the first horizontal line
    if horizontal_lines:
        first_horizontal_line = horizontal_lines[0]
        rho, theta = first_horizontal_line[0]
        angle_degrees = theta * 180 / np.pi

        print("Rho (distance from origin):", rho)
        print("Angle (in degrees):", angle_degrees)
        return (rho, angle_degrees)

    else:
        print("No horizontal lines found.")
        return 0

'''rotate the image'''
# Example usage
input_image = cv2.imread('handwritten_text2.jpg')

deskewed_image = rotate_image('handwritten_text2.jpg', 0)
if type(deskewed_image) == type(input_image):
    cv2.imshow('Original Image', input_image)
    cv2.imshow('Deskewed Image', deskewed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("error")
