import os
import cv2
import numpy as np

def load_images(image_dir):
    images = []
    for file_name in sorted(os.listdir(image_dir)):
        img_path = os.path.join(image_dir, file_name)
        img = cv2.imread(img_path)
        if img is not None:
            images.append(img)
    return images

def preprocess_images(images):
    processed_images = []
    for img in images:
        img_resized = cv2.resize(img, (128, 128))
        processed_images.append(img_resized)
    return np.array(processed_images)

if __name__ == "__main__":
    # Current script directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Define the relative path to the images directory
    image_dir = os.path.join(current_dir, '../data/images/')
    
    images = load_images(image_dir)
    processed_images = preprocess_images(images)
    
    # Save the processed images
    output_dir = os.path.join(current_dir, '../output/')
    os.makedirs(output_dir, exist_ok=True)
    np.save(os.path.join(output_dir, 'processed_images.npy'), processed_images)
    print("Images have been processed and saved.")
