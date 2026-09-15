# Lecture 1: Introduction

Core problem: Given a set of constraints, find the best solution according to some objective function.

$$
\min_{x \in \Omega} f(x)
$$

- feasible/infeasible

- constrained/unconstrained

- constraint functions

## Classifications

- discrete optimization

- continuous optimization

  - nonlinear optimization

    - convex optimization

      - linear optimization


## Examples and Applications

### Hooke's law

$$
F = -k (x-x_0) = -kx + b, \quad b = k x_0
$$

How can we figure out the value of $k$ and $b$? Theoratically, we only need two sets of experimental data points $(x_1, F_1)$ and $(x_2, F_2)$ to solve for $k$ and $b$. However, in practice, we may have more than two data points due to experimental errors, we call it noise.

So the optimization function can be:

$$
\text{error} = \min \sum_{i=1}^{n} |F_i - (-kx_i + b)|
$$

However, the absolute value function is not differentiable, so we can use the square of the error instead:

$$
\text{error} = \min \sum_{i=1}^{n} (F_i - (-kx_i + b))^2
$$

We can generalize this to a linear regression problem. The $f(x)$ can be rewritten as:

### Linear regression

$$
\hat{y} = f(x) = \sum_{i=1}^{n} w_i x_i + b = x^T w + b
$$

We would like to figure out the value of $w$ and $b$ that minimizes the error. So the optimization problem can be formulated as:

$$
l(w) = \min_{w, b} \sum_{i=1}^{n} (y_i - (x_i^T w + b))^2 = \sum_{i=1}^{n} \Delta_i^2
$$

In language of linear algebra, we can rewrite the above problem as:

$$
X = \begin{bmatrix}
x_1^T \\
x_2^T \\
\vdots \\
x_n^T
\end{bmatrix}, \quad
p = \begin{bmatrix}
p_1 \\
p_2 \\
\vdots \\
p_n
\end{bmatrix}, \quad
\Delta = X w - p = \begin{bmatrix}
x_1^T w - p_1 \\
x_2^T w - p_2 \\
\vdots \\
x_n^T w - p_n
\end{bmatrix} = \begin{bmatrix}
\Delta_1 \\
\Delta_2 \\
\vdots \\
\Delta_n
\end{bmatrix}
$$

Thus we have:

$$
l(w) = \min_{w, b} \sum_{i=1}^{n} (y_i - (x_i^T w + b))^2 = \Delta^T \Delta
$$

### Optimal transport problem

We need to ship products from $n$ warehouses to $m$ constomers.

- Unit shipping cost from warehouse $i$ to customer $j$: $c_{ij}$

- Quantity of products from warehouse $i$ to customer $j$: $x_{ij}$

- Inventory of warehouse $i$: $a_i$

- Demand of customer $j$: $b_j$

So the optimization problem can be formulated as:

1. Objective function:

$$
\min \sum_{i=1}^{n} \sum_{j=1}^{m} c_{ij} x_{ij}
$$

2. Contraints:

   - Supply constraints: $\sum_{j=1}^{m} x_{ij} = a_i$, for all $i$

   - Demand constraints: $\sum_{i=1}^{n} x_{ij} \leq b_j$, for all $j$

   - Non-negativity constraints: $x_{ij} \geq 0$, for all $i, j$

### Power allocation problem

We want to transmit information over $n$ channels. The capacity of channel $i$ is:

$$
C_i = W_i \log_2 \left( 1 + \frac{P_i}{N_i} \right), \quad \text{bits/second}
$$

The goal is to allocate power $P_i$ to each channel such that the total capacity is maximized, subject to a power constraint.

1. Objective function:

$$
\max \sum_{i=1}^{n} W_i \log_2 \left( 1 + \frac{P_i}{N_i} \right)
$$

2. Constraints:

   - Power constraint: $\sum_{i=1}^{n} P_i \leq P_{\text{total}}$

   - Non-negativity constraints: $P_i \geq 0$, for all $i$

### Binary classification problem

Represent an image by flatten the image into a vector $x \in \mathbb{R}^n$. We want to classify the image into two classes: cat or dog. We can use a label like $y \in \{-1, 1\}$, where $-1$ represents a cat and $1$ represents a dog.

We want to figure out a function $f(x): \mathbb{R}^n \to \{-1, 1\}$ that can classify the image correctly. We can call it the **classifier**. Such that:

$$
\begin{cases}
    f(x_i) > 0, & \text{iff } y_i = 1 \\
    f(x_i) < 0, & \text{iff } y_i = -1
\end{cases}
$$

