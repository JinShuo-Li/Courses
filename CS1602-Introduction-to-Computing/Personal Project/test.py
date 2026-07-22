"""
Complex CNN Implementation for CIFAR-10 Classification
====================================================

A sophisticated Convolutional Neural Network architecture combining multiple modern
CNN design patterns, optimized for training on CPU-only servers with 4 cores and 8GB RAM.

The network incorporates:
- Residual connections with skip connections
- Inception modules with parallel multi-scale convolutions
- Attention mechanisms for adaptive feature selection
- Dilated convolutions for expanded receptive fields
- Depthwise separable convolutions for parameter efficiency
- Advanced regularization techniques

Designed to train for approximately 8 hours on limited hardware resources.

Author: Jinshuo Li
Date: 2024
License: MIT
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import time
import numpy as np
from tqdm import tqdm
import warnings
warnings.filterwarnings('ignore')


class ResidualBlock(nn.Module):
    """
    Residual Block with skip connections for gradient flow in deep networks.
    
    Implements the identity mapping with optional downsampling to address
    vanishing gradient problems in deep CNN architectures.
    
    Args:
        in_channels (int): Number of input channels
        out_channels (int): Number of output channels
        stride (int): Stride for convolutional operations
        downsample (nn.Module, optional): Downsampling module for dimension matching
    """
    
    def __init__(self, in_channels, out_channels, stride=1, downsample=None):
        super(ResidualBlock, self).__init__()
        self.conv1 = nn.Conv2d(in_channels, out_channels, kernel_size=3, 
                              stride=stride, padding=1, bias=False)
        self.bn1 = nn.BatchNorm2d(out_channels)
        self.conv2 = nn.Conv2d(out_channels, out_channels, kernel_size=3,
                              stride=1, padding=1, bias=False)
        self.bn2 = nn.BatchNorm2d(out_channels)
        self.downsample = downsample
        self.dropout = nn.Dropout2d(0.1)  # Spatial dropout for regularization
        
    def forward(self, x):
        """
        Forward pass with residual connection.
        
        Args:
            x (torch.Tensor): Input tensor of shape (batch, channels, height, width)
            
        Returns:
            torch.Tensor: Output tensor with residual connection
        """
        identity = x
        if self.downsample is not None:
            identity = self.downsample(x)
            
        out = F.relu(self.bn1(self.conv1(x)))
        out = self.dropout(out)
        out = self.bn2(self.conv2(out))
        
        out += identity
        out = F.relu(out)
        return out


class InceptionModule(nn.Module):
    """
    Inception Module with parallel convolutional pathways.
    
    Implements the multi-scale feature extraction from GoogLeNet architecture
    with 1x1, 3x3, 5x5 convolutions and pooling operations in parallel.
    
    Args:
        in_channels (int): Number of input channels
    """
    
    def __init__(self, in_channels):
        super(InceptionModule, self).__init__()
        
        # 1x1 convolution branch
        self.branch1x1 = nn.Conv2d(in_channels, 32, kernel_size=1)
        
        # 3x3 convolution branch
        self.branch3x3 = nn.Sequential(
            nn.Conv2d(in_channels, 24, kernel_size=1),
            nn.Conv2d(24, 32, kernel_size=3, padding=1)
        )
        
        # 5x5 convolution branch
        self.branch5x5 = nn.Sequential(
            nn.Conv2d(in_channels, 16, kernel_size=1),
            nn.Conv2d(16, 32, kernel_size=5, padding=2)
        )
        
        # Pooling branch
        self.branch_pool = nn.Sequential(
            nn.MaxPool2d(kernel_size=3, stride=1, padding=1),
            nn.Conv2d(in_channels, 32, kernel_size=1)
        )
        
    def forward(self, x):
        """
        Forward pass through parallel convolutional branches.
        
        Args:
            x (torch.Tensor): Input tensor
            
        Returns:
            torch.Tensor: Concatenated output from all branches
        """
        branch1x1 = self.branch1x1(x)
        branch3x3 = self.branch3x3(x)
        branch5x5 = self.branch5x5(x)
        branch_pool = self.branch_pool(x)
        
        outputs = [branch1x1, branch3x3, branch5x5, branch_pool]
        return torch.cat(outputs, 1)


class AttentionGate(nn.Module):
    """
    Attention Gate for adaptive feature selection.
    
    Implements attention mechanism to emphasize important spatial features
    and suppress less relevant ones, improving feature representation.
    
    Args:
        in_channels (int): Number of input channels
    """
    
    def __init__(self, in_channels):
        super(AttentionGate, self).__init__()
        self.W_g = nn.Sequential(
            nn.Conv2d(in_channels, in_channels // 2, kernel_size=1),
            nn.BatchNorm2d(in_channels // 2)
        )
        self.W_x = nn.Sequential(
            nn.Conv2d(in_channels, in_channels // 2, kernel_size=1),
            nn.BatchNorm2d(in_channels // 2)
        )
        self.psi = nn.Sequential(
            nn.Conv2d(in_channels // 2, 1, kernel_size=1),
            nn.BatchNorm2d(1),
            nn.Sigmoid()
        )
        self.relu = nn.ReLU(inplace=True)
        
    def forward(self, g, x):
        """
        Forward pass with attention mechanism.
        
        Args:
            g (torch.Tensor): Gating signal tensor
            x (torch.Tensor): Input feature tensor
            
        Returns:
            torch.Tensor: Attention-weighted features
        """
        g1 = self.W_g(g)
        x1 = self.W_x(x)
        psi = self.relu(g1 + x1)
        psi = self.psi(psi)
        return x * psi


class ComplexCNN(nn.Module):
    """
    Complex CNN Architecture combining multiple modern design patterns.
    
    A sophisticated neural network for image classification featuring:
    1. Residual connections for gradient flow
    2. Inception modules for multi-scale feature extraction
    3. Attention mechanisms for feature selection
    4. Dilated convolutions for expanded receptive fields
    5. Depthwise separable convolutions for efficiency
    6. Comprehensive regularization techniques
    
    Args:
        num_classes (int): Number of output classes (default: 10 for CIFAR-10)
    """
    
    def __init__(self, num_classes=10):
        super(ComplexCNN, self).__init__()
        
        # Initial convolutional layers
        self.conv1 = nn.Conv2d(3, 64, kernel_size=7, stride=2, padding=3, bias=False)
        self.bn1 = nn.BatchNorm2d(64)
        self.maxpool = nn.MaxPool2d(kernel_size=3, stride=2, padding=1)
        
        # Residual block groups
        self.layer1 = self._make_layer(64, 128, 2, stride=1)
        self.layer2 = self._make_layer(128, 256, 2, stride=2)
        
        # Inception modules
        self.inception1 = InceptionModule(256)
        self.inception2 = InceptionModule(128)  # 128 channels from Inception output (32 * 4)
        
        # Attention gates
        self.attention1 = AttentionGate(256)
        self.attention2 = AttentionGate(128)
        
        # Dilated convolutions for expanded receptive field
        self.dilated_conv = nn.Sequential(
            nn.Conv2d(128, 256, kernel_size=3, padding=2, dilation=2),
            nn.BatchNorm2d(256),
            nn.ReLU(inplace=True),
            nn.Conv2d(256, 256, kernel_size=3, padding=4, dilation=4),
            nn.BatchNorm2d(256),
            nn.ReLU(inplace=True)
        )
        
        # Depthwise separable convolutions for parameter efficiency
        self.depthwise_sep = nn.Sequential(
            nn.Conv2d(256, 256, kernel_size=3, groups=256, padding=1),
            nn.Conv2d(256, 512, kernel_size=1),
            nn.BatchNorm2d(512),
            nn.ReLU(inplace=True)
        )
        
        # Global average pooling
        self.avgpool = nn.AdaptiveAvgPool2d((1, 1))
        
        # Fully connected classifier
        self.fc = nn.Sequential(
            nn.Dropout(0.5),
            nn.Linear(512, 256),
            nn.BatchNorm1d(256),
            nn.ReLU(inplace=True),
            nn.Dropout(0.3),
            nn.Linear(256, 128),
            nn.ReLU(inplace=True),
            nn.Linear(128, num_classes)
        )
        
        # Initialize weights
        self._initialize_weights()
        
    def _make_layer(self, in_channels, out_channels, blocks, stride=1):
        """
        Create a layer of residual blocks.
        
        Args:
            in_channels (int): Input channels
            out_channels (int): Output channels
            blocks (int): Number of residual blocks
            stride (int): Convolution stride
            
        Returns:
            nn.Sequential: Sequential container of residual blocks
        """
        downsample = None
        if stride != 1 or in_channels != out_channels:
            downsample = nn.Sequential(
                nn.Conv2d(in_channels, out_channels, kernel_size=1, 
                         stride=stride, bias=False),
                nn.BatchNorm2d(out_channels)
            )
            
        layers = []
        layers.append(ResidualBlock(in_channels, out_channels, stride, downsample))
        for _ in range(1, blocks):
            layers.append(ResidualBlock(out_channels, out_channels))
            
        return nn.Sequential(*layers)
    
    def _initialize_weights(self):
        """
        Initialize network weights using Kaiming initialization for Conv layers
        and normal initialization for Linear layers.
        """
        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
                if m.bias is not None:
                    nn.init.constant_(m.bias, 0)
            elif isinstance(m, nn.BatchNorm2d):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 0)
            elif isinstance(m, nn.Linear):
                nn.init.normal_(m.weight, 0, 0.01)
                nn.init.constant_(m.bias, 0)
    
    def forward(self, x):
        """
        Forward pass through the complete network.
        
        Args:
            x (torch.Tensor): Input tensor of shape (batch, 3, 32, 32)
            
        Returns:
            torch.Tensor: Output logits of shape (batch, num_classes)
        """
        # Initial feature extraction
        x = F.relu(self.bn1(self.conv1(x)))
        x = self.maxpool(x)
        
        # Residual blocks
        x = self.layer1(x)
        x = self.layer2(x)
        
        # Attention mechanism
        x = self.attention1(x, x)
        
        # Inception module
        x = self.inception1(x)
        
        # Dilated convolutions
        x = self.dilated_conv(x)
        
        # Depthwise separable convolution
        x = self.depthwise_sep(x)
        
        # Global average pooling
        x = self.avgpool(x)
        x = torch.flatten(x, 1)
        
        # Fully connected classifier
        x = self.fc(x)
        
        return x


class MixedPrecisionTrainer:
    """
    Training manager with mixed precision support.
    
    Handles the training and validation loops with optional mixed precision
    training for GPU acceleration. Falls back to standard precision on CPU.
    
    Args:
        model (nn.Module): The neural network model
        device (torch.device): Device for training (CPU/GPU)
    """
    
    def __init__(self, model, device):
        self.model = model.to(device)
        self.device = device
        self.scaler = torch.cuda.amp.GradScaler() if torch.cuda.is_available() else None
        
    def train_epoch(self, train_loader, optimizer, criterion, epoch, num_epochs):
        """
        Train the model for one epoch.
        
        Args:
            train_loader (DataLoader): Training data loader
            optimizer: Optimizer for parameter updates
            criterion: Loss function
            epoch (int): Current epoch number
            num_epochs (int): Total number of epochs
            
        Returns:
            tuple: (average loss, accuracy) for the epoch
        """
        self.model.train()
        running_loss = 0.0
        correct = 0
        total = 0
        
        pbar = tqdm(train_loader, desc=f'Epoch {epoch+1}/{num_epochs}')
        for batch_idx, (inputs, targets) in enumerate(pbar):
            inputs, targets = inputs.to(self.device), targets.to(self.device)
            
            optimizer.zero_grad()
            
            if self.scaler is not None:
                with torch.cuda.amp.autocast():
                    outputs = self.model(inputs)
                    loss = criterion(outputs, targets)
                self.scaler.scale(loss).backward()
                self.scaler.step(optimizer)
                self.scaler.update()
            else:
                outputs = self.model(inputs)
                loss = criterion(outputs, targets)
                loss.backward()
                optimizer.step()
            
            running_loss += loss.item()
            _, predicted = outputs.max(1)
            total += targets.size(0)
            correct += predicted.eq(targets).sum().item()
            
            pbar.set_postfix({
                'Loss': f'{running_loss/(batch_idx+1):.4f}',
                'Acc': f'{100.*correct/total:.2f}%'
            })
        
        return running_loss / len(train_loader), 100. * correct / total
    
    def validate(self, val_loader, criterion):
        """
        Validate the model on the validation set.
        
        Args:
            val_loader (DataLoader): Validation data loader
            criterion: Loss function
            
        Returns:
            tuple: (average loss, accuracy) for validation set
        """
        self.model.eval()
        val_loss = 0.0
        correct = 0
        total = 0
        
        with torch.no_grad():
            for inputs, targets in val_loader:
                inputs, targets = inputs.to(self.device), targets.to(self.device)
                outputs = self.model(inputs)
                loss = criterion(outputs, targets)
                
                val_loss += loss.item()
                _, predicted = outputs.max(1)
                total += targets.size(0)
                correct += predicted.eq(targets).sum().item()
        
        return val_loss / len(val_loader), 100. * correct / total


def get_data_loaders(batch_size=64):
    """
    Create data loaders for CIFAR-10 dataset with data augmentation.
    
    Args:
        batch_size (int): Batch size for training and validation
        
    Returns:
        tuple: (train_loader, test_loader) DataLoader objects
    """
    # Training transformations with data augmentation
    transform_train = transforms.Compose([
        transforms.RandomCrop(32, padding=4),
        transforms.RandomHorizontalFlip(),
        transforms.RandomRotation(15),
        transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2),
        transforms.ToTensor(),
        transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010)),
    ])
    
    # Test/validation transformations
    transform_test = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010)),
    ])
    
    # CIFAR-10 dataset
    train_dataset = datasets.CIFAR10(root='./data', train=True, 
                                     download=True, transform=transform_train)
    test_dataset = datasets.CIFAR10(root='./data', train=False, 
                                    download=True, transform=transform_test)
    
    # Create data loaders
    train_loader = DataLoader(train_dataset, batch_size=batch_size, 
                             shuffle=True, num_workers=2, pin_memory=True)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, 
                            shuffle=False, num_workers=2, pin_memory=True)
    
    return train_loader, test_loader


def train_model():
    """
    Main training function for the Complex CNN.
    
    Handles the complete training pipeline including:
    - Model initialization
    - Data loading
    - Training loop
    - Validation
    - Checkpointing
    - Performance monitoring
    
    Returns:
        tuple: (trained model, training history dictionary)
    """
    # Device configuration
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f'Using device: {device}')
    
    # Set random seeds for reproducibility
    torch.manual_seed(42)
    np.random.seed(42)
    
    # Hyperparameters optimized for 4-core 8GB CPU
    config = {
        'batch_size': 64,  # Adjusted for memory constraints
        'num_epochs': 100,  # Training epochs
        'learning_rate': 0.001,
        'weight_decay': 1e-4,
        'lr_scheduler_step': 30,  # Learning rate decay step
        'lr_scheduler_gamma': 0.1,  # Learning rate decay factor
    }
    
    # Load data
    print("Loading CIFAR-10 dataset...")
    train_loader, test_loader = get_data_loaders(config['batch_size'])
    
    # Create model
    print("Creating complex CNN model...")
    model = ComplexCNN(num_classes=10)
    
    # Model statistics
    total_params = sum(p.numel() for p in model.parameters())
    trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    print(f"Total parameters: {total_params:,}")
    print(f"Trainable parameters: {trainable_params:,}")
    
    # Create trainer
    trainer = MixedPrecisionTrainer(model, device)
    
    # Loss function with label smoothing
    criterion = nn.CrossEntropyLoss(label_smoothing=0.1)
    
    # Optimizer with weight decay
    optimizer = optim.AdamW(model.parameters(), lr=config['learning_rate'], 
                           weight_decay=config['weight_decay'])
    
    # Learning rate scheduler
    scheduler = optim.lr_scheduler.MultiStepLR(optimizer, 
                                               milestones=[config['lr_scheduler_step'], 
                                                           config['lr_scheduler_step']*2],
                                               gamma=config['lr_scheduler_gamma'])
    
    # Training loop
    print("Starting training...")
    start_time = time.time()
    
    best_acc = 0.0
    history = {'train_loss': [], 'train_acc': [], 'val_loss': [], 'val_acc': []}
    
    for epoch in range(config['num_epochs']):
        epoch_start = time.time()
        
        # Train for one epoch
        train_loss, train_acc = trainer.train_epoch(
            train_loader, optimizer, criterion, epoch, config['num_epochs']
        )
        
        # Validate
        val_loss, val_acc = trainer.validate(test_loader, criterion)
        
        # Update learning rate
        scheduler.step()
        
        # Save history
        history['train_loss'].append(train_loss)
        history['train_acc'].append(train_acc)
        history['val_loss'].append(val_loss)
        history['val_acc'].append(val_acc)
        
        # Save best model
        if val_acc > best_acc:
            best_acc = val_acc
            torch.save({
                'epoch': epoch,
                'model_state_dict': model.state_dict(),
                'optimizer_state_dict': optimizer.state_dict(),
                'val_acc': val_acc,
            }, 'best_model.pth')
        
        epoch_time = time.time() - epoch_start
        
        print(f'Epoch {epoch+1:03d}: '
              f'Train Loss: {train_loss:.4f} | Train Acc: {train_acc:.2f}% | '
              f'Val Loss: {val_loss:.4f} | Val Acc: {val_acc:.2f}% | '
              f'Time: {epoch_time:.1f}s | '
              f'Best Acc: {best_acc:.2f}%')
        
        # Save checkpoint every 10 epochs
        if (epoch + 1) % 10 == 0:
            torch.save({
                'epoch': epoch,
                'model_state_dict': model.state_dict(),
                'optimizer_state_dict': optimizer.state_dict(),
                'scheduler_state_dict': scheduler.state_dict(),
                'val_acc': val_acc,
                'history': history,
            }, f'checkpoint_epoch_{epoch+1}.pth')
    
    total_time = time.time() - start_time
    print(f"\nTraining completed in {total_time/3600:.2f} hours")
    print(f"Best validation accuracy: {best_acc:.2f}%")
    
    # Load best model for final testing
    checkpoint = torch.load('best_model.pth')
    model.load_state_dict(checkpoint['model_state_dict'])
    
    # Final test
    test_loss, test_acc = trainer.validate(test_loader, criterion)
    print(f"Final test accuracy: {test_acc:.2f}%")
    
    return model, history


def profile_memory_usage():
    """
    Profile and display current memory usage.
    
    Returns:
        float: Current memory usage in GB
    """
    import psutil
    import os
    
    process = psutil.Process(os.getpid())
    memory_usage = process.memory_info().rss / 1024 ** 3  # Convert to GB
    print(f"Current memory usage: {memory_usage:.2f} GB")
    
    # System memory information
    virtual_memory = psutil.virtual_memory()
    print(f"Total memory: {virtual_memory.total / 1024**3:.2f} GB")
    print(f"Available memory: {virtual_memory.available / 1024**3:.2f} GB")
    print(f"Memory percent used: {virtual_memory.percent}%")
    
    return memory_usage


if __name__ == "__main__":
    """
    Main execution block for training the Complex CNN on CPU.
    
    Expected runtime: ~8 hours on 4-core 8GB RAM server
    Dataset: CIFAR-10 (10 classes, 32x32 RGB images)
    """
    print("=" * 60)
    print("Complex CNN Training on 4-core 8GB CPU Server")
    print("Expected training time: ~8 hours")
    print("=" * 60)
    
    # Profile initial memory usage
    print("\nMemory usage before training:")
    initial_memory = profile_memory_usage()
    
    # Start training
    try:
        model, history = train_model()
        
        print("\nMemory usage after training:")
        final_memory = profile_memory_usage()
        print(f"Memory increase: {final_memory - initial_memory:.2f} GB")
        
        # Save training history
        import pickle
        with open('training_history.pkl', 'wb') as f:
            pickle.dump(history, f)
        print("Training history saved to training_history.pkl")
        
    except Exception as e:
        print(f"Training interrupted with error: {e}")
        import traceback
        traceback.print_exc()
    
    print("\nTraining process completed!")