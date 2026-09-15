### 3. README.md

# EcoSim: Toroidal Evolutionary Simulator

An interactive biological simulation where autonomous agents evolve, hunt, and reproduce in an infinite toroidal world.

## Features

* **Toroidal Topology:** The world wraps around edges. Agents moving off the right reappear on the left. AI logic intelligently calculates the shortest path across boundaries.
* **Real-time Evolution:** Agents mutate traits (Speed, Vision, Metabolism) over generations.
* **Visual Analytics:**
* **Carnivore Speed:** Visualized by color saturation (Dark Red = Fast, Pink = Slow).
* **Carnivore Vision:** Visualized by body size (Larger = Better Vision).
* **Kill Feed:** Visualized by yellow lightning strikes when a kill occurs.


* **Dynamic Population:** Balanced ecosystem with automatic plant regeneration and energy-based reproduction.

## Prerequisites

* **Python 3.x**
* **Tkinter** (Usually included with standard Python installations)

## Installation & Running

1. Save the source code as `ecosim.py`.
2. Run the script via terminal or command prompt:

```bash
python ecosim.py

```

## Visual Legend

| Entity | Appearance | Behavior |
| --- | --- | --- |
| **Plant** | 🟩 Green Square | Food source for herbivores. |
| **Herbivore** | 🔵 Blue Circle | Eats plants, runs from predators. Grows from small to large after birth. |
| **Carnivore** | 🔴 Red/Pink Circle | Eats herbivores. **Darker Red** = Faster. **Larger Size** = Better Vision. |
| **Hunger** | ⚪ White Outline | The predator is hungry and actively hunting. |
| **Kill Event** | ⚡ Yellow Line | Indicates a successful predation event. |

## Key Mechanics

* **Energy Cost:** Moving fast costs significantly more energy (`Speed^1.5`). This creates an evolutionary trade-off: be fast to catch prey, or be slow to conserve energy?
* **Reproduction:** Agents reproduce sexually when they have enough energy and are near a mate. Offspring inherit traits with random mutations.
* **Looping Map:** There are no corners to get trapped in. The best escape route might be across the screen edge.