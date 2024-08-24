import numpy as np
import cv2
from utils import load_images, preprocess_image, compute_features, match_features, estimate_pose, reconstruct_3d

def main():
    input_dir = "../data/images/"
    output_dir = "../output/"
    
    images = load_images(input_dir)
    preprocessed_images = [preprocess_image(img) for img in images]
    
    features = [compute_features(img) for img in preprocessed_images]
    matches = [match_features(features[i], features[i+1]) for i in range(len(features) - 1)]
    
    poses = [estimate_pose(matches[i], features[i], features[i+1]) for i in range(len(matches))]
    points_3d = reconstruct_3d(poses, images)
    
    np.save(f"{output_dir}/points_3d.npy", points_3d)
    print("3D reconstruction complete. Points saved to", f"{output_dir}/points_3d.npy")

if __name__ == "__main__":
    main()
