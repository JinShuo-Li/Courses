# Lecture 2

## Existence of solution

**Global optima**

$x^*$ is a global minimum of $f$ if $f(x^*) \leq f(x)$ for all $x \in \mathbb{R}^n$.

$x^*$ is a global maximum of $f$ if $f(x^*) \geq f(x)$ for all $x \in \mathbb{R}^n$.

**Global extrema may not exist**.

*Review: Inner product and norm*

- Enclidean inner product: $\langle x, y \rangle = x^T y = \sum_{i=1}^n x_i y_i$.
- Euclidean norm: $\|x\|_2 = \sqrt{\langle x, x \rangle} = \sqrt{\sum_{i=1}^n x_i^2}$. (L2 norm)

A norm on $\mathbb{R}^n$ is a function $\|\cdot\|: \mathbb{R}^n \to \mathbb{R}$ that satisfies the following properties:
1. $\|x\| \geq 0$ for all $x \in \mathbb{R}^n$, and $\|x\| = 0$ if and only if $x = 0$.
2. $\|\alpha x\| = |\alpha| \|x\|$ for all $\alpha \in \mathbb{R}$ and $x \in \mathbb{R}^n$.
3. $\|x + y\| \leq \|x\| + \|y\|$ for all $x, y \in \mathbb{R}^n$ (triangle inequality).
4. $\|x\| = 0$ if and only if $x = 0$.

$p$-norms are defined as $\|x\|_p = \left( \sum_{i=1}^n |x_i|^p \right)^{1/p}$ for $p \geq 1$. Common norms include:
- $p = 1$: $\|x\|_1 = \sum_{i=1}^n |x_i|$ (L1 norm)
- $p = 2$: $\|x\|_2 = \sqrt{\sum_{i=1}^n x_i^2}$ (L2 norm)
- $p = \infty$: $\|x\|_\infty = \max_{1 \leq i \leq n} |x_i|$ (L-infinity norm)

*Review: Open and closed balls*

An open ball in $\mathbb{R}^n$ with center $x_0$ and radius $r > 0$ is the set $B(x_0, r) = \{x \in \mathbb{R}^n : \|x - x_0\| < r\}$.

A closed ball in $\mathbb{R}^n$ with center $x_0$ and radius $r > 0$ is the set $\overline{B}(x_0, r) = \{x \in \mathbb{R}^n : \|x - x_0\| \leq r\}$.

The **shape** of the ball depends on the norm used. For example, in $\mathbb{R}^2$:
- The unit ball under the L2 norm is a circle.
- The unit ball under the L1 norm is a diamond (square rotated 45 degrees).
- The unit ball under the L-infinity norm is a square.

*Review: Open and closed sets*

A set $S \subseteq \mathbb{R}^n$ is **open** if for every point $x \in S$, there exists an $\epsilon > 0$ such that the open ball $B(x, \epsilon) \subseteq S$.

A set $S$ is closed if its complement $\mathbb{R}^n \setminus S$ is open. Equivalently, $S$ is closed if it contains all its limit points.

**Theorem**: A set $S \subseteq \mathbb{R}^n$ is closed if and only if it contains all its limit points.

*Review: Compactness*

A set $S$ is bounded if there exists a real number $M > 0$ such that $\|x\| \leq M$ for all $x \in S$.

**Heine-Borel Theorem**: A set $S$ is compact iff it is closed and bounded.

*Review: Continuity*

A function $f: \mathbb{R}^n \to \mathbb{R}$ is continuous at a point $x_0 \in \mathbb{R}^n$ if for every $\epsilon > 0$, there exists a $\delta > 0$ such that $\|x - x_0\| < \delta$ implies $|f(x) - f(x_0)| < \epsilon$.

**Extreme Value Theorem**: If $f$ is continuous on a compact set $S \subseteq \mathbb{R}^n$, then $f$ attains its maximum and minimum on $S$.

**The extreme value theorem gurantees the sufficient condition for the existence of a global optimum**. However, it does not guarantee the existence of a global optimum if the set is not compact or if the function is not continuous.

- Corollary: If $f$ is continuous on $\mathbb{R}^n$ and $\lim_{\|x\| \to \infty} f(x) = \infty$, then $f$ attains its minimum on $\mathbb{R}^n$.

*A function is called coercive if $\lim_{\|x\| \to \infty} f(x) = \infty$.*

**Local minimum**

$x^*$ is a local minimum of $f$ if there exists an $\epsilon > 0$ such that $f(x^*) \leq f(x)$ for all $x \in B(x^*, \epsilon)$.

$x^*$ is a strict local minimum of $f$ if there exists an $\epsilon > 0$ such that $f(x^*) < f(x)$ for all $x \in B(x^*, \epsilon) \setminus \{x^*\}$.

*Global minimum is always local minimun, but not vice versa.*

## 

*Review: Derivative*

$x$ is an interior point of a set $S \subseteq \mathbb{R}^n$ if there exists an $\epsilon > 0$ such that $B(x, \epsilon) \subseteq S$. And the interior of $S$ is the set of all interior points of $S$, denoted by $\text{int} S$.

A function $f: \mathbb{R}^n \to \mathbb{R}^m$ is differentiable at a point $x_0 \in \text{int} S$ if there exists a linear map $Df(x_0): \mathbb{R}^n \to \mathbb{R}^m$ such that

$$
\lim_{x \to x_0} \frac{\|f(x) - f(x_0) - Df(x_0)(x - x_0)\|}{\|x - x_0\|} = 0
$$

The linear map here is represented by the Jacobian matrix.

*Review: Gradient*

For a real-valued function $f: \mathbb{R}^n \to \mathbb{R}$, the gradient of $f$ at a point $x_0$ is the vector of partial derivatives, denoted by $\nabla f(x_0) = \left( \frac{\partial f}{\partial x_1}(x_0), \ldots, \frac{\partial f}{\partial x_n}(x_0) \right)^T$, is the transpose of the Jacobian matrix.

The gradient $\nabla f(x_0)$ points in the direction of the steepest ascent of the function $f$ at the point $x_0$. The negative gradient $-\nabla f(x_0)$ points in the direction of the steepest descent.

*Review: Chain Rule*

If $f: \mathbb{R}^n \to \mathbb{R}^m$ is differentiable at $x_0$ and $g: \mathbb{R}^m \to \mathbb{R}^p$ is differentiable at $y_0 = g(x_0)$, then the composition $h = f \circ g: \mathbb{R}^m \to \mathbb{R}^p$ is differentiable at $x_0$, and the differential of $h$ at $x_0$ is given by

$$
Dh(x_0) = Df(g(x_0)) \cdot Dg(x_0)
$$

