import os
import numpy as np
import matplotlib.pyplot as plt
import cv2  # Ajout de l'import de la bibliothèque OpenCV

def visualize_images(images):
    for i, img in enumerate(images):
        plt.subplot(1, len(images), i+1)
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        plt.axis('off')
    plt.show()

if __name__ == "__main__":
    # Current script directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Define the relative path to the processed images file
    processed_images_path = os.path.join(current_dir, '../output/processed_images.npy')
    
    images = np.load(processed_images_path)
    visualize_images(images)
