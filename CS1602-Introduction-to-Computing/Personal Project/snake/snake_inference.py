import pygame
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import random
import os

# --- 1. DEFINE MODEL ARCHITECTURE (Must match training) ---
class Linear_QNet(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super().__init__()
        self.linear1 = nn.Linear(input_size, hidden_size)
        self.linear2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = F.relu(self.linear1(x))
        x = self.linear2(x)
        return x

# --- 2. DEFINE GAME ENGINE (Modified for Inference) ---
# We removed the "headless" dummy driver so you can see the window.
class Direction:
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

BLOCK_SIZE = 20
SPEED = 20  # Lower speed so you can watch it play comfortably

class SnakeGameInference:
    def __init__(self, w=640, h=480):
        self.w = w
        self.h = h
        pygame.init()
        self.font = pygame.font.SysFont('arial', 25)
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Snake AI - Inference Mode')
        self.clock = pygame.time.Clock()
        self.reset()

    def reset(self):
        self.direction = Direction.RIGHT
        self.head = [self.w/2, self.h/2]
        self.snake = [self.head, 
                      [self.head[0]-BLOCK_SIZE, self.head[1]],
                      [self.head[0]-(2*BLOCK_SIZE), self.head[1]]]
        self.score = 0
        self.food = None
        self._place_food()
        self.frame_iteration = 0
        return self.get_state()

    def _place_food(self):
        x = random.randint(0, (self.w-BLOCK_SIZE )//BLOCK_SIZE )*BLOCK_SIZE
        y = random.randint(0, (self.h-BLOCK_SIZE )//BLOCK_SIZE )*BLOCK_SIZE
        self.food = [x, y]
        if self.food in self.snake:
            self._place_food()

    def play_step(self, action):
        self.frame_iteration += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        self._move(action)
        self.snake.insert(0, self.head)
        
        game_over = False
        if self.is_collision() or self.frame_iteration > 100*len(self.snake):
            game_over = True
            return game_over, self.score

        if self.head == self.food:
            self.score += 1
            self._place_food()
        else:
            self.snake.pop()
            
        self._update_ui()
        self.clock.tick(SPEED)
        return game_over, self.score

    def is_collision(self, pt=None):
        if pt is None:
            pt = self.head
        if pt[0] > self.w - BLOCK_SIZE or pt[0] < 0 or pt[1] > self.h - BLOCK_SIZE or pt[1] < 0:
            return True
        if pt in self.snake[1:]:
            return True
        return False

    def _update_ui(self):
        self.display.fill((0, 0, 0)) # Black background
        
        for pt in self.snake:
            pygame.draw.rect(self.display, (0, 255, 0), pygame.Rect(pt[0], pt[1], BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.display, (0, 50, 0), pygame.Rect(pt[0]+4, pt[1]+4, 12, 12)) # Inner square
            
        pygame.draw.rect(self.display, (255, 0, 0), pygame.Rect(self.food[0], self.food[1], BLOCK_SIZE, BLOCK_SIZE))
        
        text = self.font.render("Score: " + str(self.score), True, (255, 255, 255))
        self.display.blit(text, [0, 0])
        pygame.display.flip()

    def _move(self, action):
        clock_wise = [Direction.RIGHT, Direction.DOWN, Direction.LEFT, Direction.UP]
        idx = clock_wise.index(self.direction)

        if np.array_equal(action, [1, 0, 0]):
            new_dir = clock_wise[idx]
        elif np.array_equal(action, [0, 1, 0]):
            next_idx = (idx + 1) % 4
            new_dir = clock_wise[next_idx]
        else:
            next_idx = (idx - 1) % 4
            new_dir = clock_wise[next_idx]
        self.direction = new_dir

        x = self.head[0]
        y = self.head[1]
        if self.direction == Direction.RIGHT:
            x += BLOCK_SIZE
        elif self.direction == Direction.LEFT:
            x -= BLOCK_SIZE
        elif self.direction == Direction.DOWN:
            y += BLOCK_SIZE
        elif self.direction == Direction.UP:
            y -= BLOCK_SIZE
        self.head = [x, y]

    def get_state(self):
        head = self.snake[0]
        point_l = [head[0] - BLOCK_SIZE, head[1]]
        point_r = [head[0] + BLOCK_SIZE, head[1]]
        point_u = [head[0], head[1] - BLOCK_SIZE]
        point_d = [head[0], head[1] + BLOCK_SIZE]
        
        dir_l = self.direction == Direction.LEFT
        dir_r = self.direction == Direction.RIGHT
        dir_u = self.direction == Direction.UP
        dir_d = self.direction == Direction.DOWN

        state = [
            (dir_r and self.is_collision(point_r)) or 
            (dir_l and self.is_collision(point_l)) or 
            (dir_u and self.is_collision(point_u)) or 
            (dir_d and self.is_collision(point_d)),

            (dir_u and self.is_collision(point_r)) or 
            (dir_d and self.is_collision(point_l)) or 
            (dir_l and self.is_collision(point_u)) or 
            (dir_r and self.is_collision(point_d)),

            (dir_d and self.is_collision(point_r)) or 
            (dir_u and self.is_collision(point_l)) or 
            (dir_r and self.is_collision(point_u)) or 
            (dir_l and self.is_collision(point_d)),
            
            dir_l, dir_r, dir_u, dir_d,
            self.food[0] < self.head[0],
            self.food[0] > self.head[0],
            self.food[1] < self.head[1],
            self.food[1] > self.head[1]
        ]
        return np.array(state, dtype=int)

# --- 3. RUN INFERENCE ---
def run_inference():
    # Load Model
    model_path = './model/model.pth'
    if not os.path.exists(model_path):
        print("Error: model.pth not found. Train the AI first.")
        return

    model = Linear_QNet(11, 256, 3)
    model.load_state_dict(torch.load(model_path))
    model.eval() # Set to evaluation mode

    game = SnakeGameInference()
    
    print("Starting Inference... Press Ctrl+C to stop.")
    
    while True:
        state = game.get_state()
        state_tensor = torch.tensor(state, dtype=torch.float)
        
        # Get prediction (No random moves, pure exploitation)
        prediction = model(state_tensor)
        move = torch.argmax(prediction).item()
        final_move = [0, 0, 0]
        final_move[move] = 1
        
        game_over, score = game.play_step(final_move)
        
        if game_over:
            print(f'Game Over. Final Score: {score}')
            game.reset()

if __name__ == '__main__':
    run_inference()