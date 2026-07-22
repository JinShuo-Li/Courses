# 数学分析期中

范围: 函数项级数$\to$多元函数的微分学

时间: 2026年4月29日

作者: 李谨硕

## 函数项级数

函数项级数是指由一列函数项组成的级数, 形式为:
$$S(x) = \sum_{n=1}^{\infty} u_n(x)$$



### 敛散性

在开始具体的数学推导之前, 让我们先思考一个直观的问题：为什么我们要研究函数项级数？

答案在于我们希望将简单函数的良好性质(例如连续、可导、可积)“传递”给稍微复杂的函数组合. 这就是为什么我们要研究**收敛性**——它使得这种“传递”成为可能. 

在这里, 我们将像探险一样, 从最基本的点态收敛出发, 逐步发现它的缺陷, 并最终引出更强大的工具：一致收敛. 

#### 点态收敛

让我们从最自然的直觉开始. 既然函数项级数在每一个具体的点上都会退化成普通的数项级数, 那我们为什么不逐点考察它的行为呢？这就是**点态收敛**的思想. 

**点态收敛**: 如果对于一个固定的$x_0\in E$, 若*数项级数*$\sum_{n=1}^{\infty} u_n(x_0)$收敛, 则称函数项级数在$x_0$点态收敛. $x_0$称为函数项级数的收敛点.

- 全体收敛点的集合称为函数项级数的**收敛域**, 记为$D$.
- 定义在收敛域上的函数$S(x) = \sum_{n=1}^{\infty} u_n(x)$称为函数项级数的**和函数**. 我们称$\sum_{n=1}^{\infty} u_n(x)$在$D$上点态收敛于$S(x)$.
- 给出一个函数项级数, 可以作出它的**部分和函数**$S_n(x) = \sum_{k=1}^{n} u_k(x)$, 则函数项级数在$x_0$点态收敛于$S(x_0)$等价于$\lim_{n\to\infty} S_n(x_0) = S(x_0)$.

点态收敛不保证可以维持函数的诸多**分析性质**.



#### 一致收敛

点态收敛时, 各个点之间的收敛速度可能**大相径庭**, 这就导致了函数项级数的和函数可能无法保持连续性、可微性等分析性质. 因此, 我们引入了**一致收敛**的概念. 我们将会**迫使**函数项级数在每个点上以**相近的速度**收敛, 从而保证和函数的分析性质.

回顾点态收敛的定义, 我们实际上想要表达的是:

$$
\forall \epsilon > 0, \exists N(x_0, \epsilon) \in \mathbb{N}^*, \text{s.t.} \forall n > N(x_0, \epsilon), |S_n(x_0) - S(x_0)| < \epsilon
$$

在点态收敛中, $N$是 **依赖于$x_0$** 的. 这就导致了不同的点可能有不同的收敛速度. 为了保证函数项级数在每个点上以相近的速度收敛, 我们需要**去掉**$N$对$x_0$的依赖, 从而得到一致收敛的定义:

**一致收敛**: 如果对于任意$\epsilon > 0$, 存在$N(\epsilon) \in \mathbb{N}^*$, 使得对于所有$n > N(\epsilon)$和所有$x \in D$, 都有$|S_n(x) - S(x)| < \epsilon$, 则称函数项级数在$D$上一致收敛于$S(x)$.

用类似的数理逻辑的语言来表达一致收敛的定义, 可以写成:
$$
\forall \epsilon > 0, \exists N(\epsilon) \in \mathbb{N}^*, \text{s.t.} \forall n > N(\epsilon), \forall x \in D, |S_n(x) - S(x)| < \epsilon
$$

换言之, $N$的选取**不依赖于$x$**, 这就保证了函数项级数在每个点上以相近的速度收敛.

由上述定义我们可以直接得到如下推论:

**推论**: 若函数项级数$\sum_{n=1}^{\infty} u_n(x)$在$D$上一致收敛, 则函数项序列$\{u_n(x)\}$在$D$上一致收敛于0.

然而一致收敛是一个过强的条件, 因此我们引入了**内闭一致收敛**的概念. 内闭一致收敛只要求函数项级数在$D$的每个**闭区间**上以相近的速度收敛, 从而保证和函数在$D$的每个内点上保持连续性、可微性等分析性质.

**内闭一致收敛**: 若对于任意$[a,b] \subset D$, 函数项级数$\sum_{n=1}^{\infty} u_n(x)$在$[a,b]$上一致收敛, 则称函数项级数在$D$上内闭一致收敛.

一致收敛有两个等价的充要条件:

- 设函数项序列$\{S_n(x)\}$在$D$上一致收敛于$S(x)$, 定义$S_n(x)$和$S(x)$之间的距离为:
$$d(S_n, S) = \sup_{x \in D} |S_n(x) - S(x)|$$
则函数项级数$\sum_{n=1}^{\infty} u_n(x)$在$D$上一致收敛于$S(x)$当且仅当:
$$\lim_{n\to\infty} d(S_n, S) = 0$$
本定理的证明非常简单, 直接利用一致收敛的定义即可. 这里从略.

$\boxed{\text{Q.E.D.}}$

- 设函数项序列$\{S_n(x)\}$在$D$上点态收敛于$S(x)$, 那么函数项级数$\sum_{n=1}^{\infty} u_n(x)$在$D$上一致收敛于$S(x)$当且仅当对于任意数列$\{x_n\},x_n \in D$且:
$$
\lim_{n\to\infty} (S_n(x_n) - S(x_n)) = 0
$$
下面给出该定理的证明.  
**必要性**: 通过上一个等价条件的定义, 可以直接得到充分性.
**充分性**: 反证法.   
即假设函数项级数$\sum_{n=1}^{\infty} u_n(x)$在$D$上不一致收敛于$S(x)$.
$$
\exists \epsilon_0 > 0, \forall N >0, \exists n > N, \exists x \in D, \text{s.t.} |S_n(x) - S(x)| \geq \epsilon_0
$$
我们依次取$N=1,2,3,\cdots$, 可以得到数列$\{n_k\}$和$\{x_k\}$, 使得对于任意$k \in \mathbb{N}^*$, 都有$|S_{n_k}(x_k) - S(x_k)| \geq \epsilon_0$. 从而得到数列$\{x_n\}$, 使得对于任意$k \in \mathbb{N}^*$, 都有$|S_{n_k}(x_k) - S(x_k)| \geq \epsilon_0$. 从而得到:
$$\lim_{n\to\infty} (S_n(x_n) - S(x_n)) \neq 0$$
与充分性矛盾. 因此函数项级数$\sum_{n=1}^{\infty} u_n(x)$在$D$上一致收敛于$S(x)$.   
本定理常用于说明函数项级数不一致收敛.



#### 一致收敛级数的判别

1. Cauchy一致收敛判别法
函数项级数$\sum_{n=1}^{\infty} u_n(x)$在$D$上一致收敛的充分必要条件是, 对于任意$\epsilon > 0$, 存在$N(\epsilon) \in \mathbb{N}^*$, 使得:
$$
\left| u_{n+1}(x) + u_{n+2}(x) + \cdots + u_{n+p}(x) \right| < \epsilon, \forall n > N(\epsilon), \forall p \in \mathbb{N}^*, \forall x \in D
$$
证明与其他Cauchy判别法类似, 这里从略.

$\boxed{\text{Q.E.D.}}$

2. Weierstrass 判别法
设函数项级数$\sum_{n=1}^{\infty} u_n(x)$满足$|u_n(x)| \leq a_n$对于所有$n \in \mathbb{N}^*$和所有$x \in D$, 其中$\sum_{n=1}^{\infty} a_n$是一个收敛的数项级数, 则函数项级数$\sum_{n=1}^{\infty} u_n(x)$在$D$上一致收敛.
证明: 直接利用Cauchy一致收敛判别法即可. 这里从略.

$\boxed{\text{Q.E.D.}}$

3. A-D判别法
若函数项级数$\sum_{n=1}^{\infty} a_n(x)\cdot b_n(x)$满足下面两个条件之一, 则函数项级数$\sum_{n=1}^{\infty} a_n(x)\cdot b_n(x)$在$D$上一致收敛.
- $a_n(x)$在$D$上对固定的$x$, 随着$n$的增大单调, 且一致有界. 且函数项级数$\sum_{n=1}^{\infty} b_n(x)$在$D$上一致收敛.
- $a_n(x)$在$D$上对固定的$x$, 随着$n$的增大单调, 且一致收敛于0. 且函数项级数$\sum_{n=1}^{\infty} b_n(x)$在$D$上一致有界.
这里的证明需要用到Abel引理, 即:
**Abel引理**: 设数列$\{a_n\}$满足对于任意$n \in \mathbb{N}^*$, 都有$|a_n| \leq M$且对于任意$n \in \mathbb{N}^*$, 都有$a_{n+1} \leq a_n$. 设数列$\{b_n\}$满足对于任意$n \in \mathbb{N}^*$, 都有$|b_1 + b_2 + \cdots + b_n| \leq N$. 则对于任意$n \in \mathbb{N}^*$, 都有:
$$|a_1 b_1 + a_2 b_2 + \cdots + a_n b_n| \leq 2MN$$
证明: 直接利用数列的单调性和有界性即可. 这里从略.

$\boxed{\text{Q.E.D.}}$



#### 一致收敛级数的分析性质

一致收敛的函数项级数可以保持连续性、可微性、可积性等分析性质. 下面我们将分别介绍这些分析性质.

**连续性**: 若函数项级数$\sum_{n=1}^{\infty} u_n(x)$在$D$上一致收敛于$S(x)$, 且对于任意$n \in \mathbb{N}^*$, $u_n(x)$在$D$上连续, 则和函数$S(x)$在$D$上连续.

**证明**: 我们很容易可以得到下面三个表达式:

$$
\begin{aligned}
&|S_N(x_0) - S(x_0)| < \frac{\epsilon}{3} \\
&|S_N(x_0 + h) - S(x_0+h)| < \frac{\epsilon}{3} \\
&|S_N(x_0 + h) - S_N(x_0)| < \frac{\epsilon}{3}
\end{aligned}
$$

其中$N$是根据一致收敛的定义选取的. 由三角不等式, 可以得到:
$$
|S(x_0 + h) - S(x_0)| \leq |S_N(x_0 + h) - S(x_0+h)| + |S_N(x_0 + h) - S_N(x_0)| + |S_N(x_0) - S(x_0)| < \epsilon
$$

连续性定理也可以看作是**可以交换极限**. 即为:
$$\lim_{x \to x_0} \left( \lim_{n \to \infty} S_n(x) \right) = \lim_{n \to \infty} \left( \lim_{x \to x_0} S_n(x) \right)$$

**可积性**: 若函数项级数$\sum_{n=1}^{\infty} u_n(x)$在$[a,b]$上一致收敛于$S(x)$, 对于任意$n$都有$u_n(x)$连续, 且对于任意$n \in \mathbb{N}^*$, $u_n(x)$在$[a,b]$上可积, 则和函数$S(x)$在$[a,b]$上可积, 且:
$$\int_a^b S(x) dx = \sum_{n=1}^{\infty} \int_a^b u_n(x) dx$$

