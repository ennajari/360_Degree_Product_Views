import torch
import torch.nn as nn
import torch.optim as optim

class Simple3DModel(nn.Module):
    def __init__(self):
        super(Simple3DModel, self).__init__()
        self.fc = nn.Sequential(
            nn.Linear(128 * 128 * 3, 1024),
            nn.ReLU(),
            nn.Linear(1024, 512),
            nn.ReLU(),
            nn.Linear(512, 3 * 128 * 128)
        )
    
    def forward(self, x):
        return self.fc(x)

def train_3d_model(images):
    images = images.reshape(len(images), -1)
    images = torch.tensor(images, dtype=torch.float32)
    
    model = Simple3DModel()
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    
    for epoch in range(10):
        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, images)
        loss.backward()
        optimizer.step()
        print(f"Epoch {epoch+1}/10, Loss: {loss.item():.4f}")
    
    return model

if __name__ == "__main__":
    # Current script directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Define the relative path to the processed images file
    processed_images_path = os.path.join(current_dir, '../output/processed_images.npy')
    
    images = np.load(processed_images_path)
    
    model = train_3d_model(images)
    
    # Save the model
    model_path = os.path.join(current_dir, '../output/3d_model.pth')
    torch.save(model.state_dict(), model_path)
    print(f"3D model saved at {model_path}.")
