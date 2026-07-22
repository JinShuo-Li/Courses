import pygame
import numpy as np
import random
import math
import sys

# Constants
WIDTH, HEIGHT = 1280, 720
TILE_SIZE = 32
GRID_W = 40  # 1280 / 32
GRID_H = 22  # roughly fit
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 50, 50)
GREEN = (50, 200, 50)
BLUE = (50, 50, 200)
GREY = (100, 100, 100)
DARK_GREY = (50, 50, 50)
YELLOW = (255, 255, 0)
BROWN = (139, 69, 19)
CYAN = (0, 255, 255)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)

class Graph:
    def __init__(self, data=None):
        if data is None:
            data = []
        self.data = data

    def add_edge(self, start, end, weight=1):
        """
        Add an edge or update weight between start and end vertices.
        """
        vertices_count = len(self.data)
        if not (isinstance(start, int) and isinstance(end, int)):
            raise TypeError("4-1: Vertex indices must be integers")
        if not (0 <= start < vertices_count and 0 <= end < vertices_count):
            raise ValueError(f"4-2: Vertex index out of range. Valid range: 0 to {vertices_count-1}")
        if not isinstance(weight, (int, float)):
            raise TypeError("4-3: Weight must be a number")
            
        self.data[start][end] = weight

    def remove_edge(self, start, end):
        """
        Remove the edge from start to end (set weight to 0).
        """
        vertices_count = len(self.data)
        if not (isinstance(start, int) and isinstance(end, int)):
            raise TypeError("5-1: Vertex indices must be integers")
        if not (0 <= start < vertices_count and 0 <= end < vertices_count):
            raise ValueError(f"5-2: Vertex index out of range. Valid range: 0 to {vertices_count-1}")
            
        self.data[start][end] = 0
    
    def add_vertex(self, connections=[]):
        """
        Add a new vertex to the graph. connections is a list of weights from the new vertex to existing vertices.
        0 weight means no edge.
        """
        if not isinstance(connections, list):
            raise TypeError("6-1: Connections must be a list")

        current_size = len(self.data)
        for weight in connections:
             if not isinstance(weight, (int, float)):
                raise TypeError("6-2: Weights must be numbers")

        new_row = [0] * (current_size + 1)
        for i in range(min(len(connections), current_size)):
            new_row[i] = connections[i]

        for i, row in enumerate(self.data):
            row.append(new_row[i])
        
        self.data.append(new_row)
    
    def remove_vertex(self, vertex):
        """
        Remove a vertex and all associated edges. while removing the vertex, all the indices of vertices after it should be decremented by 1.
        """
        vertices_count = len(self.data)
        if not isinstance(vertex, int):
            raise TypeError("7-1: Vertex index must be an integer")
        if not (0 <= vertex < vertices_count):
            raise ValueError(f"7-2: Vertex index out of range. Valid range: 0 to {vertices_count-1}")

        self.data.pop(vertex)
        for row in self.data:
            row.pop(vertex)

    def BFS(self, start, end):
        """
        Find shortest path using Breadth-First Search (unweighted).
        """
        vertices_count = len(self.data)
        queue = [start]
        mat = self.data
        memory = {start: None}
        found = False
        idx = 0

        while idx < len(queue):
            curr = queue[idx]
            if curr == end:
                found = True
                break
            
            for i in range(vertices_count):
                if mat[curr][i] != 0 and i not in memory:
                    memory[i] = curr
                    queue.append(i)
                    if i == end:
                        found = True
                        break
            if found:
                break
            idx += 1
            
        if not found:
            return None
            
        path = []
        index = end
        while index is not None:
            path.append(index)
            index = memory[index]
        return path[::-1]

    def find_path_DFS(self, start, end):
        """
        Find a path using Depth-First Search.
        """
        vertices_count = len(self.data)
        stack = [start]
        mat = self.data
        memory = {start: None}
        found = False
        
        while len(stack) > 0:
            curr = stack.pop()
            if curr == end:
                found = True
                break
            
            for i in range(vertices_count):
                if mat[curr][i] != 0 and i not in memory:
                    memory[i] = curr
                    stack.append(i)
                    
        if not found:
            return None
            
        path = []
        curr_node = end
        while curr_node is not None:
            path.append(curr_node)
            curr_node = memory[curr_node]
        return path[::-1]
    
    def dijkstra(self, start, end):
        """
        Find shortest path using Dijkstra's Algorithm (weighted).
        """
        vertices_count = len(self.data)
        distances = {i: float('inf') for i in range(vertices_count)}
        distances[start] = 0
        visited = [False] * vertices_count
        parent = {start: None}
        
        for _ in range(vertices_count):
            min_dist = float('inf')
            curr = -1
            for i in range(vertices_count):
                if not visited[i] and distances[i] < min_dist:
                    min_dist = distances[i]
                    curr = i
            if curr == -1 or distances[curr] == float('inf'):
                break
            if curr == end:
                break
            visited[curr] = True
            for i in range(vertices_count):
                if curr < len(self.data) and i < len(self.data[curr]):
                    weight = self.data[curr][i]
                    if weight > 0 and not visited[i]:
                        new_dist = distances[curr] + weight
                        if new_dist < distances[i]:
                            distances[i] = new_dist
                            parent[i] = curr
                        
        if end not in parent:
            return None
            
        path = []
        curr_node = end
        while curr_node is not None:
            path.append(curr_node)
            curr_node = parent[curr_node]   
        return path[::-1]

