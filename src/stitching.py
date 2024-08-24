import cv2
import numpy as np
import os

def stitch_images(images):
    # Initialize the ORB detector
    orb = cv2.ORB_create()
    
    # List to hold keypoints and descriptors
    keypoints_list = []
    descriptors_list = []
    
    # Detect ORB features and compute descriptors
    for img in images:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        keypoints, descriptors = orb.detectAndCompute(gray, None)
        keypoints_list.append(keypoints)
        descriptors_list.append(descriptors)
    
    # Create a BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    
    # Initialize list of matches
    matches_list = []
    
    # Find matches between consecutive images
    for i in range(len(descriptors_list) - 1):
        matches = bf.match(descriptors_list[i], descriptors_list[i+1])
        matches = sorted(matches, key=lambda x: x.distance)
        matches_list.append(matches)
    
    # Compute homographies and stitch images
    stitched_image = images[0]
    for i in range(len(matches_list)):
        # Get the matching keypoints
        src_pts = np.float32([keypoints_list[i][m.queryIdx].pt for m in matches_list[i]]).reshape(-1, 1, 2)
        dst_pts = np.float32([keypoints_list[i+1][m.trainIdx].pt for m in matches_list[i]]).reshape(-1, 1, 2)
        
        # Compute homography
        H, _ = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC)
        
        # Warp the image
        height, width = images[i+1].shape[:2]
        warped_image = cv2.warpPerspective(images[i+1], H, (width, height))
        
        # Blend the images
        stitched_image = cv2.addWeighted(stitched_image, 0.5, warped_image, 0.5, 0)
    
    return stitched_image

def main():
    # Define the path to the image directory
    image_dir = '../data/images'  # Update this path as needed
    
    # Get all image filenames from the directory
    image_filenames = [f'image{i}.png' for i in range(1, 29)]  # Assuming images are named image1.png to image28.png
    image_paths = [os.path.join(image_dir, filename) for filename in image_filenames]

    # Load images
    images = [cv2.imread(img_path) for img_path in image_paths if os.path.isfile(img_path)]

    if not images:
        print("No images were loaded. Check the image paths.")
        return

    # Stitch images
    stitched_image = stitch_images(images)

    if stitched_image is not None:
        # Save or display the stitched image
        cv2.imwrite('../output/stitched_image.jpg', stitched_image)
        print("Stitched image saved successfully!")

if __name__ == "__main__":
    main()