本定理同样可以表达为: 积分运算可以与无限求和运算交换次序. 即为:
$$\int_a^b \left( \lim_{n \to \infty} S_n(x) \right) dx = \lim_{n \to \infty} \left( \int_a^b S_n(x) dx \right)$$

**证明**: 由已知, 根据一致连续性的定义, 我们可以得到:

$$
\left| S_n(x) - S(x) \right| < \epsilon
$$

我们直接两侧积分, 就可以得到:

$$
\left| \int_a^b S_n(x) dx - \int_a^b S(x) dx \right| < (b-a) \epsilon
$$

也就是说, 考虑如下的数项级数:

$$
I_n = \int_a^b S_n(x) dx
$$

我们可以得到:
$$\left| I_n - \int_a^b S(x) dx \right| < (b-a) \epsilon$$

换言之, 数项级数$\{I_n\}$收敛于$\int_a^b S(x) dx$. 由数项级数的定义, 可以得到:
$$
\lim_{n\to\infty} I_n = \lim_{n\to\infty} \int_a^b S_n(x) dx = \int_a^b \lim_{n \to \infty} S_n(x) dx
$$

到这里即完成证明. 思路非常清晰.

**可微性**(可导性): 对于函数序列$\{S_n(x)\}$, 如果它满足下面三条:
- $S_n(x)$在$[a,b]$上可微且有连续的导函数;
- $S_n'(x)$在$[a,b]$上一致收敛于$\sigma(x)$;
- $S_n(a) $在$[a,b]$上点态收敛于$S(x)$.

那么$S(x)$在$[a,b]$上可微, 且$S'(x) = \sigma(x)$.

**证明**: 由于$S_n'(x)$在$[a,b]$上一致收敛于$\sigma(x)$, 根据一致连续性的可积性质:

$$
\int_a^x \sigma (t) dt = \lim_{n\to\infty} \int_a^x S_n'(t) dt = \lim_{n\to\infty} (S_n(x) - S_n(a)) = S(x) - S(a)
$$

由已知条件, 等式两侧均可导. 因此, 可以得到:
$$\sigma(x) = S'(x)$$

同理, 这个定理也可以理解为: 对于一致收敛的函数项级数, 导数运算可以与无限求和运算交换次序. 即为:
$$\left( \lim_{n \to \infty} S_n(x) \right)' = \lim_{n \to \infty} S_n'(x)$$

**Dini定理**: 设函数序列$\{S_n(x)\}$在闭区间$[a,b]$上点态收敛于$S(x)$. 如果:

- $S_n(x)$在$[a,b]$上连续;
- $S(x)$在$[a,b]$上连续;
- 对于任意$x \in [a,b]$, $S_n(x)$单调趋近于$S(x)$.

则函数项级数$\sum_{n=1}^{\infty} u_n(x)$在$[a,b]$上一致收敛于$S(x)$.

这里的证明不要求掌握, 从略.

### 幂级数

前文中我们讨论的函数项级数的一般形式是非常宽泛的, 在实际中, 如果对于每一种函数都要从头判断一致收敛与否, 难免有些繁琐. 于是, 数学家们开始思考：有没有一种特殊而又非常基本的函数组合, 能够自动满足上述优秀的分析性质？

答案是肯定的, 那就是像多项式一样简单而优美的**幂级数**. 

**定义**: 形如
$$
\sum_{n=0}^{\infty} a_n (x - x_0)^n
$$
的级数称为以$x_0$为中心的幂级数, 其中$a_n$是常数.

为了方便讨论, 我们更多的时候会讨论以0为中心的幂级数, 即:
$$\sum_{n=0}^{\infty} a_n x^n$$

**收敛半径**: 根据Cauchy收敛准则, 我们可以知道对于任意固定的$x$, 数项级数$\sum_{n=0}^{\infty} a_n x^n$收敛当且仅当:
$$\lim_{n\to\infty} \sqrt[n]{|a_n x^n|} = \lim_{n\to\infty} \sqrt[n]{|a_n|} \cdot |x| < 1$$

我们约定:

$$
A = \varlimsup_{n \to \infty} \sqrt[n]{|a_n|}
$$

因此, 定义幂级数$\sum_{n=0}^{\infty} a_n x^n$的**收敛半径**为:

$$
R = \begin{cases}
0, & A = +\infty \\
+\infty, & A = 0 \\
\frac{1}{A}, & 0 < A < +\infty
\end{cases}
$$

或者我们可以简记为$R = \frac{1}{A}$, 当然这种标记是不标准的, 笔者也不推荐. 但是确实方便记忆. 所以不失为一种不错的记忆方法.

**定理**(Cauchy-Hadamard定理): 幂级数$\sum_{n=0}^{\infty} a_n x^n$的收敛半径为$R = \frac{1}{A}$, 其中$A = \varlimsup_{n \to \infty} \sqrt[n]{|a_n|}$.

**证明**: 直接利用Cauchy收敛准则即可. 这里从略.

$\boxed{\text{Q.E.D.}}$

**定理**(d'Alembert定理): 若幂级数$\sum_{n=0}^{\infty} a_n x^n$满足$\lim_{n\to\infty} \frac{|a_{n+1}|}{|a_n|} = A$, 则幂级数的收敛半径为$R = \frac{1}{A}$.

**证明**: 这里的证明需要采用下面的不等式:

$$
\varliminf_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right| \leq \varliminf_{n \to \infty} \sqrt[n]{|a_n|} \leq \varlimsup_{n \to \infty} \sqrt[n]{|a_n|} \leq \varlimsup_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right|
$$

因此, 由已知条件, 可以得到:
$$A = \lim_{n\to\infty} \frac{|a_{n+1}|}{|a_n|} = \varliminf_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right| = \varlimsup_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right|$$

因此, 可以得到:
$$A = \varliminf_{n \to \infty} \sqrt[n]{|a_n|} = \varlimsup_{n \to \infty} \sqrt[n]{|a_n|}$$

因此, 可以得到:
$$R = \frac{1}{A}$$

#### 幂函数的性质

**定理**(Abel第二定理): 设幂级数$\sum_{n=0}^{\infty} a_n x^n$的收敛半径为$R > 0$, 则幂级数在$(-R,R)$上内闭一致收敛于和函数$S(x)$.

证明: 我们直接放缩到绝对值最大的边界, 并说明这一边界的绝对值小于$R$. 这里从略.

$\boxed{\text{Q.E.D.}}$

同理, 根据前面提及的三大性质, 可以得到幂级数在$(-R,R)$上保持连续性、可微性、可积性等分析性质. 这里从略.

$\boxed{\text{Q.E.D.}}$

#### 幂级数的展开

**定理**: 设函数$f(x)$在$(-R,R)$上无穷阶可微, 则函数$f(x)$在$(-R,R)$上可以展开成幂级数, 即存在数列$\{a_n\}$使得对于任意$x \in (-R,R)$, 都有:
$$f(x) = \sum_{n=0}^{\infty} a_n x^n$$

实际上我们得到的就是**Taylor级数**. 其中$a_n$可以通过下面的公式计算得到:
$$a_n = \frac{f^{(n)}(0)}{n!}$$

换言之, 函数$f(x)$在$(-R,R)$上的Taylor级数为:
$$f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(0)}{n!} x^n$$

当然我们完全可以要求函数$f(x)$在$(-R,R)$上以$x_0$为中心展开成幂级数, 即存在数列$\{a_n\}$使得对于任意$x \in (-R+x_0,R+x_0)$, 都有:
$$f(x) = \sum_{n=0}^{\infty} a_n (x - x_0)^n$$

其中$a_n$可以通过下面的公式计算得到:
$$a_n = \frac{f^{(n)}(x_0)}{n!}$$

换言之, 函数$f(x)$在$(-R+x_0,R+x_0)$上的Taylor级数为:
$$f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(x_0)}{n!} (x - x_0)^n$$

由于Taylor级数要求函数$f(x)$在$(-R,R)$上无穷阶可微, 因此Taylor级数的展开是一个非常强的条件. 我们未来还会介绍更多的级数, 比如Fourier级数. 这些级数的展开条件相对弱得多, 因此它们的应用范围也更广泛. 这里暂时不会涉及.

---

## Euclid 空间上的极限和连续

本部分我们会简单涉及一些拓扑学的内容, 并完成从一元微积分学到多元微积分学的过渡. 我们从此开始转向研究多元函数的分析性质.

### Euclid空间

让我们首先回顾一下一元函数的**极限**定义:

**定义**: 设函数$f(x)$定义在$E$的某个邻域内, $x_0$是$E$的一个内点. 如果对于任意$\epsilon > 0$, 存在$\delta > 0$, 使得对于所有$x \in E$且$0 < |x - x_0| < \delta$, 都有$|f(x) - A| < \epsilon$, 则称函数$f(x)$在$x_0$处的极限为$A$, 记为$\lim_{x\to x_0} f(x) = A$.

整个定义的关键在于$|x - x_0| < \delta$这个条件. 这个条件**刻画了$x$与$x_0$之间的距离**, 从而保证了函数$f(x)$在$x$附近的行为. 但是当我们转向研究多元函数时, 我们需要一个新的工具来刻画点与点之间的距离, 换言之, 我们需要重新定义距离. 这是我们定义空间时最重要的任务.

但是在此之前, 让我们用公理化的语言重新定义一下空间:

**定义**: 记$R$是实数全体, 定义$n$个$R$的Descartes积
$$R^n = R \times R \times \cdots \times R = \{(x_1, x_2, \ldots, x_n) : x_i \in R, i = 1, 2, \ldots, n\}$$

其中$R$出现$n$次. 对于$R^n$中的每个元素我们都称之为**点**或者**向量**, $x_i$称为点$(x_1, x_2, \ldots, x_n)$的第$i$个**坐标**. 特别的, 我们定义$R^n$中的点$(0, 0, \ldots, 0)$为**零向量**.

特别的, 如果我们为$R^n$中的点定义如下的加法和数乘运算:
- 加法: 对于任意$x = (x_1, x_2, \cdots, x_n), y = (y_1, y_2, \cdots, y_n) \in R^n$, 定义$x + y = (x_1 + y_1, x_2 + y_2, \cdots, x_n + y_n)$.
- 数乘: 对于任意$x = (x_1, x_2, \cdots, x_n) \in R^n$和任意$\lambda \in R$, 定义$\lambda x = (\lambda x_1, \lambda x_2, \cdots, \lambda x_n)$.

此时的$R^n$就被称作**向量空间**, 也是一个常见的**线性空间**.

如果我们再在$R^n$中定义**内积**运算, 即:

$$\langle x, y \rangle = x_1 y_1 + x_2 y_2 + \cdots + x_n y_n = \sum_{i=1}^n x_i y_i$$

