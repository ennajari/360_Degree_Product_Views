import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def train_model(images):
    # Dummy labels for training
    labels = np.arange(len(images))

    # Flatten images for the model
    flat_images = images.reshape(len(images), -1)
    
    X_train, X_test, y_train, y_test = train_test_split(flat_images, labels, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier(n_estimators=10)
    model.fit(X_train, y_train)
    
    accuracy = model.score(X_test, y_test)
    print(f"Model trained with accuracy: {accuracy*100:.2f}%")
    
    return model

if __name__ == "__main__":
    # Current script directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Define the relative path to the processed images file
    processed_images_path = os.path.join(current_dir, '../output/processed_images.npy')
    
    images = np.load(processed_images_path)
    
    model = train_model(images)
    
    # Save the model (optional)
    model_path = os.path.join(current_dir, '../output/model.pkl')
    with open(model_path, 'wb') as f:
        np.save(f, model)
    print(f"Model saved at {model_path}.")
