import cv2
import numpy as np
from PIL import Image

def getEstimation(image):
    pil_image = Image.open(image)

    # Get DPI from metadata
    dpi = pil_image.info.get("dpi")

    # Convert to NumPy array for OpenCV operations
    image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)

    # Convert to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_green = (30, 50, 50)
    upper_green = (80, 255, 255)

    mask = cv2.inRange(hsv_image, lower_green, upper_green)

    plant_area = cv2.countNonZero(mask)

    # Estimate LAI assuming average basil leaf area and flat leaves
    average_leaf_area = 0.01
    ground_area = image.shape[0] * image.shape[1] / (dpi[0] * dpi[1])

    # Calculate estimated LAI
    estimated_lai = plant_area / ground_area * average_leaf_area

    # Print results
    return estimated_lai