内积运算显然具有以下四条性质 (我们理应在线性代数课程中学习过并完成过证明):
- 正定性: 对于任意$x \in R^n$, 都有$\langle x, x \rangle \geq 0$, 且当且仅当$x$是零向量时, $\langle x, x \rangle = 0$.
- 对称性: 对于任意$x, y \in R^n$, 都有$\langle x, y \rangle = \langle y, x \rangle$.
- 线性性: 对于任意$x, y, z \in R^n$和任意$\lambda \in R$, 都有$\langle x + y, z \rangle = \langle x, z \rangle + \langle y, z \rangle$和$\langle \lambda x, y \rangle = \lambda \langle x, y \rangle$.
- Cauchy-Schwarz不等式: 对于任意$x, y \in R^n$, 都有$|\langle x, y \rangle| \leq \sqrt{\langle x, x \rangle} \cdot \sqrt{\langle y, y \rangle}$

**定义**: 配备了内积运算和向量空间结构的$R^n$就被称作**Euclid空间**.

下面, 我们不妨思考一下距离应该具有什么性质:
- 非负性: 对于任意$x, y \in R^n$, 都有$d(x, y) \geq 0$, 且当且仅当$x = y$时, $d(x, y) = 0$
- 对称性: 对于任意$x, y \in R^n$, 都有$d(x, y) = d(y, x)$.
- 三角不等式: 对于任意$x, y, z \in R^n$, 都有$d(x, z) \leq d(x, y) + d(y, z)$. 这条是由平面三角形的基本性质决定的, 我们决定在更高维度上延续它.

我们可以很容易的发现, 距离应该具有的朴素性质, 和内积运算的朴素性质不谋而合, 因此我们可以通过内积运算来定义距离.

**定义**(范数): 设$x \in R^n$, 定义$x$的范数为:
$$\|x\| = \sqrt{\langle x, x \rangle} = \sqrt{x_1^2 + x_2^2 + \cdots + x_n^2}$$

**定义**(距离): 设$x, y \in R^n$, 定义$x$与$y$之间的距离为:
$$d(x, y) = \sqrt{\langle x - y, x - y \rangle} = \sqrt{(x_1 - y_1)^2 + (x_2 - y_2)^2 + \cdots + (x_n - y_n)^2}$$

实际上, **距离**就是**范数**的推广. 也就是说, 距离是定义在两个点之间的函数, 而范数是定义在一个点上的函数. 当然, 距离和范数之间有着密切的联系, 因为距离可以通过范数来定义, 即$d(x, y) = \|x - y\|$.

自然, 范数和距离都具有我们之前提到的那些朴素性质. 这里不再赘述.

#### Euclid空间的性质

现在我们已经充分良好的定义了一个空间和配备在这个空间上的诸多良好性质, 我们就可以开始研究定义在这个空间上的函数了. 当然, 这里我们主要关注的是**多元函数**, 因为一元函数的分析性质我们已经非常熟悉了.

然而, 为了更好的给出多元函数的极限的定义, 我们首先需要对我们刚刚认识的这个空间构建一些了解. 最浅层次的, 我们需要知道一元函数中涉及到的各种事物存不存在一个双射到多元函数中. 例如, 在一元函数中, 我们有数列、极限、连续性、可微性等概念. 那么在多元函数中, 这些概念是否存在? 如果存在, 那么它们的定义是什么? 下面我们将逐一介绍这些概念.

**定义**: 多元函数是指定义在$R^n$上的函数, 即$f: R^n \to R$. 其中$n$被称为函数的**变量个数**或者**维数**. 我们可以把多元函数写作:
$$f(x_1, x_2, \cdots, x_n)$$

至此, 我们完成了从一元函数到多元函数的过渡. 下面我们将继续研究多元函数的分析性质, 包括极限、连续性、可微性等. 这里我们先从极限开始. 我们依旧遵从之前的思路, 先定义数列的极限, 然后再定义函数的极限. 这里我们先介绍数列的极限.

**定义**(数列极限): 设$\{x_n\}$是$R^n$中的一个数列, 如果存在$x_0 \in R^n$, 使得对于任意$\epsilon > 0$, 存在$N \in \mathbb{N}^*$, 使得对于所有$n > N$, 都有$d(x_n, x_0) < \epsilon$, 则称数列$\{x_n\}$收敛于$x_0$, 记为$\lim_{n\to\infty} x_n = x_0$, 反之则称数列$\{x_n\}$发散.

显然, 或者说近乎直观的, 我们可以得到下面这个定理:

**定理**: 设$\{x_n\}$是$R^n$中的一个数列, 则数列$\{x_n\}$收敛于$x_0$当且仅当对于任意$i = 1, 2, \cdots, n$, 数列$\{x_{n,i}\}$收敛于$x_{0,i}$, 其中$x_{n,i}$和$x_{0,i}$分别是数列$\{x_n\}$和点$x_0$的第$i$个坐标.

下面我们将讨论一些拓扑学的概念, 以便更好的理解多元函数的极限和连续性等分析性质. 这里我们先介绍**开集**和**闭集**的概念. 我们可以把它们看作是**开区间**和**闭区间**在多元函数中的推广.

空间中的点无非可以分成三种:
- 内点: 如果点$x$存在一个邻域$U$, 使得$U$中的所有点都属于集合$E$, 则称$x$是集合$E$的一个内点.
- 边界点: 如果点$x$任意一个邻域$U$, 都存在$U$中的点属于集合$E$, 也存在$U$中的点不属于集合$E$, 则称$x$是集合$E$的一个边界点.
- 外点: 如果点$x$存在一个邻域$U$, 使得$U$中的所有点都不属于集合$E$, 则称$x$是集合$E$的一个外点.

但是为了描述集合的边界问题, 我们还需要定义**聚点**的概念. 设$E$是$R^n$中的一个集合, 如果点$x$的任意一个邻域$U$, 都存在$U$中的点属于集合$E$, 则称$x$是集合$E$的一个聚点.

至此, 我们可以定义**开集**和**闭集**了:
- 开集: 如果集合$E$中的每个点都是集合$E$的一个内点, 则称集合$E$是一个开集.
- 闭集: 如果集合$E$包含了集合$E$的所有聚点, 则称集合$E$是一个闭集.

而$S$与它的全部聚点集合$S'$的并集$S \cup S'$被称为集合$S$的**闭包**.

**定理**: $R^n$中的点集$S$是一个闭集当且仅当$R^n \setminus S$是一个开集.