# --- Game Objects ---

class object:
    def __init__(self, level=1, position=(0,0), health=0, sheld=0):
        self.level = level
        self.position = position
        self.health = health
        self.sheld = sheld
        self.name = "Object"
        self.color = WHITE
        self.max_health = health

    def draw(self, screen, x, y):
        rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
        pygame.draw.rect(screen, self.color, rect)
        
        # Draw Health Bar
        if self.health < self.max_health:
            bar_width = TILE_SIZE
            bar_height = 4
            health_pct = max(0, self.health / self.max_health)
            pygame.draw.rect(screen, RED, (x, y - 6, bar_width, bar_height))
            pygame.draw.rect(screen, GREEN, (x, y - 6, bar_width * health_pct, bar_height))

class iron_miner(object):
    def __init__(self, level=1, position=(0,0), health=0, sheld=0):
        super().__init__(level, position, health, sheld)
        self.mining_speed = 2 * level ** 2
        self.storage_capacity = 100 + level * 50
        self.name = "Iron Miner"
        self.color = ORANGE
        self.health = 100 + level * 50
        self.max_health = self.health

class steel_mill(object):
    def __init__(self, level=1, position=(0,0), health=0, sheld=0):
        super().__init__(level, position, health, sheld)
        self.health = 50 + level * 30
        self.production_rate = 2 * level ** 2
        self.storage_capacity = 100 + level * 50
        self.name = "Steel Mill"
        self.color = GREY
        self.max_health = self.health

class cannonball_factory(object):
    def __init__(self, level=1, position=(0,0), health=0, sheld=0):
        super().__init__(level, position, health, sheld)
        self.health = 50 + level * 30
        self.production_rate = 2 * level ** 2
        self.storage_capacity = 100 + level * 50
        self.damage = 10 + level * 5
        self.name = "Cannonball Fac"
        self.color = BLACK
        self.max_health = self.health
    
class woodcutter(object):
    def __init__(self, level=1, position=(0,0), health=0, sheld=0):
        super().__init__(level, position, health, sheld)
        self.health = 50 + level * 30
        self.cutting_speed = 2 * level ** 2
        self.storage_capacity = 100 + level * 50
        self.name = "Woodcutter"
        self.color = BROWN
        self.max_health = self.health

class lumber_mill(object):
    def __init__(self, level=1, position=(0,0), health=0, sheld=0):
        super().__init__(level, position, health, sheld)
        self.health = 50 + level * 30
        self.production_rate = 2 * level ** 2
        self.storage_capacity = 100 + level * 50
        self.name = "Lumber Mill"
        self.color = YELLOW
        self.max_health = self.health

class arrow_factory(object):
    def __init__(self, level=1, position=(0,0), health=0, sheld=0):
        super().__init__(level, position, health, sheld)
        self.health = 50 + level * 30
        self.production_rate = 2 * level ** 2
        self.storage_capacity = 100 + level * 50
        self.damage = 20 + level * 8
        self.name = "Arrow Fac"
        self.color = PURPLE
        self.max_health = self.health

