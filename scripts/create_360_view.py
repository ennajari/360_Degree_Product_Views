import os
import cv2
import numpy as np
from PIL import Image

def create_360_view(input_folder, output_file, num_frames=36):
    image_files = [f for f in os.listdir(input_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]
    image_files.sort() 

    first_image = cv2.imread(os.path.join(input_folder, image_files[0]))
    height, width = first_image.shape[:2]

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_file, fourcc, 30, (width, height))

    for _ in range(3):  
        for image_file in image_files:
            image_path = os.path.join(input_folder, image_file)
            frame = cv2.imread(image_path)
            
            for _ in range(5):  
                out.write(frame)

    out.release()

    print(f"360-degree view created and saved as {output_file}")

if __name__ == "__main__":
    input_folder = "data/images/Ball_Cap"  
    output_file = "output/ball_cap_360_view.mp4"
    create_360_view(input_folder, output_file)