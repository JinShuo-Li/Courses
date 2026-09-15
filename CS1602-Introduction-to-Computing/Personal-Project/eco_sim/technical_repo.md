### 2. Technical Report

# Technical Report: EcoSim Evolutionary Simulation

## 1. Introduction

EcoSim is an agent-based simulation (ABS) designed to observe emergent behaviors and evolutionary dynamics in a simplified predator-prey ecosystem. Unlike standard grid-based simulations, EcoSim operates in a continuous Euclidean space with a toroidal (wrap-around) topology, allowing for infinite movement without boundary constraints.

## 2. System Architecture

The simulation is built using Python and Tkinter for visualization. It follows a modular entity-component system (ECS) inspired structure:

### 2.1 Entities

* **Plants (Green Squares):** Stationary energy sources. They spawn stochastically and provide energy to herbivores.
* **Herbivores (Blue Circles):** Primary consumers. They consume plants and attempt to evade carnivores.
* **Carnivores (Red/Pink Circles):** Secondary consumers. They hunt herbivores to survive and reproduce.

### 2.2 Core Components

* **Role_Movement:** Handles position , speed, and direction.
* **Role_Prey:** Defines energy value and predator detection capabilities.
* **Role_Predator:** Defines hunting range and hunger status.
* **Role_Reproduction:** Manages energy thresholds, cooldowns, and mate finding.

## 3. Key Algorithms

### 3.1 Toroidal Topology (Infinite Map)

To eliminate "corner trapping" behaviors common in bounded simulations, the world is topologically a torus.

* **Position Wrapping:** If an agent moves past , its position becomes .
* **Shortest Path Calculation:** The distance between two points  and  is calculated by considering the wrap-around.



This ensures agents always take the shortest path, even if it means crossing the screen edge.

### 3.2 Evolutionary Genetics

Agents pass traits to offspring with a high mutation rate () to accelerate observable evolution.

* **Traits Subject to Mutation:** Movement Speed, Detection Range, Energy Efficiency.
* **Selection Pressure:**
* **Speed:** Faster agents catch prey/escape easier but consume significantly more energy (Energy Consumption ).
* **Size (Visualized):** Carnivore size represents detection range. Larger detection range allows finding prey easier but implies different metabolic costs (implicit in mutation balance).



### 3.3 State Machine

Agents operate on a simple priority-based state machine:

1. **Flee/Hunt:** High priority if threat/food is detected.
2. **Forage:** Move towards nearest food source.
3. **Wander:** Random walk with inertia if no targets are visible.
4. **Reproduce:** If energy and cooldown allow, search for a mate nearby.

## 4. Visual Feedback

To make the internal state of the simulation transparent to the observer:

* **Predators:**
* **Color:** Indicates Speed. Dark Red (Fast)  Pink (Slow).
* **Size:** Indicates Detection Range. Larger = Higher Range.
* **White Outline:** Indicates "Hungry" status (actively hunting).


* **Events:** A yellow line connects predator and prey at the moment of a kill, providing immediate feedback on predation events.

## 5. Conclusion

The simulation successfully demonstrates dynamic equilibrium. Populations fluctuate based on resource availability. Evolutionary trends are observable: in high-density prey environments, predators tend to evolve lower speeds (energy-saving), while in scarce environments, high-speed and high-detection traits become dominant despite the energy cost.