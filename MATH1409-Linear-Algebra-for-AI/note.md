# Linear Algebra for Artificial Intelligence

课程内容:

- 线性空间和线性变换
- Jordan标准形
- 矩阵分解和应用
- 向量范数
- 梯度矩阵

## 线性空间

线性空间的定义: 设$V$是一个非空集合, $F$是一个数域, 如果在$V$中定义了两个运算: 向量加法和数乘, 并且这两个运算满足以下八条公理, 那么我们称$V$为一个定义在$F$上的线性空间(或向量空间).
   
公理如下:
- 向量加法封闭性: 对于任意的$\vec{u}, \vec{v} \in V$, $\vec{u} + \vec{v} \in V$.
- 向量加法交换律: 对于任意的$\vec{u}, \vec{v} \in V$, $\vec{u} + \vec{v} = \vec{v} + \vec{u}$.
- 向量加法结合律: 对于任意的$\vec{u}, \vec{v}, \vec{w} \in V$, $(\vec{u} + \vec{v}) + \vec{w} = \vec{u} + (\vec{v} + \vec{w})$.
- 零向量存在性: 存在一个零向量$\vec{0} \in V$, 使得对于任意的$\vec{v} \in V$, $\vec{v} + \vec{0} = \vec{v}$.
- 负向量存在性: 对于任意的$\vec{v} \in V$, 存在一个负向量$-\vec{v} \in V$, 使得$\vec{v} + (-\vec{v}) = \vec{0}$.
- 数乘封闭性: 对于任意的$\alpha \in F$和$\vec{v} \in V$, $\alpha \vec{v} \in V$.
- 数乘分配律: 对于任意的$\alpha, \beta \in F$和$\vec{v} \in V$, $(\alpha + \beta) \vec{v} = \alpha \vec{v} + \beta \vec{v}$.
- 数乘结合律: 对于任意的$\alpha, \beta \in F$和$\vec{v} \in V$, $\alpha (\beta \vec{v}) = (\alpha \beta) \vec{v}$.

线性空间中的元素统称为"向量", 但它们不一定是几何意义上的向量. 例如, 函数空间中的元素也是向量, 但它们不是几何意义上的向量.

### 线性差分方程

定义: 给定$a_0, a_1, \ldots, a_n \in F$, 且$a_n \neq 0$, 一个线性差分方程是形如
$$
a_n y_{k+n} + a_{n-1} y_{k+n-1} + \cdots + a_1 y_{k+1} + a_0 y_k = f_k
$$
的方程, 其中$y_k$是未知序列, $f_k$是已知序列. 若方程对$\forall k \in \mathbb{Z}$都成立, 则称其为$n$阶线性差分方程. 若$f_k = 0$对$\forall k \in \mathbb{Z}$都成立, 则称其为齐次线性差分方程; 否则称其为非齐次线性差分方程.

满足上述方程的序列$y_k$称为该线性差分方程的解. 线性差分方程的解空间是一个线性空间, 因为它满足线性空间的八条公理. 它通常具有$y_k=r^k$的形式的解.

### 线性子空间

定义: 设$V$是一个定义在数域$F$上的线性空间, 如果$W$是$V$的一个子集, 且$W$本身也是一个线性空间, 那么我们称$W$是$V$的一个线性子空间. 线性子空间必须满足以下条件:
- $W$包含零向量: $\vec{0} \in W$.
- $W$对向量加法封闭: 对于任意的$\vec{u}, \vec{v} \in W$, $\vec{u} + \vec{v} \in W$.
- $W$对数乘封闭: 对于任意的$\alpha \in F$和$\vec{v} \in W$, $\alpha \vec{v} \in W$.

线性子空间的和: $U + V = \{ \vec{u} + \vec{v} \mid \vec{u} \in U, \vec{v} \in V \}$

线性子空间的交: $U \cap V = \{ \vec{v} \mid \vec{v} \in U, \vec{v} \in V \}$

子空间的交和和都是子空间. 交是子空间的子集, 和是子空间的超集. 但是子空间的并不一定是子空间. 我们可以取完全正交的两个维度.

定义: 设$V$是一个定义在数域$F$上的线性空间, 如果$U$和$W$是$V$的两个线性子空间, 且满足以下条件: $U \cap W = \{ \vec{0} \}$ (即$U$和$W$只有零向量一个公共元素), 则和$U + W$称为$V$的一个直和, 记作$U \oplus W$.