**定理**(De' Morgan定律): 设$A$和$B$是$R^n$中的两个集合, 则有下面的等式成立:
$$\begin{aligned}
&\text{(1) } R^n \setminus (A \cup B) = (R^n \setminus A) \cap (R^n \setminus B) \\
&\text{(2) } R^n \setminus (A \cap B) = (R^n \setminus A) \cup (R^n \setminus B)
\end{aligned}$$

当然这个定理也可以扩展到任意多个集合的情况:
$$\begin{aligned}&\text{(1) } R^n \setminus \left( \bigcup_{i=1}^m A_i \right) = \bigcap_{i=1}^m (R^n \setminus A_i) \\
&\text{(2) } R^n \setminus \left( \bigcap_{i=1}^m A_i \right) = \bigcup_{i=1}^m (R^n \setminus A_i)
\end{aligned}$$

#### Euclid空间的基本定理

本部分涉及的定理将更多局限在$R^2$中, 以便更好的说明问题. 当然, 这些定理也可以推广到更高维度的空间中.

**闭矩形套定理**

**定理**: 设$\Delta_k = [a_k, b_k] \times [c_k, d_k]$是$R^2$中的一个闭矩形, 其中$a_k < b_k$且$c_k < d_k$. 如果$\Delta_1 \supset \Delta_2 \supset \cdots \supset \Delta_k \supset \cdots$, 且满足:

$$
\lim_{k\to\infty} \sqrt{(b_k - a_k)^2 + (d_k - c_k)^2} = 0
$$

则存在唯一的点$(x_0, y_0)$使得$\bigcap_{k=1}^{\infty} \Delta_k = \{(x_0, y_0)\}$. 且:
$$\begin{aligned}
&\lim_{k\to\infty} a_k = \lim_{k\to\infty} b_k = x_0 \\
&\lim_{k\to\infty} c_k = \lim_{k\to\infty} d_k = y_0
\end{aligned}$$

**证明思路**: 只需要对于两个方向分别运用闭区间套定理即可. 这里从略.

$\boxed{\text{Q.E.D.}}$

同理我们也可以得到**Cantor闭区域套定理**. 这里我们不再赘述.

**Bolzano-Weierstrass定理**

在正式阐述Bolzano-Weierstrass定理之前, 我们需要定义一下什么是有界性:

**定义**: 设$E$是$R^n$中的一个集合, 如果存在一个实数$M > 0$, 使得对于任意$x \in E$, 都有$\|x\| < M$, 则称集合$E$是一个有界集.

**定理**(Bolzano-Weierstrass定理): 设$\{x_n\}$是$R^n$中的一个数列, 如果数列$\{x_n\}$是有界的, 则数列$\{x_n\}$存在一个收敛的子数列.

**证明思路**: 先在第一个坐标上利用Bolzano-Weierstrass定理找到一个收敛的子数列, 然后在第二个坐标上利用Bolzano-Weierstrass定理找到一个收敛的子数列, 以此类推, 最后得到一个收敛的子数列. 这里从略.

$\boxed{\text{Q.E.D.}}$

换言之, 这是一个递归的过程, 每次递归都在一个坐标上进行, 最后得到一个收敛的子数列. 这里的思路非常清晰.

**Cauchy收敛准则**

**定理**(Cauchy收敛准则): 设$\{x_n\}$是$R^n$中的一个数列, 则数列$\{x_n\}$收敛当且仅当对于任意$\epsilon > 0$, 存在$N \in \mathbb{N}^*$, 使得对于所有$m, n > N$, 都有$d(x_m, x_n) < \epsilon$.

**证明**: 设数列$\{x_n\}$收敛于$x_0$, 则对于任意$\epsilon > 0$, 存在$N \in \mathbb{N}^*$, 使得对于所有$n > N$, 都有$d(x_n, x_0) < \frac{\epsilon}{2}$. 因此, 对于任意$m, n > N$, 都有:
$$d(x_m, x_n) \leq d(x_m, x_0) + d(x_0, x_n) < \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon$$

反之, 设对于任意$\epsilon > 0$, 存在$N \in \mathbb{N}^*$, 使得对于所有$m, n > N$, 都有$d(x_m, x_n) < \epsilon$. 则数列$\{x_n\}$是有界的. 根据Bolzano-Weierstrass定理, 数列$\{x_n\}$存在一个收敛的子数列$\{x_{n_k}\}$, 设数列$\{x_{n_k}\}$收敛于$x_0$. 则对于任意$\epsilon > 0$, 存在$K \in \mathbb{N}^*$, 使得对于所有$k > K$, 都有$d(x_{n_k}, x_0) < \frac{\epsilon}{2}$. 因此, 对于任意$n > N$和任意$k > K$, 都有:
$$d(x_n, x_0) \leq d(x_n, x_{n_k}) + d(x_{n_k}, x_0) < \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon$$

其实本定理的证明和一元函数中的Cauchy收敛准则的证明是完全一样的, 只是我们需要把绝对值替换成距离. 这里的思路非常清晰.

**Heine-Borel定理**

我们首先定义什么是开覆盖:

**定义**: 设$E$是$R^n$中的一个集合, 如果对于任意$\alpha \in A$, $G_\alpha$都是$R^n$中的一个开集, 且满足$E \subset \bigcup_{\alpha \in A} G_\alpha$, 则称集合$\{G_\alpha\}_{\alpha \in A}$是集合$E$的一个开覆盖.

我们首先给出紧集的开覆盖定义:

**定义**: 设$E$是$R^n$中的一个集合, 如果对于任意$E$的开覆盖$\{G_\alpha\}_{\alpha \in A}$, 都存在有限个开集$G_{\alpha_1}, G_{\alpha_2}, \cdots, G_{\alpha_m}$使得$E \subset G_{\alpha_1} \cup G_{\alpha_2} \cup \cdots \cup G_{\alpha_m}$, 则称集合$E$是一个紧集.

**定理**(Heine-Borel定理): 设$E$是$R^n$中的一个集合, 则集合$E$是一个紧集当且仅当集合$E$是一个有界闭集.

**注意**: 本定理只在$R^n$中成立, 更一般的说, 本定理只在有限维赋范空间中成立. 在无限维赋范空间中, 紧集的定义和性质都发生了很大的变化, 这里我们不再赘述. 我们只给出反例: 在无限维赋范空间中, 闭球是一个有界闭集, 但是它不是一个紧集.

下面给出$n=2$时本定理的证明. 需要注意本定理的证明相对复杂.

**证明**:

1. 必要性
   - 有界
     设$S$为紧集, 显然$\{O(0,1)\subset R^2| x\in S\}$是$S$的一个开覆盖, 因此存在有限个开集$O(0,1), O(x_1,1), \cdots, O(x_m,1)$使得$S \subset O(0,1) \cup O(x_1,1) \cup \cdots \cup O(x_m,1)$. 因此, 可以得到$S \subset O(0,1) \cup O(x_1,1) \cup \cdots \cup O(x_m,1) \subset O(0,M)$, 其中$M = 2\max\{\|x_1\|, \|x_2\|, \cdots, \|x_m\|\} + 1$. 因此, 集合$S$是有界的.
   - 闭集
     运用反证法, 我们假设存在$a \in \overline{S} \setminus S$, 即$a$是$S$的聚点但不在$S$中. 我们构造开集:
     $$G_n = \{x \in R^2 : \|x - a\| > \frac{1}{n}\}, n = 1, 2, \cdots$$
    显然, $\{G_n\}_{n=1}^{\infty}$是$S$的一个开覆盖. 因此, 存在有限个开集$G_{n_1}, G_{n_2}, \cdots, G_{n_k}$使得$S \subset G_{n_1} \cup G_{n_2} \cup \cdots \cup G_{n_k}$. 设$N = \max\{n_1, n_2, \cdots, n_k\}$, 则对于任意$n > N$, 都有$G_n \subset G_N$, 因此, 可以得到$S \subset G_{n_1} \cup G_{n_2} \cup \cdots \cup G_{n_k} \subset G_N$. 这与$a$是$S$的一个聚点矛盾. 因此, 集合$S$是闭集.
2. 充分性
   设$S$是一个有界闭集, 但是不是紧的. 则存在$S$的一个开覆盖$\{G_\alpha\}_{\alpha \in A}$, 使得对于任意有限个开集$G_{\alpha_1}, G_{\alpha_2}, \cdots, G_{\alpha_m}$, 都有$S \not\subset G_{\alpha_1} \cup G_{\alpha_2} \cup \cdots \cup G_{\alpha_m}$.

   我们现在使用一个递归的过程来构造一个数列$\{x_n\}$, 使得数列$\{x_n\}$没有收敛的子数列, 从而得到矛盾.

   任何有界闭集都包含在一个闭矩形中, 因此, 存在一个闭矩形$\Delta_1$使得$S \subset \Delta_1$. 将$\Delta_1$平均分成四个闭矩形$\Delta_{11}, \Delta_{12}, \Delta_{13}, \Delta_{14}$, 则至少存在一个闭矩形$\Delta_{1i_1}$使得$S \cap \Delta_{1i_1}$不可以被有限个开集覆盖.

   以此类推, 根据闭矩形套定理, 我们可以得到一个闭矩形套$\{\Delta_k\}$, 使得$\Delta_1 \supset \Delta_2 \supset \cdots \supset \Delta_k \supset \cdots$, 且满足:
   $$ \lim_{k\to\infty} \sqrt{(b_k - a_k)^2 + (d_k - c_k)^2} = 0 $$
   其中$\Delta_k = [a_k, b_k] \times [c_k, d_k]$. 根据闭矩形套定理, 存在唯一的点$(x_0, y_0)$使得$\bigcap_{k=1}^{\infty} \Delta_k = \{(x_0, y_0)\}$.
   因此, 适当选取任意包含点$(x_0, y_0)$的无限有界开集, 都可以得到一个包含点$(x_0, y_0)$的开集$G_\alpha$, 使得$S \cap G_\alpha$不可以被有限个开集覆盖. 因此, 可以得到$S \subset G_\alpha \cup G_{\alpha_1} \cup G_{\alpha_2} \cup \cdots \cup G_{\alpha_m}$, 其中$G_{\alpha_1}, G_{\alpha_2}, \cdots, G_{\alpha_m}$是$S$的一个有限子覆盖. 这与之前的假设矛盾. 因此, 集合$S$是紧集.

$\boxed{\text{Q.E.D.}}$

有一个类似本定理的三个等价条件:

**定理**: 设$S$是$R^n$中的一个集合, 则下面三个条件是等价的:
- 集合$S$是一个紧集.
- 集合$S$是一个有界闭集.
- 集合$S$中的任意无限子集都在$S$中有一个聚点.

证明: 我们只需要证明(2) $\Leftrightarrow$ (3)

(2) $\Rightarrow$ (3): 设 $S$ 是一个有界闭集, 且 $A$ 是 $S$ 的任意一个无限子集. 由于 $S$ 是有界集, 显然 $A$ 也是有界集. 根据 Bolzano-Weierstrass 定理, 有界无限集 $A$ 必然至少存在一个聚点 $x_0$. 因为 $A \subset S$, 所以 $x_0$ 也是集合 $S$ 的聚点. 又因为 $S$ 是闭集, 它包含其所有的聚点, 故必然有 $x_0 \in S$. 这就证明了 $S$ 中的任意无限子集都在 $S$ 中有一个聚点. 

(3) $\Rightarrow$ (2): 已知 $S$ 中的任意无限子集都在 $S$ 中有一个聚点, 我们需要证明 $S$ 既是有界集又是闭集. 
- **证明有界性**: 反证法. 假设 $S$ 是无界集, 则对于任意正整数 $n$, 都可以找到一点 $x_n \in S$ 使得 $\|x_n\| > n$. 由此构成的无穷序列集合 $A = \{x_1, x_2, \dots \}$ 是 $S$ 的一个无限子集. 由于 $A$ 中的点可以无限远离原点, $A$ 不可能存在任何有限处的聚点, 这与前提“$A$ 在 $S$ 中有聚点”矛盾. 故 $S$ 必须是有界的. 
- **证明闭集性**: 设 $x_0$ 是 $S$ 的任意一个聚点(如果 $S$ 没有聚点则自然为闭集). 根据聚点的定义, 我们可以在 $S$ 中找到一个由互不相同的点组成的收敛序列 $\{x_n\}$, 且该序列趋于 $x_0$. 将这些点收集得到集合 $B = \{x_n\}$, 它显然是 $S$ 的一个无限子集. 根据已知条件, $B$ 在 $S$ 中一定有一个聚点；而该点列是收敛的, 它唯一的聚点就是极限 $x_0$. 因此 $x_0 \in S$. 这说明 $S$ 包含了它所有的聚点, 因此 $S$ 是一个闭集. 

$\boxed{\text{Q.E.D.}}$

### 多元函数

本部分开始, 我将给出多元函数的定义, 并介绍多元函数的极限与连续性.

**定义**: 设$D$是$R^n$中的一个集合, $D$到$R$的一个映射$f: D \to R$被称为一个多元函数. 其中$n$被称为函数的**变量个数**或者**维数**. 我们可以把多元函数写作:
$$f(x_1, x_2, \cdots, x_n), \quad z = f(x_1, x_2, \cdots, x_n)$$

#### 多元函数的极限

**定义**: 设函数$f(x_1, x_2, \cdots, x_n)$定义在$D$的某个邻域内, $x_0 = (x_{0,1}, x_{0,2}, \cdots, x_{0,n})$是$D$的一个内点. 如果对于任意$\epsilon > 0$, 存在$\delta > 0$, 使得对于所有$x = (x_1, x_2, \cdots, x_n) \in D$且$0 < d(x, x_0) < \delta$, 都有$|f(x) - A| < \epsilon$, 则称函数$f(x_1, x_2, \cdots, x_n)$在$x_0$处的极限为$A$, 记为:

$$\lim_{x\to x_0} f(x) = A$$

多元函数的极限要求函数值从任何方向以任何方式趋近, 都必须趋近于同一个值. 这就要求函数在$x_0$附近的行为非常规律, 因此多元函数的极限是一个非常强的条件. 当然, 多元函数的极限也可以定义在无穷远处, 这里我们不再赘述.

对于多元函数的极限, 我们自然而然的希望可以把它拆成多个一元函数的极限来处理, 这就涉及到所谓**累次极限**的概念. 这里我们先介绍一下累次极限的定义:

我们讨论二元函数

**定义**(累次极限): 设$D$是$R^2$中的一个集合, $f(x,y)$是定义在$D$上的一个二元函数, $x_0$和$y_0$分别是集合$\{x : (x,y) \in D\}$和$\{y : (x,y) \in D\}$的内点. 如果对于任意$\epsilon > 0$, 存在$\delta > 0$, 使得对于所有$x \in \{x : (x,y) \in D\}$且$0 < |x - x_0| < \delta$, 都有$|\lim_{y\to y_0} f(x,y) - A| < \epsilon$, 则称函数$f(x,y)$在$x_0$处的累次极限为$A$, 记为:
$$\lim_{x\to x_0} \lim_{y\to y_0} f(x,y) = A$$
这也称作先对$y$再对$x$的累次极限. 同理, 如果对于任意$\epsilon > 0$, 存在$\delta > 0$, 使得对于所有$y \in \{y : (x,y) \in D\}$且$0 < |y - y_0| < \delta$, 都有$|\lim_{x\to x_0} f(x,y) - A| < \epsilon$, 则称函数$f(x,y)$在$y_0$处的累次极限为$A$, 记为:
$$\lim_{y\to y_0} \lim_{x\to x_0} f(x,y) = A$$
这也称作先对$x$再对$y$的累次极限.

但是二次极限和二重极限不一定同时存在且相等. 然而我们可以给出一组存在条件:

**定理**: 若二元函数$f(x,y)$在$(x_0,y_0)$点存在二重极限
$$
\lim_{(x,y)\to(x_0,y_0)} f(x,y) = A
$$
且当$x\neq x_0$时, 函数$f(x,y)$在$y_0$点存在极限
$$\lim_{y\to y_0} f(x,y) = g(x)
$$
则二元函数$f(x,y)$在$(x_0,y_0)$点的二重极限等于先对$y$再对$x$的累次极限, 即:
$$\lim_{(x,y)\to(x_0,y_0)} f(x,y) = \lim_{x\to x_0} \lim_{y\to y_0} f(x,y)$$

**证明**: 只需要对下面这个表达式给出证明即可:

$$ \lim_{x \to x_0} g(x) = A $$

设$\epsilon > 0$是任意的, 因为二重极限存在, 则存在$\delta_1 > 0$, 使得对于所有$(x,y) \in D$且$0 < d((x,y), (x_0,y_0)) < \delta_1$, 都有$|f(x,y) - A| < \epsilon$. 因此, 对于任意$x \in \{x : (x,y) \in D\}$且$0 < |x - x_0| < \delta_1$, 都有$|\lim_{y\to y_0} f(x,y) - A| < \epsilon$. 又因为当$x\neq x_0$时, 函数$f(x,y)$在$y_0$点存在极限, 则对于任意$x \in \{x : (x,y) \in D\}$且$0 < |x - x_0| < \delta_1$, 都有$|g(x) - A| < \epsilon$. 因此, 可以得到对于任意$x \in \{x : (x,y) \in D\}$且$0 < |x - x_0| < \delta_1$, 都有$|g(x) - A| < \epsilon$. 这就证明了$\lim_{x\to x_0} g(x) = A$. 至此, 完成证明.

$\boxed{\text{Q.E.D.}}$

#### 多元函数的连续性

**定义**: 设函数$f(x_1, x_2, \cdots, x_n)$定义在$D$的某个邻域内, $x_0 = (x_{0,1}, x_{0,2}, \cdots, x_{0,n})$是$D$的一个内点. 如果函数$f(x_1, x_2, \cdots, x_n)$在$x_0$处的极限存在且等于$f(x_0)$, 则称函数$f(x_1, x_2, \cdots, x_n)$在$x_0$处连续. 换言之:

$$\lim_{x\to x_0} f(x) = f(x_0)$$

**定理**: 连续映射将紧集映射为紧集.

这个定理主要是针对向量值函数而言的, 我们可以给出如下的定义:

**定义**: 设$D$是$R^n$中的一个集合, $f: D \to R^m$是定义在$D$上的一个向量值函数, 其中$m$被称为函数的**值的维数**. 如果对于任意$\epsilon > 0$, 存在$\delta > 0$, 使得对于所有$x = (x_1, x_2, \cdots, x_n) \in D$且$0 < d(x, x_0) < \delta$, 都有$d(f(x), f(x_0)) < \epsilon$, 则称函数$f: D \to R^m$在$x_0$处连续.

---

## 多元函数的微分学

从现在开始, 我们将正式进入多元函数的微分学部分. 这里我们首先介绍一下多元函数的偏导数, 然后再介绍一下多元函数的全微分, 最后我们将介绍一下多元函数的可微性.

### 多元函数的偏导数

**定义**: 设函数$f(x_1, x_2, \cdots, x_n)$定义在$D$的某个邻域内, $x_0 = (x_{0,1}, x_{0,2}, \cdots, x_{0,n})$是$D$的一个内点. 如果对于任意$\epsilon > 0$, 存在$\delta > 0$, 使得对于所有$x_i \in \{x_i : (x_1, x_2, \cdots, x_n) \in D\}$且$0 < |x_i - x_{0,i}| < \delta$, 都有

$$\left| \frac{f(x_1, x_2, \cdots, x_i, \cdots, x_n) - f(x_1, x_2, \cdots, x_{0,i}, \cdots, x_n)}{x_i - x_{0,i}} - A \right| < \epsilon$$

则称函数$f(x_1, x_2, \cdots, x_n)$在$x_0$处关于第$i$个变量的偏导数为$A$, 记为:
$$\frac{\partial f}{\partial x_i}(x_0) = A$$

偏导数的定义和一元函数的导数的定义非常相似, 只是我们需要把绝对值替换成距离, 并且我们需要把函数值的变化量替换成函数值在某个方向上的变化量. 这里的思路非常清晰. 下面给出**方向导数**的定义:

**定义**: 设函数$f(x_1, x_2, \cdots, x_n)$定义在$D$的某个邻域内, $x_0 = (x_{0,1}, x_{0,2}, \cdots, x_{0,n})$是$D$的一个内点. 如果对于任意$\epsilon > 0$, 存在$\delta > 0$, 使得对于所有$t \in \{t : (x_0 + t\mathbf{u}) \in D\}$且$0 < |t| < \delta$, 都有
$$\left| \frac{f(x_0 + t\mathbf{u}) - f(x_0)}{t} - A \right| < \epsilon$$
则称函数$f(x_1, x_2, \cdots, x_n)$在$x_0$处关于方向$\mathbf{u}$的方向导数为$A$, 记为:
$$D_{\mathbf{u}} f(x_0) = A$$

另有常见的表达形式是借助三角函数表达, 但是这种表述一般局限于二元函数.

#### 高阶偏导数

**定义**: 设$z=f(x,y)$是定义在$D \subset R^2$上的具有偏导数的函数:

$$
\frac{\partial z}{\partial x} = f_x(x,y), \quad \frac{\partial z}{\partial y} = f_y(x,y)
$$

假设这两个偏导数的偏导数也存在, 则称函数$z=f(x,y)$的二阶偏导数为:
$$\begin{aligned}
&\frac{\partial^2 z}{\partial x^2} = f_{xx}(x,y) \quad \frac{\partial^2 z}{\partial y^2} = f_{yy}(x,y) \\
&\frac{\partial^2 z}{\partial x \partial y} = f_{xy}(x,y) \quad \frac{\partial^2 z}{\partial y \partial x} = f_{yx}(x,y)
\end{aligned}$$

其中$\frac{\partial^2 z}{\partial x \partial y}$和$\frac{\partial^2 z}{\partial y \partial x}$分别表示先对$y$后对$x$以及先对$x$后对$y$的二阶偏导数.

计算法则完全一致. 类似的也可以得到更高阶的偏导数, 这里我们不再赘述.

**定理**: 若函数$z=f(x,y)$的二阶偏导数$\frac{\partial^2 z}{\partial x \partial y}$和$\frac{\partial^2 z}{\partial y \partial x}$在$D$内连续, 则对于任意$(x,y) \in D$, 都有:
$$\frac{\partial^2 z}{\partial x \partial y} = \frac{\partial^2 z}{\partial y \partial x}$$

**证明**: 我们考虑下面这个差商:

$$
I = \frac{[f(x_0+\Delta x, y_0+ \Delta y) - f(x_0+\Delta x,y_0)]-[f(x_0, y_0+\Delta y)-f(x_0,y_0)]}{\Delta x \Delta y}
$$

构造下面两个一元函数:

$$
\phi(x) = f(x, y_0 + \Delta y) - f(x, y_0)
$$
$$
\psi(y) = f(x_0 + \Delta x, y) - f(x_0, y)
$$

则差商 $I$ 可以被表示为两者的增量形式:
$$
I = \frac{\phi(x_0+\Delta x) - \phi(x_0)}{\Delta x \Delta y} = \frac{\psi(y_0+\Delta y) - \psi(y_0)}{\Delta x \Delta y}
$$

对 $\phi(x)$ 在 $[x_0, x_0+\Delta x]$ 上应用拉格朗日中值定理(不妨设 $\Delta x > 0$):
$$ \phi(x_0+\Delta x) - \phi(x_0) = \phi'(\xi_1)\Delta x $$
其中 $\xi_1$ 介于 $x_0$ 与 $x_0+\Delta x$ 之间. 而 $\phi'(x) = f_x(x, y_0+\Delta y) - f_x(x, y_0)$, 故
$$ \phi'(\xi_1) = f_x(\xi_1, y_0+\Delta y) - f_x(\xi_1, y_0) $$
将上式看作关于 $y$ 的函数在 $[y_0, y_0+\Delta y]$ 上的增量, 再次应用拉格朗日中值定理:
$$ f_x(\xi_1, y_0+\Delta y) - f_x(\xi_1, y_0) = f_{xy}(\xi_1, \eta_1)\Delta y $$
其中 $\eta_1$ 介于 $y_0$ 与 $y_0+\Delta y$ 之间. 因此 $I = f_{xy}(\xi_1, \eta_1)$.

同理, 对 $\psi(y)$ 在 $[y_0, y_0+\Delta y]$ 上应用拉格朗日中值定理, 然后再对 $x$ 应用拉格朗日中值定理, 可得:
$$ \psi(y_0+\Delta y) - \psi(y_0) = \psi'(\eta_2)\Delta y = [f_y(x_0+\Delta x, \eta_2) - f_y(x_0, \eta_2)]\Delta y = f_{yx}(\xi_2, \eta_2)\Delta x \Delta y $$
其中 $\eta_2$ 介于 $y_0$ 与 $y_0+\Delta y$ 之间, $\xi_2$ 介于 $x_0$ 与 $x_0+\Delta x$ 之间. 因此 $I = f_{yx}(\xi_2, \eta_2)$.

于是我们有:
$$ f_{xy}(\xi_1, \eta_1) = f_{yx}(\xi_2, \eta_2) $$

令 $\Delta x \to 0, \Delta y \to 0$, 由于 $\xi_1, \xi_2 \to x_0$, $\eta_1, \eta_2 \to y_0$, 且二阶混合偏导数 $f_{xy}$ 和 $f_{yx}$ 在点 $(x_0, y_0)$ 处连续, 取极限即得:
$$ f_{xy}(x_0, y_0) = f_{yx}(x_0, y_0) $$
$\boxed{\text{Q.E.D.}}$

### 全微分与可微性

**定义**: 一般的, 对于函数$z = f(x_1, x_2, \cdots, x_n)$在点$(x_1, x_2, \cdots, x_n)$处的全微分定义为:
$$df = \frac{\partial f}{\partial x_1}dx_1 + \frac{\partial f}{\partial x_2}dx_2 + \cdots + \frac{\partial f}{\partial x_n}dx_n$$

如果函数$f(x_1, x_2, \cdots, x_n)$在点$(x_1, x_2, \cdots, x_n)$处可微, 则称函数在该点处的全微分为:
$$df = f'(x_1, x_2, \cdots, x_n)$$


**定义**(可微条件): 设函数$f(x_1, x_2, \cdots, x_n)$定义在$D$的某个邻域内, $x_0 = (x_{0,1}, x_{0,2}, \cdots, x_{0,n})$是$D$的一个内点. 考虑函数的全增量:

$$
\Delta f = f(x_{0,1} + \Delta x_1, x_{0,2} + \Delta x_2, \cdots, x_{0,n} + \Delta x_n) - f(x_{0,1}, x_{0,2}, \cdots, x_{0,n})
$$

若存在只与$(x_1, x_2, \cdots, x_n)$有关的参数$A_1, A_2, \cdots, A_n$, 使得:
$$
\Delta f = A_1 \Delta x_1 + A_2 \Delta x_2 + \cdots + A_n \Delta x_n + o(\sqrt{\Delta x_1^2 + \Delta x_2^2 + \cdots + \Delta x_n^2})
$$

其中$o(\sqrt{\Delta x_1^2 + \Delta x_2^2 + \cdots + \Delta x_n^2})$表示$\sqrt{\Delta x_1^2 + \Delta x_2^2 + \cdots + \Delta x_n^2}$的高阶无穷小量. 换言之:

$$
\lim_{\sqrt{\Delta x_1^2 + \Delta x_2^2 + \cdots + \Delta x_n^2} \to 0} \frac{o(\sqrt{\Delta x_1^2 + \Delta x_2^2 + \cdots + \Delta x_n^2})}{\sqrt{\Delta x_1^2 + \Delta x_2^2 + \cdots + \Delta x_n^2}} = 0
$$

则称函数$f(x_1, x_2, \cdots, x_n)$在$x_0$处可微, 记为:
$$f'(x_0) = (A_1, A_2, \cdots, A_n)$$

**定理**: 可微必定可导.

证明略, 这里的思路非常清晰. 可微的定义要求函数的增量可以被一个线性函数所近似, 因此, 可微必定可导. 但是可导不一定可微, 这里我们可以给出一个反例:
$$f(x,y) = \begin{cases}\frac{x^2y}{x^4+y^2}, & (x,y) \neq (0,0) \\ 0, & (x,y) = (0,0) \end{cases}$$

函数$f(x,y)$在点$(0,0)$处的偏导数存在且等于0, 但是函数$f(x,y)$在点$(0,0)$处不可微. 因此, 可导不一定可微.

#### 高阶微分

**定义**: 设函数$z=f(x,y)$是定义在$D \subset R^2$上的一个二元函数, 则函数$z=f(x,y)$的二阶微分定义为:
$$d^2f = f_{xx}dx^2 + 2f_{xy}dxdy + f_{yy}dy^2$$

**证明**: 用定义即可. 只需注意, 在可微的条件下, 恒有:

$$
f_{xy} f(x,y) = f_{yx} f(x,y)
$$

### *向量值函数的微分学

本部分不会在期中考试中有所涉及, 但是出于完整性的考虑, 我们给出不带证明的介绍.

我们讨论的是$R^n$上, 在区域$D$中的$n$元$m$维向量值函数:

$$
\boldsymbol{f}: D \to R^m
$$

我们可以把它写成坐标分量的形式:

$$
\boldsymbol{f}(x) = \begin{pmatrix}
f_1(x_1, x_2, \cdots, x_n) \\
f_2(x_1, x_2, \cdots, x_n) \\
\vdots \\
f_m(x_1, x_2, \cdots, x_n)
\end{pmatrix}
$$

#### Jacobi矩阵与可微性

对于向量值函数, 我们可以类比一元函数的导数, 来定义向量值函数的可微性. 若存在一个 $m \times n$ 的矩阵 $\boldsymbol{A}$, 使得当 $\Delta x \to 0$ 时, 成立:

$$
\boldsymbol{f}(x_0 + \Delta x) - \boldsymbol{f}(x_0) = \boldsymbol{A} \Delta x + o(\|\Delta x\|)
$$

则称向量值函数 $\boldsymbol{f}$ 在点 $x_0$ 处**可微**, 并且矩阵 $\boldsymbol{A}$ 被称为向量值函数 $\boldsymbol{f}$ 在点 $x_0$ 处的**导数**.

事实表明, 当 $\boldsymbol{f}$ 可微时, 矩阵 $\boldsymbol{A}$ 是唯一确定的, 并且它恰好是由各分量函数的偏导数排成的矩阵, 称为 **Jacobi矩阵** (Jacobian matrix):

$$
J_{\boldsymbol{f}}(x_0) = \begin{pmatrix}
\frac{\partial f_1}{\partial x_1} & \frac{\partial f_1}{\partial x_2} & \cdots & \frac{\partial f_1}{\partial x_n} \\
\frac{\partial f_2}{\partial x_1} & \frac{\partial f_2}{\partial x_2} & \cdots & \frac{\partial f_2}{\partial x_n} \\
\vdots & \vdots & \ddots & \vdots \\
\frac{\partial f_m}{\partial x_1} & \frac{\partial f_m}{\partial x_2} & \cdots & \frac{\partial f_m}{\partial x_n}
\end{pmatrix}
$$

这就将标量函数的可微性自然地推广到了向量值函数. 一般我们也直接记为 $\boldsymbol{f}'(x_0)$.

#### 向量值函数的链式法则

向量值函数的微分学最漂亮的结果之一就是链式法则的矩阵形式. 它与一元函数的链式法则在形式上完全一致.

**定理** (链式法则): 设 $\boldsymbol{f}: R^n \to R^m$, $\boldsymbol{g}: R^m \to R^p$. 若 $\boldsymbol{f}$ 在 $x_0$ 处可微, $\boldsymbol{g}$ 在 $y_0 = \boldsymbol{f}(x_0)$ 处可微, 则复合函数 $\boldsymbol{h} = \boldsymbol{g} \circ \boldsymbol{f}$ 在 $x_0$ 处可微, 且其导数 (Jacobi矩阵) 为两者Jacobi矩阵的乘积:

$$
J_{\boldsymbol{g} \circ \boldsymbol{f}}(x_0) = J_{\boldsymbol{g}}(y_0) \cdot J_{\boldsymbol{f}}(x_0)
$$

这个定理不仅形式优美, 而且十分实用, 各类多元复合函数求导法则, 都可以看作是这一矩阵乘法法则的具体分量展开.

### 梯度

**定义**: 设$D \subset R^2$, 若函数$z=f(x,y)$在$(x_0,y_0)$处可偏导, 则称函数$z=f(x,y)$在$(x_0,y_0)$处的梯度为:
$$\nabla f(x_0,y_0) = \left( \frac{\partial f}{\partial x}(x_0,y_0), \frac{\partial f}{\partial y}(x_0,y_0) \right)$$

也可以写作:

$$
\text{grad} f(x_0,y_0) = f_x(x_0,y_0) \hat{i} + f_y(x_0,y_0) \hat{j}
$$

梯度具有一系列类似导数的基本性质:

- 线性性质: $\nabla (af + bg) = a\nabla f + b\nabla g$, 其中$a$和$b$是常数.
- 积的求导法则: $\nabla (fg) = f\nabla g + g\nabla f$.
- 商的求导法则: $\nabla \left( \frac{f}{g} \right) = \frac{g\nabla f - f\nabla g}{g^2}$, 其中$g \neq 0$.

### 多元复合函数的求导法则

**定理**: 设$g$在$(u_0, v_0) \in D_g$处可导, 即$x=x(u,v), y=y(u,v)$在$(u_0, v_0)$处可偏导. 记$x_0 = x(u_0, v_0), y_0 = y(u_0, v_0)$, 若$f$在$(x_0, y_0) \in D_f$处可微, 那么:

$$
\begin{aligned}
&\frac{\partial}{\partial u}z = \frac{\partial}{\partial x}f \cdot \frac{\partial}{\partial u}x + \frac{\partial}{\partial y} f \cdot \frac{\partial}{\partial u}y \\
&\frac{\partial}{\partial v}z = \frac{\partial}{\partial x} f \cdot \frac{\partial}{\partial v}x + \frac{\partial}{\partial y} f \cdot \frac{\partial}{\partial v}y
\end{aligned}
$$

这条定理也叫做**链式法则**. 这里的思路非常清晰, 只需要把复合函数的增量表示成内外函数增量的乘积, 然后再对内外函数分别应用可微的定义即可. 这里我们不再赘述.

#### 一阶全微分的形式不变性

**定理**: 我们假设$z=f(x,y), x=x(u,v), y=y(u,v)$, 如果$f$在$(x_0,y_0)$处可微, $x(u,v), y(u,v)$在$(u_0,v_0)$处可偏导, 那么:

$$
dz = \frac{\partial f}{\partial x}dx + \frac{\partial f}{\partial y}dy = \frac{\partial f}{\partial x}\left(\frac{\partial x}{\partial u}du + \frac{\partial x}{\partial v}dv\right) + \frac{\partial f}{\partial y}\left(\frac{\partial y}{\partial u}du + \frac{\partial y}{\partial v}dv\right)
$$

$$
dz= \frac{\partial f}{\partial x}dx + \frac{\partial f}{\partial y}dy = \frac{\partial f}{\partial u}du + \frac{\partial f}{\partial v}dv
$$

这条定理也叫做**一阶全微分的形式不变性**. 这意味着无论$x,y$是$u,v$的函数还是其他变量的函数, 一阶全微分的表达式都是一样的.

### 二元函数的Taylor公式

**定理**: 假设$f(x,y)$在点$(x_0,y_0)$处具有$k+1$阶连续偏导数, 则对于小邻域内任意$(x,y)=(x_0+\Delta x, y_0+\Delta y)$, 都有:

$$
f(x+\Delta x, y+\Delta y) = f(x,y) + \sum_{n=1}^k \frac{1}{n!} \left( \Delta x \frac{\partial}{\partial x} + \Delta y \frac{\partial}{\partial y} \right)^n f(x,y) + R_k
$$
其中$R_k$是余项, 满足:
$$
\lim_{\sqrt{\Delta x^2 + \Delta y^2} \to 0} \frac{R_k}{\sqrt{\Delta x^2 + \Delta y^2}^k} = 0
$$
这条定理也叫做**二元函数的Taylor公式**. 常见的余项称作拉格朗日余项:
$$
R_k = \frac{1}{(k+1)!} \left( \Delta x \frac{\partial}{\partial x} + \Delta y \frac{\partial}{\partial y} \right)^{k+1} f(x+\theta_1 \Delta x, y+\theta_2 \Delta y)
$$

我们取$k=0$, 就可以得到二元函数的**微分中值定理**:

**定理**: 设函数$f(x,y)$在$D$内具有连续偏导数, $P_0=(x_0,y_0)$和$P=(x,y)$是$D$内的两点, 则存在$\theta \in (0,1)$使得:
$$
f(x_0+\Delta x,y_0+\Delta y) - f(x_0,y_0) = f_x(x_0+\theta \Delta x, y_0+\theta \Delta y) \Delta x + f_y(x_0+\theta \Delta x, y_0+\theta \Delta y) \Delta y
$$

### 隐函数

很多时候, 用显示的, 分离好的函数来描述一个关系是非常困难的, 这时候我们就需要用到隐函数. 隐函数就是用一个二元函数方程来描述一个关系, 即:
$$F(x,y) = 0$$

**定理**(一元隐函数存在定理): 若二元函数$F(x,y)$满足条件:
- $F(x_0,y_0) = 0$
- 在闭矩形$R = \{(x,y) : |x-x_0| \leq a, |y-y_0| \leq b\}$上连续且具有连续偏导数
- $F_y(x_0,y_0) \neq 0$

那么在$(x_0,y_0)$**附近**可以唯一确定隐函数$y=f(x)$, 使得$F(x,f(x)) = 0$. 这里的**附近**是指存在一个开区间$(x_0 - \delta, x_0 + \delta)$, 使得对于任意$x \in (x_0 - \delta, x_0 + \delta)$, 都有$F(x,f(x)) = 0$. 并且进一步的我们可以得到:

$$
\frac{dy}{dx} = - \frac{F_x(x,y)}{F_y(x,y)}
$$

这里的证明我们略过. 同时, 我们可以很轻易的把上述结论推广到多元隐函数的情况:

**定理**(多元隐函数存在定理): 若 $n+1$ 元函数 $F(x_1, x_2, \dots, x_n, y)$ 满足条件:
- $F(x_1^0, x_2^0, \dots, x_n^0, y_0) = 0$
- 在点 $(x_1^0, x_2^0, \dots, x_n^0, y_0)$ 的某邻域内具有连续的偏导数
- $F_y(x_1^0, x_2^0, \dots, x_n^0, y_0) \neq 0$

那么在点 $(x_1^0, x_2^0, \dots, x_n^0)$ 的某邻域内, 方程 $F(x_1, x_2, \dots, x_n, y) = 0$ 可以唯一确定一个连续且具有连续偏导数的隐函数 $y = f(x_1, x_2, \dots, x_n)$ 使得 $y_0 = f(x_1^0, x_2^0, \dots, x_n^0)$. 并且其偏导数为:

$$
\frac{\partial y}{\partial x_i} = - \frac{F_{x_i}(x_1, x_2, \dots, x_n, y)}{F_y(x_1, x_2, \dots, x_n, y)}, \quad (i = 1, 2, \dots, n)
$$

#### 多元函数方程组

很多时候, 我们需要处理多个隐函数方程组成的方程组, 例如著名的外包络线问题:

$$
\begin{cases}
F(x,y,z) = 0 \\
\frac{\partial F}{\partial z} = 0
\end{cases}
$$

我们可以把上述定理推广到多元函数方程组的情况:

**定理**(多元函数方程组存在定理): 设$F(x,y,u,v)$和$G(x,y,u,v)$是定义在$D \subset R^4$上的两个四元函数, 满足条件:
- $F(x_0,y_0,u_0,v_0) = 0, G(x_0,y_0,u_0,v_0) = 0$
- 在闭长方体$R = \{(x,y,u,v) : |x-x_0| \leq a, |y-y_0| \leq b, |u-u_0| \leq c, |v-v_0| \leq d\}$上连续且具有连续偏导数
- $\frac{\partial(F,G)}{\partial(u,v)} = \begin{vmatrix} F_u & F_v \\ G_u & G_v \end{vmatrix} \neq 0$
那么在点$(x_0,y_0)$的某邻域内, 方程组
$$\begin{cases}
F(x,y,u,v) = 0 \\
G(x,y,u,v) = 0
\end{cases}$$
可以唯一确定一个连续且具有连续偏导数的隐函数组:
$$\begin{cases}
u = f(x,y) \\
v = g(x,y)
\end{cases}$$

而且我们可以得到隐函数组的偏导数:
$$
\begin{pmatrix}
\frac{\partial u}{\partial x} & \frac{\partial u}{\partial y} \\
\frac{\partial v}{\partial x} & \frac{\partial v}{\partial y}
\end{pmatrix}
= - \begin{pmatrix}
F_u & F_v \\
G_u & G_v
\end{pmatrix}^{-1} \cdot \begin{pmatrix}F_x & F_y \\
G_x & G_y
\end{pmatrix}
$$

但是实际上我们在求解的时候, 更方便的方式是两个方程直接对$x$和$y$求偏导数, 然后再解出$\frac{\partial u}{\partial x}, \frac{\partial u}{\partial y}, \frac{\partial v}{\partial x}, \frac{\partial v}{\partial y}$. 而不是利用线性代数的方法去求解. 这里我们不再赘述.

### 多元函数的几何应用

#### 空间中的切线和法平面

**空间曲线的参数方程**: 设空间曲线$C$的参数方程为:
$$\begin{cases}
x = x(t) \\
y = y(t) \\
z = z(t)
\end{cases}$$

也可以写成向量值函数的形式:
$$\boldsymbol{r}(t) = x(t)\hat{i} + y(t)\hat{j} + z(t)\hat{k}$$

**空间曲线的切线**: 设空间曲线$C$的参数方程为$\boldsymbol{r}(t)$, 则空间曲线$C$在点$\boldsymbol{r}(t_0)$处的切线方程为:
$$\frac{x - x(t_0)}{x'(t_0)} = \frac{y - y(t_0)}{y'(t_0)} = \frac{z - z(t_0)}{z'(t_0)}$$

**空间曲线的切向量**: 设空间曲线$C$的参数方程为$\boldsymbol{r}(t)$, 则空间曲线$C$在点$\boldsymbol{r}(t_0)$处的切向量为:
$$\boldsymbol{r}'(t_0) = x'(t_0)\hat{i} + y'(t_0)\hat{j} + z'(t_0)\hat{k}$$

**空间曲线的法平面**: 也就是以切向量为法向量的平面. 设空间曲线$C$的切向量为$\boldsymbol{r}'(t_0)$, 则空间曲线$C$在点$\boldsymbol{r}(t_0)$处的法平面方程为:
$$x'(t_0)(x - x(t_0)) + y'(t_0)(y - y(t_0)) + z'(t_0)(z - z(t_0)) = 0$$

我们有时候不仅会使用参数方程来表达空间中的曲线, 我们也会使用两个空间中的曲面来表达空间中的曲线. 比如说:

$$
\begin{cases}
    F(x, y, z) = 0 \\
    G(x, y, z) = 0
\end{cases}
$$

我们假定它的Jacobi矩阵始终行满秩:

$$
\text{rank}
\begin{pmatrix}
F_x & F_y & F_z \\
G_x & G_y & G_z
\end{pmatrix} = 2
$$

根据前面在微分部分的知识, 我们显然有:

$$
\frac{\partial (F,G)}{\partial (x,y)} = \begin{vmatrix}
    F_x & F_y \\
    G_x & G_y
\end{vmatrix}, \quad
\frac{\partial (F,G)}{\partial (y,z)} = \begin{vmatrix}
    F_y & F_z \\
    G_y & G_z
\end{vmatrix}, \quad
\frac{\partial (F,G)}{\partial (z,x)} = \begin{vmatrix}
    F_z & F_x \\
    G_z & G_x
\end{vmatrix}
$$

则空间曲线$C$在点$P(x_0,y_0,z_0)$处的切向量为:
$$
\boldsymbol{r}'(P_0) = \frac{\partial (F,G)}{\partial (y,z)}\hat{i} + \frac{\partial (F,G)}{\partial (z,x)}\hat{j} + \frac{\partial (F,G)}{\partial (x,y)}\hat{k}
$$

>
> **理解这些雅可比记号的几何意义：**
> 
> 这个记号 $\frac{\partial (F,G)}{\partial (x,y)}$ 本质上是雅可比(Jacobian)行列式的简写. 在这里，它不仅是为了简化二阶行列式的书写，更是为了表达**两个法向量的外积（叉乘）**.
> 
> 空间曲线是由曲面 $F(x,y,z)=0$ 和 $G(x,y,z)=0$ 相交构成的。因为曲线同时在这两个曲面上，所以曲线的切向量一定同时垂直于这两个曲面的法向量 $\nabla F = (F_x, F_y, F_z)$ 和 $\nabla G = (G_x, G_y, G_z)$.
> 
> 求同时垂直于这两个向量的方向，可以直接用外积表示：
> $$ \nabla F \times \nabla G = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ F_x & F_y & F_z \\ G_x & G_y & G_z \end{vmatrix} $$
> 将该行列式按第一行展开，$\hat{i}$, $\hat{j}$, $\hat{k}$ 前的系数刚好就是这三个雅可比行列式：$\frac{\partial (F,G)}{\partial (y,z)}$, $\frac{\partial (F,G)}{\partial (z,x)}$, $\frac{\partial (F,G)}{\partial (x,y)}$。这就是切向量公式的本质来源.
> 

#### 空间中的切平面和法线

空间中的曲面可以用一个二元函数来表示也可以用一个隐函数来表示. 一般的:

$$F(x,y,z) = 0$$

表达式中的$F$是一个三元函数, 其零点集就是我们要讨论的曲面. 设$P_0=(x_0,y_0,z_0)$是曲面上的一个点, 则曲面在点$P_0$处的切平面方程为:
$$F_x(x_0,y_0,z_0)(x-x_0) + F_y(x_0,y_0,z_0)(y-y_0) + F_z(x_0,y_0,z_0)(z-z_0) = 0$$

这个切平面的法向量是:
$$\boldsymbol{n} = F_x(x_0,y_0,z_0)\hat{i} + F_y(x_0,y_0,z_0)\hat{j} + F_z(x_0,y_0,z_0)\hat{k}$$

这本质上是因为曲面在点$P_0$处的切平面与曲面在点$P_0$处的梯度垂直, 因此切平面的法向量就是曲面在点$P_0$处的梯度. 这里我们不再赘述.

### 极值问题

#### 无条件极值

**极值的必要条件**：设函数 $z=f(x,y)$ 在点 $(x_0,y_0)$ 处具有偏导数, 且在该点取得极值, 则有：
$$f_x(x_0,y_0) = 0, \quad f_y(x_0,y_0) = 0$$
满足此条件的点 $(x_0,y_0)$ 称为函数 $f(x,y)$ 的**驻点**. 

**极值的充分条件**：设函数 $z=f(x,y)$ 在驻点 $(x_0,y_0)$ 的某邻域内具有连续的二阶偏导数, 记：
$$A = f_{xx}(x_0,y_0), \quad B = f_{xy}(x_0,y_0), \quad C = f_{yy}(x_0,y_0)$$
且 $\Delta = AC - B^2$, 则：
1. 当 $\Delta > 0$ 时, 函数在 $(x_0,y_0)$ 处取得极值. 其中, 当 $A < 0$ 时取得**极大值**；当 $A > 0$ 时取得**极小值**. 
2. 当 $\Delta < 0$ 时, 函数在 $(x_0,y_0)$ 处**不取得极值**(此点称为鞍点). 
3. 当 $\Delta = 0$ 时, 可能是极值点也可能不是, 需要进一步判定. 

**一些说明**: 关于表达式$AC-B^2$的来源:

我们现在对$f(x+h, y+k)$进行二阶Taylor展开, 可以得到:
$$
f(x+h, y+k) = f(x,y) + f_x h + f_y k + \frac{1}{2} (f_{xx} h^2 + 2f_{xy} hk + f_{yy} k^2) + o(h^2 + k^2)
$$

由于一阶偏微分在驻点处为$0$，因此我们可以把增量表示为:

$$
f(x+h, y+k) - f(x,y) = \frac{1}{2} (f_{xx} h^2 + 2f_{xy} hk + f_{yy} k^2) + o(h^2 + k^2)
$$

换言之, 我们实际上是在讨论二次型 $Q(h,k) = f_{xx} h^2 + 2f_{xy} hk + f_{yy} k^2$ 的正定性. 我们把二次型 $Q(h,k)$ 写成矩阵的形式:

$$
Q(h,k) = \begin{pmatrix} h & k \end{pmatrix} \begin{pmatrix} f_{xx} & f_{xy} \\ f_{xy} & f_{yy} \end{pmatrix} \begin{pmatrix} h \\ k \end{pmatrix} = \begin{pmatrix} h & k \end{pmatrix} \begin{pmatrix} A & B \\ B & C \end{pmatrix} \begin{pmatrix} h \\ k \end{pmatrix}
$$

讨论矩阵:

$$
H = \begin{pmatrix} A & B \\ B & C \end{pmatrix}
$$

行列式:

$$
|H| = \begin{vmatrix} A & B \\ B & C \end{vmatrix} = AC - B^2
$$

由于$H$为实对称矩阵, 因此它的正定性可以通过行列式来判定. 当$|H| > 0$且$A > 0$时, $H$为正定矩阵, 因此二次型$Q(h,k)$为正定, 函数在驻点处取得极小值. 当$|H| > 0$且$A < 0$时, $H$为负定矩阵, 因此二次型$Q(h,k)$为负定, 函数在驻点处取得极大值. 当$|H| < 0$时, $H$为不定矩阵, 因此二次型$Q(h,k)$为不定, 函数在驻点处不取得极值(鞍点). 当$|H| = 0$时, $H$为半正定或半负定矩阵, 因此二次型$Q(h,k)$可能是半正定或半负定, 函数在驻点处可能取得极值也可能不取得极值.


#### 条件极值

条件极值是指在某些约束条件下求目标函数的极值. 通常使用**拉格朗日乘数法**. 

**【拉格朗日乘数法原理与几何直观】**
* **等值线相切**：以二维条件 $g(x,y)=0$ (约束曲线) 下求 $f(x,y)$ 极值为例，观察 $f(x,y)=c$ 的一系列等值线。当在约束曲线上探寻极值时，极值点必须是约束曲线与某条等值线**恰好相切**的位置（若相交，则说明还可顺着约束曲线走向更高或更低的等值线）.
* **梯度共线**：由于在极值点处两曲线相切，且梯度（$\nabla f$和$\nabla g$）始终垂直于各自所在的等值线，故在极值点两者的**梯度法向量必然共线（互相平行）**。用公式表达即 $\nabla f = -\lambda \nabla g$.
* **辅助函数的构造**：为了将“有约束的寻找问题”统一转化为“无约束寻找极值点”的计算步骤，构造了辅助函数 $L(x,y,\lambda) = f(x,y) + \lambda g(x,y)$。对自变量求偏导并令其为 $0$ ($L_x=0, L_y=0$) 其实就是在应用“梯度共线”的条件（$f_x+\lambda g_x=0$）；对 $\lambda$ 求导令其为 $0$ ($L_\lambda=0$)，则是补回了“落在约束回线”的前提($g=0$)
* **多约束情况**：多约束(如面和面相交成一条线作为约束)同理，在极值点处目标函数 $f$ 的梯度须平躺在 $g$ 和 $h$ 的梯度所张成的法平面内部。即 $\nabla f = -\lambda \nabla g - \mu \nabla h$。也就对应了多乘子构造：$L = f + \lambda g + \mu h$.

**单约束条件**：求目标函数 $f(x,y,z)$ 在约束条件 $g(x,y,z) = 0$ 下的极值. 
构造拉格朗日函数：
$$L(x,y,z,\lambda) = f(x,y,z) + \lambda g(x,y,z)$$
求 $L$ 驻点的方程组：
$$
\begin{cases}
L_x = f_x + \lambda g_x = 0 \\
L_y = f_y + \lambda g_y = 0 \\
L_z = f_z + \lambda g_z = 0 \\
L_\lambda = g(x,y,z) = 0
\end{cases}
$$
解此方程组得到的 $(x,y,z)$ 即为可能的条件极值点.

**多约束条件**：若有多个约束, 如 $g(x,y,z) = 0$ 和 $h(x,y,z) = 0$, 则构造：
$$L(x,y,z,\lambda,\mu) = f(x,y,z) + \lambda g(x,y,z) + \mu h(x,y,z)$$
并按照同样的方法对所有变量(包含 $\lambda, \mu$)求偏导并令其为0即可求解.

## 重积分

为了讨论重积分, 我们需要先讨论一下$R^2$上的面积问题, 因为重积分的定义是基于面积的, 且$D \subset R^2$的面积并不一定存在.

### 定义

**定义**: 设$D \subset R^2$是一个有界区域, 设$U= [a,b] \times [c,d]$是一个矩形, 且$D \subset U$.

在$[a,b]$和$[c,d]$上分别取分点:
$$a = x_0 < x_1 < \cdots < x_m = b$$
$$c = y_0 < y_1 < \cdots < y_n = d$$
则$U$被划分成了$m \times n$个小矩形, 记为$R_{ij} = [x_{i-1}, x_i] \times [y_{j-1}, y_j]$.

对于点集$D$, 我们给出如下两条定义:

- 完全包含在$D$中的小矩形的面积之和:
$$mA = \sum_{R_{ij} \subset D} \text{area}(R_{ij})$$

- 与$D$交集非空的小矩形的面积之和:
$$mB = \sum_{R_{ij} \cap D \neq \emptyset} \text{area}(R_{ij})$$

若在原有划分的基础上, 继续增加分点加细, 且$mA$不减, $mB$不增, 记$mA$和$mB$的上确界和下确界分别为$mD_*$和$mD^*$, 则称$mD_*$为$D$的内面积, $mD^*$为$D$的外面积. 如果$mD_* = mD^*$, 则称$D$的面积存在, 记为$mD$.

下面给出一个定理, 作为面积存在的充分必要条件: (证明通过可数可加性完成):

**定理**: 设$D \subset R^2$是一个有界区域, 则$D$的面积存在的充分必要条件是它的边界$\partial D$的面积为$0$.

#### 二重积分的概念

二重积分的讨论过程和讨论一元函数的定积分的讨论过程非常类似. 设二元函数$z=f(x,y)$在区域$D$上有定义, 且$D$的面积存在.

1. 将$D$划分为$n$个小区域$\Delta D_i$, 记$\Delta \sigma_i$为$\Delta D_i$的面积.
2. 在每个小区域$\Delta D_i$内任取一点$P_i$, 记$f(P_i)$为函数$f$在点$P_i$处的函数值.
3. 计算求和: $S = \sum_{i=1}^n f(P_i) \Delta \sigma_i$.
4. 记$\lambda = \max \{\text{diam}(\Delta D_i) : i=1,2,\cdots,n\}$, 则当$\lambda \to 0$时, 若$S$的极限存在且与划分方式无关, 则称函数$f$在区域$D$上可积, 记为:
$$\iint_D f(x,y) d\sigma = \lim_{\lambda \to 0} \sum_{i=1}^n f(P_i) \Delta \sigma_i$$

同理, 我们也可以利用Darboux大和和Darboux小和来讨论二重积分的存在性. 设$M_i = \sup \{f(x,y) : (x,y) \in \Delta D_i\}$, $m_i = \inf \{f(x,y) : (x,y) \in \Delta D_i\}$, 则Darboux大和和Darboux小和分别为:
$$U = \sum_{i=1}^n M_i \Delta \sigma_i, \quad L = \sum_{i=1}^n m_i \Delta \sigma_i$$
当$\lambda \to 0$时, 若$U$和$L$的极限存在且相等, 则称函数$f$在区域$D$上可积, 记为:
$$\iint_D f(x,y) d\sigma = \lim_{\lambda \to 0} U = \lim_{\lambda \to 0} L$$
其充要条件为:
$$\lim_{\lambda \to 0} (U - L) = 0$$

更进一步的, 我们同样可以用振幅$\omega_i$来讨论二重积分的存在性. 设$\omega_i = M_i - m_i$, 则当$\lambda \to 0$时, 若$\sum_{i=1}^n \omega_i \Delta \sigma_i$的极限存在且为$0$, 则称函数$f$在区域$D$上可积, 记为:
$$\iint_D f(x,y) d\sigma = \lim_{\lambda \to 0} \sum_{i=1}^n M_i \Delta \sigma_i = \lim_{\lambda \to 0} \sum_{i=1}^n m_i \Delta \sigma_i$$
其充要条件为:
$$\lim_{\lambda \to 0} \sum_{i=1}^n \omega_i \Delta \sigma_i = 0$$

根据上述定义我们很容易得到:

**若函数$f$在零边界闭区域$D$上连续, 则$f$在$D$上可积.**

#### 多重积分的概念与性质

多重积分的定义与二重积分的定义完全类似, 只是我们需要把区域$D$替换成$R^n$中的一个区域, 把面积$\Delta \sigma_i$替换成体积$\Delta V_i$, 把二重积分$\iint_D f(x,y) d\sigma$替换成$n$重积分$\iiint_D f(x_1,x_2,\cdots,x_n) dV$. 这里我们不再赘述.

**质心的计算**:

$$\begin{aligned}
&\bar{x} = \frac{1}{mD} \iint_D x f(x,y) d\sigma \\
&\bar{y} = \frac{1}{mD} \iint_D y f(x,y) d\sigma
\end{aligned}$$

$$mD = \iint_D f(x,y) d\sigma$$

其中$f(x,y)$是区域$D$上每个点的密度函数.

对于三维物体:

$$\begin{aligned}
&\bar{x} = \frac{1}{mD} \iiint_D x f(x,y,z) dV \\
&\bar{y} = \frac{1}{mD} \iiint_D y f(x,y,z) dV \\
&\bar{z} = \frac{1}{mD} \iiint_D z f(x,y,z) dV
\end{aligned}$$

$$mD = \iiint_D f(x,y,z) dV$$

其中$f(x,y,z)$是区域$D$上每个点的密度函数.

### 性质

我们主要以二重积分为例讨论.

- **线性性质**: 设函数$f$和$g$在区域$D$上可积, 则对于任意常数$a$和$b$, 函数$af + bg$在区域$D$上也可积, 且有:
$$\iint_D (af + bg) d\sigma = a \iint_D f d\sigma + b \iint_D g d\sigma$$

- **区域可加性**: 设$\Omega_1$和$\Omega_2$是区域$D$的两个子区域, 且$\Omega_1 \cap \Omega_2 = \emptyset$, 则对于任意函数$f$在区域$D$上可积, 都有:
$$\iint_D f d\sigma = \iint_{\Omega_1} f d\sigma + \iint_{\Omega_2} f d\sigma$$

- **保序性质**: 设函数$f$和$g$在区域$D$上可积, 且对于任意$(x,y) \in D$, 都有$f(x,y) \leq g(x,y)$, 则有:
$$\iint_D f d\sigma \leq \iint_D g d\sigma$$

- **绝对可积性**: 设函数$f$在区域$D$上可积, 则函数$|f|$在区域$D$上也可积, 且有:
$$\left| \iint_D f d\sigma \right| \leq \iint_D |f| d\sigma$$

- **积分中值定理**: 设$f$和$g$在区域$D$上可积, 且$g$不变号, 则存在$\xi \in [\inf_{(x,y) \in D} f(x,y), \sup_{(x,y) \in D} f(x,y)]$, 使得:
$$\iint_D f g d\sigma = \xi \iint_D g d\sigma$$
进一步的, 若函数$f$在区域$D$上连续, 则存在$(x_0,y_0) \in D$, 使得:
$$\iint_D f g d\sigma = f(x_0,y_0) \iint_D g d\sigma$$