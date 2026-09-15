import random
from math import sin, cos, pi, atan2
import time

DATA = {
    "Tick": 0.01,
    "Mutation_rate": 0.9,
    "Energy_efficiency": 0.8,
    "Seed": 44,
    "World_width": 220.0,
    "World_height": 140.0,
    "Plant_nutrition": 20.0,
    "Plant_detect_range": 30.0,
    "Plant_spawn_rate": 50.0,
    "Plant_max": 1000,
    "Herb_init_n": 80,
    "Herb_energy_init": 30.0,
    "Herb_energy_max": 80.0,
    "Herb_energy_use": 0.3,
    "Herb_speed": 5.0,
    "Herb_sense_pred": 50.0,
    "Herb_repro_threshold": 40.0,
    "Herb_repro_cooldown": 4.0,
    "Herb_repro_distance": 9.0,
    "Herb_lifespan": 80.0,
    "Carn_init_n": 12,
    "Carn_energy_init": 60.0,
    "Carn_energy_max": 150.0,
    "Carn_energy_use": 0.6,
    "Carn_speed": 7.0,
    "Carn_detect_prey": 60.0,
    "Carn_hunger_threshold": 100.0,
    "Carn_repro_threshold": 110.0,
    "Carn_repro_cooldown": 5.0,
    "Carn_repro_distance": 11.0,
    "Carn_lifespan": 100.0,
    "Plant_eat_radius": 3.0,
    "Capture_radius": 4.0,
    "Steps_per_frame": 1,
    "Max_frames": 100000,
}

SYS_TIME = 0.0

def get_toroidal_delta(a, b, w, h):
    dx = b[0] - a[0]
    dy = b[1] - a[1]
    if dx > w / 2:
        dx -= w
    elif dx < -w / 2:
        dx += w
    if dy > h / 2:
        dy -= h
    elif dy < -h / 2:
        dy += h
    return dx, dy

def distance_sq_toroidal(a, b, w, h):
    dx, dy = get_toroidal_delta(a, b, w, h)
    return dx*dx + dy*dy

def wrap_position(org, env):
    mv = org.properties.movement
    mv.position[0] = mv.position[0] % env.width
    mv.position[1] = mv.position[1] % env.height

class role_prey:
    def __init__(self, energy, detected_range, mode):
        self.energy = energy
        self.range = detected_range
        self.mode = mode

class role_predator:
    def __init__(self, detecting_range, status):
        self.range = detecting_range
        self.status = status

class movement:
    def __init__(self, position, speed, direction):
        self.position = position
        self.speed = speed
        self.direction = direction

class role_reproduction:
    def __init__(self, energy_thereshold, status, mode, cooldown, record, time, distance, youth):
        self.energy_thereshold = energy_thereshold
        self.status = status
        self.mode = mode
        self.cooldown = cooldown
        self.record = record
        self.time = time
        self.distance = distance
        self.youth = youth

class properties:
    def __init__(self, role_prey, role_predator, role_movement, role_reproduction, energy, energy_max, energy_consumption_rate, birth_time, life_span, species):
        self.prey = role_prey
        self.predator = role_predator
        self.movement = role_movement
        self.reproduction = role_reproduction
        self.energy = energy
        self.energy_max = energy_max
        self.energy_consumption_rate = energy_consumption_rate
        self.birth_time = birth_time
        self.life_span = life_span
        self.species = species
        if self.prey is not None and self.prey.mode == 1:
            self.prey.energy = self.energy * DATA["Energy_efficiency"]

class environment:
    def __init__(self, width, height, prey_lst, predator_lst, parameters):
        self.width = width
        self.height = height
        self.prey_lst = prey_lst
        self.predator_lst = predator_lst
        self.parameters = parameters

