import cv2
import numpy as np

def load_images(directory):
    images = []
    for i in range(1, 49):
        path = f"{directory}/image{i}.png"
        img = cv2.imread(path)
        if img is not None:
            images.append(img)
        else:
            print(f"Failed to load image {path}")
    return images

def preprocess_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return cv2.equalizeHist(gray)

def compute_features(image):
    sift = cv2.SIFT_create()
    keypoints, descriptors = sift.detectAndCompute(image, None)
    return keypoints, descriptors

def match_features(desc1, desc2):
    bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)
    matches = bf.match(desc1[1], desc2[1])
    return sorted(matches, key=lambda x: x.distance)

def estimate_pose(matches, features1, features2):
    src_pts = np.float32([features1[0][m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
    dst_pts = np.float32([features2[0][m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)
    H, _ = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
    return H

def reconstruct_3d(poses, images):
    # Simplified 3D reconstruction
    points_3d = []
    for pose in poses:
        # This is a placeholder; actual 3D reconstruction requires more complex algorithms
        points_3d.append(pose)  
    return np.array(points_3d)
