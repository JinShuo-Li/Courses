# Lecture 3 Convex Sets and Functions

## Convex Sets

### Lines, line segments, and rays

Given two points $x_1, x_2 \in \mathbb{R}^n$, the line through these points is defined as the set of all points of the form:
$$
\{x \in \mathbb{R}^n : x = \alpha x_1 + (1 - \alpha) x_2 = x_2 + \alpha (x_1 - x_2), \alpha \in \mathbb{R}\}.
$$

The line segment between $x_1$ and $x_2$ is defined as the set of all points of the form:
$$
\{x \in \mathbb{R}^n : x = \alpha x_1 + (1 - \alpha) x_2 = x_2 + \alpha (x_1 - x_2), \alpha \in [0, 1]\}.
$$

The ray starting at $x_1$ and passing through $x_2$ is defined as the set of all points of the form:
$$
\{x \in \mathbb{R}^n : x = \alpha x_1 + (1 - \alpha) x_2 = x_2 + \alpha (x_1 - x_2), \alpha \in [0, \infty)\}.
$$

### Convex sets

A set $C \subseteq \mathbb{R}^n$ is convex if for any two points $x_1, x_2 \in C$, the line segment between them lies entirely within $C$. Formally, this means that for all $\alpha \in [0, 1]$:

$$
x_1 \in C, x_2 \in C \implies \alpha x_1 + \overline{\alpha} x_2 \in C.
$$

*Note*: For $\alpha \in [0, 1]$, we have $\overline{\alpha} = 1 - \alpha$. And $\alpha x + \overline{\alpha} y$ is called a convex combination of $x$ and $y$.