class organisms:
    def __init__(self, properties):
        self.properties = properties
        self.time = SYS_TIME
        self.alive = True

    def normal_update(self, env=None):
        dt = DATA["Tick"]
        base_use = self.properties.energy_consumption_rate
        speed_penalty = 0.02 * (self.properties.movement.speed ** 1.5) if self.properties.movement else 0
        self.properties.energy -= (base_use + speed_penalty) * dt
        
        if self.properties.energy <= 0.0 or (self.time - self.properties.birth_time) > self.properties.life_span:
            self.alive = False
            return False
        
        mv = self.properties.movement
        if mv is not None:
            mv.position[0] += mv.speed * dt * cos(mv.direction)
            mv.position[1] += mv.speed * dt * sin(mv.direction)
        
        if env is not None and mv is not None:
            wrap_position(self, env)
            
        if self.properties.energy > self.properties.energy_max:
            self.properties.energy = self.properties.energy_max
        if self.properties.prey is not None and self.properties.prey.mode == 1:
            self.properties.prey.energy = self.properties.energy * DATA["Energy_efficiency"]
        return True

    def mutation(self):
        r = DATA["Mutation_rate"]
        left_bound, right_bound = 1.0 - r * 2, 1.0 + r * 2

        def scale_mut(x, min_v=None, max_v=None):
            if random.random() < 0.3:
                x2 = x * random.uniform(left_bound, right_bound)
            else:
                x2 = x
            if min_v is not None: x2 = max(min_v, x2)
            if max_v is not None: x2 = min(max_v, x2)
            return x2

        if self.properties.movement:
            if random.random() < r: self.properties.movement.speed = scale_mut(self.properties.movement.speed, min_v=2.0)
            if random.random() < r: self.properties.movement.direction = (self.properties.movement.direction + random.uniform(-pi, pi)) % (2 * pi)

        if self.properties.predator and random.random() < r:
            self.properties.predator.range = scale_mut(self.properties.predator.range, min_v=20.0, max_v=150.0)

        if self.properties.prey and self.properties.prey.mode == 1 and random.random() < r:
             self.properties.prey.range = scale_mut(self.properties.prey.range, min_v=10.0, max_v=100.0)

        if random.random() < r: self.properties.energy_consumption_rate = scale_mut(self.properties.energy_consumption_rate, min_v=0.1)
        if random.random() < r: self.properties.life_span = scale_mut(self.properties.life_span, min_v=20.0)

    def reproduce(self, partner):
        if not (self.properties.reproduction and partner.properties.reproduction): return None
        if self.properties.species != partner.properties.species: return None

        rep1, rep2 = self.properties.reproduction, partner.properties.reproduction
        if rep1.status != 1 or rep2.status != 1: return None
        if self.properties.energy < rep1.energy_thereshold or partner.properties.energy < rep2.energy_thereshold: return None
        
        w, h = DATA["World_width"], DATA["World_height"]
        if distance_sq_toroidal(self.properties.movement.position, partner.properties.movement.position, w, h) > min(rep1.distance, rep2.distance)**2:
            return None

        self.properties.energy -= rep1.energy_thereshold * 0.6
        partner.properties.energy -= rep2.energy_thereshold * 0.6
        rep1.status, rep2.status = 0, 0
        rep1.record.append(self.time)
        rep2.record.append(partner.time)
        rep1.youth, rep2.youth = 0.0, 0.0

        child_pos = list(self.properties.movement.position)
        child_pos[0] += random.uniform(-1, 1)
        child_pos[1] += random.uniform(-1, 1)
        
        child_speed = (self.properties.movement.speed + partner.properties.movement.speed) / 2.0
        child_movement = movement(child_pos, child_speed, random.uniform(0, 2*pi))

        child_prey = role_prey(0.0, (self.properties.prey.range + partner.properties.prey.range)/2, self.properties.prey.mode) if self.properties.prey else None
        child_predator = role_predator((self.properties.predator.range + partner.properties.predator.range)/2, 0) if self.properties.predator else None

        child_reproduction = role_reproduction(
            (rep1.energy_thereshold + rep2.energy_thereshold)/2, 0, rep1.mode,
            (rep1.cooldown + rep2.cooldown)/2, [], 0.0, 
            (rep1.distance + rep2.distance)/2, 0.0
        )

        child_emax = (self.properties.energy_max + partner.properties.energy_max)/2
        child_energy = child_emax * 0.4
        
        child_prop = properties(
            child_prey, child_predator, child_movement, child_reproduction,
            child_energy, child_emax,
            (self.properties.energy_consumption_rate + partner.properties.energy_consumption_rate)/2,
            self.time, (self.properties.life_span + partner.properties.life_span)/2, self.properties.species
        )
        child = organisms(child_prop)
        child.time = self.time
        child.mutation()
        return child

    def chase_prey(self, prey_list):
        if not self.properties.predator or self.properties.predator.status == 0: return False
        mypos = self.properties.movement.position
        r_sq = self.properties.predator.range**2
        w, h = DATA["World_width"], DATA["World_height"]
        
        best, best_d2 = None, None
        best_delta = (0, 0) 

        for p in prey_list:
            if not p.alive: continue
            dx, dy = get_toroidal_delta(mypos, p.properties.movement.position, w, h)
            d2 = dx*dx + dy*dy
            
            if d2 <= r_sq and (best is None or d2 < best_d2):
                best, best_d2 = p, d2
                best_delta = (dx, dy)
        
        if best:
            target_angle = atan2(best_delta[1], best_delta[0])
            self.properties.movement.direction = target_angle
            return True
        return False

    def escape_predator(self, predator_list):
        if not self.properties.prey: return False
        mypos = self.properties.movement.position
        s_sq = self.properties.prey.range**2
        w, h = DATA["World_width"], DATA["World_height"]
        
        best, best_d2 = None, None
        best_delta = (0, 0)

        for p in predator_list:
            if not p.alive or not p.properties.predator or p.properties.predator.status == 0: continue
            
            dx, dy = get_toroidal_delta(mypos, p.properties.movement.position, w, h)
            d2 = dx*dx + dy*dy
            
            if d2 <= s_sq and d2 <= p.properties.predator.range**2:
                if best is None or d2 < best_d2:
                    best, best_d2 = p, d2
                    best_delta = (dx, dy) 
        
        if best:
            target_angle = atan2(-best_delta[1], -best_delta[0])
            self.properties.movement.direction = target_angle
            return True
        return False

    def forage_plants(self, plants):
        mypos = self.properties.movement.position
        detect_sq = DATA["Plant_detect_range"]**2
        w, h = DATA["World_width"], DATA["World_height"]
        
        best, best_d2 = None, None
        best_delta = (0, 0)
        
        for p in plants:
            if not p.alive: continue
            dx, dy = get_toroidal_delta(mypos, p.properties.movement.position, w, h)
            d2 = dx*dx + dy*dy
            if d2 <= detect_sq and (best is None or d2 < best_d2):
                best, best_d2 = p, d2
                best_delta = (dx, dy)
                
        if best:
            self.properties.movement.direction = atan2(best_delta[1], best_delta[0])
            return True
        return False

    def wander(self):
        mv = self.properties.movement
        mv.direction = (mv.direction + random.uniform(-0.5, 0.5)) % (2 * pi)

