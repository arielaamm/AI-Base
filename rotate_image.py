import math
import cv2
import numpy as np


def rotate_image(image, angle_degrees) -> np.ndarray:
    # Step 1: Load the image
    image = cv2.imread(image)

    # Step 2: Get image dimensions
    (h, w) = image.shape[:2]

    # Step 3: Calculate the center of the image
    center = (w // 2, h // 2)

    # Step 4: Perform the rotation
    rotation_matrix = cv2.getRotationMatrix2D(center, -angle_degrees, 1.0)
    rotated_image = cv2.warpAffine(
        image, rotation_matrix, (w, h), flags=cv2.INTER_CUBIC)
    return rotated_image

def get_angle_rotation(image):
    list = []
    (h, w) = image.shape[:2]
    for i in range(360):
        angle_radians = math.radians(i)
        slope = math.tan(angle_radians)
        for x in range(w, 0, -1):
            for y in range(h):
                list +=(count_ray_intersections(image,(x,y),(w,w*slope)),i)
    return max(list)[1]

def count_ray_intersections(image, start_point, end_point):
    # Apply Canny edge detection
    edges = cv2.Canny(image, 100, 200)

    # Initialize the number of intersections
    num_intersections = 0

    # Get the (x, y) coordinates of the line segment
    x1, y1 = start_point
    x2, y2 = end_point

    # Get the slope of the line segment
    dx = x2 - x1
    dy = y2 - y1

    # Calculate the step size for the ray
    num_steps = max(abs(dx), abs(dy))
    if num_steps != 0:
        x_step = dx / num_steps 
        y_step = dy / num_steps
    else:
        return 0

    # Start from the starting point and increment along the ray
    x, y = x1, y1
    for _ in range(int(num_steps)):
        # Round the coordinates to integers to access the pixel values
        x_rounded, y_rounded = int(round(x)), int(round(y))

        # Check if the pixel is within the image bounds
        if 0 <= y_rounded < image.shape[0] and 0 <= x_rounded < image.shape[1]:
            # Check if the pixel is an edge (white pixel in the Canny edge-detected image)
            if edges[y_rounded, x_rounded] == 255:
                num_intersections += 1

        # Move along the ray
        x += x_step
        y += y_step

    return num_intersections



input_image = cv2.imread('images//handwritten_text.jpg')
a = get_angle_rotation(input_image)
deskewed_image = rotate_image(input_image,a)

if type(deskewed_image) == type(input_image):
    cv2.imshow('Original Image', input_image)
    cv2.imshow('Deskewed Image', deskewed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("error")