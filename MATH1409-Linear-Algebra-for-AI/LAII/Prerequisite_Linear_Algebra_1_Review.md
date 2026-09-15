# 线性代数 I

## 运算的扩展

我们在线性代数中除了针对矩阵和向量的加法, 数乘, 以及专门针对矩阵的乘法之外, 还会引入一些针对向量的运算:

### 线性空间 $\mathbb{R}^n$中的点积

点积是一个将两个向量映射到一个标量的运算, 其定义如下:

对于 $\mathbf{u} = (u_1, u_2, \ldots, u_n)^T$ 和 $\mathbf{v} = (v_1, v_2, \ldots, v_n)^T$ 两个向量, 它们的点积定义为:

$$
\mathbf{u} \cdot \mathbf{v} = u_1 v_1 + u_2 v_2 + \ldots + u_n v_n
$$

#### 酉空间: 配备了内积的复空间

在复空间 $\mathbb{C}^n$ 中, 我们可以定义一个类似于点积的运算, 叫做内积. 内积的定义如下:

对于 $\mathbf{u} = (u_1, u_2, \ldots, u_n)^T$ 和 $\mathbf{v} = (v_1, v_2, \ldots, v_n)^T$ 两个向量, 它们的内积定义为:

$$
\langle \mathbf{u}, \mathbf{v} \rangle = u_1 \overline{v_1} + u_2 \overline{v_2} + \ldots + u_n \overline{v_n}
$$

我们一般用$\overline{A^T}$来表示复数矩阵$A$的共轭转置, 也叫做厄米共轭. 内积满足以下性质:
1. 共轭对称性: $\langle \mathbf{u}, \mathbf{v} \rangle = \overline{\langle \mathbf{v}, \mathbf{u} \rangle}$
2. 线性: $\langle a\mathbf{u} + b\mathbf{v}, \mathbf{w} \rangle = a\langle \mathbf{u}, \mathbf{w} \rangle + b\langle \mathbf{v}, \mathbf{w} \rangle$
3. 正定性: $\langle \mathbf{u}, \mathbf{u} \rangle \geq 0$, 且当且仅当 $\mathbf{u} = \mathbf{0}$ 时等号成立.
4. 非退化性: $\langle \mathbf{u}, \mathbf{v} \rangle = 0$ 对所有 $\mathbf{v}$ 都成立当且仅当 $\mathbf{u} = \mathbf{0}$.
5. 共轭线性: $\langle \mathbf{u}, a\mathbf{v} + b\mathbf{w} \rangle = \overline{a}\langle \mathbf{u}, \mathbf{v} \rangle + \overline{b}\langle \mathbf{u}, \mathbf{w} \rangle$

### 三维Euclid空间中的叉积

叉积是一个将两个向量映射到一个新向量的运算, 其定义如下:

对于 $\mathbf{u} = (u_1, u_2, u_3)^T$ 和 $\mathbf{v} = (v_1, v_2, v_3)^T$ 两个向量, 它们的叉积定义为:

$$
\mathbf{u} \times \mathbf{v} = \begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
u_1 & u_2 & u_3 \\
v_1 & v_2 & v_3
\end{vmatrix}
$$

其中 $\mathbf{i}, \mathbf{j}, \mathbf{k}$ 是三维空间中的标准基向量。

用行列式展开后, 叉积可以表示为:

$$
\mathbf{u} \times \mathbf{v} = (u_2 v_3 - u_3 v_2) \mathbf{i} - (u_1 v_3 - u_3 v_1) \mathbf{j} + (u_1 v_2 - u_2 v_1) \mathbf{k}
$$

对于一般的$n$维空间, 叉积的定义并不适用, 因此我们通常只在三维空间中使用叉积运算.

## 多种分解

在学习线性代数的过程中, 我们会遇到各种各样的矩阵分解方法, 这些分解方法可以帮助我们更好地理解矩阵的结构和性质. 以下是一些常见的矩阵分解方法:

### 满秩分解

**Recall**: 矩阵的标准型: 设$A$是一个$m \times n$的矩阵, 经过初等变换化为形如:
$$
A=\begin{pmatrix}
    E_r & O \\
    O & O
\end{pmatrix}
$$
则称$A$为矩阵的标准型.

**定义**: 设$A$是一个$m \times n$的矩阵, 如果存在一个$m \times r$的矩阵$B$和一个$r \times n$的矩阵$C$, 使得$A = BC$, 且$r$是$A$的秩, 则称$A$具有满秩分解.

我们当然不需要再额外要求$B$和$C$的秩, 因为如果$A=BC$且$r$是$A$的秩, 那么$B$和$C$的秩必然也是$r$.

**定理**: $A$经过初等变换化为Hermite标准型$H = \begin{pmatrix}
    H_r \\
    O
\end{pmatrix}$, 其中主元所在的列为$j_1 < j_2 < \ldots < j_r$, 那么:

$$
A = (A_{j_1}, A_{j_2}, \ldots, A_{j_r})H_r
$$

就是$A$的一个满秩分解.

也可以用下面的方式说明:

$$
A = P' \begin{pmatrix}
    E_r & O \\
    O & O
\end{pmatrix} Q'
= P' \begin{pmatrix}
    E_r \\
    O
\end{pmatrix} \begin{pmatrix}
    E_r & O
\end{pmatrix} Q'
= P \times Q
$$

**推导与证明**:

1. **初等行变换等价于左乘可逆矩阵**
矩阵 $A$ 经过一系列初等行变换化为 Hermite 标准型(行最简形) $H$，等价于存在一个可逆矩阵 $P$（初等矩阵的乘积），使得：
$$
PA = H = \begin{pmatrix} H_r \\ O \end{pmatrix}
$$
在两边同时左乘 $P^{-1}$，得到：
$$
A = P^{-1}H = P^{-1}\begin{pmatrix} H_r \\ O \end{pmatrix}
$$

1. **利用分块矩阵乘法展开**
我们将 $P^{-1}$ 按照列进行分块：前 $r$ 列记为 $P_1$，其余列记为 $P_2$，即 $P^{-1} = (P_1, P_2)$。  
代入上式，利用分块矩阵的乘法：
$$
A = (P_1, P_2)\begin{pmatrix} H_r \\ O \end{pmatrix} = P_1 H_r + P_2 O = P_1 H_r
$$

1. **确定 $P_1$ 的构成**
在行最简形矩阵 $H$ 中，主元所在的列 $j_1, j_2, \ldots, j_r$ 正好依次构成了单位矩阵的列向量 $e_1, e_2, \ldots, e_r$。
对于公式 $A = P^{-1}H$，它对矩阵的每一列都成立。因此，$A$ 的第 $j_k$ 列等于 $P^{-1}$ 乘以 $H$ 的第 $j_k$ 列：
$$
A_{j_k} = P^{-1} H_{j_k} = P^{-1} e_k
$$
根据矩阵乘法的性质，$P^{-1} e_k$ 提取出来的恰好是 $P^{-1}$ 的第 $k$ 列！
所以，$P^{-1}$ 的前 $r$ 列对应的就是 $A$ 的主元列 $A_{j_k}$。
也就是：
$$
P_1 = (A_{j_1}, A_{j_2}, \ldots, A_{j_r})
$$

将其代回 $A = P_1 H_r$，就得到了：
$$
A = (A_{j_1}, A_{j_2}, \ldots, A_{j_r})H_r
$$
由于 $A_{j_k}$ 都是原矩阵的线性无关列（列满秩），$H_r$ 是行最简形的非零行（行满秩），该式即为满秩分解。

### LU分解 (三角分解)

Alan Turing 在 1948 年提出了 LU 分解的概念, 该分解将一个矩阵分解为一个下三角矩阵和一个上三角矩阵的乘积. LU 分解在数值分析和计算机科学中有着广泛的应用, 特别是在求解线性方程组和计算行列式时.

LU分解本质上来自初等行变换获得Hermite标准型的过程.

**定义**: 对于一个 $n \times n$ 的矩阵 $A$, 如果存在一个下三角矩阵 (主对角线上的元素为1) $L$ 和一个上三角矩阵 $U$, 使得 $A = LU$, 则称 $A$ 具有 LU 分解.

**LU分解不唯一**

**定理**: 一个**可逆矩阵** $A$ 具有**唯一** LU 分解的充分必要条件是 $A$ 的所有顺序主子式都不为零.

如何计算 LU 分解呢? 我们可以使用高斯消元法来实现. 具体步骤如下:

1. **初始化**: 设 $L$ 为单位矩阵, $U$ 为零矩阵.
2. **消元过程**: 对于 $A$ 的每一列, 使用高斯消元法将其转换为上三角形式. 在这个过程中, 记录下每一步的消元系数, 将其存储在 $L$ 中.
3. **完成分解**: 当 $A$ 被转换为上三角矩阵 $U$ 后, $L$ 中存储的消元系数就构成了下三角矩阵. 最终, 我们得到了 $A = LU$ 的分解.

**结论**: 任何正定矩阵都具有 LU 分解.

由LU分解和上述结论可以直接推出下面这种分解形式:

#### Cholesky分解

**定义**(Cholesky分解): 对于一个正定矩阵 $A$, 如果存在一个主元为正数的下三角矩阵 $L$ 使得 $A = LL^T$, 则称 $A$ 具有 Cholesky 分解.

**定理**: 实正定矩阵存在唯一的 Cholesky 分解.

证明: 设 $A$ 是一个 $n \times n$ 的实正定矩阵, 由上面的定理我们不难知道$A$一定存在唯一的$LU$分解, 即存在一个下三角矩阵$L$和一个上三角矩阵$U$, 使得$A=LU$.

$$
A = LU = \begin{pmatrix}
    1 & &  \\
     & \ddots &  \\
    * & & 1
\end{pmatrix} \times \begin{pmatrix}
    u_{11} &  & * \\
     & \ddots & \\
     &  & u_{nn}
\end{pmatrix} = 
\begin{pmatrix}
    1 & &  \\
     & \ddots &  \\
    * & & 1
\end{pmatrix} \times \begin{pmatrix}
    u_{11} &  &  \\
     & \ddots & \\
     &  & u_{nn}
\end{pmatrix} \times
\begin{pmatrix}
    1 &  & * \\
     & \ddots & \\
     &  & 1
\end{pmatrix} = L' T U'
$$

由于$A$是正定矩阵, 且实对称, 取转置后根据LU分解的唯一性不难知道:

$$
L' = U'^T
$$

所以我们可以得到:

$$
A = L' T L'^T
=\begin{pmatrix}
    1 & &  \\
     & \ddots &  \\
    * & & 1
\end{pmatrix} \times \begin{pmatrix}
    \sqrt{u_{11}} &  &  \\
     & \ddots & \\
     &  & \sqrt{u_{nn}}
\end{pmatrix} \times
\begin{pmatrix}
    \sqrt{u_{11}} &  &  \\
     & \ddots & \\
     &  & \sqrt{u_{nn}}
\end{pmatrix} \times
\begin{pmatrix}
    1 &  & * \\
     & \ddots & \\
     &  & 1
\end{pmatrix} = G G^T
$$