def random_pos(env): return [random.uniform(0, env.width), random.uniform(0, env.height)]

def make_plant(env):
    return organisms(properties(role_prey(DATA["Plant_nutrition"],0,0),None,movement(random_pos(env),0,0),None,DATA["Plant_nutrition"],DATA["Plant_nutrition"],0,SYS_TIME,1e18,"plant"))

def make_herbivore(env):
    return organisms(properties(
        role_prey(0,DATA["Herb_sense_pred"],1),None,
        movement(random_pos(env),DATA["Herb_speed"],random.uniform(0,2*pi)),
        role_reproduction(DATA["Herb_repro_threshold"],0,1,DATA["Herb_repro_cooldown"],[],0,DATA["Herb_repro_distance"],DATA["Herb_repro_cooldown"]),
        DATA["Herb_energy_init"],DATA["Herb_energy_max"],DATA["Herb_energy_use"],SYS_TIME,DATA["Herb_lifespan"],"herbivore"
    ))

def make_carnivore(env):
    return organisms(properties(
        role_prey(0,18,1),role_predator(DATA["Carn_detect_prey"],0),
        movement(random_pos(env),DATA["Carn_speed"],random.uniform(0,2*pi)),
        role_reproduction(DATA["Carn_repro_threshold"],0,1,DATA["Carn_repro_cooldown"],[],0,DATA["Carn_repro_distance"],DATA["Carn_repro_cooldown"]),
        DATA["Carn_energy_init"],DATA["Carn_energy_max"],DATA["Carn_energy_use"],SYS_TIME,DATA["Carn_lifespan"],"carnivore"
    ))