class wall(object):
    def __init__(self, level=1, position=(0,0), health=0, sheld=0):
        super().__init__(level, position, health, sheld)
        self.health = 50 + 50 * level ** 2
        self.defense = 50 + level * 20
        self.name = "Wall"
        self.color = DARK_GREY
        self.max_health = self.health

class transporter(object):
    def __init__(self, level=1, position=(0,0), health=0, sheld=0):
        super().__init__(level, position, health, sheld)
        self.speed = 5 + level * 2
        self.max_flow = 20 * level ** 2
        self.name = "Transporter"
        self.color = BLUE
        self.health = 50
        self.max_health = self.health

class turret(object):
    def __init__(self, level=1, position=(0,0), health=0, sheld=0):
        super().__init__(level, position, health, sheld)
        self.health = 50 + level * 30
        self.damage = 30 + level * 10
        self.range = 3  # Range in tiles
        self.fire_rate = 30 # Frames per shot
        self.cooldown = 0
        self.name = "Turret"
        self.color = RED
        self.max_health = self.health

    def draw(self, screen, x, y):
        super().draw(screen, x, y)
        # Draw range or gun
        center = (x + TILE_SIZE//2, y + TILE_SIZE//2)
        pygame.draw.circle(screen, BLACK, center, 5)

class arrow_tower(turret):
    def __init__(self, level=1, position=(0,0), health=0, sheld=0):
        super().__init__(level, position, health, sheld)
        self.damage = 20 + level * 8
        self.range = 4
        self.fire_rate = 20
        self.name = "Arrow Tower"
        self.color = (255, 100, 100)
        self.max_health = self.health

class radar(object):
    def __init__(self, level=1, position=(0,0), health=0, sheld=0):
        super().__init__(level, position, health, sheld)
        self.detection_range = 200 + level * 50
        self.name = "Radar"
        self.color = CYAN
        self.health = 100
        self.max_health = self.health

class base(object):
    def __init__(self, level=1, position=(0,0), health=0, sheld=0):
        super().__init__(level, position, health, sheld)
        self.health = 500 + level * 100
        self.name = "Base"
        self.color = WHITE
        self.max_health = self.health
        self.position = position

class sheld_generator(object):
    def __init__(self, level=1, position=(0,0), health=0, sheld=0):
        super().__init__(level, position, health, sheld)
        self.health = 50 + level * 30
        self.production_rate = 100 + level * 50
        self.name = "Shield Gen"
        self.color = (100, 100, 255)
        self.max_health = self.health

class ResourceNode:
    def __init__(self, type_name, position):
        self.type = type_name # "Iron", "Wood"
        self.position = position
        
    def draw(self, screen, x, y):
        color = ORANGE if self.type == "Iron" else BROWN
        pygame.draw.circle(screen, color, (x + TILE_SIZE//2, y + TILE_SIZE//2), TILE_SIZE // 3)

class game_board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[None for _ in range(width)] for _ in range(height)]
        self.resources = [[None for _ in range(width)] for _ in range(height)]
    
    def is_valid(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def get_object(self, x, y):
        if self.is_valid(x, y):
            return self.grid[y][x]
        return None

    def add_object(self, obj, x, y):
        if self.is_valid(x, y):
            self.grid[y][x] = obj
            obj.position = (x, y)
            return True
        return False
        
    def remove_object(self, x, y):
        if self.is_valid(x, y):
            self.grid[y][x] = None

class enemy:
    def __init__(self, level=1, position=(0,0), health=30):
        self.level = level
        self.position = [float(position[0]), float(position[1])] # Float for smooth movement
        self.health = health + level * 20
        self.max_health = self.health
        self.damage = 5 + level * 2
        self.speed = 0.05 + min(level * 0.01, 0.1)
        self.path = []
        self.target_base = None

    def move(self, board_width, board_height, base_pos):
        # Simple movement towards base
        dx = base_pos[0] - self.position[0]
        dy = base_pos[1] - self.position[1]
        dist = math.hypot(dx, dy)
        
        if dist > 0.1:
            self.position[0] += (dx / dist) * self.speed
            self.position[1] += (dy / dist) * self.speed
            
    def draw(self, screen):
        x = int(self.position[0] * TILE_SIZE)
        y = int(self.position[1] * TILE_SIZE)
        pygame.draw.circle(screen, RED, (x + TILE_SIZE//2, y + TILE_SIZE//2), TILE_SIZE // 3)
        
        # Health bar
        if self.health < self.max_health:
            pygame.draw.rect(screen, RED, (x, y - 5, TILE_SIZE, 3))
            pygame.draw.rect(screen, GREEN, (x, y - 5, TILE_SIZE * (self.health/self.max_health), 3))

class enemy_generator:
    def __init__(self, level=1):
        self.level = level
        self.wave_timer = 0
        self.wave_interval = 600 # frames
        self.active_enemies = []
        
    def update(self, game_state):
        self.wave_timer += 1
        if self.wave_timer > self.wave_interval:
            self.wave_timer = 0
            self.level += 1
            self.spawn_wave(game_state)
            
    def spawn_wave(self, game_state):
        count = self.level * 2
        for _ in range(count):
            edge = random.randint(0, 3)
            if edge == 0: # Top
                pos = (random.randint(0, game_state.board.width-1), 0)
            elif edge == 1: # Right
                pos = (game_state.board.width-1, random.randint(0, game_state.board.height-1))
            elif edge == 2: # Bottom
                pos = (random.randint(0, game_state.board.width-1), game_state.board.height-1)
            else: # Left
                pos = (0, random.randint(0, game_state.board.height-1))
                
            new_enemy = enemy(self.level, pos)
            game_state.enemies.append(new_enemy)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Yorg.io Clone")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 16)
        
        self.board = game_board(GRID_W, GRID_H)
        self.init_resources()
        
        # Place Base
        self.base_pos = (GRID_W//2, GRID_H//2)
        base_obj = base(position=self.base_pos)
        self.board.add_object(base_obj, *self.base_pos)
        
        self.resources_held = {"Iron": 100, "Wood": 100, "Steel": 0, "Arrow": 0}
        
        self.enemies = []
        self.enemy_gen = enemy_generator()
        
        self.selected_building_type = None
        self.building_types = {
            pygame.K_1: ("Iron Miner", iron_miner, {"Iron": 0, "Wood": 50}),
            pygame.K_2: ("Woodcutter", woodcutter, {"Iron": 0, "Wood": 0}),
            pygame.K_3: ("Wall", wall, {"Iron": 10, "Wood": 20}),
            pygame.K_4: ("Turret", turret, {"Iron": 50, "Wood": 50}),
            pygame.K_5: ("Arrow Tower", arrow_tower, {"Iron": 100, "Wood": 100}),
            # Add more mappings as needed
        }
        
        self.game_over = False

    def init_resources(self):
        # Scatter some resources
        for _ in range(30):
            x, y = random.randint(0, GRID_W-1), random.randint(0, GRID_H-1)
            if (x, y) != (GRID_W//2, GRID_H//2):
                self.board.resources[y][x] = ResourceNode("Iron", (x,y))
        for _ in range(30):
            x, y = random.randint(0, GRID_W-1), random.randint(0, GRID_H-1)
            if (x, y) != (GRID_W//2, GRID_H//2):
                self.board.resources[y][x] = ResourceNode("Wood", (x,y))

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key in self.building_types:
                    self.selected_building_type = self.building_types[event.key]
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # Left click
                    self.place_building()
                    
    def place_building(self):
        if not self.selected_building_type:
            return
            
        mx, my = pygame.mouse.get_pos()
        gx, gy = mx // TILE_SIZE, my // TILE_SIZE
        
        if not self.board.is_valid(gx, gy):
            return
            
        # Check resources and empty space
        name, cls, cost = self.selected_building_type
        
        if self.board.grid[gy][gx] is not None:
            return # Occupied

        # Special check: Miner needs resource
        if name == "Iron Miner":
            res = self.board.resources[gy][gx]
            if not res or res.type != "Iron":
                print("Needs Iron Node!")
                return
        
        # Check cost
        can_afford = True
        for res, amount in cost.items():
            if self.resources_held.get(res, 0) < amount:
                can_afford = False
                
        if can_afford:
            for res, amount in cost.items():
                self.resources_held[res] -= amount
            new_b = cls(position=(gx, gy))
            self.board.add_object(new_b, gx, gy)

    def update(self):
        if self.game_over:
            return

        self.enemy_gen.update(self)
        
        # Resources Production (Simplified: Global tick)
        if pygame.time.get_ticks() % 1000 < 20: # Once roughly per second
            for y in range(self.board.height):
                for x in range(self.board.width):
                    obj = self.board.grid[y][x]
                    if isinstance(obj, iron_miner):
                        self.resources_held["Iron"] += obj.level
                    elif isinstance(obj, woodcutter):
                        # Verify nearby tree (logic simplified for now, assumes placed near tree)
                         self.resources_held["Wood"] += obj.level

        # Enemies move
        base_obj = self.board.get_object(*self.base_pos)
        if not base_obj or base_obj.health <= 0:
            self.game_over = True
            return

        for e in self.enemies:
            e.move(self.board.width, self.board.height, self.base_pos)
            
            # Damage buildings
            path_x, path_y = int(e.position[0]), int(e.position[1])
            target = self.board.get_object(path_x, path_y)
            if target and target != base_obj: # Prefer buildings in way
                target.health -= e.damage * 0.1
                if target.health <= 0:
                    self.board.remove_object(path_x, path_y)
            elif target == base_obj:
                 target.health -= e.damage * 0.1
                 if target.health <= 0:
                    self.game_over = True


        # Turrets fire
        for y in range(self.board.height):
            for x in range(self.board.width):
                obj = self.board.grid[y][x]
                if isinstance(obj, turret):
                   if obj.cooldown > 0:
                       obj.cooldown -= 1
                   else:
                       # Find target
                       for e in self.enemies:
                           dist = math.hypot(e.position[0]-x, e.position[1]-y)
                           if dist <= obj.range:
                               e.health -= obj.damage
                               # Draw laser line temporarily
                               start = (x*TILE_SIZE+TILE_SIZE//2, y*TILE_SIZE+TILE_SIZE//2)
                               end = (e.position[0]*TILE_SIZE, e.position[1]*TILE_SIZE)
                               pygame.draw.line(self.screen, YELLOW, start, end, 2)
                               obj.cooldown = obj.fire_rate
                               break

        # Cleanup dead enemies
        new_enemies = []
        for e in self.enemies:
            if e.health > 0:
                new_enemies.append(e)
            else:
                pass # Die
        self.enemies = new_enemies

    def draw(self):
        self.screen.fill(BLACK)
        
        # Draw grid
        for x in range(0, WIDTH, TILE_SIZE):
            pygame.draw.line(self.screen, DARK_GREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILE_SIZE):
            pygame.draw.line(self.screen, DARK_GREY, (0, y), (WIDTH, y))

        # Draw Resources
        for y in range(self.board.height):
            for x in range(self.board.width):
                res = self.board.resources[y][x]
                if res:
                    res.draw(self.screen, x*TILE_SIZE, y*TILE_SIZE)

        # Draw Buildings
        for y in range(self.board.height):
            for x in range(self.board.width):
                obj = self.board.grid[y][x]
                if obj:
                    obj.draw(self.screen, x*TILE_SIZE, y*TILE_SIZE)

        # Draw Enemies
        for e in self.enemies:
            e.draw(self.screen)
            
        # Draw UI
        ui_y = 10
        for res, amt in self.resources_held.items():
            text = self.font.render(f"{res}: {int(amt)}", True, WHITE)
            self.screen.blit(text, (10, ui_y))
            ui_y += 20
        
        self.screen.blit(self.font.render("Keys: 1=Miner 2=Wood 3=Wall 4=Turret 5=Adv.Turret", True, CYAN), (10, HEIGHT - 30))

        if self.selected_building_type:
             text = self.font.render(f"Selected: {self.selected_building_type[0]} Cost: {self.selected_building_type[2]}", True, GREEN)
             self.screen.blit(text, (10, ui_y + 10))

        if self.game_over:
             text = pygame.font.SysFont("Arial", 50).render("GAME OVER", True, RED)
             self.screen.blit(text, (WIDTH//2 - 100, HEIGHT//2))

        pygame.display.flip()

    def run(self):
        while True:
            self.handle_input()
            self.update()
            self.draw()
            self.clock.tick(FPS)

if __name__ == "__main__":
    game = Game()
    game.run()

