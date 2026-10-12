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

Examples of convex sets include:

- Empty set $\emptyset$
- A hyperplane $\{x \in \mathbb{R}^n : a^T x = b\}$ for some $a \in \mathbb{R}^n, b \in \mathbb{R}$

*Proof*: Let $x_1, x_2 \in \{x \in \mathbb{R}^n : a^T x = b\}$. Then $a^T x_1 = b$ and $a^T x_2 = b$. For any $\alpha \in [0, 1]$, we have:

$$
a^T (\alpha x_1 + \overline{\alpha} x_2) = \alpha a^T x_1 + \overline{\alpha} a^T x_2 = \alpha b + \overline{\alpha} b = b.
$$

**Proposition**: The intersection of any collection of convex sets is convex. (Set intersection preserves convexity.)

*Proof*: Let $\{C_i\}_{i \in I}$ be a collection of convex sets, and let $C = \bigcap_{i \in I} C_i$. Take any two points $x_1, x_2 \in C$. Since $x_1, x_2 \in C$, it follows that $x_1, x_2 \in C_i$ for all $i \in I$. By the definition of convexity, for any $\alpha \in [0, 1]$, we have:

$$
\alpha x_1 + \overline{\alpha} x_2 \in C_i \quad \forall i \in I.
$$

Therefore, $\alpha x_1 + \overline{\alpha} x_2 \in C$, which proves that $C$ is convex.

Affine spaces are also convex.