class agent:
    def __init__(self, env, plants, herbs, carns):
        self.env, self.plants, self.herbivores, self.carnivores = env, plants, herbs, carns

    def update(self):
        global SYS_TIME
        SYS_TIME += DATA["Tick"]
        world_w, world_h = DATA["World_width"], DATA["World_height"]

        for o in self.plants + self.herbivores + self.carnivores: o.time = SYS_TIME
        
        if len(self.plants) < DATA["Plant_max"]:
            for _ in range(int(DATA["Plant_spawn_rate"] * DATA["Tick"])): self.plants.append(make_plant(self.env))
            
        for c in self.carnivores:
            if c.alive and c.properties.predator:
                c.properties.predator.status = 1 if c.properties.energy < DATA["Carn_hunger_threshold"] else 0
        
        for o in self.herbivores + self.carnivores:
            if o.alive and o.properties.reproduction:
                o.properties.reproduction.youth += DATA["Tick"]
                status = 1 if (o.properties.reproduction.youth >= o.properties.reproduction.cooldown and o.properties.energy >= o.properties.reproduction.energy_thereshold) else 0
                o.properties.reproduction.status = status

        for herb in self.herbivores:
            if herb.alive: 
                if not herb.escape_predator(self.carnivores) and not herb.forage_plants(self.plants): herb.wander()
        for carn in self.carnivores:
            if carn.alive:
                if not carn.chase_prey(self.herbivores): carn.wander()

        for o in self.plants + self.herbivores + self.carnivores: 
            if o.alive: o.normal_update(self.env)

        eat_sq = DATA["Plant_eat_radius"]**2
        for herb in self.herbivores:
            if herb.alive:
                for p in self.plants:
                    if p.alive and distance_sq_toroidal(herb.properties.movement.position, p.properties.movement.position, world_w, world_h) <= eat_sq:
                        herb.properties.energy = min(herb.properties.energy + p.properties.prey.energy, herb.properties.energy_max)
                        p.alive = False; break
        
        cap_sq = DATA["Capture_radius"]**2
        for carn in self.carnivores:
            if carn.alive and carn.properties.predator and carn.properties.predator.status == 1:
                target, best_d = None, None
                for herb in self.herbivores:
                    if herb.alive:
                        d = distance_sq_toroidal(carn.properties.movement.position, herb.properties.movement.position, world_w, world_h)
                        if d <= cap_sq and (target is None or d < best_d): target, best_d = herb, d
                if target:
                    gain = target.properties.prey.energy if target.properties.prey else 20.0
                    carn.properties.energy = min(carn.properties.energy + gain, carn.properties.energy_max)
                    target.alive = False

        def breed(pop):
            ready = [x for x in pop if x.alive and x.properties.reproduction and x.properties.reproduction.status == 1]
            random.shuffle(ready)
            used, babies = set(), []
            for i in range(len(ready)):
                if id(ready[i]) in used: continue
                for j in range(i+1, len(ready)):
                    if id(ready[j]) in used: continue
                    child = ready[i].reproduce(ready[j])
                    if child:
                        babies.append(child); used.add(id(ready[i])); used.add(id(ready[j])); break
            pop.extend(babies)
        
        breed(self.herbivores)
        breed(self.carnivores)

        self.plants = [x for x in self.plants if x.alive]
        self.herbivores = [x for x in self.herbivores if x.alive]
        self.carnivores = [x for x in self.carnivores if x.alive]

def build_simulation():
    global SYS_TIME
    SYS_TIME = 0.0
    random.seed(DATA["Seed"])
    env = environment(DATA["World_width"], DATA["World_height"], [], [], {})
    sim = agent(env, 
                [make_plant(env) for _ in range(400)], 
                [make_herbivore(env) for _ in range(DATA["Herb_init_n"])], 
                [make_carnivore(env) for _ in range(DATA["Carn_init_n"])])
    return sim

def main():
    sim = build_simulation()
    print(f"{'Gen':<8} | {'H_Pop':<6} | {'C_Pop':<6} | {'H_Spd':<6} {'H_Rng':<6} {'H_Lif':<6} | {'C_Spd':<6} {'C_Rng':<6} {'C_Lif':<6}")
    print("-" * 75)
    
    start_time = time.time()
    frames = 0
    
    while frames < DATA["Max_frames"]:
        sim.update()
        frames += 1
        
        if frames % 100 == 0:
            c_cnt = len(sim.carnivores)
            h_cnt = len(sim.herbivores)
            
            h_spd, h_rng, h_lif = 0.0, 0.0, 0.0
            c_spd, c_rng, c_lif = 0.0, 0.0, 0.0
            
            if h_cnt > 0:
                h_spd = sum(h.properties.movement.speed for h in sim.herbivores) / h_cnt
                h_rng = sum(h.properties.prey.range for h in sim.herbivores) / h_cnt
                h_lif = sum(h.properties.life_span for h in sim.herbivores) / h_cnt

            if c_cnt > 0:
                c_spd = sum(c.properties.movement.speed for c in sim.carnivores) / c_cnt
                c_rng = sum(c.properties.predator.range for c in sim.carnivores) / c_cnt
                c_lif = sum(c.properties.life_span for c in sim.carnivores) / c_cnt
                
            print(f"{frames:<8} | {h_cnt:<6} | {c_cnt:<6} | {h_spd:<6.2f} {h_rng:<6.2f} {h_lif:<6.1f} | {c_spd:<6.2f} {c_rng:<6.2f} {c_lif:<6.1f}")
            
            if c_cnt == 0:
                print("\n[Simulation Ended] Predators Extinct.")
                break
            if h_cnt == 0:
                print("\n[Simulation Ended] Prey Extinct.")
                break

    end_time = time.time()
    print("-" * 75)
    print(f"Simulation finished in {end_time - start_time:.4f} seconds.")

if __name__ == "__main__":
    main()