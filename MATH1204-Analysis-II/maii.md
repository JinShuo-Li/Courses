# 数学分析 II

本课程编号为`MATH1204`, 是课程`MATH1203`的后继课程.

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



2. Weierstrass 判别法
设函数项级数$\sum_{n=1}^{\infty} u_n(x)$满足$|u_n(x)| \leq a_n$对于所有$n \in \mathbb{N}^*$和所有$x \in D$, 其中$\sum_{n=1}^{\infty} a_n$是一个收敛的数项级数, 则函数项级数$\sum_{n=1}^{\infty} u_n(x)$在$D$上一致收敛.
证明: 直接利用Cauchy一致收敛判别法即可. 这里从略.



3. A-D判别法
若函数项级数$\sum_{n=1}^{\infty} a_n(x)\cdot b_n(x)$满足下面两个条件之一, 则函数项级数$\sum_{n=1}^{\infty} a_n(x)\cdot b_n(x)$在$D$上一致收敛.
- $a_n(x)$在$D$上对固定的$x$, 随着$n$的增大单调, 且一致有界. 且函数项级数$\sum_{n=1}^{\infty} b_n(x)$在$D$上一致收敛.
- $a_n(x)$在$D$上对固定的$x$, 随着$n$的增大单调, 且一致收敛于0. 且函数项级数$\sum_{n=1}^{\infty} b_n(x)$在$D$上一致有界.
这里的证明需要用到Abel引理, 即:
**Abel引理**: 设数列$\{a_n\}$满足对于任意$n \in \mathbb{N}^*$, 都有$|a_n| \leq M$且对于任意$n \in \mathbb{N}^*$, 都有$a_{n+1} \leq a_n$. 设数列$\{b_n\}$满足对于任意$n \in \mathbb{N}^*$, 都有$|b_1 + b_2 + \cdots + b_n| \leq N$. 则对于任意$n \in \mathbb{N}^*$, 都有:
$$|a_1 b_1 + a_2 b_2 + \cdots + a_n b_n| \leq 2MN$$
证明: 直接利用数列的单调性和有界性即可. 这里从略.





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



同理, 根据前面提及的三大性质, 可以得到幂级数在$(-R,R)$上保持连续性、可微性、可积性等分析性质. 这里从略.



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



同理我们也可以得到**Cantor闭区域套定理**. 这里我们不再赘述.

**Bolzano-Weierstrass定理**

在正式阐述Bolzano-Weierstrass定理之前, 我们需要定义一下什么是有界性:

**定义**: 设$E$是$R^n$中的一个集合, 如果存在一个实数$M > 0$, 使得对于任意$x \in E$, 都有$\|x\| < M$, 则称集合$E$是一个有界集.

**定理**(Bolzano-Weierstrass定理): 设$\{x_n\}$是$R^n$中的一个数列, 如果数列$\{x_n\}$是有界的, 则数列$\{x_n\}$存在一个收敛的子数列.

**证明思路**: 先在第一个坐标上利用Bolzano-Weierstrass定理找到一个收敛的子数列, 然后在第二个坐标上利用Bolzano-Weierstrass定理找到一个收敛的子数列, 以此类推, 最后得到一个收敛的子数列. 这里从略.



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

#### 计算

- **矩形区域上的重积分计算**:

设函数$f$在矩形区域$D = [a,b] \times [c,d]$上可积, 则有:
$$\iint_D f(x,y) d\sigma = \int_c^d \left( \int_a^b f(x,y) dx \right) dy = \int_a^b \left( \int_c^d f(x,y) dy \right) dx$$

采用更一般的记号, 我们可以写作:
$$\iint_D f(x,y) d\sigma = \int_c^d dy \int_a^b f(x,y) dx = \int_a^b dx \int_c^d f(x,y) dy$$

在我们会遇到的情况中, 由于函数$f$在矩形区域$D$上连续, 因此函数$f$在矩形区域$D$上可积, 上述公式中的积分都存在且相等. **重积分可以利用累次积分来计算.**

由本定理直接得到:

假设$f(x)$在$x\in [a,b]$上可积, $g(y)$在$y \in [c,d]$上可积, 则函数$f(x)g(y)$在矩形区域$D = [a,b] \times [c,d]$上可积, 且有:
$$\iint_D f(x)g(y) d\sigma = \int_c^d g(y) dy \cdot \int_a^b f(x) dx$$

- **一般区域上的重积分计算**

设函数$f$在区域$D$上可积, 且区域$D$满足如下条件:
$$D = \{ (x,y) | y_1(x) \leq y \leq y_2(x), a \leq x \leq b \}$$

其中函数$y_1(x)$和$y_2(x)$在区间$[a,b]$上连续, 则有:
$$\iint_D f(x,y) d\sigma = \int_a^b dx \int_{y_1(x)}^{y_2(x)} f(x,y) dy$$

推导如下: 我们记$c=\min_{x \in [a,b]} y_1(x)$, $d = \max_{x \in [a,b]} y_2(x)$, 则$D$被包含在矩形区域$[a,b] \times [c,d]$内. 因为原来的函数在定义域上会产生冲突, 我们重新定义一个函数$\tilde{f}(x,y)$:

$$\tilde{f}(x,y) = \begin{cases}
f(x,y), & y_1(x) \leq y \leq y_2(x) \\
0, & \text{Otherwise}
\end{cases}$$

则函数$\tilde{f}$在矩形区域$[a,b] \times [c,d]$上连续, 因此函数$\tilde{f}$在矩形区域$[a,b] \times [c,d]$上可积. 因为:

$$
\int_a^b \tilde{f} (x,y) dy = \int_{c}^{y_1(x)} 0 dy + \int_{y_1(x)}^{y_2(x)} f(x,y) dy + \int_{y_2(x)}^d 0 dy = \int_{y_1(x)}^{y_2(x)} f(x,y) dy
$$

我们很容易可以推出:

$$\iint_D f(x,y) d\sigma = \iint_{[a,b] \times [c,d]} \tilde{f}(x,y) d\sigma = \int_a^b dx \int_c^d \tilde{f}(x,y) dy = \int_a^b dx \int_{y_1(x)}^{y_2(x)} f(x,y) dy$$

即为我们想要的结果.

### 变量代换

由于二维与更高维的变换具有和一维上的变换不同的性质, 我们先介绍**曲线坐标**.

#### 曲线坐标

设$U$为$uv$平面上的一个开集, $V$为$xy$平面上的一个开集, 映射:

$$T: x = x(u,v), y = y(u,v)$$

是一个从$U$到$V$的一一映射, 则称$T$为一个曲线坐标变换. 相应的有逆变换$T^{-1}$.

在$U$中取直线$u=u_0$和$v=v_0$, 则在$V$中分别得到两条曲线, 分别称作$v$线和$u$线. 由于映射$T$是一一对应的, 因此$V$中的每个点既可以用$xy$坐标表示, 也可以用$uv$坐标表示. 那么我们称两个坐标系之间的关系为**曲线坐标变换**.

#### 二重积分的变量代换

设$x=x(u,v), y=y(u,v)$是一个从$U$到$V$的曲线坐标变换, 且具有连续偏导数. 且$\frac{\partial (x,y)}{\partial (u,v)} \neq 0$, 假设$f(x,y)$在区域$T(D)$上可积, 则有:

$$
\iint_{T(D)} f(x,y) dxdy = \iint_D f(x(u,v), y(u,v)) \left| \frac{\partial (x,y)}{\partial (u,v)} \right| du dv
$$

这里可以说明一下, Jacobi行列式:
$$\frac{\partial (x,y)}{\partial (u,v)} = \begin{vmatrix}\frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} \\ \frac{\partial y}{\partial u} & \frac{\partial y}{\partial v} \end{vmatrix}$$

实际上可以视作从$D$中的一个小矩形$\Delta u \times \Delta v$到$T(D)$中的一个小平行四边形的面积的比值. 这实际上也和行列式的几何意义不谋而合.

一种非常常见的代换是**极坐标变换**. 设$x=r \cos \theta$, $y = r \sin \theta$, 则有:

$$\iint_D f(x,y) dx dy = \iint_{D'} f(r \cos \theta, r \sin \theta) r dr d\theta$$

这里的Jacobi行列式可以写作:

$$\frac{\partial (x,y)}{\partial (r,\theta)} = \begin{vmatrix}\cos \theta & -r \sin \theta \\ \sin \theta & r \cos \theta \end{vmatrix} = r$$

#### 多重积分的变量代换

设$x_1 = x_1(u_1,u_2,\cdots,u_n), x_2 = x_2(u_1,u_2,\cdots,u_n), \cdots, x_n = x_n(u_1,u_2,\cdots,u_n)$是一个从$U$到$V$的曲线坐标变换, 且具有连续偏导数. 且$\frac{\partial (x_1,x_2,\cdots,x_n)}{\partial (u_1,u_2,\cdots,u_n)} \neq 0$, 假设$f(x_1,x_2,\cdots,x_n)$在区域$T(D)$上可积, 则有:
$$\iiint_{T(D)} f(x_1,x_2,\cdots,x_n) dx_1 dx_2 \cdots dx_n = \iiint_D f(x_1(u_1,u_2,\cdots,u_n), x_2(u_1,u_2,\cdots,u_n), \cdots, x_n(u_1,u_2,\cdots,u_n)) \left| \frac{\partial (x_1,x_2,\cdots,x_n)}{\partial (u_1,u_2,\cdots,u_n)} \right| du_1 du_2 \cdots du_n$$

其中Jacobi行列式为:
$$\frac{\partial (x_1,x_2,\cdots,x_n)}{\partial (u_1,u_2,\cdots,u_n)} = \begin{vmatrix}\frac{\partial x_1}{\partial u_1} & \frac{\partial x_1}{\partial u_2} & \cdots & \frac{\partial x_1}{\partial u_n} \\ \frac{\partial x_2}{\partial u_1} & \frac{\partial x_2}{\partial u_2} & \cdots & \frac{\partial x_2}{\partial u_n} \\ \vdots & \vdots & \ddots & \vdots \\ \frac{\partial x_n}{\partial u_1} & \frac{\partial x_n}{\partial u_2} & \cdots & \frac{\partial x_n}{\partial u_n} \end{vmatrix}$$

在多重积分中有两类非常常见的代换, 分别是**柱面坐标变换**和**球坐标变换**.

柱面坐标变换: 设$x = r \cos \theta$, $y = r \sin \theta$, $z = z$, 则有:
$$\iiint_D f(x,y,z) dx dy dz = \iiint_{D'} f(r \cos \theta, r \sin \theta, z) r dr d\theta dz$$

球坐标变换: 设$x = r \sin \varphi \cos \theta$, $y = r \sin \varphi \sin \theta$, $z = r \cos \varphi$, 则有:
$$\iiint_D f(x,y,z) dx dy dz = \iiint_{D'} f(r \sin \varphi \cos \theta, r \sin \varphi \sin \theta, r \cos \varphi) r^2 \sin \varphi dr d\varphi d\theta$$

它们的Jacobi行列式分别为:
$$\frac{\partial (x,y,z)}{\partial (r,\theta,z)} = \begin{vmatrix}\cos \theta & -r \sin \theta & 0 \\ \sin \theta & r \cos \theta & 0 \\ 0 & 0 & 1 \end{vmatrix} = r$$

$$\frac{\partial (x,y,z)}{\partial (r,\varphi,\theta)} = \begin{vmatrix}\sin \varphi \cos \theta & r \cos \varphi \cos \theta & -r \sin \varphi \sin \theta \\ \sin \varphi \sin \theta & r \cos \varphi \sin \theta & r \sin \varphi \cos \theta \\ \cos \varphi & -r \sin \varphi & 0\end{vmatrix} = r^2 \sin \varphi$$

## 曲线积分, 曲面积分和场论

### 曲线积分

对于空间中曲线长度问题, 设曲线$L$可以用参数方程表示为:
$$L: \begin{cases}
x = x(t) \\
y = y(t) \\
z = z(t)
\end{cases} \quad t \in [a,b]$$

其中$x(t), y(t), z(t)$在$[a,b]$上连续可导. 将$[a,b]$划分为$n$个小区间$[t_{i-1}, t_i]$, 在每一小段上取对应的曲线弧长为$
\Delta s_i$. 当划分加细时, 曲线$L$的长度定义为:
$$
S = \lim_{\lambda \to 0} \sum_{i=1}^n \Delta s_i
$$
其中$\lambda = \max\{t_i - t_{i-1}\}$. 由弧长公式可知:
$$
S = \int_a^b \sqrt{(x'(t))^2 + (y'(t))^2 + (z'(t))^2} \, dt
$$
因此我们记弧长微元为:
$$
ds = \sqrt{(x'(t))^2 + (y'(t))^2 + (z'(t))^2} \, dt
$$

#### 第一类曲线积分

设$L$是$R^3$中的一条光滑曲线, 则对于一个定义在$L$上的函数$f$, 我们可以定义**曲线积分**:
$$\int_L f(x,y,z) ds = \lim_{\lambda \to 0} \sum_{i=1}^n f(P_i) \Delta s_i$$

其中$\lambda = \max \{\text{diam}(\Delta L_i) : i=1,2,\cdots,n\}$, $\Delta s_i$是曲线$L$上小段$\Delta L_i$的长度, $P_i$是小段$\Delta L_i$上的一个点.

其中$f(x,y,z)$可以理解为曲线$L$上每个点的密度函数, 因此曲线积分可以理解为沿着曲线$L$的一个质量.

$f(x,y,z)$被称作被积函数. $L$被称作积分路径.

同二重积分一样的, 曲线积分一样具有线性性, 路径可加性等性质.

下面介绍如何计算第一类曲线积分:

**定理**: 设$L$是光滑曲线, 函数$f(x,y,z)$在$L$上连续. 且L可以写作:

$$L: \begin{cases}
x = x(t) \\
y = y(t) \\
z = z(t)
\end{cases} \quad t \in [a,b]$$

则有:
$$\int_L f(x,y,z) ds = \int_a^b f(x(t), y(t), z(t)) \sqrt{(x'(t))^2 + (y'(t))^2 + (z'(t))^2} dt$$

这里很显然, 因为$L$连续, 那么有:

$$\Delta s_i = \int_{t_{i-1}}^{t_i} \sqrt{(x'(t))^2 + (y'(t))^2 + (z'(t))^2} dt$$

取$P_i$为$\Delta L_i$上对应的点, 则有:

$$f(P_i) \Delta s_i = f(x(t_i), y(t_i), z(t_i)) \int_{t_{i-1}}^{t_i} \sqrt{(x'(t))^2 + (y'(t))^2 + (z'(t))^2} dt$$

因此当$\lambda \to 0$时, 上式的求和就变成了定积分, 从而得到了上述的结果.

**性质**:

- **线性性质**: 设函数$f$和$g$在曲线$L$上连续, 则对于任意常数$a$和$b$, 函数$af + bg$在曲线$L$上也连续, 且有:
$$\int_L (af + bg) ds = a \int_L f ds + b \int_L g ds$$

- **路径可加性**: 设$L_1$和$L_2$是曲线$L$的两条子曲线, 且$L_1 \cap L_2 = \emptyset, \quad L = L_1 \cup L_2$, 则对于任意函数$f$在曲线$L$上连续, 都有:
$$\int_L f ds = \int_{L_1} f ds + \int_{L_2} f ds$$

#### 第二类曲线积分

第二类曲线积分在物理意义上可以理解为沿着曲线$L$, 力$\vec{F}$对位移$\vec{r}$做的功.

设$L$是$R^3$中的一条光滑曲线, 则对于一个定义在$L$上的向量函数$\vec{F} = (P(x,y,z), Q(x,y,z), R(x,y,z))$, 我们可以定义**第二类曲线积分**:

$$\int_L \vec{F} \cdot d\vec{r} = \lim_{\lambda \to 0} \sum_{i=1}^n \vec{F}(P_i) \cdot \Delta \vec{r}_i$$

我们记在$(x,y,z)$点处的切向量为$\vec{r}'(t) = (x'(t), y'(t), z'(t))$, 则有:

$$d\vec{r} = \vec{r}'(t) dt$$

**定理**: 设$L$是光滑曲线, 向量函数$\vec{F} = (P(x,y,z), Q(x,y,z), R(x,y,z))$在$L$上连续. 且L可以写作:

$$L: \begin{cases}
x = x(t) = \cos \alpha \\
y = y(t) = \cos \beta \\
z = z(t) = \cos \gamma
\end{cases} \quad t \in [a,b]$$

其中单位切向量可以写作:

$$\vec{T} = \frac{\vec{r}'(t)}{\|\vec{r}'(t)\|} = (\cos \alpha, \cos \beta, \cos \gamma)$$

则有:

$$\int_L \vec{F} \cdot d\vec{r} = \int_a^b [P(x, y, z) \cos \alpha + Q(x, y, z) \cos \beta + R(x, y, z) \cos \gamma] ds$$

我们必须强制给$L$一个方向, 否则这个积分将无法定义. 这是积分的要求.

第二类曲线积分具有一系列性质:

- **方向性**: 记$-L$为曲线$L$的反向, 则有:
$$
\int_{-L} \vec{F} \cdot d\vec{r} = - \int_L \vec{F} \cdot d\vec{r}
$$

- **线性性质**: 设向量函数$\vec{F}$和$\vec{G}$在曲线$L$上连续, 则对于任意常数$a$和$b$, 向量函数$a\vec{F} + b\vec{G}$在曲线$L$上也连续, 且有:
$$
\int_L (a\vec{F} + b\vec{G}) \cdot d\vec{r} = a \int_L \vec{F} \cdot d\vec{r} + b \int_L \vec{G} \cdot d\vec{r}
$$

第二类曲线积分的具体计算方法如下:

设光滑曲线$L$可以用参数方程表示为:

$$x = x(t), \quad y = y(t), \quad z = z(t)$$

这里$t: a \to b$足够表征曲线的方向. 我们就采用$a$到$b$的方向, 且$a < b$. 则单位切向量可以写作:

$$
\vec{\tau} = \frac{\vec{r}'(t)}{\|\vec{r}'(t)\|} = \frac{1}{\sqrt{x'^2(t)+ y'^2(t)+ z'^2(t)}} (x'(t), y'(t), z'(t)) = (\cos \alpha, \cos \beta, \cos \gamma)
$$

同时, 弧长微元可以写作:

$$
ds = \sqrt{(x'(t))^2 + (y'(t))^2 + (z'(t))^2} dt
$$

我们发现根式刚好可以抵消掉分母, 从而得到:

$$
\int_L P(x,y,z) dx + Q(x,y,z) dy + R(x,y,z) dz = \int_a^b [P(x, y, z) x'(t) + Q(x, y, z) y'(t) + R(x, y, z) z'(t)] dt
$$

### 曲面积分

**曲面的面积问题**

设曲面$\Sigma$的方程为:

$$x=x(u,v), \quad y=y(u,v), \quad z=z(u,v)$$

即: $\vec{r}(u,v) = (x(u,v), y(u,v), z(u,v)), \quad (u,v) \in D$, 其中$D$是$uv$平面上的一个具有光滑边界的有界闭区间. 相应的Jacobi矩阵为:

$$J = \frac{\partial (x,y,z)}{\partial (u,v)}=\begin{pmatrix}\frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} \\ \frac{\partial y}{\partial u} & \frac{\partial y}{\partial v} \\ \frac{\partial z}{\partial u} & \frac{\partial z}{\partial v} \end{pmatrix}$$

利用Jacobi矩阵我们可以在$uv$平面上的小区域和$xyz$空间中的小曲面$\Sigma$中建立一个映射关系, 从而可以把$uv$平面上的面积元素$du dv$映射到$xyz$空间中的面积元素$dS$. 我们先考虑$uv$平面中的小矩形$P_1P_2P_3P_4$, 其中$P_1 = (u,v)$, $P_2 = (u+\Delta u, v)$, $P_3 = (u+\Delta u, v+\Delta v)$, $P_4 = (u, v+\Delta v)$. 则在$xyz$空间中对应的四个点分别为:
$$\begin{aligned}&\vec{r}(P_1) = (x(u,v), y(u,v), z(u,v)) \\
&\vec{r}(P_2) = (x(u+\Delta u, v), y(u+\Delta u, v), z(u+\Delta u, v)) \\
&\vec{r}(P_3) = (x(u+\Delta u, v+\Delta v), y(u+\Delta u, v+\Delta v), z(u+\Delta u, v+\Delta v)) \\
&\vec{r}(P_4) = (x(u, v+\Delta v), y(u, v+\Delta v), z(u, v+\Delta v)) \end{aligned}$$

我们可以近似的把$P_1P_2P_3P_4$映射成一个平行四边形, 其面积的计算可以用外积来完成, 也就是$\Delta S = \| \vec{P_1P_2} \times \vec{P_1P_4} \|$.

显然, u曲线和v曲线在$P_1$处的切向量分别为$\vec{r}_u(u,v)$和$\vec{r}_v(u,v)$, 因此$\vec{P_1P_2}$和$\vec{P_1P_4}$分别可以近似的表示为$\vec{r}_u(u,v) \Delta u$和$\vec{r}_v(u,v) \Delta v$, 误差项分别为$o(\Delta u)$和$o(\Delta v)$, 所以我们不难得知

$$
\begin{aligned}
    \vec{Q_1Q_2} = \vec{r}(P_2) - \vec{r}(P_1) &= \vec{r}_u (u,v) \Delta u + o(\Delta u) \\
    \vec{Q_1Q_4} = \vec{r}(P_4) - \vec{r}(P_1) &= \vec{r}_v (u,v) \Delta v + o(\Delta v)
\end{aligned}
$$

根据这个指导思想, 我们可以完成以下运算:

$$
dS = \| \vec{Q_1Q_2} \times \vec{Q_1Q_4} \| = \| (\vec{r}_u (u,v) \Delta u + o(\Delta u)) \times (\vec{r}_v (u,v) \Delta v + o(\Delta v)) \| = \| \vec{r}_u (u,v) \times \vec{r}_v(u,v) \| du dv
$$

所以曲面的面积可以表示为:

$$
S = \iint_D \| \vec{r}_u (u,v) \times \vec{r}_v(u,v) \| du dv
$$

更具体的计算方法如下:

$$
\begin{aligned}
    S &= \iint_D \| \vec{r}_u (u,v) \times \vec{r}_v(u,v) \| du dv \\
    &= \iint_D \left|
    \begin{vmatrix}
        \vec{i} & \vec{j} & \vec{k} \\
        \frac{\partial x}{\partial u} & \frac{\partial y}{\partial u} & \frac{\partial z}{\partial u} \\
        \frac{\partial x}{\partial v} & \frac{\partial y}{\partial v} & \frac{\partial z}{\partial v}
    \end{vmatrix}
    \right| du dv \\
    &= \iint_D \sqrt{\left( \frac{\partial y}{\partial u} \frac{\partial z}{\partial v} - \frac{\partial z}{\partial u} \frac{\partial y}{\partial v} \right)^2 + \left( \frac{\partial z}{\partial u} \frac{\partial x}{\partial v} - \frac{\partial x}{\partial u} \frac{\partial z}{\partial v} \right)^2 + \left( \frac{\partial x}{\partial u} \frac{\partial y}{\partial v} - \frac{\partial y}{\partial u} \frac{\partial x}{\partial v} \right)^2 } du dv \\
    &= \iint_D \sqrt{EG-F^2} du dv
\end{aligned}
$$

$$E = \vec{r}_u \cdot \vec{r}_u$$
$$F = \vec{r}_u \cdot \vec{r}_v$$ 
$$G = \vec{r}_v \cdot \vec{r}_v$$

现在考虑两种特殊情况:

1. 当曲面$\Sigma$可以用一个函数$z=f(x,y)$来表示时, 则有:

$$\begin{aligned}
S &= \iint_D \sqrt{EG-F^2} du dv \\
&= \iint_D \sqrt{1 + \left( \frac{\partial z}{\partial x} \right)^2 + \left( \frac{\partial z}{\partial y} \right)^2} dx dy
\end{aligned}$$

2. 当曲面可以用一个方程$H(x,y,z) = 0$来表示时, 则有:
$$
S = \iint_D \sqrt{EG-F^2} du dv = \iint_D \frac{\| \text{grad} H \|}{\|H_z\|} dx dy
$$

#### 第一类曲面积分

设$\Sigma$是$R^3$中的一个光滑曲面, 则对于一个定义在$\Sigma$上的函数$f$, 我们可以定义**曲面积分**:
$$\iint_{\Sigma} f(x,y,z) dS = \lim_{\lambda \to 0} \Sigma_{i=1}^n f(P_i) \Delta S_i$$

设$\Sigma$的方程为:

$$x=x(u,v), \quad y=y(u,v), \quad z=z(u,v)$$

我们采用类似的技巧来计算第一类曲面积分, 这里省略过程:

$$\iint_{\Sigma} f(x,y,z) dS = \iint_D f(x(u,v), y(u,v), z(u,v)) \sqrt{EG-F^2} du dv$$

特别的, 当曲面$\Sigma$可以用一个函数$z=g(x,y)$来表示时, 则有:

$$\iint_{\Sigma} f(x,y,z) dS = \iint_D f(x,y,g(x,y)) \sqrt{1 + \left( \frac{\partial g}{\partial x} \right)^2 + \left( \frac{\partial g}{\partial y} \right)^2} dx dy$$

#### 第二类曲面积分

为了引入第二类曲面积分, 我们需要对曲面的定义做一些修改和调整. 我们需要定义什么是曲面的**侧**.

**曲面的侧**

设$\Sigma$是一张光滑曲面, $P$为曲面上任意一点, $\Gamma_P$是过点$P$且不经过曲面边界的任意一条闭曲线, 取定$\Sigma$在$P$处的一个单位法向量, 倘若该向量沿着$\Gamma_P$的方向旋转一周后仍然指向同一侧, 则称$\Sigma$为单侧曲面.

我们的积分将沿着一侧完成.

前面我们已经知道, 曲面的法向量可以表示为:

$$
\pm r_u \times r_v = \pm \left( \frac{\partial(y,z)}{\partial(u,v)}, \frac{\partial(z,x)}{\partial(u,v)}, \frac{\partial(x,y)}{\partial(u,v)} \right)
$$

所以单位法向量可以写作:

$$
\vec{n} = (\cos \alpha, \cos \beta, \cos \gamma) = \frac{1}{\pm \sqrt{EG-F^2}} \left( \frac{\partial(y,z)}{\partial(u,v)}, \frac{\partial(z,x)}{\partial(u,v)}, \frac{\partial(x,y)}{\partial(u,v)} \right)
$$

取定一个符号也就意味着取定了一个侧. 曲面的双侧性和方向余弦的连续性保证了不会在连续改变坐标的过程中翻转到另一个侧.

下面给出第二类曲面积分的定义:

设$\Sigma$是$R^3$中的一个单侧光滑曲面, 则对于一个定义在$\Sigma$上的向量函数$\vec{F} = (P(x,y,z), Q(x,y,z), R(x,y,z))$, 我们可以定义**第二类曲面积分**:

假设曲面上每一点都有一个单位法向量$\vec{n} = (\cos \alpha, \cos \beta, \cos \gamma)$, 则有:

$$
\begin{aligned}
    \iint_{\Sigma} \vec{F} \cdot \vec{n} dS &= \lim_{\lambda \to 0} \sum_{i=1}^n \vec{F}(P_i) \cdot \vec{n}_i \Delta S_i \\
    &= \iint_{\Sigma} [P(x,y,z) \cos \alpha + Q(x,y,z) \cos \beta + R(x,y,z) \cos \gamma] dS
\end{aligned}
$$

这就是**第二类曲面积分**的定义.

**性质**:

- **线性性质**: 设向量函数$\vec{F}$和$\vec{G}$在曲面$\Sigma$上连续, 则对于任意常数$a$和$b$, 向量函数$a\vec{F} + b\vec{G}$在曲面$\Sigma$上也连续, 且有:
$$
\iint_{\Sigma} (a\vec{F} + b\vec{G}) \cdot \vec{n} dS = a \iint_{\Sigma} \vec{F} \cdot \vec{n} dS + b \iint_{\Sigma} \vec{G} \cdot \vec{n} dS
$$

- **方向性**: 记$-\Sigma$为曲面$\Sigma$的反向, 则有:
$$
\iint_{-\Sigma} \vec{F} \cdot \vec{n} dS = - \iint_{\Sigma} \vec{F} \cdot \vec{n} dS
$$

- **曲面可加性**: 设$\Sigma_1$和$\Sigma_2$是曲面$\Sigma$的两条子曲面, 且$\Sigma_1 \cap \Sigma_2 = \emptyset, \quad \Sigma = \Sigma_1 \cup \Sigma_2$, 则对于任意向量函数$\vec{F}$在曲面$\Sigma$上连续, 都有:
$$
\iint_{\Sigma} \vec{F} \cdot \vec{n} dS = \iint_{\Sigma_1} \vec{F} \cdot \vec{n} dS + \iint_{\Sigma_2} \vec{F} \cdot \vec{n} dS
$$

下面讨论如何计算第二类曲面积分:

设$\Sigma$的方程为:

$$x=x(u,v), \quad y=y(u,v), \quad z=z(u,v)$$

则有:

$$
\begin{aligned}
\iint_{\Sigma} \vec{F} \cdot \vec{n} dS &= \iint_D [P(x,y,z) \cos \alpha + Q(x,y,z) \cos \beta + R(x,y,z) \cos \gamma] \sqrt{EG-F^2} du dv \\
&= \iint_D [P(x,y,z) \frac{\partial(y,z)}{\partial(u,v)} + Q(x,y,z) \frac{\partial(z,x)}{\partial(u,v)} + R(x,y,z) \frac{\partial(x,y)}{\partial(u,v)}] du dv
\end{aligned}
$$

**注意**: 很多时候我们会把第二类曲面积分表示为:

$$\iint_{\Sigma} P dy dz + Q dz dx + R dx dy$$

这是和外积有关的一个记号, 也就是:

$$\vec{F} \cdot \vec{n} dS = (P, Q, R) \cdot (\cos \alpha, \cos \beta, \cos \gamma) dS = P dy dz + Q dz dx + R dx dy$$

### Green公式, Stokes公式和Gauss公式

在本部分我们会对三种特殊的积分公式进行介绍, 这三种公式分别是**Green公式**, **Stokes公式**和**Gauss公式**. 这三种公式在物理学中有着非常重要的意义, 是电磁学等领域的基础.

#### Green公式

**定理**: 设$D$是$R^2$中的一个单连通有界闭区域, 如果函数$P(x,y)$和$Q(x,y)$在$D$上连续且具有连续偏导数, 则有:

$$
\int_{\partial D} P dx + Q dy = \iint_D \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dx dy
$$

其中$\partial D$表示区域$D$的边界, 取正向. 正向的约定: 取法向量指向$+z$时, 沿$\partial D$的走向为逆时针, 即右手螺旋准则中四指弯曲的方向.

**证明**: 先证明对矩形$D=[a,b]\times[c,d]$成立. 由一维微积分基本定理,
$$
\int_{\partial D} P dx + Q dy = \int_a^b P(x,c) dx - \int_a^b P(x,d) dx + \int_c^d Q(b,y) dy - \int_c^d Q(a,y) dy
$$
另一方面,
$$
\iint_D \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dx dy
= \int_c^d \int_a^b \frac{\partial Q}{\partial x} dx dy - \int_a^b \int_c^d \frac{\partial P}{\partial y} dy dx
$$
对内层积分用牛顿-莱布尼茨公式, 得到与边界积分同样的表达式, 因而矩形情形成立.

对一般单连通有界闭区域$D$, 用网格把$D$细分为若干小矩形并取其并集逼近$D$. 在每个小矩形上应用已证结论并求和, 内部公共边的线积分因方向相反相互抵消, 只剩下外边界$\partial D$上的积分. 令网格加细并取极限, 由$P,Q$的连续性及偏导连续性可把和的极限换成二重积分的极限, 从而得到
$$
\int_{\partial D} P dx + Q dy = \iint_D \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dx dy
$$

准确的说, Green公式的意义在于把**第二类曲线积分**转化成了一个**重积分**问题.

我们一般不会在笔记中记录例子, 但是在这里有一个非常有趣的应用.

如何计算椭圆$\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$所围成区域$D$的面积?

我们可以把这个问题转化成一个曲线积分问题, 注意取边界的正向(逆时针):

$$
\int_{\partial D} x dy - y dx
$$

根据Green公式, 令$P=-y,\ Q=x$, 则

$$
\iint_D \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dx dy
= \iint_D (1-(-1))\,dx dy = 2\iint_D dx dy
$$

于是
$$
\text{area}(D) = \iint_D dx dy = \frac{1}{2}\int_{\partial D} x dy - y dx
$$

再对椭圆作参数化: $x=a\cos t,\ y=b\sin t,\ t\in[0,2\pi]$. 则
$$
\begin{aligned}
\int_{\partial D} x dy - y dx
&= \int_0^{2\pi} \left(a\cos t\cdot b\cos t - b\sin t\cdot(-a\sin t)\right) dt \\
&= \int_0^{2\pi} ab(\cos^2 t + \sin^2 t)\,dt = 2\pi ab
\end{aligned}
$$
所以椭圆的面积为
$$
\text{area}(D)=\pi ab.
$$

最强大的一点是这个环路积分是生凑出来的, 但是却能得到正确的结果. 这就是Green公式的魅力所在.

另外, Green公式在物理中是有意义的. 物理中很多时候第二类曲线积分是对应于做功的, 而曲线积分中的函数$\vec{F}$则是对应于力的. 而如果在空间中两点间任意路径的曲线积分都是定值, 那么这个力就被称作**保守力**. 用数学的语言表述:

**定理**: 设$D$是$R^2$中的一个单连通有界闭区域, 如果函数$P(x,y)$和$Q(x,y)$在$D$上连续且具有连续偏导数, 则以下条件等价:

1. 对$D$内任意两点$A$和$B$, 沿着$D$内的任意路径$\Gamma$从$A$到$B$的曲线积分$\int_{\Gamma} P dx + Q dy$都是定值.
2. 对于$D$内任意一条闭曲线$\Gamma$, 曲线积分$\int_{\Gamma} P dx + Q dy = 0$.
3. 存在$D$上的可微函数$U(x,y)$, 使得$\frac{\partial U}{\partial x} = P$, $\frac{\partial U}{\partial y} = Q$, 且
$$
dU = P dx + Q dy
$$
4. 在$D$的范围内恒成立: $\frac{\partial P}{\partial y} = \frac{\partial Q}{\partial x}$

这组定理称为**Green定理**. 证明中最困难的部分是证明条件2$\Rightarrow$条件3, 其他部分的证明都比较简单.

我们给出条件2$\Rightarrow$条件3的证明:

我们任意选取定点$(x_0, y_0) \in D$, 并定义函数$U(x,y)$为:

$$
U(x,y) = \int_{\Gamma} P dx + Q dy
$$

其中$\Gamma$是$D$内任意一条从$(x_0, y_0)$到$(x,y)$的路径. 由于条件2的存在, $U(x,y)$的定义不依赖于路径的选择. 所以函数$U(x,y)$是良定义的. 接下来我们需要证明$U(x,y)$满足$\frac{\partial U}{\partial x} = P$, $\frac{\partial U}{\partial y} = Q$.

$$
\begin{aligned}
    \frac{\Delta U}{\Delta x} &= \frac{U(x+\Delta x, y)- U(x, y)}{\Delta x}\\
    &= \frac{1}{\Delta x} \left( \int_{(x_0, y_0)}^{(x+\Delta x, y)} P dx + Q dy - \int_{(x_0, y_0)}^{(x, y)} P dx + Q dy \right) \\
    &= \frac{1}{\Delta x} \int_{(x, y)}^{(x+\Delta x, y)} P dx + Q dy \\
    &= \frac{1}{\Delta x} \int_x^{x+\Delta x} P(x,y) dx \to P(x,y) \quad (\Delta x \to 0)
\end{aligned}
$$

同理可以证明$\frac{\partial U}{\partial y} = Q$. 从而完成证明.

**定理**: 设$D$是$R^2$中的一个单连通有界闭区域, 如果函数$P(x,y)$和$Q(x,y)$在$D$上连续且具有连续偏导数, 则路径积分:

$$\int_{\Gamma} P dx + Q dy$$

与路径无关的充分必要条件是在$D$上存在一个原函数$U(x,y)$, 使得:

$$
\int_{\widehat{AB}} P dx + Q dy = U(B) - U(A)
$$

#### Gauss公式

**定理**: 设$\Omega$是$R^3$中的一个单连通有界闭区域, 如果函数$P(x,y,z)$, $Q(x,y,z)$和$R(x,y,z)$在$\Omega$上连续且具有连续偏导数, 则有:

$$
\iint_{\partial \Omega} P dy dz + Q dz dx + R dx dy = \iiint_{\Omega} \left( \frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y} + \frac{\partial R}{\partial z} \right) dx dy dz
$$

Gauss公式的意义在于把**第二类曲面积分**转化成了一个**重积分**问题. 在物理上Gauss公式和闭曲面通量, 散度, 源/汇等概念有着密切的联系.

#### Stokes公式

设$\Sigma$是$R^3$中的一个单侧光滑曲面, $\partial \Sigma$是$\Sigma$的边界, 则对于一个定义在$\Sigma$上的向量函数$\vec{F} = (P(x,y,z), Q(x,y,z), R(x,y,z))$, 如果函数$P(x,y,z)$, $Q(x,y,z)$和$R(x,y,z)$在$\Sigma$上连续且具有连续偏导数, 则有:

$$
\int_{\partial \Sigma} P dx + Q dy + R dz = \iint_{\Sigma} \left( \frac{\partial R}{\partial y} - \frac{\partial Q}{\partial z} \right) dy dz + \left( \frac{\partial P}{\partial z} - \frac{\partial R}{\partial x} \right) dz dx + \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dx dy
$$

Stokes公式的意义在于把**第二类曲线积分**转化成了一个**第二类曲面积分**问题. 在物理上Stokes公式和旋度, 涡旋等概念有着密切的联系.

证明过于复杂, 我们不在这里给出. 证明的核心思想是把曲面$\Sigma$细分成若干小块, 每一小块都近似于一个平面, 从而可以应用Green公式. 最后把所有小块的结果加起来, 内部公共边的线积分因方向相反相互抵消, 只剩下边界$\partial \Sigma$上的积分.

我们利用行列式记号把Stokes公式的右边表达式写成更简洁的形式:

$$
\int_{\partial \Sigma} P dx + Q dy + R dz =
\iint_{\Sigma} \begin{vmatrix}\vec{i} & \vec{j} & \vec{k} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ P & Q & R \end{vmatrix} \cdot \vec{n} dS
= \iint_{\Sigma}
\begin{vmatrix}
    \cos \alpha & \cos \beta & \cos \gamma \\
    \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\
    P & Q & R
\end{vmatrix} dS
$$

日常应用我们一般会采取后面给出的这种形式用来计算.

### 场论

我们为了了更好的理解Green公式, Stokes公式和Gauss公式, 需要引入一些物理学中的概念, 这些概念在电磁学等领域有着非常重要的意义.

### 梯度

对于一个定义在$R^3$上的标量函数$f(x,y,z)$, 我们可以定义它的**梯度**为:

$$
\text{grad} f = \nabla f = \left( \frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \frac{\partial f}{\partial z} \right)
$$

产生的新的函数$\nabla f$是一个向量函数, 其每个分量都是$f$的偏导数. 梯度的物理意义在于它表示了函数$f$在空间中的变化率和变化方向.

### 散度

对于一个定义在$R^3$上的向量函数$\vec{F} = (P(x,y,z), Q(x,y,z), R(x,y,z))$, 我们可以定义它的**散度**为:

$$
\text{div} \vec{F} = \nabla \cdot \vec{F} = \frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y} + \frac{\partial R}{\partial z}
$$

梯度和散度的差异在于梯度面对的是标量函数, 而散度面对的是向量函数. 梯度产生了一个向量函数, 而散度产生了一个标量函数. 散度的物理意义在于它表示了向量函数$\vec{F}$在空间中的发散程度, 也就是源/汇的强弱.

### 旋度

对于一个定义在$R^3$上的向量函数$\vec{F} = (P(x,y,z), Q(x,y,z), R(x,y,z))$, 我们可以定义它的**旋度**为:

$$
\text{curl} \vec{F} = \nabla \times \vec{F} = \left( \frac{\partial R}{\partial y} - \frac{\partial Q}{\partial z}, \frac{\partial P}{\partial z} - \frac{\partial R}{\partial x}, \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right)
$$

旋度的物理意义在于它表示了向量函数$\vec{F}$在空间中的旋转程度, 也就是涡旋的强弱.

### 保守场和势能

对于一个定义在$R^3$上的向量函数$\vec{F} = (P(x,y,z), Q(x,y,z), R(x,y,z))$, 如果存在一个标量函数$U(x,y,z)$, 使得$\nabla U = \vec{F}$, 则称$\vec{F}$为**保守场**, $U$为$\vec{F}$的**势能**. 保守场的物理意义在于它表示了一个力场, 其做功只与起点和终点的位置有关, 与路径无关. 势能的物理意义在于它表示了一个系统的能量状态, 其数值大小反映了系统的稳定程度.

关于场论部分, 关于能量部分有兴趣可以参考我的分析力学的笔记. 那里做了比较详细的阐述, 也有更理论性的表述.

## 含参变量积分

含参变量的积分本质上就是对一个多元函数, 但是积分变量只是对其中一个变量进行积分, 其他变量则被当作参数来处理. 比如:

$$
\begin{aligned}
    I(y) = \int_a^b f(x,y) dx \\
    J(x) = \int_a^b f(x,y) dy
\end{aligned}
$$

### 含参变量的常义积分

#### 性质

**连续性定理**: 设$f(x,y)$在闭矩形$D=[a,b] \times [c,d]$
上连续, 则函数:

$$
I(y) = \int_a^b f(x,y) dx
$$

在$[c,d]$上连续.

由这个定理我们可以直接推出下面的表达式, 也就是极限运算和积分运算可交换:

$$
\lim_{y \to y_0} \int_a^b f(x,y) dx = \int_a^b \lim_{y \to y_0} f(x,y) dx
$$

**积分次序交换定理**: 设$f(x,y)$在$D=[a,b] \times [c,d]$上连续, 那么:

$$
\int_c^d dy \int_a^b f(x,y) dx = \int_a^b dx \int_c^d f(x,y) dy
$$

**积分号下求导定理**: 设$f(x,y)$和$f_y(x,y)$都在闭矩形$D=[a,b] \times [c,d]$上连续, 则$I_y = \int_a^b f(x,y) dx$在$[c,d]$上可导. 且:

$$
\frac{d}{dy} I(y) = \int_a^b f_y(x,y) dx
$$

### 含参变量的反常积分

类似传统的反常积分, 含参变量的反常积分也可以分成两类, 一类是积分区间无界, 另一类是被积函数存在瑕点.

#### 反常积分的一致收敛性

在这里我们分成两类讨论. 类似函数项级数, 反常积分也有一致收敛性的概念. 反常积分的一致收敛性是指对于一个含参变量的反常积分, 当参数在某个区间内变化时, 反常积分的值能够以某种方式趋近于一个极限值, 并且这个极限值与参数无关.

- **无穷区间的反常积分的一致收敛性**

**定义**: 设$f(x,y)$在$[a,+\infty) \times [c,d]$上连续, 则反常积分$\int_a^{+\infty} f(x,y) dx$在$[c,d]$上一致收敛, 如果存在一个函数$F(y)$使得对于任意$\varepsilon > 0$, 存在一个常数$M > a$, 当$x > M$时, 对于任意$y \in [c,d]$, 都有:

$$
\left| \int_M^{+\infty} f(x,y) dx \right| < \varepsilon
$$

- **瑕点的反常积分的一致收敛性**

**定义**: 设$f(x,y)$在$(a,b] \times [c,d]$上连续, 则反常积分$\int_a^b f(x,y) dx$在$[c,d]$上一致收敛, 如果存在一个函数$F(y)$使得对于任意$\varepsilon > 0$, 存在一个常数$\delta > 0$, 当$0 < x - a < \delta$时, 对于任意$y \in [c,d]$, 都有:

$$
\left| \int_a^{a+\delta} f(x,y) dx \right| < \varepsilon
$$

#### 一致收敛的判别法

**Cauchy判别法**:

含参变量的反常积分 $\int_a^{+\infty} f(x,y) dx$ 在 $[c,d]$ 上一致收敛的充要条件是：对于任意 $\varepsilon > 0$，存在常数 $M > a$，使得对于任意的 $A_1, A_2 > M$ 及任意的 $y \in [c,d]$，都有：
$$
\left| \int_{A_1}^{A_2} f(x,y) dx \right| < \varepsilon
$$

**Weierstrass M-test**:

设函数 $f(x,y)$ 在 $[a, +\infty) \times [c,d]$ 上连续。如果存在一个仅依赖于 $x$ 的非负函数 $g(x)$ (称为优函数)，使得对于所有的 $x \in [a, +\infty)$ 和 $y \in [c,d]$，都有 $|f(x,y)| \le g(x)$，并且反常积分 $\int_a^{+\infty} g(x) dx$ 收敛，则含参变量反常积分 $\int_a^{+\infty} f(x,y) dx$ 在 $[c,d]$ 上绝对收敛且一致收敛。

**Abel判别法**:

设 $f(x,y)$ 和 $g(x,y)$ 在 $[a, +\infty) \times [c,d]$ 上连续，且满足以下两个条件：
1. 积分 $\int_a^{+\infty} f(x,y) dx$ 在 $[c,d]$ 上一致收敛;
2. 对任意固定的 $y \in [c,d]$, 函数 $g(x,y)$ 关于 $x$ 单调，并且在 $[a, +\infty) \times [c,d]$ 上一致有界(即存在常数 $M > 0$，使得 $|g(x,y)| \le M$).

则反常积分 $\int_a^{+\infty} f(x,y)g(x,y) dx$ 在 $[c,d]$ 上一致收敛。

**Dirichlet判别法**:

设 $f(x,y)$ 和 $g(x,y)$ 在 $[a, +\infty) \times [c,d]$ 上连续，且满足以下两个条件:
1. 积分 $\int_a^A f(x,y) dx$ 在 $[c,d]$ 上一致有界(即存在常数 $M > 0$，使得对于所有 $A > a$ 和 $y \in [c,d]$ 都有 $\left| \int_a^A f(x,y) dx \right| \le M$);
2. 对任意固定的 $y \in [c,d]$，函数 $g(x,y)$ 关于 $x$ 单调, 并且当 $x \to +\infty$ 时, $g(x,y)$ 关于 $y$ 在 $[c,d]$ 上一致趋近于 0.

则反常积分 $\int_a^{+\infty} f(x,y)g(x,y) dx$ 在 $[c,d]$ 上一致收敛.

#### 一致收敛的分析性质

1. **连续性**: 如果 $f(x,y)$ 在 $[a, +\infty) \times [c,d]$ 上连续, 且反常积分 $I(y) = \int_a^{+\infty} f(x,y) dx$ 在 $[c,d]$ 上一致收敛, 那么 $I(y)$ 是 $[c,d]$ 上的连续函数.
2. **可积性**: 如果 $f(x,y)$ 在 $[a, +\infty) \times [c,d]$ 上连续，且反常积分 $I(y) = \int_a^{+\infty} f(x,y) dx$ 在 $[c,d]$ 上一致收敛，那么 $I(y)$ 在 $[c,d]$ 上可积，且积分顺序可以交换:
$$
\int_c^d \left( \int_a^{+\infty} f(x,y) dx \right) dy = \int_a^{+\infty} \left( \int_c^d f(x,y) dy \right) dx
$$
3. **可微性**: 设 $f(x,y)$ 及 $\frac{\partial f}{\partial y}(x,y)$ 在 $[a, +\infty) \times [c,d]$ 上连续, 且满足:
   - 存在 $y_0 \in [c,d]$, 使得积分 $\int_a^{+\infty} f(x,y_0) dx$ 收敛;
   - 积分 $\int_a^{+\infty} \frac{\partial f}{\partial y}(x,y) dx$ 在 $[c,d]$ 上一致收敛.

   那么 $I(y) = \int_a^{+\infty} f(x,y) dx$ 在 $[c,d]$ 上可导，且求导与积分可以交换顺序:
$$
\frac{d}{dy} \int_a^{+\infty} f(x,y) dx = \int_a^{+\infty} \frac{\partial f}{\partial y}(x,y) dx
$$

### Euler积分

#### Beta函数

$$
B(p,q) = \int_0^1 x^{p-1} (1-x)^{q-1} dx
$$

由于Beta函数可能存在两个瑕点, 我们按照中点$\frac{1}{2}$进行分割处理:

$$
B(p,q) = \int_0^{\frac{1}{2}} x^{p-1} (1-x)^{q-1} dx + \int_{\frac{1}{2}}^1 x^{p-1} (1-x)^{q-1} dx
$$

前面一项的敛散性主要由$x^{p-1}$决定, 后面一项的敛散性主要由$(1-x)^{q-1}$决定. 显然, 当$p>0$且$q>0$时, Beta函数收敛.

所以Beta函数的定义域为$(0, +\infty) \times (0, +\infty)$.

**性质**

- Beta函数在定义域上连续. (证明利用一致收敛性+Weierstrass M-test完成)
- 对称性: $B(p,q) = B(q,p)$. (证明通过变量代换$x = 1-t$完成)
- 递推公式: $B(p,q) = \frac{q-1}{p+q-1} B(p, q-1)$. (证明通过分部积分完成)

> 计算过程如下:
$$\begin{aligned}
B(p,q) &= \int_0^1 \frac{1}{p} (1-x)^{q-1} d(x^p) \\
&= \frac{1}{p} (1-x)^{q-1} x^p \Big|_0^1 + \frac{q-1}{p} \int_0^1 x^p (1-x)^{q-2} dx \\
&= \frac{q-1}{p} \int_0^1 [1-(1-x)]x^{p-1}(1-x)^{q-2} dx \\
&= \frac{q-1}{p} \int_0^1 x^{p-1}(1-x)^{q-2} dx - \frac{q-1}{p} \int_0^1 x^{p-1}(1-x)^{q-1} dx \\
&= \frac{q-1}{p} B(p, q-1) - \frac{q-1}{p} B(p, q) \\
\end{aligned}$$
可以解得:
$$B(p,q) = \frac{q-1}{p+q-1} B(p, q-1)$$
即为所求.

**一些代换**

1. 我们对Beta函数做一次变量代换: $x=\cos^2 \phi$, 得到:

$$
B(p,q) = 2 \int_0^{\frac{\pi}{2}} \sin^{2q-1} \phi \cos^{2p-1} \phi d\phi
$$

我们不难观察到: $B(\frac{1}{2}, \frac{1}{2}) = \pi$

2. 我们再令$x = \frac{t}{1+t}$, 得到:

$$
B(p,q) = \int_0^{+\infty} \frac{t^{p-1}+t^{q-1}}{(1+t)^{p+q}} dt
$$

从这个表达式可以非常明显的观察到对称性.

#### Gamma函数

$$
\Gamma(s) = \int_0^{+\infty} x^{s-1} e^{-x} dx
$$

同样, 由于Gamma函数可能存在一个瑕点, 在无穷点的敛散性也可能遇到问题, 因此我们按照$1$进行分割处理:

$$
\Gamma(s) = \int_0^1 x^{s-1} e^{-x} dx + \int_1^{+\infty} x^{s-1} e^{-x} dx
$$

后面一项必然收敛. 所以Gamma函数的定义域为$(0, +\infty)$.

**性质**

- Gamma函数连续且可导. 且任意阶导数都存在. (证明利用一致收敛性+Weierstrass M-test完成, 任意阶导数证明类似)
- 递推公式: $\Gamma(s+1) = s \Gamma(s)$. (证明通过分部积分完成)

> 计算过程如下:
$$\begin{aligned}
\Gamma(s+1) &= \int_0^{+\infty} x^s e^{-x} dx \\
&= -\int_0^{+\infty} x^s d(e^{-x}) \\
&= -x^s e^{-x} \Big|_0^{+\infty} + s \int_0^{+\infty} x^{s-1} e^{-x} dx \\
&= s \Gamma(s)
\end{aligned}$$

当然, 根据递推公式, 我们可以知道:

$$\Gamma(n+1) = n!, \quad n \in \mathbb{N}$$

**一些变换**

我们对Gamma函数做一次变量代换: $x = t^2$, 得到:

$$\Gamma(s) = 2 \int_0^{+\infty} t^{2s-1} e^{-t^2} dt$$

我们很容易知道: $\Gamma(\frac{1}{2}) = \sqrt{\pi}$

**定义域的延拓**

由递推公式我们可以得到:

$$
\Gamma(s) = \frac{\Gamma(s+1)}{s}
$$

我们可以把$\Gamma(s)$的定义域从$(0, +\infty)$无限延拓到$(-\infty, +\infty) \setminus \{0, -1, -2, \cdots\}$

#### Beta函数与Gamma函数的关系

$$
B(p,q) = \frac{\Gamma(p) \Gamma(q)}{\Gamma(p+q)}
$$

> *证明*
$$ \Gamma(p) = 2 \int_0^{+\infty} t^{2p-1} e^{-t^2} dt, \quad \Gamma(q) = 2 \int_0^{+\infty} t^{2q-1} e^{-t^2} dt $$
$$\begin{aligned}
\Gamma(p) \Gamma(q) &= 4 \int_0^{+\infty} \int_0^{+\infty} t^{2p-1} s^{2q-1} e^{-t^2 - s^2} dt ds \\
&= 4 \iint_{\Omega} t^{2p-1} s^{2q-1} e^{-t^2 - s^2} dt ds
\end{aligned}$$
我们做一次极坐标变换: $t = r \cos \theta$, $s = r \sin \theta$, 则有:
$$\begin{aligned}
\Gamma(p) \Gamma(q) &= 2 \int_0^{\frac{\pi}{2}} \cos^{2p-1} \theta \sin^{2q-1} \theta d\theta \cdot 2 \int_0^{+\infty} r^{2p+2q-1} e^{-r^2} dr \\
&= 2 \int_0^{\frac{\pi}{2}} \cos^{2p-1} \theta \sin^{2q-1} \theta d\theta \cdot \Gamma(p+q) \\
&= B(p,q) \cdot \Gamma(p+q)
\end{aligned}$$

**关于Gamma函数的三个重要结论**

- Legendre公式

$$
\Gamma(s) \Gamma(s+\frac{1}{2}) = \frac{\sqrt{\pi}}{2^{2s-1}} \Gamma(2s)
$$

- 余元公式

$$
\Gamma(s) \Gamma(1-s) = \frac{\pi}{\sin \pi s}
$$

- Stirling公式

$$
\Gamma(s+1) = \sqrt{2\pi s} \left( \frac{s}{e} \right)^s e^{\frac{\theta}{12s}}
$$

这三个公式完全不需要记住, 证明也不需要掌握, 因为考试**根本不考**.

## Fourier级数

在前面章节的学习中我们接触了Taylor级数, 但是Taylor级数只能在函数的某个点附近进行展开, 因此它的适用范围非常有限. Fourier级数则是可以在一个区间内对函数进行展开, 因此它的适用范围更广.

### 函数的Fourier级数展开

**三角函数系**:

在区间 $[-L, L]$ (通常取 $L = \pi$) 上, 我们定义如下的函数列为三角函数系:

$$
1, \cos\frac{\pi x}{L}, \sin\frac{\pi x}{L}, \cos\frac{2\pi x}{L}, \sin\frac{2\pi x}{L}, \cdots, \cos\frac{n\pi x}{L}, \sin\frac{n\pi x}{L}, \cdots
$$

**三角函数的正交性**:

三角函数系具有正交性, 即在区间 $[-L, L]$ 上, **任意两个不同项的乘积的积分值都是 0**. 

具体的数学表达为以下几个积分公式:

1. 任意频率的正弦与余弦正交 (对任意正整数 $m, n$):
$$
\int_{-L}^{L}\sin\frac{n\pi x}{L}\cos\frac{m\pi x}{L}\,dx = 0
$$

2. 不同频率的正弦与正弦正交 (对任意正整数 $m \neq n$):
$$
\int_{-L}^{L}\sin\frac{n\pi x}{L}\sin\frac{m\pi x}{L}\,dx = 0
$$

3. 不同频率的余弦与余弦正交 (对任意正整数 $m \neq n$):
$$
\int_{-L}^{L}\cos\frac{n\pi x}{L}\cos\frac{m\pi x}{L}\,dx = 0
$$

4. 常数项 $1$ 与任意正弦、余弦项正交 (对任意正整数 $n$):
$$
\int_{-L}^{L} 1 \cdot \cos\frac{n\pi x}{L}\,dx = 0, \quad \int_{-L}^{L} 1 \cdot \sin\frac{n\pi x}{L}\,dx = 0
$$

*(附注: 若两项**相同**, 比如 $\sin\frac{n\pi x}{L} \cdot \sin\frac{n\pi x}{L}$, 它在 $[-L, L]$ 的积分值为 $L$; 若为 $1 \cdot 1$, 积分值为 $2L$.)*

**Fourier级数展开**:

设 $f(x)$ 是定义在区间 $[-L, L]$ 上的函数, 则 $f(x)$ 的 Fourier 级数展开式为:

$$
f(x) \sim \frac{a_0}{2} + \sum_{n=1}^{\infty} \left( a_n \cos\frac{n\pi x}{L} + b_n \sin\frac{n\pi x}{L} \right)
$$

其中, Fourier 系数 $a_0, a_n, b_n$ 可以利用三角函数的正交性求得 (等式两边同乘对应的基底然后再在 $[-L, L]$ 上积分):

$$
a_0 = \frac{1}{L} \int_{-L}^{L} f(x) \, dx
$$

$$
a_n = \frac{1}{L} \int_{-L}^{L} f(x) \cos\frac{n\pi x}{L} \, dx \quad (n = 1, 2, \cdots)
$$

$$
b_n = \frac{1}{L} \int_{-L}^{L} f(x) \sin\frac{n\pi x}{L} \, dx \quad (n = 1, 2, \cdots)
$$

特别地, 当 $L = \pi$ 时, 周期为 $2\pi$ 的函数的 Fourier 级数为:
$$
f(x) \sim \frac{a_0}{2} + \sum_{n=1}^{\infty} (a_n \cos nx + b_n \sin nx)
$$

对于非周期函数, 我们可以把它看作是一个周期为 $2L$ 的函数在 $[-L, L]$ 上的限制, 从而也可以进行 Fourier 级数展开.

**定理**:

1. 如果$f(x)$是定义在对称区间上的奇函数, 则它的 Fourier 级数展开式中只有正弦项, 即 $a_0 = a_n = 0$.
2. 如果$f(x)$是定义在对称区间上的偶函数, 则它的 Fourier 级数展开式中只有余弦项, 即 $b_n = 0$.

所以根据以上定理, 我们可以进行**正弦展开**或者**余弦展开**.

对于非对称区间, 我们可以通过延拓 (奇/偶) 延拓实现正弦展开/余弦展开.

### Fourier级数的收敛判别法与Dirichlet积分

记Fourier级数的部分和函数序列为:

$$
S_m(x) = \frac{a_0}{2} + \sum_{n=1}^m (a_n \cos nx + b_n \sin nx)
$$

将Fourier系数的公式 $a_n = \frac{1}{\pi} \int_{-\pi}^{\pi} f(t) \cos nt dt$ 和 $b_n = \frac{1}{\pi} \int_{-\pi}^{\pi} f(t) \sin nt dt$ 代入上式:

$$
\begin{aligned}
    S_m(x) &= \frac{1}{2\pi} \int_{-\pi}^{\pi} f(t) dt + \sum_{n=1}^m \left( \frac{\cos nx}{\pi} \int_{-\pi}^{\pi} f(t) \cos nt dt + \frac{\sin nx}{\pi} \int_{-\pi}^{\pi} f(t) \sin nt dt \right) \\
    &= \frac{1}{\pi} \int_{-\pi}^{\pi} f(t) \left( \frac{1}{2} + \sum_{n=1}^m (\cos nx \cos nt + \sin nx \sin nt) \right) dt \\
    &= \frac{1}{\pi} \int_{-\pi}^{\pi} f(t) \left( \frac{1}{2} + \sum_{n=1}^m \cos n(t-x) \right) dt
\end{aligned}
$$

其中，大括号内的和式被称为 **Dirichlet核 (Dirichlet Kernel)**，记为 $D_m(u)$ (此处 $u = t - x$):
$$
D_m(u) = \frac{1}{2} + \sum_{n=1}^m \cos nu
$$

利用三角恒等式对 $D_m(u)$ 进行求和，将两边同乘 $2\sin \frac{u}{2}$:
$$
\begin{aligned}
2 D_m(u) \sin \frac{u}{2} &= \sin \frac{u}{2} + \sum_{n=1}^m 2\cos nu \sin \frac{u}{2} \\
&= \sin \frac{u}{2} + \sum_{n=1}^m \left( \sin\left(n + \frac{1}{2}\right)u - \sin\left(n - \frac{1}{2}\right)u \right) \\
&= \sin \frac{u}{2} + \left( \sin \frac{3}{2}u - \sin \frac{1}{2}u \right) + \dots + \left( \sin\left(m + \frac{1}{2}\right)u - \sin\left(m - \frac{1}{2}\right)u \right) \\
&= \sin\left(m + \frac{1}{2}\right)u
\end{aligned}
$$
(这里利用了裂项相消)，因此得到:
$$
D_m(u) = \frac{\sin \left(m+\frac{1}{2}\right)u}{2 \sin \frac{u}{2}}
$$

将其代回 $S_m(x)$ 的表达式中，并利用变量代换 $u = t - x \Rightarrow t = x + u, dt = du$:

$$
\begin{aligned}
    S_m(x) &= \frac{1}{\pi} \int_{-\pi}^{\pi} f(t) \frac{\sin \left(m+\frac{1}{2}\right)(t-x)}{2 \sin \frac{t-x}{2}} dt \\
    &= \frac{1}{\pi} \int_{-\pi-x}^{\pi-x} f(x+u) \frac{\sin \left(m+\frac{1}{2}\right)u}{2 \sin \frac{u}{2}} du
\end{aligned}
$$

考虑到被积函数 $d(u) = f(x+u) D_m(u)$ 是以 $2\pi$ 为周期的函数，它在一个完整周期区间 $[-\pi-x, \pi-x]$ 上的积分等于在 $[-\pi, \pi]$ 上的积分。并且由于 $D_m(u)$ 是偶函数，我们可将积分区间拆分为 $[-\pi, 0]$ 和 $[0, \pi]$ 来推导 **Dirichlet积分**:

$$
\begin{aligned}
    S_m(x) &= \frac{1}{\pi} \int_{-\pi}^{\pi} f(x+t) \frac{\sin \left(m+\frac{1}{2}\right)t}{2 \sin \frac{t}{2}} dt \\
    &= \frac{1}{\pi} \left( \int_{-\pi}^0 f(x+t) D_m(t) dt + \int_0^\pi f(x+t) D_m(t) dt \right)
\end{aligned}
$$

在第一个积分中作代换 $t = -u$，利用 $D_m(-u) = D_m(u)$:
$$
\int_{-\pi}^0 f(x+t) D_m(t) dt = \int_{\pi}^0 f(x-u) D_m(-u) (-du) = \int_0^\pi f(x-u) D_m(u) du
$$

两部分合并，即可将部分和表示为：
$$
S_m(x) = \frac{1}{\pi} \int_0^\pi [f(x+t) + f(x-t)] \frac{\sin \left(m+\frac{1}{2}\right)t}{2 \sin \frac{t}{2}} dt
$$

为了研究极限定理，假设级数在 $x$ 处收敛到某个值 $\sigma(x)$。我们希望证明:
$$
\lim_{m \to +\infty} (S_m(x) - \sigma(x)) = 0
$$

注意到对 Dirichlet 核在 $[0, \pi]$ 上直接积分，根据其定义式有:
$$
\frac{1}{\pi} \int_0^\pi 2 D_m(t) dt = \frac{1}{\pi} \int_0^\pi \left( 1 + 2 \sum_{n=1}^m \cos nt \right) dt = \frac{1}{\pi} (\pi + 0) = 1
$$
我们可以在 $\sigma(x)$ 乘上这个恒为1的积分表达式：
$$
\sigma(x) = \sigma(x) \cdot 1 = \frac{1}{\pi} \int_0^\pi 2\sigma(x) \frac{\sin \left(m+\frac{1}{2}\right)t}{2 \sin \frac{t}{2}} dt
$$

将 $S_m(x)$ 和 $\sigma(x)$ 带有相同积分核的表达式相减，我们得到：
$$
S_m(x) - \sigma(x) = \frac{1}{\pi} \int_0^\pi [f(x+t) + f(x-t) - 2\sigma(x)] \frac{\sin \left(m+\frac{1}{2}\right)t}{2 \sin \frac{t}{2}} dt
$$

那么级数收敛 $\lim_{m \to +\infty} S_m(x) = \sigma(x)$，就等价于必须满足:
$$
\lim_{m \to +\infty} \int_0^\pi [f(x+t) + f(x-t) - 2\sigma(x)] \frac{\sin \left(m+\frac{1}{2}\right)t}{2 \sin \frac{t}{2}} dt = 0
$$

**Riemann-Lebesgue引理**: 设$f(x)$在$[a,b]$上可积, 则:
$$
\lim_{n \to +\infty} \int_a^b f(x) \sin nx dx = 0, \quad \lim_{n \to +\infty} \int_a^b f(x) \cos nx dx = 0
$$



---

## 结语

数学分析横跨两个学期，今天终于画上句号了。

回头看这门课，它对我的影响可能比我想象的要深。不只是学了一套工具，更多是一种看问题的方式：从更抽象、更一般的角度去想事情，用更严谨、更系统的方式去拆问题。这种思维习惯，后来潜移默化的延伸到了我做其他事情的方方面面。

特别想感谢梁进教授。一整年的课，愣是没让人觉得枯燥。他讲课有一种感染人的热情，幽默，也认真，经常让我在课堂上觉得可惜——可惜我不是数学专业的，不能在这条路上走得更深。不过能透过这门课窥见一点人类智力的顶峰，看到数学本身的那种美和力量，已经很值了。

祝我们以后不管学什么、做什么，都能往前再走远一点。

**MATH1203**, **MATH1204** 笔记到此结束。

2026.06.15

于上海交通大学