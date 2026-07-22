# 线性代数 II

目录:

- [线性代数 II](#线性代数-ii)
  - [线性空间与线性变换](#线性空间与线性变换)
    - [子空间及其运算](#子空间及其运算)
      - [子空间上的运算](#子空间上的运算)
      - [子空间的性质](#子空间的性质)
      - [补子空间](#补子空间)
    - [线性变换与矩阵](#线性变换与矩阵)
      - [伴随变换](#伴随变换)
      - [投影变换](#投影变换)
      - [矩阵的张量积](#矩阵的张量积)
  - [方阵的Jordan标准型与零化多项式](#方阵的jordan标准型与零化多项式)
    - [方阵的Jordan标准型](#方阵的jordan标准型)
    - [方阵的零化多项式](#方阵的零化多项式)
    - [Jordan标准型的求法](#jordan标准型的求法)
  - [矩阵分解及其应用](#矩阵分解及其应用)
    - [矩阵的满秩分解](#矩阵的满秩分解)
    - [矩阵的QR分解与LU分解](#矩阵的qr分解与lu分解)
    - [矩阵的谱分解与三角分解](#矩阵的谱分解与三角分解)
    - [矩阵的奇异值分解](#矩阵的奇异值分解)
  - [向量范数](#向量范数)
  - [梯度矩阵](#梯度矩阵)

## 线性空间与线性变换

线性空间本质上就是配备了**向量加法**和**数乘**运算的集合. 向量加法和数乘运算满足八条公理, 满足这样的集合就可以称为**线性空间**. 对于线性空间中的元素, 我们称之为**向量**.

**定义**: 设$V$是一个非空集合, 定义在$V$上的向量加法和数乘运算满足以下八条公理:

1. **加法交换律**: 对任意 $\alpha, \beta \in V$, 有 $\alpha + \beta = \beta + \alpha$
2. **加法结合律**: 对任意 $\alpha, \beta, \gamma \in V$, 有 $(\alpha + \beta) + \gamma = \alpha + (\beta + \gamma)$
3. **存在零元素**: 存在元素 $\mathbf{0} \in V$, 使得对任意 $\alpha \in V$, 有 $\alpha + \mathbf{0} = \alpha$
4. **存在负元素**: 对任意 $\alpha \in V$, 存在元素 $-\alpha \in V$, 使得 $\alpha + (-\alpha) = \mathbf{0}$
5. **数乘结合律**: 对任意纯量 $k, m$ 及 $\alpha \in V$, 有 $k(m\alpha) = (km)\alpha$
6. **数乘单位元**: 对任意 $\alpha \in V$, 有 $1\alpha = \alpha$（$1$ 为纯量数域的单位元）
7. **数乘分配律**（纯量乘法对因数加法的分配律）: 对任意纯量 $k, m$ 及 $\alpha \in V$, 有 $(k + m)\alpha = k\alpha + m\alpha$
8. **数乘分配向量律**（纯量乘法对向量加法的分配律）: 对任意纯量 $k$ 及 $\alpha, \beta \in V$, 有 $k(\alpha + \beta) = k\alpha + k\beta$

满足上述八条公理的集合 $V$ 就称为**线性空间**.

### 子空间及其运算

**定义**: 设 $V$ 是一个线性空间, 如果 $W$ 是 $V$ 的一个子集, 且 $W$ 本身也是一个线性空间, 也配备有上述两种运算且满足线性空间的公理, 则称 $W$ 是 $V$ 的一个**子空间**.

线性空间$V$的非空子集$L$构成子空间的充分必要条件是: $L$对于$V$中给定的线性运算封闭.

#### 子空间上的运算

- **子空间的和**: 设 $W_1$ 和 $W_2$ 是线性空间 $V$ 的两个子空间, 则它们的和定义为 $W_1 + W_2 = \{ w_1 + w_2 \mid w_1 \in W_1, w_2 \in W_2 \}$.

- **子空间的交**: 设 $W_1$ 和 $W_2$ 是线性空间 $V$ 的两个子空间, 则它们的交定义为 $W_1 \cap W_2 = \{ w \in V \mid w \in W_1 \text{ 且 } w \in W_2 \}$.

  **定理**: 设 $W_1$ 和 $W_2$ 是线性空间 $V$ 的两个子空间, 则 $W_1 + W_2$ 和 $W_1 \cap W_2$ 都是 $V$ 的子空间. 证明略

- **子空间的直和**: 设 $W_1$ 和 $W_2$ 是线性空间 $V$ 的两个子空间, 如果 $W_1 \cap W_2 = \{ \mathbf{0} \}$, 则称 $W_1$ 和 $W_2$ 的和是它们的**直和**, 记为 $W_1 \oplus W_2$.

  特别的, 当 $W_1$ 和 $W_2$ 是 $V$ 的两个子空间, 且 $V = W_1 \oplus W_2$, 则称 $V$ 是 $W_1$ 和 $W_2$ 的**直和**.

**定理**: 若$V$是数域$F$上的线性空间, $U$ 和 $W$ 是 $V$ 的两个子空间, 则下述四个命题等价:

1. $U \oplus W$.
2. $U\oplus W$中任意元素都存在如下唯一分解式:
  $$v = u + w, \quad u \in U, w \in W$$
3. 零向量分解唯一.
4. $U$和$W$的一组基合起来构成$U+W$的一组基.

下面给出证明:

(1) $\Rightarrow$ (2):

设 $v \in U \oplus W$, 则存在 $u \in U$ 和 $w \in W$, 使得 $v = u + w$. 假设存在另一组分解式 $v = u' + w'$, 其中 $u' \in U$ 和 $w' \in W$. 则有:
$$u+ w = u' + w' \Rightarrow u - u' = w' - w$$

由于 $U$ 和 $W$ 的交只有零向量, 所以 $u - u' = \mathbf{0}$ 和 $w' - w = \mathbf{0}$, 从而 $u = u'$ 和 $w = w'$. 因此分解式唯一.

(2) $\Rightarrow$ (3):

由于$0+0=0$显然成立, 假设存在另一组分解式 $0 = u + w$, 其中 $u \in U$ 和 $w \in W$. 则有:
$$0 = u + w \Rightarrow u = -w$$

由于 $U$ 和 $W$ 的交只有零向量, 所以 $u = \mathbf{0}$ 和 $w = \mathbf{0}$. 因此零向量分解唯一.

(3) $\Rightarrow$ (4):

先证明 $B_U \cup B_W$ 是 $U + W$ 的一组生成元. 设 $v \in U + W$, 则存在 $u \in U$ 和 $w \in W$, 使得 $v = u + w$. 由于 $B_U$ 和 $B_W$ 分别是 $U$ 和 $W$ 的一组基, 则存在 $B_U$ 中元素的线性组合等于 $u$, 存在 $B_W$ 中元素的线性组合等于 $w$. 因此, 存在 $B_U \cup B_W$ 中元素的线性组合等于 $v$. 从而, $B_U \cup B_W$ 是 $U + W$ 的一组生成元.

设 $B_U$ 和 $B_W$ 分别是 $U$ 和 $W$ 的一组基. 假设 $B_U \cup B_W$ 不是 $U + W$ 的一组基, 则存在 $v \in U + W$, 使得 $v$ 可以表示为 $B_U \cup B_W$ 中元素的两种不同线性组合. 设:
$$v = \sum_{i=1}^m a_i u_i + \sum_{j=1}^n b_j w_j = \sum_{i=1}^m a'_i u_i + \sum_{j=1}^n b'_j w_j$$
其中 $u_i \in B_U$ 和 $w_j \in B_W$. 则有:
$$\sum_{i=1}^m (a_i - a'_i) u_i = \sum_{j=1}^n (b'_j - b_j) w_j$$

由于 $B_U$ 和 $B_W$ 分别是 $U$ 和 $W$ 的一组基, 则 $a_i - a'_i = 0$ 和 $b'_j - b_j = 0$. 从而, $v$ 可以表示为 $B_U \cup B_W$ 中元素的唯一线性组合. 矛盾. 因此, $B_U \cup B_W$ 是 $U + W$ 的一组基.

(4) $\Rightarrow$ (1):

设 $B_U$ 和 $B_W$ 分别是 $U$ 和 $W$ 的一组基, 且 $B_U \cup B_W$ 是 $U + W$ 的一组基. 则 $B_U \cup B_W$ 中元素的线性组合可以表示 $U + W$ 中的任意元素.

设 $v \in U + W$, 则存在 $u \in U$ 和 $w \in W$, 使得 $v = u + w$. 由于 $B_U$ 和 $B_W$ 分别是 $U$ 和 $W$ 的一组基, 则存在 $B_U$ 中元素的线性组合等于 $u$, 存在 $B_W$ 中元素的线性组合等于 $w$. 因此, 存在 $B_U \cup B_W$ 中元素的线性组合等于 $v$. 从而, $U + W = U \oplus W$.

证明完毕.

**推广定义**: 设 $V$ 是一个线性空间, 如果 $V$ 可以表示为 $V = W_1 \oplus W_2 \oplus \cdots \oplus W_k$, 其中 $W_i$ 是 $V$ 的子空间, 且 $W_i \cap \sum_{j=1}^{i-1} W_j = \{ \mathbf{0} \}$ 对任意 $i \neq j$, 则称 $V$ 是 $W_1, W_2, \ldots, W_k$ 的**直和**. 记作:

$$\oplus_{i=1}^k W_i = W_1 \oplus W_2 \oplus \cdots \oplus W_k$$

**注意**: 仅满足$W_i \cap W_j = \{ \mathbf{0} \}$对任意$i \neq j$并不足以令$V = W_1 \oplus W_2 \oplus \cdots \oplus W_k$.

同理, 对于多个子空间的直和, 我们也有如下等价的四个命题:

1. $\oplus_{i=1}^k W_i$.
2. $\oplus_{i=1}^k W_i$中任意元素都存在如下唯一分解式:
  $$v = w_1 + w_2 + \cdots + w_k, \quad w_i \in W_i$$
3. 零向量分解唯一.
4. $W_i$ 的一组基合起来构成 $\oplus_{i=1}^k W_i$ 的一组基.

证明从略, 基本思路是一致的, 实在不行就递归.

#### 子空间的性质

**维数公式**: 设 $V$ 是一个线性空间, $U$ 和 $W$ 是 $V$ 的两个子空间, 则有如下维数公式:
$$\dim(U + W) = \dim(U) + \dim(W) - \dim(U \cap W)$$

**证明**: 
设 $\dim(U \cap W) = r$, $\dim(U) = n$, $\dim(W) = m$.
首先取 $U \cap W$ 的一组基 $\alpha_1, \alpha_2, \cdots, \alpha_r$.
由于 $U \cap W \subseteq U$, 我们可以将这组基扩充为 $U$ 的一组基: $\alpha_1, \cdots, \alpha_r, \beta_1, \cdots, \beta_{n-r}$.
同理, 因为 $U \cap W \subseteq W$, 我们也可以将其扩充为 $W$ 的一组基: $\alpha_1, \cdots, \alpha_r, \gamma_1, \cdots, \gamma_{m-r}$.

接下来证明向量组 $\alpha_1, \cdots, \alpha_r, \beta_1, \cdots, \beta_{n-r}, \gamma_1, \cdots, \gamma_{m-r}$ 是 $U + W$ 的一组基.

**第一步, 证明生成性**:
任取 $v \in U + W$, 则存在 $u \in U$ 和 $w \in W$ 使得 $v = u + w$. 由于 $u$ 可由 $\alpha_i, \beta_j$ 线性表出, $w$ 可由 $\alpha_i, \gamma_k$ 线性表出, 因此 $v = u + w$ 显然可以由这组向量线性综合表示. 也就是说它们生成了 $U + W$.

**第二步, 证明线性无关**:
假设存在一组系数使其线性组合为零向量:
$$k_1\alpha_1 + \cdots + k_r\alpha_r + l_1\beta_1 + \cdots + l_{n-r}\beta_{n-r} + p_1\gamma_1 + \cdots + p_{m-r}\gamma_{m-r} = \mathbf{0}$$
移项可得:
$$p_1\gamma_1 + \cdots + p_{m-r}\gamma_{m-r} = -(k_1\alpha_1 + \cdots + k_r\alpha_r + l_1\beta_1 + \cdots + l_{n-r}\beta_{n-r})$$
上式左边是 $W$ 中的向量, 右边是 $U$ 中的向量. 既然它们相等, 那么这个向量一定属于它们的交集 $U \cap W$.
既然属于 $U \cap W$, 就可以由 $U \cap W$ 的基线性表出, 即存在常数 $c_1, \cdots, c_r$ 使得:
$$p_1\gamma_1 + \cdots + p_{m-r}\gamma_{m-r} = c_1\alpha_1 + \cdots + c_r\alpha_r$$
也即:
$$c_1\alpha_1 + \cdots + c_r\alpha_r - p_1\gamma_1 - \cdots - p_{m-r}\gamma_{m-r} = \mathbf{0}$$
因为 $\alpha_1, \cdots, \alpha_r, \gamma_1, \cdots, \gamma_{m-r}$ 是 $W$ 的基, 是线性无关的, 所以这所有的系数必然都为 $0$. 特别地, 有 $p_1 = \cdots = p_{m-r} = 0$.
将 $p$ 皆为 $0$ 代回第一条等式, 得到:
$$k_1\alpha_1 + \cdots + k_r\alpha_r + l_1\beta_1 + \cdots + l_{n-r}\beta_{n-r} = \mathbf{0}$$
同理, 因为 $\alpha_1, \cdots, \alpha_r, \beta_1, \cdots, \beta_{n-r}$ 是 $U$ 的基, 同样线性相关, 因此系数也全为零: $k_1 = \cdots = k_r = 0$, $l_1 = \cdots = l_{n-r} = 0$.
由所有的组合系数 $(k, l, p)$ 都等于 $0$, 我们就证明了这 $r + (n-r) + (m-r)$ 个向量组成的并集是线性无关的.

综上所述, 这组向量是 $U + W$ 的基. 于是:
$$\dim(U + W) = r + (n-r) + (m-r) = n + m - r = \dim(U) + \dim(W) - \dim(U \cap W)$$

证明完毕.

**推论**: 设 $V$ 是一个线性空间, $U$ 和 $W$ 是 $V$ 的两个子空间, 若$V = U \oplus W$, 则:

$$\dim(V) = \dim(U) + \dim(W)$$

#### 补子空间

**定义**: 设 $V$ 是一个线性空间, $U$ 是 $V$ 的一个子空间, 如果存在 $V$ 的另一个子空间 $W$, 使得 $V = U \oplus W$, 则称 $W$ 是 $U$ 在 $V$ 中的一个**补子空间**.

对于定义了**内积**的线性空间, 我们可以定义**正交补**.

**定义**: 设 $V$ 是一个内积空间, $U$ 是 $V$ 的一个子空间, 则称 $U$ 的**正交补**为:
$$U^\perp = \{ v \in V \mid \langle u, v \rangle = 0, \forall u \in U \}$$

**定理**: 设 $V$ 是一个内积空间, $U$ 是 $V$ 的一个子空间, 则 $V = U \oplus U^\perp$.

**证明**:

1. **证明 $U \cap U^\perp = \{ \mathbf{0} \}$**:

设 $v \in U \cap U^\perp$, 则 $v \in U$ 且 $v \in U^\perp$. 
根据正交补的定义，既然 $v \in U^\perp$, 它应该与 $U$ 中的所有向量正交，当然也包括它自己。
所以 $\langle v, v \rangle = 0$. 由于内积的正定性, 这说明只能有 $v = \mathbf{0}$. 因此, $U \cap U^\perp = \{ \mathbf{0} \}$.

2. **证明 $U + U^\perp = V$**:

这里以有限维空间为例。设 $\dim(U) = k$, 并取 $U$ 的一组标准正交基 $e_1, e_2, \cdots, e_k$.
任取 $v \in V$, 我们提取它在子空间 $U$ 上的正交投影，构造如下向量 $u$:
$$u = \sum_{i=1}^k \langle v, e_i \rangle e_i$$
由于 $e_1, \cdots, e_k \in U$, 显然有 $u \in U$.
现令 $w = v - u$, 接下来我们需要证明 $w \in U^\perp$.
对于 $U$ 基底中的任意一个向量 $e_j$ ($1 \le j \le k$), 计算它与 $w$ 的内积:
$$\langle w, e_j \rangle = \langle v - u, e_j \rangle = \langle v, e_j \rangle - \left\langle \sum_{i=1}^k \langle v, e_i \rangle e_i, e_j \right\rangle$$
由于 $e_1, \cdots, e_k$ 是标准正交基，即当 $i \neq j$ 时 $\langle e_i, e_j \rangle = 0$，当 $i = j$ 时 $\langle e_j, e_j \rangle = 1$。所以求和项中只有 $i=j$ 的项保留了下来：
$$\langle w, e_j \rangle = \langle v, e_j \rangle - \langle v, e_j \rangle \langle e_j, e_j \rangle = \langle v, e_j \rangle - \langle v, e_j \rangle = 0$$
既然 $w$ 垂直于 $U$ 的所有基向量，那么由内积的线性性质，它一定垂直于 $U$ 中的任意向量。这就证明了 $w \in U^\perp$.
因此，对于任意的 $v \in V$，都可以分解为 $v = u + w$，其中 $u \in U$, $w \in U^\perp$。即 $U + U^\perp = V$.

综合 1 和 2，由直和等价命题可知 $V = U \oplus U^\perp$. 证明完毕.

**注意**: 补空间不一定唯一, 因为基的选取不唯一. 但正交补是唯一的.

**正交投影**: 设 $V$ 是一个内积空间, $U$ 是 $V$ 的一个子空间, 则对于任意 $v \in V$, 存在唯一的分解式 $v = u + w$, 其中 $u \in U$ 和 $w \in U^\perp$. 其中 $u$ 就是 $v$ 在子空间 $U$ 上的**正交投影**. 记作$P_U(v) = u$.

正交投影可以这样给出: 设$\eta_1, \cdots, \eta_k$是$U$的一组标准正交基, 则对于任意$v \in V$, $v$在$U$上的正交投影为:
$$P_U(v) = \sum_{i=1}^k \langle v, \eta_i \rangle \eta_i$$

### 线性变换与矩阵

**定义**: 设$V$和$W$是数域$F$上的线性空间, $\sigma$是$V$到$W$的映射, 如果对于任意的$\alpha, \beta \in V$和任意的常数$k \in F$, 都满足以下两个条件:
1. $\sigma(\alpha + \beta) = \sigma(\alpha) + \sigma(\beta)$
2. $\sigma(k\alpha) = k\sigma(\alpha)$

那么我们称$\sigma$是一个**线性变换**, 也称为**线性映射**.


伴随着线性变换, 我们可以定义线性变换的**核**和**像**:
- **核**: 线性变换$\sigma$的核是指所有被$\sigma$映射到零向量的向量集合, 记为$\text{Ker}(\sigma) = \{\alpha \in V | \sigma(\alpha) = 0\}$.
- **像**: 线性变换$\sigma$的像是指所有可以被$\sigma$映射到的向量集合, 记为$\text{Im}(\sigma) = \{\sigma(\alpha) | \alpha \in V\}$.

**定理** $\text{Im}(\sigma)$是$W$的子空间, $\text{Ker}(\sigma)$是$V$的子空间.

这个定理的证明非常简单, 只需要验证$\text{Im}(\sigma)$和$\text{Ker}(\sigma)$满足子空间的定义即可. 但是任何一个**线性变换**的**核**和**像**是其核心特征, 很多时候我们研究线性变换, 就是为了研究它的核和像.

**定义**: 针对**核**和**像**, 我们可以定义**秩**和**零度**:
- **秩**: 线性变换$\sigma$的秩是指$\text{Im}(\sigma)$的维数, 记为$\text{rank}(\sigma) = \dim(\text{Im}(\sigma))$.
- **零度**: 线性变换$\sigma$的零度是指$\text{Ker}(\sigma)$的维数, 记为$\text{nullity}(\sigma) = \dim(\text{Ker}(\sigma))$.

**定理**: 设$V$和$W$是数域$F$上的线性空间, $\sigma: V \to W$是一个线性变换, 则有以下关系:
$$\text{rank}(\sigma) + \text{nullity}(\sigma) = \dim(V)$$

这个定理被称为**秩-零度定理**, 它揭示了线性变换的秩和零度之间的关系, 以及它们与定义域的维数之间的关系. 这个定理是线性代数中非常重要的一个定理, 它揭示了线性变换的一个**守恒结构**.

上面所有的线性变换都是对抽象而虚无缥缈的线性空间的讨论, 但是实际上我们经常(事实上总是)需要讨论具体的线性变换. 而我们在具象化一个抽象的线性空间的时候, 总是通过把它**向量**化来实现的. 也就是说, 我们把一个抽象的线性空间$V$中的每个元素$\alpha$都看作是一个向量$\vec{v}$, 这样我们就可以把线性变换$\sigma: V \to W$看作是一个**向量到向量**的映射. 而对于向量到向量的**变换**, 我们自然就会采用**矩阵**来表示它. 也就是说, 我们把线性变换$\sigma$看作是一个矩阵$A$, 这样我们就可以通过矩阵乘法来计算线性变换的结果.

具体来说, 考虑一个线性变换$\sigma: V \to W$, 其中$V$和$W$分别是维数为$n$和$m$的线性空间. 我们可以选择$V$中的一个基$\{\vec{v_1}, \vec{v_2}, \ldots, \vec{v_n}\}$和$W$中的一个基$\{\vec{w_1}, \vec{w_2}, \ldots, \vec{w_m}\}$. 那么对于每个基向量$\vec{v_i}$, 线性变换$\sigma$会将它映射到$W$中的一个向量$\sigma(\vec{v_i})$, 这个向量可以表示为$W$中的基向量的线性组合:
$$\sigma(\vec{v_i}) = a_{1i}\vec{w_1} + a_{2i}\vec{w_2} + \ldots + a_{mi}\vec{w_m}$$
其中$a_{ji}$是一个数, 表示$\sigma(\vec{v_i})$在$W$中的第$j$个基向量$\vec{w_j}$上的系数. 这样我们就可以把线性变换$\sigma$表示为一个$m \times n$的矩阵$A$, 其中第$j$行第$i$列的元素就是$a_{ji}$:
$$A = \begin{bmatrix}a_{11} & a_{12} & \ldots & a_{1n} \\a_{21} & a_{22} & \ldots & a_{2n} \\\vdots & \vdots & \ddots & \vdots \\a_{m1} & a_{m2} & \ldots & a_{mn}\end{bmatrix}$$
这样我们就可以通过矩阵乘法来计算线性变换的结果. 例如, 对于一个向量$\vec{v} = x_1\vec{v_1} + x_2\vec{v_2} + \ldots + x_n\vec{v_n}$, 线性变换$\sigma$的结果就是:
$$\sigma(\vec{v}) = A \begin{bmatrix}x_1 \\x_2 \\\vdots \\x_n\end{bmatrix}=Ax$$
通过这个具体化的过程, 我们就可以把抽象的线性变换表示为具体的矩阵形式.

由此, 我们真的为所有的线性变换, 用任意的假设, 提供了一个具体的表示方法, 即利用矩阵来表示线性变换. 现在我们继续把上面关于线性变换的性质, 例如核和像, 秩和零度, 单射和满射, 都用矩阵的语言来重新表述一下.

1. **核**: 线性变换$\sigma$的核就是矩阵$A$的**零空间**, 也就是说, 核中的向量$\vec{v}$满足$A\vec{v} = \vec{0}$.
2. **像**: 线性变换$\sigma$的像就是矩阵$A$的**列空间**, 也就是说, 像中的向量$\vec{w}$满足$\vec{w} = A\vec{v}$对于某个$\vec{v}$.
3. **秩**: 线性变换$\sigma$的秩就是矩阵$A$的**列秩**, 也就是说, 秩是矩阵$A$的列空间的维数.
4. **零度**: 线性变换$\sigma$的零度就是矩阵$A$的**零空间**的维数.
5. **单射**: 线性变换$\sigma$是单射, 如果矩阵$A$的零空间只有零向量, 也就是说, $A\vec{v} = \vec{0}$只有$\vec{v} = \vec{0}$这个解.
6. **满射**: 线性变换$\sigma$是满射, 如果矩阵$A$的列空间等于整个值域空间$W$, 也就是说, $A\vec{v}$可以得到$W$中的任意向量.
7. **秩-零度定理**: 线性变换$\sigma$的秩加上零度等于定义域的维数, 也就是说, $\text{rank}(A) + \text{nullity}(A) = n$, 其中$n$是定义域$V$的维数.

下面介绍几种特殊的线性变换, 以及它们在矩阵中的表示.

#### 伴随变换

**定义**: 设$V$和$W$是数域$F$上的内积空间, $\sigma: V \to W$是一个线性变换, 如果存在一个线性变换$\sigma^*: W \to V$, 使得对于任意的$\alpha \in V$和$\beta \in W$, 都满足以下条件:
$$\langle \sigma(\alpha), \beta \rangle = \langle \alpha, \sigma^*(\beta) \rangle$$
那么我们称$\sigma^*$是$\sigma$的**伴随变换**, 也称为**伴随映射**.

当我们选定具体的基之后, **伴随变换**$\sigma^*$就对应于矩阵$A$的**共轭转置**$A^*$, 也就是说, $\sigma^*$对应于矩阵$A^*$, 其中$A^* = \overline{A^T}$, $\overline{A}$表示矩阵$A$的共轭, $T$表示矩阵的转置. 伴随变换$\sigma^*$的定义就是为了满足内积的关系, 因此它具有一些特殊的性质, 例如:

1. $\sigma^{**} = \sigma$, 也就是说, 伴随变换的伴随变换就是它自己.
2. $(\tau \circ \sigma)^* = \sigma^* \circ \tau^*$
3. 如果$\sigma$是单射, 则$\sigma^*$是满射; 如果$\sigma$是满射, 则$\sigma^*$是单射.

最后, 让我们先对先前的结论**伴随变化**对应于矩阵的**共轭转置**给出证明.

**定理**: 设$A,B$分别为线性变换$\sigma$和$\tau$在某组标准正交基下的矩阵表示, 则有:

$$\tau = \sigma^* \leftrightarrow B = A^*$$

**证明**:

$\Rightarrow$: 假设$\alpha_1, \alpha_2, \ldots, \alpha_n$是$V$的一组标准正交基, 那么, $\sigma(\alpha_1, \alpha_2, \ldots, \alpha_n) = (\alpha_1, \alpha_2, \ldots, \alpha_n)A$, $\tau(\alpha_1, \alpha_2, \ldots, \alpha_n) = (\alpha_1, \alpha_2, \ldots, \alpha_n)B$.

我们任意选取$i,j \in \{1,2,\ldots,n\}$, 那么:
$$\langle \sigma(\alpha_i), \alpha_j \rangle = \langle \sum_{k=1}^n a_{ki} \alpha_k, \alpha_j \rangle  = a_{ji} = \langle \alpha_i, \sum_{k=1}^n b_{kj} \alpha_k \rangle = b_{ij}$$

所以, $B = A^*$.

$\Leftarrow$: 显然, 不加证明, 简单推导即可得到.

#### 投影变换

**定义**: 设$V$是数域$F$上的线性空间, $W$是$V$的一个子空间, 则对于任意的$v \in V$, 存在唯一的分解式$v = w + w'$, 其中$w \in W$和$w' \in W^\perp$. 那么我们可以定义一个线性变换$\sigma: V \to V$, 使得对于任意的$v \in V$, 都满足$\sigma(v) = w$. 这个线性变换$\sigma$就称为**投影变换**.

显然, 投影变换$\sigma$满足$\sigma^2 = \sigma$, 也就是说, 投影变换是一个幂等变换. 反过来说, 如果一个线性变换$\sigma$满足$\sigma^2 = \sigma$, 那么它就是一个投影变换. 也就是说, 投影变换的定义等价于幂等变换的定义.

**证明**:

**必要性 ($\Rightarrow$)**: 
设 $\sigma$ 是一个投影变换。则对于任意的 $v \in V$, 基于子空间的直和分解, 存在唯一的分解式 $v = w + w'$, 其中 $w \in W$ 和 $w' \in W'$. 根据定义有 $\sigma(v) = w$. 
对于提取出的向量 $w$, 由于 $w \in W$, 它所对应的唯一分解就是 $w = w + \mathbf{0}$. 因此 $\sigma(w) = w$.
于是有:
$$\sigma^2(v) = \sigma(\sigma(v)) = \sigma(w) = w = \sigma(v)$$
这说明 $\sigma^2 = \sigma$ 恒成立。

**充分性 ($\Leftarrow$)**: 
若线性变换 $\sigma$ 是幂等变换，满足 $\sigma^2 = \sigma$.
我们要证明 $V$ 可作直和分解，且 $\sigma$ 刚好是对应的投影变换。
令像空间 $W_1 = \text{Im}(\sigma) = \{\sigma(v) \mid v \in V\}$，核空间 $W_2 = \text{Ker}(\sigma) = \{v \in V \mid \sigma(v) = \mathbf{0}\}$.
对于任意的 $v \in V$, 可以将其恒等拆分为两部分:
$$v = \sigma(v) + (v - \sigma(v))$$
显然第一项 $\sigma(v) \in W_1$. 对于第二项，我们计算它的像:
$$\sigma(v - \sigma(v)) = \sigma(v) - \sigma^2(v) = \sigma(v) - \sigma(v) = \mathbf{0}$$
这说明第二项被 $\sigma$ 映射为零，即 $v - \sigma(v) \in \text{Ker}(\sigma) = W_2$. 因此 $V = W_1 + W_2$.
接下来证明是直和：若任取 $x \in W_1 \cap W_2$. 因为 $x \in W_1$, 存在某 $y \in V$ 使得 $x = \sigma(y)$. 又因 $x \in W_2$, 所以必有 $\sigma(x) = \mathbf{0}$.
结合两者得: $\mathbf{0} = \sigma(x) = \sigma(\sigma(y)) = \sigma^2(y) = \sigma(y) = x$. 这证明了 $W_1 \cap W_2 = \{\mathbf{0}\}$.
这说明 $V$ 的确可以分解为直和 $V = W_1 \oplus W_2$.
且对于分解 $v = \underbrace{\sigma(v)}_{\in W_1} + \underbrace{(v - \sigma(v))}_{\in W_2}$，映射 $\sigma$ 恰好作用并提取了它在 $W_1$ 中的分量，该形式完全契合投影变换的定义。证明完毕。

#### 矩阵的张量积

## 方阵的Jordan标准型与零化多项式

### 方阵的Jordan标准型

### 方阵的零化多项式

### Jordan标准型的求法

## 矩阵分解及其应用

### 矩阵的满秩分解

### 矩阵的QR分解与LU分解

### 矩阵的谱分解与三角分解

### 矩阵的奇异值分解

## 向量范数

## 梯度矩阵