We can consider linear classifiers, such that:

$$
f(x) = w^T x + b
$$

We have two ways to determine the parameters $w$ and $b$: **logistic regression** and **support vector machine (SVM)**.

#### Logistic regression

Logistic regression assumes the probability of the label $y$ given the input $x$ is modeled by a logistic function:

$$
P(y=1|x) = \frac{1}{1 + e^{-(w^T x + b)}}, \quad P(y=-1|x) = 1 - P(y=1|x) = \frac{e^{-(w^T x + b)}}{1 + e^{-(w^T x + b)}}
$$

(Here we use a **sigmoid** function to map the linear combination of features to a probability)

$$
\sigma(z) = \frac{1}{1 + e^{-z}}
$$

To determine $w$ and $b$, we can use the maximum likelihood estimation (MLE) method. The likelihood function is:

$$
L(w, b) = \prod_{i=1}^{n} P(y_i|x_i)
$$

or equivalently, the minus log-likelihood function is:

$$
l(w, b) = -\sum_{i=1}^{n} \log P(y_i|x_i) = \sum_{i=1}^{n} \log(1 + e^{-y_i(w^T x_i + b)})
$$

And the optimization problem can be formulated as:

$$
\min_{w, b} l(w, b) = \sum_{i=1}^{n} \log(1 + e^{-y_i(w^T x_i + b)})
$$

#### Support vector machine (SVM)

Core idea: **A classifier with a larger margin is more robust against noise.**

- Objective function: maximize the margin between the two classes.

$$
\max \min_i \text{dist}(x_i, P)
$$

- Constraints: all data points are correctly classified: the points of each class are on the correct side of the hyperplane.

$$
y_i (w^T x_i + b) \geq 0, \quad \forall i
$$

Assume the data is **linearly separable**, which means that there exists a hyperplane

$$
P: w^T x + b = 0
$$

such that

$$
y_i(w^T x_i+b) > 0, \quad \forall i
$$

There may be many hyperplanes that can correctly separate the data. SVM tries to choose the one with the largest margin.

##### Distance from a point to a hyperplane

Given a hyperplane

$$
P: w^T x+b=0,
$$

the vector $w$ is perpendicular to the hyperplane.

The distance from a point $x_i$ to the hyperplane is

$$
\boxed{
\text{dist}(x_i,P)
=
\frac{|w^Tx_i+b|}{\|w\|}
}
$$

To see why, let $x_i'$ be the orthogonal projection of $x_i$ onto the hyperplane.

Since

$$
x_i-x_i' \perp P
$$

and $w$ is also perpendicular to $P$, we have

$$
x_i-x_i'=\gamma_i w
$$

for some $\gamma_i\in\mathbb{R}$.

Therefore,

$$
x_i'=x_i-\gamma_iw.
$$

Because $x_i'$ lies on the hyperplane,

$$
w^Tx_i'+b=0.
$$

Substituting $x_i'=x_i-\gamma_iw$ gives

$$
w^T(x_i-\gamma_iw)+b=0,
$$

so

$$
\gamma_i
=
\frac{w^Tx_i+b}{w^Tw}.
$$

Hence,

$$
\begin{aligned}
\text{dist}(x_i,P)
&=
\|x_i-x_i'\| \\
&=
\|\gamma_iw\| \\
&=
|\gamma_i|\|w\| \\
&=
\frac{|w^Tx_i+b|}{\|w\|}.
\end{aligned}
$$

##### Margin

The **margin** of the classifier is defined as the minimum distance from the training data to the separating hyperplane:

$$
\text{margin}
=
\min_{1\leq i\leq n}
\frac{|w^Tx_i+b|}{\|w\|}.
$$

Therefore, the SVM problem can initially be written as

$$
\max_{w,b}
\min_{1\leq i\leq n}
\frac{|w^Tx_i+b|}{\|w\|}
$$

subject to

$$
y_i(w^Tx_i+b)>0,
\quad i=1,2,\ldots,n.
$$

However, this form is not easy to solve directly, so we would like to reformulate it.

##### Reformulation of the SVM problem

Since all samples are correctly classified,

$$
y_i = \operatorname{sign}(w^T x_i+b).
$$

Therefore,

$$
|w^Tx_i+b|
=
y_i(w^Tx_i+b).
$$

So the margin can be written as

$$
\min_i
\frac{y_i(w^Tx_i+b)}{\|w\|}.
$$

Another important observation is that the same hyperplane can have many different representations.

For any $\alpha>0$,

$$
w^Tx+b=0
$$

and

