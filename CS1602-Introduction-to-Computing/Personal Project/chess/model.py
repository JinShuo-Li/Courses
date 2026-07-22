import torch
import torch.nn as nn

class ChessNet(nn.Module):
    """
    Simple CNN for Chess Board Evaluation.
    Input: 12x8x8 bitboard representation (6 piece types * 2 colors).
    Output: Scalar value (board evaluation).
    """
    def __init__(self):
        super(ChessNet, self).__init__()
        # 3 Convolutional blocks
        self.conv1 = nn.Conv2d(12, 16, kernel_size=3, padding=1)
        self.relu = nn.ReLU()
        self.bn1 = nn.BatchNorm2d(16)
        
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, padding=1)
        self.bn2 = nn.BatchNorm2d(32)
        
        self.conv3 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.bn3 = nn.BatchNorm2d(64)
        
        # Fully connected layers for regression (value prediction)
        self.flatten = nn.Flatten()
        self.fc1 = nn.Linear(64 * 8 * 8, 128)
        self.fc2 = nn.Linear(128, 1) # Output score

    def forward(self, x):
        x = self.relu(self.bn1(self.conv1(x)))
        x = self.relu(self.bn2(self.conv2(x)))
        x = self.relu(self.bn3(self.conv3(x)))
        x = self.flatten(x)
        x = self.relu(self.fc1(x))
        x = torch.tanh(self.fc2(x)) # Output between -1 (Loss) and 1 (Win)
        return x