import tkinter as tk
import random
import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def add(self, v): return Vector(self.x + v.x, self.y + v.y)
    def sub(self, v): return Vector(self.x - v.x, self.y - v.y)
    def mult(self, n): return Vector(self.x * n, self.y * n)
    def div(self, n): return Vector(self.x / n, self.y / n)
    def mag(self): return math.sqrt(self.x**2 + self.y**2)
    def normalize(self):
        m = self.mag()
        if m != 0: return self.div(m)
        return Vector(0, 0)
    def limit(self, max_val):
        if self.mag() > max_val:
            return self.normalize().mult(max_val)
        return self

WIDTH, HEIGHT = 1400, 900
INIT_PREY = 50
INIT_PREDATOR = 6
MAX_FOOD = 150
FOOD_GROWTH_RATE = 0.1
MUTATION = 0.9

class DNA:
    def __init__(self, genes=None):
        if genes:
            self.max_speed = max(1.0, genes[0] + random.uniform(-MUTATION, MUTATION))
            self.max_force = max(0.02, genes[1] + random.uniform(-MUTATION/10, MUTATION/10))
            self.sense = max(40, genes[2] + random.uniform(-MUTATION*5, MUTATION*5))
        else:
            self.max_speed = random.uniform(1.5, 2.5) 
            self.max_force = random.uniform(0.05, 0.15) 
            self.sense = random.uniform(60, 120)

class Agent:
    def __init__(self, x, y, dna, species):
        self.pos = Vector(x, y)
        self.vel = Vector(random.uniform(-1, 1), random.uniform(-1, 1))
        self.acc = Vector(0, 0)
        
        self.species = species
        self.dna = dna
        self.energy = 200    
        self.health = 100
        self.age = 0
        self.stamina = 100
        if species == 'prey':
            self.size = 6 + (3 - self.dna.max_speed) * 2
        else:
            self.size = 10 + (3 - self.dna.max_speed) * 3

    def update(self):
        self.age += 1
        self.vel = self.vel.add(self.acc)
        self.vel = self.vel.limit(self.dna.max_speed)
        self.pos = self.pos.add(self.vel)
        self.acc = Vector(0, 0)

        if self.pos.x > WIDTH: self.pos.x = 0
        if self.pos.x < 0: self.pos.x = WIDTH
        if self.pos.y > HEIGHT: self.pos.y = 0
        if self.pos.y < 0: self.pos.y = HEIGHT

        speed_cost = (self.vel.mag()**2 * 0.005) 
        size_cost = self.size * 0.005
        base_metabolism = 0.05 if self.species == 'predator' else 0.01
        self.energy -= (speed_cost + size_cost + base_metabolism)

        if self.vel.mag() < self.dna.max_speed * 0.6:
            self.stamina = min(100, self.stamina + 0.5)
        if self.energy <= 0:
            self.health -= 2

        max_lifespan = 2000 if self.species == 'prey' else 2500
        return self.health > 0 and self.age < max_lifespan

    def apply_force(self, force):
        self.acc = self.acc.add(force)
    def seek(self, target_pos):
        desired = target_pos.sub(self.pos)
        desired = desired.normalize().mult(self.dna.max_speed)
        steer = desired.sub(self.vel)
        steer = steer.limit(self.dna.max_force)
        return steer

    def flee(self, target_pos):
        desired = self.pos.sub(target_pos)
        desired = desired.normalize().mult(self.dna.max_speed)
        steer = desired.sub(self.vel)
        steer = steer.limit(self.dna.max_force)
        return steer

    def hunt_behavior(self, preys):
        closest = None
        min_dist = float('inf')
        
        for p in preys:
            d = math.hypot(p.pos.x - self.pos.x, p.pos.y - self.pos.y)
            if d < self.dna.sense and d < min_dist:
                min_dist = d
                closest = p
        
        if closest:
            if min_dist < 80 and self.stamina > 20:
                self.stamina -= 1.5
                force = self.seek(closest.pos).mult(1.3)
            else:
                force = self.seek(closest.pos)
            
            self.apply_force(force)
            if min_dist < self.size + closest.size - 2:
                max_cap = 600
                gain = 100
                self.energy = min(max_cap, self.energy + gain)
                closest.health = 0
                return True
        else:
            self.wander()
        return False

    def prey_behavior(self, foods, predators):
        closest_pred = None
        min_dist = float('inf')
        
        for p in predators:
            d = math.hypot(p.pos.x - self.pos.x, p.pos.y - self.pos.y)
            if d < self.dna.sense and d < min_dist:
                min_dist = d
                closest_pred = p
        
        if closest_pred:
            if self.stamina > 0:
                self.stamina -= 2
                force = self.flee(closest_pred.pos).mult(1.8)
            else:
                force = self.flee(closest_pred.pos)
            self.apply_force(force)
            return 

        if self.energy < 250:
            closest_food = None
            min_dist = float('inf')
            
            for f in foods:
                d = math.hypot(f.x - self.pos.x, f.y - self.pos.y)
                if d < self.dna.sense and d < min_dist:
                    min_dist = d
                    closest_food = f
            
            if closest_food:
                force = self.seek(closest_food)
                self.apply_force(force)
                if min_dist < self.size + 4:
                    self.energy = min(300, self.energy + 40)
                    if closest_food in foods: foods.remove(closest_food)
            else:
                self.wander()
        else:
            self.wander()

    def wander(self):
        wander_point = self.vel.normalize().mult(40)
        wander_point = wander_point.add(self.pos)
        theta = random.uniform(-0.5, 0.5)
        x = math.cos(theta) * 15
        y = math.sin(theta) * 15
        target = wander_point.add(Vector(x, y))
        force = self.seek(target)
        self.apply_force(force.mult(0.4))

    def reproduce(self):
        if self.species == 'prey':
            threshold = 200      
            cost = 80            
            chance = 0.05        
        else:
            threshold = 450
            cost = 350
            chance = 0.005

        if self.energy > threshold and random.random() < chance:
            self.energy -= cost
            new_dna = DNA([self.dna.max_speed, self.dna.max_force, self.dna.sense])
            return Agent(self.pos.x, self.pos.y, new_dna, self.species)
        return None