$$
(\alpha w)^Tx+\alpha b=0
$$

represent exactly the same hyperplane.

That is,

$$
x\in P
\iff
w^Tx+b=0
\iff
\tilde w^Tx+\tilde b=0,
$$

where

$$
\tilde w=\alpha w,
\qquad
\tilde b=\alpha b.
$$

Therefore, we are free to choose a convenient scaling of $w$ and $b$.

We choose $\alpha$ such that

$$
\min_i y_i(\tilde w^Tx_i+\tilde b)=1.
$$

Then all training samples satisfy

$$
y_i(\tilde w^Tx_i+\tilde b)\geq1.
$$

Under this normalization, the minimum value in the numerator is $1$, so the margin becomes

$$
\frac{1}{\|\tilde w\|}.
$$

Therefore, maximizing the margin is equivalent to solving

$$
\max_{\tilde w,\tilde b}
\frac{1}{\|\tilde w\|}
$$

subject to

$$
y_i(\tilde w^Tx_i+\tilde b)\geq1,
\quad i=1,\ldots,n.
$$

Since for $z>0$,

$$
\max \frac{1}{z}
\iff
\min z
\iff
\min \frac12 z^2,
$$

we obtain

$$
\boxed{
\begin{aligned}
\min_{w,b} \quad
& \frac12\|w\|^2 \\
\text{s.t.} \quad
& y_i(w^Tx_i+b)\geq1,
\quad i=1,\ldots,n.
\end{aligned}
}
$$

This is the standard formulation of the **hard-margin SVM**.

##### Hard-margin SVM

The hard-margin SVM is

$$
\boxed{
\begin{aligned}
\min_{w,b}\quad
&\frac12\|w\|^2\\
\text{s.t.}\quad
&y_i(w^Tx_i+b)\geq1,
\quad \forall i.
\end{aligned}
}
$$

The decision boundary is

$$
w^Tx+b=0.
$$

The two hyperplanes closest to the training samples are

$$
w^Tx+b=1
$$

and

$$
w^Tx+b=-1.
$$

The distance from either of these hyperplanes to the decision boundary is

$$
\frac{1}{\|w\|}.
$$

Therefore, the total width between the two boundary hyperplanes is

$$
\frac{2}{\|w\|}.
$$

The data points that lie on the margin satisfy

$$
y_i(w^Tx_i+b)=1.
$$

These points determine the margin and are called **support vectors**.

Hard-margin SVM assumes that the data is linearly separable. If the data is not linearly separable, the constraints

$$
y_i(w^Tx_i+b)\geq1
$$

cannot all be satisfied.

Therefore, we need to relax the constraints.

##### Soft-margin SVM

For data that is not perfectly linearly separable, we introduce **slack variables**

$$
\xi_i\geq0.
$$

Instead of requiring

$$
y_i(w^Tx_i+b)\geq1,
$$

we relax the constraint to

$$
y_i(w^Tx_i+b)\geq1-\xi_i.
$$

The variable $\xi_i$ measures how much the $i$-th sample violates the margin constraint.

However, if we only relax the constraints without any penalty, we could simply choose arbitrarily large $\xi_i$. Therefore, the violations must also be penalized in the objective function.

The soft-margin SVM is

$$
\boxed{
\begin{aligned}
\min_{w,b,\xi}\quad
&
\frac12\|w\|^2
+
C\sum_{i=1}^{n}\xi_i
\\
\text{s.t.}\quad
&
y_i(w^Tx_i+b)\geq1-\xi_i,
\quad i=1,\ldots,n,
\\
&
\xi_i\geq0,
\quad i=1,\ldots,n.
\end{aligned}
}
$$

where $C>0$ is a hyperparameter.

There are two parts in the objective function:

$$
\underbrace{\frac12\|w\|^2}_{\text{maximize the margin}}
+
\underbrace{C\sum_{i=1}^{n}\xi_i}_{\text{penalize constraint violations}}.
$$

So soft-margin SVM balances two goals:

1. make the margin as large as possible;
2. avoid too many violations of the classification constraints.

The parameter $C$ determines the trade-off between them.

- A larger $C$ gives a larger penalty to violations, so the classifier tries harder to classify the training data correctly.

- A smaller $C$ allows more violations in exchange for a potentially larger margin.

Therefore, compared with hard-margin SVM,

$$
\text{Hard-margin SVM}
\quad\Rightarrow\quad
\text{perfect separation is required},
$$

while

$$
\text{Soft-margin SVM}
\quad\Rightarrow\quad
\text{some violations are allowed and penalized}.
$$