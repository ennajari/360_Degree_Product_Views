import cv2
import numpy as np
import os
from pathlib import Path

def create_360_view(images_path, output_path):
    images = [cv2.imread(os.path.join(images_path, img)) for img in sorted(os.listdir(images_path))]
    if not images:
        raise ValueError("No images found in the directory.")

    # Assuming images are of the same size
    height, width, _ = images[0].shape
    video_writer = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'XVID'), 20.0, (width, height))

    for img in images:
        video_writer.write(img)

    video_writer.release()
    print(f"360-degree view video saved to {output_path}")

if __name__ == "__main__":
    create_360_view('data/images/Ball_Cap', 'output/ball_cap_360_view.avi')