等价定义: 设$V$是一个定义在数域$F$上的线性空间, 如果$U$和$W$是$V$的两个线性子空间, 且满足以下条件: 对于任意的$\vec{v} \in U + W$, 存在唯一的一对$\vec{u} \in U$和$\vec{w} \in W$, 使得$\vec{v} = \vec{u} + \vec{w}$, 则和$U + W$称为$V$的一个直和, 记作$U \oplus W$.

例1: $V=\mathbb{R}^2$, $U = \{ (x, 0) \mid x \in \mathbb{R} \}$, $W = \{ (0, y) \mid y \in \mathbb{R} \}$. 则$U \oplus W = \mathbb{R}^2$.   

正是因为$V$的每个元素都可以唯一表示为$U$中的一个元素和$W$中的一个元素的和, 所以$U \oplus W = V$.

并不是所有的和都是直和, $U$和$W$的直和可以视为$V$的一个恰好划分. 若$U$和$W$的直和构成$V$, 则称$U$是$W$在$V$中的一个补空间. 补子空间一般不唯一.

**直和的性质**: 这四个命题等价:

* $U \oplus W$
* $U+W$中任意一个元素都可以唯一表示为$U$中的一个元素和$W$中的一个元素的和.
* 零向量分解唯一
* $U$和$W$的一组基合起来是$U \oplus W$的一组基

**多个子空间的直和**: 设$V$是一个定义在数域$F$上的线性空间, 如果$U_1, U_2, \ldots, U_k$是$V$的$k$个线性子空间, 且满足以下条件: 对于任意的$\vec{v} \in U_1 + U_2 + \cdots + U_k$, 存在唯一的一组$\vec{u}_1 \in U_1, \vec{u}_2 \in U_2, \ldots, \vec{u}_k \in U_k$, 使得$\vec{v} = \vec{u}_1 + \vec{u}_2 + \cdots + \vec{u}_k$, 则和$U_1 + U_2 + \cdots + U_k$称为$V$的一个直和, 记作$U_1 \oplus U_2 \oplus \cdots \oplus U_k$. 记作:

$$
\oplus_{i=1}^k U_i
$$

**维数公式**: 设$V$是一个定义在数域$F$上的线性空间, 如果$U$和$W$是$V$的两个线性子空间, 则有以下维数公式:

$$
\dim U + \dim W - \dim (U \cap W) = \dim (U + W)
$$

而对于直和运算, 维数公式简化为:

$$
\dim U + \dim W = \dim (U \oplus W)
$$

因为$\dim (U \cap W) = 0$ (即$U$和$W$只有零向量一个公共元素).

### 正交补空间

*内积*: 设$V$是一个定义在数域$F$上的线性空间, 如果对于任意的$\vec{u}, \vec{v} \in V$, 定义了一个数$\langle \vec{u}, \vec{v} \rangle \in F$, 满足以下条件:
- 对于任意的$\vec{u}, \vec{v}, \vec{w} \in V$和$\alpha \in F$, 有$\langle \vec{u} + \vec{v}, \vec{w} \rangle = \langle \vec{u}, \vec{w} \rangle + \langle \vec{v}, \vec{w} \rangle$ (线性)
- 对于任意的$\vec{u}, \vec{v} \in V$和$\alpha \in F$, 有$\langle \alpha \vec{u}, \vec{v} \rangle = \alpha \langle \vec{u}, \vec{v} \rangle$ (线性)
- 对于任意的$\vec{u}, \vec{v} \in V$, 有$\langle \vec{u}, \vec{v} \rangle = \overline{\langle \vec{v}, \vec{u} \rangle}$ (共轭对称)
- 对于任意的$\vec{v} \in V$, 有$\langle \vec{v}, \vec{v} \rangle \geq 0$, 且$\langle \vec{v}, \vec{v} \rangle = 0$当且仅当$\vec{v} = \vec{0}$ (正定)

则称这种运算为$V$上的一个内积, $V$是一个内积空间. 内积空间中的元素统称为"向量", 但它们不一定是几何意义上的向量. 例如, 函数空间中的元素也是向量, 但它们不是几何意义上的向量.

**正交补空间**: 设$V$是一个定义在数域$F$上的内积空间, 如果$W$是$V$的一个线性子空间, 则称$W$的正交补空间为
$$
W^\perp = \{ \vec{v} \in V \mid \langle \vec{v}, \vec{w} \rangle = 0, \forall \vec{w} \in W \}
$$

正交补空间$W^\perp$也是$V$的一个线性子空间.   
直和分解: $V = W \oplus W^\perp$.   
维数公式: $\dim W + \dim W^\perp = \dim V$.