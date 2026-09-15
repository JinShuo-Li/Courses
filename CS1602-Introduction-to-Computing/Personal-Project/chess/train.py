import torch
import torch.optim as optim
import os
from model import ChessNet

def train_dummy():
    """
    Simulates training with random data.
    In production, replace 'inputs' and 'targets' with parsed PGN data.
    """
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = ChessNet().to(device)
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    criterion = torch.nn.MSELoss()

    print(f"Starting training on {device}...")

    # Training loop
    epochs = 1000
    save_interval = 2 # Save every 2 epochs
    
    for epoch in range(1, epochs + 1):
        model.train()
        
        # Dummy data: Batch size 32, 12 channels, 8x8 board
        inputs = torch.randn(32, 12, 8, 8).to(device) 
        targets = torch.randn(32, 1).to(device) # Random scores -1 to 1

        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, targets)
        loss.backward()
        optimizer.step()

        print(f"Epoch [{epoch}/{epochs}] Loss: {loss.item():.4f}")

        # Save checkpoint
        if epoch % save_interval == 0:
            filename = f"chess_model_epoch_{epoch}.pth"
            torch.save(model.state_dict(), filename)
            print(f"Saved checkpoint: {filename}")

if __name__ == "__main__":
    train_dummy()