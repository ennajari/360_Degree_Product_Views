import os
from preprocess import load_images
from visualize import visualize_images

if __name__ == "__main__":
    # Current script directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Define the relative path to the images directory
    image_dir = os.path.join(current_dir, '../data/images/')
    
    images = load_images(image_dir)
    
    # Visualize the loaded images
    visualize_images(images)
