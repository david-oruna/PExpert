from PIL import Image
import numpy as np
import cv2


def haller_index_(img):
    # Convert the image to a binary image using thresholding

    _, binary_image = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY)

    # Define a kernel for morphological operations
    kernel = np.ones((5, 5), np.uint8)

    # Apply morphological opening to remove noise
    opened_image = cv2.morphologyEx(binary_image, cv2.MORPH_OPEN, kernel)

    # Apply morphological closing to fill gaps
    closed_image = cv2.morphologyEx(opened_image, cv2.MORPH_CLOSE, kernel)
    
    # Find the rows and columns where the binary image is white (255)
    rows, cols = np.where(binary_image == 255)
    min_col, max_col = cols.min(), cols.max()
    center_col = (min_col + max_col) // 2

    # Find the vertical distance between the topmost and bottommost white pixels in the center column
    white_pixel_rows = np.where(binary_image[:, center_col] == 255)[0]
    vertical_distance = white_pixel_rows.max() - white_pixel_rows.min()

    # If the vertical distance is less than 50, use the mean vertical distance
    if vertical_distance < 50:
        vertical_distance = white_pixel_rows.mean()

    # Calculate the horizontal distances for each row
    horizontal_distances = []
    for row in range(binary_image.shape[0]):
        white_pixel_columns = np.where(binary_image[row, :] == 255)[0]
        if white_pixel_columns.size > 0:
            horizontal_distance = white_pixel_columns.max() - white_pixel_columns.min()
            horizontal_distances.append(horizontal_distance)

    # If there are horizontal distances, calculate the Haller index
    if horizontal_distances:
        max_horizontal_distance = max(horizontal_distances)
        haller_index = max_horizontal_distance / vertical_distance
        return haller_index
    else:
        return None
