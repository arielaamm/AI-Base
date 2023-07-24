import cv2
import numpy as np


def rotate_image(image_path, angle_degrees) -> np.ndarray:
    # Step 1: Load the image
    image = cv2.imread(image_path)

    # Step 2: Get image dimensions
    (h, w) = image.shape[:2]

    # Step 3: Calculate the center of the image
    center = (w // 2, h // 2)

    # Step 4: Perform the rotation
    rotation_matrix = cv2.getRotationMatrix2D(center, -angle_degrees, 1.0)
    rotated_image = cv2.warpAffine(
        image, rotation_matrix, (w, h), flags=cv2.INTER_CUBIC)
    return rotated_image