class Simulation(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("EcoSim - Predator-Prey Simulation")
        self.canvas = tk.Canvas(self, width=WIDTH, height=HEIGHT, bg="#1a1a1a")
        self.canvas.pack()
        
        self.foods = [Vector(random.uniform(0,WIDTH), random.uniform(0,HEIGHT)) for _ in range(200)]
        self.agents = []

        for _ in range(INIT_PREY):
            self.agents.append(Agent(random.uniform(0,WIDTH), random.uniform(0,HEIGHT), DNA(), 'prey'))
        for _ in range(INIT_PREDATOR):
            self.agents.append(Agent(random.uniform(0,WIDTH), random.uniform(0,HEIGHT), DNA(), 'predator'))

        self.loop()

    def loop(self):
        self.canvas.delete("all")

        if len(self.foods) < MAX_FOOD:
            for _ in range(2): 
                if random.random() < FOOD_GROWTH_RATE:
                    if self.foods and random.random() < 0.8:
                        parent = random.choice(self.foods)
                        offset_x = random.uniform(-20, 20)
                        offset_y = random.uniform(-20, 20)
                        new_pos = Vector(max(0, min(WIDTH, parent.x + offset_x)), 
                                       max(0, min(HEIGHT, parent.y + offset_y)))
                        self.foods.append(new_pos)
                    else:
                        self.foods.append(Vector(random.uniform(0,WIDTH), random.uniform(0,HEIGHT)))

        for f in self.foods:
            self.canvas.create_rectangle(f.x-1.5, f.y-1.5, f.x+1.5, f.y+1.5, fill="#3CB371", outline="")

        new_agents = []
        prey_list = [a for a in self.agents if a.species == 'prey']
        pred_list = [a for a in self.agents if a.species == 'predator']
        
        for a in self.agents:
            alive = a.update()
            
            if alive:
                if a.species == 'prey':
                    a.prey_behavior(self.foods, pred_list)
                    angle = math.atan2(a.vel.y, a.vel.x)
                    s = a.size
                    p1 = (a.pos.x + math.cos(angle)*s, a.pos.y + math.sin(angle)*s)
                    p2 = (a.pos.x + math.cos(angle + 2.5)*s, a.pos.y + math.sin(angle + 2.5)*s)
                    p3 = (a.pos.x + math.cos(angle - 2.5)*s, a.pos.y + math.sin(angle - 2.5)*s)
                    
                    fill_col = f'#4682B4'
                    self.canvas.create_polygon(p1, p2, p3, fill=fill_col, outline="")
                    
                else:
                    a.hunt_behavior(prey_list)
                    fill_col = "#FF6347" 
                    outline = "white" if a.stamina > 30 else ""
                    self.canvas.create_oval(a.pos.x-a.size, a.pos.y-a.size, 
                                          a.pos.x+a.size, a.pos.y+a.size, 
                                          fill=fill_col, outline=outline, width=2 if outline else 0)

                child = a.reproduce()
                if child: new_agents.append(child)
                new_agents.append(a)
        
        self.agents = new_agents

        count_prey = len(prey_list)
        count_pred = len(pred_list)

        total_size_prey = sum([p.size for p in prey_list])
        total_size_pred = sum([p.size for p in pred_list])
        avg_size_prey = total_size_prey / count_prey if count_prey > 0 else 0
        avg_size_pred = total_size_pred / count_pred if count_pred > 0 else 0
        
        status = "STABLE"
        status_col = "green"
        if count_prey < 20 or count_pred/count_prey > 0.5: 
            status = "COLLAPSE IMMINENT"
            status_col = "red"
        elif count_pred < 2 or count_pred/count_prey < 0.05:
            status = "PREDATOR EXTINCTION"
            status_col = "orange"
            
        self.canvas.create_text(10, 10, anchor="nw", 
                              text=f"Prey: {count_prey} | Predators: {count_pred} | Food: {len(self.foods)} | Status: {status} | Average Size Prey: {avg_size_prey:.2f} | Average Size Predators: {avg_size_pred:.2f}", 
                              fill=status_col, font=("Consolas", 14, "bold"))

        self.after(20, self.loop)

if __name__ == "__main__":
    app = Simulation()
    app.mainloop()