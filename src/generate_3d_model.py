import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def generate_simple_3d_model(camera_matrices):
    points = []
    for matrix in camera_matrices:
        # Extract translation from the homography matrix
        tx = matrix[0, 2]
        ty = matrix[1, 2]
        tz = matrix[2, 2]
        points.append([tx, ty, tz])
    
    return np.array(points)

def plot_3d_model(points):
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(points[:, 0], points[:, 1], points[:, 2])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.title("Modèle 3D généré")
    plt.show()

if __name__ == "__main__":
    input_dir = "../output/"
    transformations_path = os.path.join(input_dir, "transformations.npy")
    transformations = np.load(transformations_path)
    
    points = generate_simple_3d_model(transformations)
    plot_3d_model(points)
    print("Modèle 3D généré et affiché.")
