import cv2
import os
import constants

# Directory path for input sharp images
sharp_img_dir = constants.SHARP_IMG_DIR
# Directory path for resulting blurred images
blurred_img_dir = constants.GAUSSIAN_BLUR_IMG_DIR

# Method for blurring images
def blur_images():
    # Read all image paths in sharp images directory
    img_paths = os.listdir(sharp_img_dir)
    # Iterate over all images
    for img_path in img_paths:
        # Read a specific sharp image from its path
        sharp_img = cv2.imread(f'{sharp_img_dir}/{img_path}', cv2.IMREAD_COLOR)
        # Using OpenCV Gaussian Blur function to create blurring
        blur_img = cv2.GaussianBlur(sharp_img, (31, 31), 0)
        # Writing blurred images to the output directory
        cv2.imwrite(f'{blurred_img_dir}/{img_path}', blur_img)

# Invoke the method to generate blurred images from sharp images
blur_images()
