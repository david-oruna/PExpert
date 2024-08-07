from PIL import Image
import numpy as np
import cv2

def haller_index(img_path):
    image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    
    _, binary_image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY)

    kernel = np.ones((5,5), np.uint8)
    opened_image = cv2.morphologyEx(binary_image, cv2.MORPH_OPEN, kernel)

    closed_image = cv2.morphologyEx(opened_image, cv2.MORPH_CLOSE, kernel)
    
    rows, cols = np.where(binary_image == 255)
    min_col, max_col = cols.min(), cols.max()
    center_col = (min_col + max_col) // 2
    white_pixel_rows = np.where(binary_image[:, center_col]==255)[0]
    vertical_distance = white_pixel_rows.max() - white_pixel_rows.min()

    if vertical_distance < 50:
        vertical_distance = white_pixel_rows.mean()


    horizontal_distances = []
    for row in range(binary_image.shape[0]):
        white_pixel_columns = np.where(binary_image[row, :] == 255)[0]
        if white_pixel_columns.size > 0:
            horizontal_distance = white_pixel_columns.max()-white_pixel_columns.min()
            horizontal_distances.append(horizontal_distance)

    if horizontal_distances:
        max_horizontal_distance = max(horizontal_distances)
        haller_index = max_horizontal_distance / vertical_distance
        return haller_index
    else:
        return None


def haller_index_(img):
    image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    _, binary_image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY)

    kernel = np.ones((5,5), np.uint8)
    opened_image = cv2.morphologyEx(binary_image, cv2.MORPH_OPEN, kernel)

    closed_image = cv2.morphologyEx(opened_image, cv2.MORPH_CLOSE, kernel)
    
    rows, cols = np.where(binary_image == 255)
    min_col, max_col = cols.min(), cols.max()
    center_col = (min_col + max_col) // 2
    white_pixel_rows = np.where(binary_image[:, center_col]==255)[0]
    vertical_distance = white_pixel_rows.max() - white_pixel_rows.min()

    if vertical_distance < 50:
        vertical_distance = white_pixel_rows.mean()


    horizontal_distances = []
    for row in range(binary_image.shape[0]):
        white_pixel_columns = np.where(binary_image[row, :] == 255)[0]
        if white_pixel_columns.size > 0:
            horizontal_distance = white_pixel_columns.max()-white_pixel_columns.min()
            horizontal_distances.append(horizontal_distance)

    if horizontal_distances:
        max_horizontal_distance = max(horizontal_distances)
        haller_index = max_horizontal_distance / vertical_distance
        return haller_index
    else:
        return None
