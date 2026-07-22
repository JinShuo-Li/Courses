# 数学分析期末考试复习

我们将在本部分简略的复习基本概念和一些技巧. 所有的公式用$\LaTeX$完成

## 不定积分
不定积分本质上就是在求导函数的原函数, 概念上很简单, 但是技术性内容较多, 我们主要介绍一些技术性的细节

### 定义和基本性质

**定义**: 一个函数$f(x)$若在某个区间上和另一个函数$F(x)$有如下关系: 
$$
F'(x) = f(x)
$$
则称$F(x)$是$f(x)$的一个原函数.

**定义**: 一个函数$f(x)$的原函数的全体称为这个函数的不定积分, 记为: 
$$
\int f(x)  dx
$$
特别的, 我们可以根据定义得出: 
$$
\int f(x) dx = F(x) + C
$$
倘若$F(x)$是$f(x)$的一个原函数.

**性质**: 不定积分具有线性性质
$$
\int [k_1f(x)+k_2g(x)]dx = k_1\int F(x) +k_2\int G(x) +C
$$

### 基本方法和技巧
在不定积分中, 常用的技巧是**换元积分法**和**分部积分法**, 其中换元积分法分为第一类和第二类两种.

#### 换元积分法

**第一类换元积分法**:
$$
\int f(x) dx = \int h(g(x))g'(x)dx = \int h(g(x))d(g(x)) = \int h(u) du, (u = g(x))
$$
这种换元积分法把对$f(x)$的积分转化为了对$h(u)$的积分, 倘若后者更容易计算, 便可以借助换元积分法完成简化计算. 换元积分法的核心在于寻找$u = g(x)$.

下面介绍一些技巧:

线性换元: 即$g(x) = ax+b$的形式, 这种形式是最简单的换元积分.

>e.g. 求$\int \frac{dx}{2x-1}$.  
解:
$$
\int \frac{dx}{2x-1} = \frac{1}{2}\int \frac{d(2x-1)}{2x-1}=\frac{1}{2} \ln (2x-1) +C
$$

三角换元: 利用三角函数间的代换关系实现换元积分.

>e.g. 求$\int \tan x dx$.  

$$
\int \tan x dx = \int \frac{\sin x}{\cos x} dx = -\int \frac{d(\cos x)}{\cos x} = -\ln |\cos x| + C
$$

>e.g. 求$\int \sec x dx$.  

$$
\int \sec x dx = \int \frac{1}{\cos x} dx = \int \frac{\cos x}{\cos ^2 x} dx = \frac{d(\sin x)}{1-\sin^2 x}
$$
令$u = \sin x$, 我们可以得到: 
$$
\int \sec x dx = \frac{1}{2} \ln \frac{1+\sin x}{1 - \sin x} +C
$$

>e.g. 求$\int \tan^nx dx +\int \tan^{n+2}x dx$

$$
\int \tan^nx dx +\int \tan^{n+2}x dx = \int \tan^n x (\tan^2 x+1)dx
$$

因为$\sec^2x = \tan^2x+1$, 而且$\frac{d}{dx} \tan x = \sec^2 x$. 我们进行变量代换:

$$
\int \tan^nx dx +\int \tan^{n+2}x dx = \int \tan^n x d(\tan x)
$$

我们至此把问题转化为了幂函数的积分问题, 下面的过程省略不谈.

**第二类换元积分法**

第二类换元积分法本质上是第一类换元积分法的逆过程, 写作:

$$
\int f(x)dx = \int f(\phi (x))d(\phi (x)) = \int f(\phi (x))\phi'(x)dx
$$

下面依旧介绍一些方法和技巧: 

三角换元: 第二类换元积分法最常用的方法就是三角换元法.

>e.g. 求$\int \sqrt{a^2 - x^2}dx$.

令$x = \phi (t) = a \sin t$, 于是我们只需要求:

$$
\int \sqrt{a^2 - x^2}dx =a^2 \int \cos^2 t dt= \frac{a^2}{2}\int (1+\cos 2t)dt = \frac{a^2}{2} (t + \frac{\sin 2t}{2}) +C
$$

代回$t = \phi^{-1} (x) = \arcsin \frac{x}{a}$

$$
\therefore \int \sqrt{a^2 - x^2}dx = \frac{1}{2} x \sqrt{a^2 - x^2} + \frac{a^2}{2} \arcsin\frac{x}{a} +C
$$

如果我们在被积函数的表达式中看到诸如: $\sqrt{a^2 - x^2}$, $\sqrt{x^2-a^2}$, $\sqrt{x^2 + a^2}$的格式, 可以用分别用 $x = a\sin t$, $x = a \sec t$, $x = a \tan t$来进行代换, 从而简化积分运算.

而对于在分子分母含有复杂带三角函数分式的函数, 我们可以用"万能代换"进行计算处理, 具体思想就是设$t = \tan \frac{\alpha}{2}$, 然后进行代换操作.

常用的公式如下:

$$
\sin \alpha = \frac{2 \tan \frac{\alpha}{2}}{1+\tan^2 \frac{\alpha}{2}}, \cos x = \frac{1-\tan^2 \frac{\alpha}{2}}{1+\tan^2 \frac{\alpha}{2}}, \tan x = \frac{2 \tan \frac{\alpha}{2}}{1-\tan^2 \frac{\alpha}{2}}
$$

所以任意三角有理函数的积分都可以重写为:

$$
\int R(\sin x, \cos x) dx = \int R(\frac{2t}{1+t^2},\frac{1-t^2}{1+t^2}) \frac{2}{1+t^2}dt
$$

这个代换在处理形如$\int \frac{1+\sin x}{1+\cos x}dx$的不定积分时十分有效, 这里省略具体计算.

#### 分部积分法

分部积分法本质上可以被认为是函数乘积求导的逆运算

由于对任意两个可导的函数$u(x)$, $v(x)$, 都存在下列关系式:
$$
d[u(x)v(x)] = v(x)d[u(x)]+u(x)d[v(x)]
$$

我们可以反推出:

$$
\int u(x)v'(x)dx = u(x)v(x)- \int v(x)u'(x)dx
$$

这就是**分部积分**公式.

分部积分法的威力体现在它可以把积分问题部分的转化为对$u(x)$求导数的问题, 然后在一定程度上这就可以简化运算.

>e.g.求$\int x \cos x dx$.

$$
\int x \cos x dx = \int x d(\sin x) = x \sin x - \int \sin x dx = x \sin x + \cos x +C
$$

在运用分部积分法的时候, 选取谁作为$u(x)$是一门艺术, 一般来说, 我们会选取具有某种"重复"性质的函数作为$u(x)$, 然后多次运用分部积分法, 最终用解方程的方法解出来积分式的答案. 具体来说, 我们希望指数函数, 三角函数作为$u(x)$, 而我们在选择通过求导化简的函数的时候, 我们总是希望把对数函数, 幂函数选择作为$v(x)$, 然后通过一次或者多次运用分部积分将他们化作有理函数的形式.

我们也可以进一步推导得到多次运用分部积分法得到的一个表达式:

$$
\int u v^{(n+1)} dx = u v^{(n)} - u'v^{(n-1)} +u''v^{(n-2)} - u^{(3)}v^{(n-3)} + \cdots + (-1)^n u^{(n)} v + (-1)^{n+1} \int u^{n+1} v dx
$$

同时, 很多时候在运用分部积分法的时候还可以直接把$u(x)$设为$1$, 这样可能会方便计算. 比如下面这个例子:

>e.g.求$\int \ln x dx$.

$$
\int \ln x dx = \int 1 \cdot \ln x dx = x\ln x - \int x \cdot \frac{1}{x} dx =x\ln x - x +C
$$

下面提供一个基本积分表, 供参考.

$$
\int \frac{1}{a^2 + x^2}dx = \frac{1}{a}\arctan\left(\frac{x}{a}\right) + C 
$$
$$
\int \frac{1}{x^2 - a^2} \, dx = \frac{1}{2a}\ln\left|\frac{x-a}{x+a}\right| + C
$$
$$
\int \frac{1}{a^2 - x^2} \, dx = \frac{1}{2a}\ln\left|\frac{a+x}{a-x}\right| + C 
$$
$$
\int \frac{x}{a^2 + x^2} \, dx = \frac{1}{2}\ln(a^2 + x^2) + C
$$
$$
\int \frac{1}{\sqrt{a^2 - x^2}} \, dx = \arcsin\left(\frac{x}{a}\right) + C
$$
$$
\int \frac{1}{\sqrt{x^2 + a^2}} \, dx = \ln|x + \sqrt{x^2 + a^2}| + C
$$
$$
\int \frac{1}{\sqrt{x^2 - a^2}} \, dx = \ln|x + \sqrt{x^2 - a^2}| + C
$$
$$
\int \frac{1}{x\sqrt{x^2 - a^2}} \, dx = \frac{1}{a}\text{arcsec}\left|\frac{x}{a}\right| + C
$$
$$
\int \sqrt{a^2 - x^2} \, dx = \frac{x}{2}\sqrt{a^2 - x^2} + \frac{a^2}{2}\arcsin\left(\frac{x}{a}\right) + C
$$
$$
\int \frac{1}{x\sqrt{a^2 - x^2}} \, dx = \frac{1}{a}\ln\left|\frac{a - \sqrt{a^2 - x^2}}{x}\right| + C
$$
$$
\int \sqrt{x^2 + a^2} \, dx = \frac{x}{2}\sqrt{x^2 + a^2} + \frac{a^2}{2}\ln|x + \sqrt{x^2 + a^2}| + C
$$
$$
\int \frac{1}{x\sqrt{a^2 + x^2}} \, dx = -\frac{1}{a}\ln\left|\frac{a + \sqrt{a^2 + x^2}}{x}\right| + C
$$
$$
\int \sqrt{x^2 - a^2} \, dx = \frac{x}{2}\sqrt{x^2 - a^2} - \frac{a^2}{2}\ln|x + \sqrt{x^2 - a^2}| + C 
$$
$$
\int \sin^2 x \, dx = \frac{x}{2} - \frac{\sin(2x)}{4} + C 
$$
$$
\int \cos^2 x \, dx = \frac{x}{2} + \frac{\sin(2x)}{4} + C
$$
$$
\int \tan^2 x \, dx = \tan x - x + C
$$
$$
\int \cot^2 x \, dx = -\cot x - x + C
$$
$$
\int \sec^3 x \, dx = \frac{1}{2}(\sec x \tan x + \ln|\sec x + \tan x|) + C
$$
$$
\int \csc^3 x \, dx = \frac{1}{2}(-\csc x \cot x + \ln|\csc x - \cot x|) + C
$$
$$
\int \arcsin x \, dx = x\arcsin x + \sqrt{1-x^2} + C
$$
$$
\int \arccos x \, dx = x\arccos x - \sqrt{1-x^2} + C
$$
$$
\int \arctan x \, dx = x\arctan x - \frac{1}{2}\ln(1+x^2) + C
$$
$$
\int \text{arcsec} x \, dx = x\text{arcsec} x - \ln|x + \sqrt{x^2 - 1}| + C
$$
$$
\int \text{arccot} x \, dx = x\text{arccot} x + \frac{1}{2}\ln(1+x^2) + C
$$
$$
\int \sinh x \, dx = \cosh x + C
$$
$$
\int \cosh x \, dx = \sinh x + C
$$
$$
\int \tanh x \, dx = \ln(\cosh x) + C 
$$
$$
\int \coth x \, dx = \ln|\sinh x| + C
$$
$$
\int \text{sech}^2 x \, dx = \tanh x + C 
$$
$$
\int \text{csch}^2 x \, dx = -\coth x + C 
$$
$$
\int \text{sech} x \, dx = \arctan(\sinh x) + C 
$$
$$
\int \text{csch} x \, dx = \ln\left|\tanh\left(\frac{x}{2}\right)\right| + C
$$
$$
\int \sinh^2 x \, dx = \frac{\sinh(2x)}{4} - \frac{x}{2} + C 
$$
$$
\int \cosh^2 x \, dx = \frac{\sinh(2x)}{4} + \frac{x}{2} + C
$$
$$
\int e^{ax} \sin(bx) \, dx = \frac{e^{ax}}{a^2+b^2}(a\sin(bx) - b\cos(bx)) + C 
$$
$$
\int e^{ax} \cos(bx) \, dx = \frac{e^{ax}}{a^2+b^2}(a\cos(bx) + b\sin(bx)) + C
$$

### 有理函数的积分

刚才的部分中, 我们系统性的介绍了两种积分法的基本运用. 然而, 我们在具体实践中会发现, 不是所有的函数都能显性的写出其原函数的表达式. 但是对于一类称为有理函数的特殊函数, 我们总是能写出其积分的数学表达式. 本部分将特别介绍有理函数的积分.

**定义**: 对于多项式$p_m(x)$和$q_n(x)$, 分别为$m$次多项式和$n$次多项式, 形如$R(x) = \frac{p_m(x)}{q_n(x)}$的函数被称为有理函数. 

特别的, 当$m<n$ 时我们称$R(x)$为真分式, 反之为假分式. 

在后面的问题中, 我们总假定有理函数$R(x)$是真分式. 否则我们总可以通过带余除法把假分式转化为真分式和一个多项式的和. 同时, 我们假设$q_n(x)$的最高次项系数为$1$.

由**代数学基本定理**可以知道, n次方程必有n个根. 由于复根必共轭存在, 我们一定可以把一个多项式$q_n(x)$唯一的分解为:

$$
q_n(x) = \prod^{i}_{k=1} (x-\alpha_k)^{m_k} \cdot \prod^{j}_{k=1}(x^2 + 2\xi_kx+\eta_k^2)^{n_k}
$$

**定理**: 设有理函数$R(x)$中$q_n(x)$有$k$重实根$\alpha$, 那么一定存在实数$\lambda$和多项式$p_1(x)$, 而且$p_1(x)$的次数低于$(x-\alpha)^{k-1} q_1(x)$的次数, 成立:

$$
\frac{p(x)}{q(x)} = \frac{\lambda}{(x-\alpha)^k}+\frac{p_1(x)}{(x-\alpha)^{k-1} q_1(x)}
$$

证明: 我们只需要令$\frac{p(\alpha)}{q_1(\alpha)} = \lambda$, 则$x=\alpha$是多项式$p(x)-\lambda q_1(x)$的根, 所以:

$$
p(x)-\lambda q_1(x) = (x-a)p_1(x)
$$

代回表达式即可推出.

同理我们也可以知道:

$$
\frac{p(x)}{q(x)} = \frac{\mu x + \upsilon}{(x^2+2\xi x + \eta^2)^l}+\frac{p^*(x)}{(x^2+2\xi x + \eta^2)^{l-1} q^*(x)}
$$

这意味着我们可以把任何一个有理函数写成上面分离出来的两种形式的和. 分别计算上面两种形式的积分并不是难事. 此略.

## 定积分

定积分和不定积分的起源不一样, 原理不一样, 思维不一样, 但是最后却通过Newton-Leibniz公式紧密结合在了一起. 注意本节仅讨论黎曼积分. 更广泛的积分比如反常积分我们将在后面介绍.

定积分的几何意义很明确, 就是求一个曲线$y=f(x)$和区间限$x=a$, $x=b$以及$x$轴本身围城的面积大小. 如果这个区域在x轴上方, 则定积分为正, 反之为负. 下面我们将基于这个朴素理解给出严格定义.

说到底定积分的严格定义本质上就是在细化什么情况下我们能**确定**积分值的大小, 什么时候不行. 我们可以先看两个例子, 对于函数$f(x)=x$在$[0,1]$上和x轴围成的面积大小, 这显然是可以确定的, 无论怎么求, 怎么处理, 我们都可以确定这个面积是$\frac{1}{2}$, 毫无疑问. 但是对于Dirichlet函数:

$$
f(x) =
\begin{cases}
    1, x\in \mathbb{Q} \\
    0, x\notin \mathbb{Q}\\
\end{cases}
$$

我们很明显难以确定其在$[0,1]$上和x轴围成的面积, 我们现在即将给出的定义就是要说明Dirichlet函数的这个面积是求不出来的. 下面我们具体说明.

### 定积分的定义和基本性质

**定义**: 设$f(x)$是定义在$[a,b]$上的有界函数, 在$[a,b]$上任意取分点$\{ x_i \}_{i=0}^n$形成一种划分:

$$
P: a=x_0 < x_1 < \cdots < x_n = b
$$

并在任意取点: $\xi_i \in [x_{i-1},x_i]$, 记小区间$[x_{i-1},x_i]的长度为\Delta x_i = x_i - x_{i-1}$, 令$\lambda = \max_{1 \le i \le n} \Delta x_i$, 若当$\lambda \rightarrow 0$时, 极限:

$$
\lim_{\lambda \rightarrow 0} \sum_{i=1}^{n}f(\xi_i) \Delta x_i
$$

存在, 且极限值既与划分$P$无关, 又与$\xi_i$的选取无关, 则称$f(x)$在$[a,b]$上黎曼可积.

$$
S_n = \sum^{n}_{i=1} f(\xi_i) \Delta x_i
$$

称为黎曼和, 其极限值$I$被称为$f(x)$在$[a,b]$上的定积分, 记作:

$$
I = \lim_{n \to \infty} S_n = \int_{a}^{b} f(x) dx
$$

$a$和$b$被称为下限和上限. 在上面的定义中, 我们要求$a < b$, 但是我们规定:

$$
\int_a^b g(x) dx = - \int_b^a g(x) dx
$$

并且不难推知: $\int_a^a f(x)dx = 0$. 上述定义的几何意义是非常明确的, 但是作为定义, 其用在判定可积性上不具有可操作性, 所以我们必须引入新的判定方式.

### 定积分的可积条件

在本部分, 我们关心的是定积分的可积性, 而定积分的可积性本质上就是极限的存在性问题. 而在处理极限的存在性的问题的时候, 一个重要的定理就是**夹逼定理**:

设$y_n$是我们要判断敛散性的数列, 而且对于另外两个无穷数列$x_n$和$z_n$恒有:
$x_n \le y_n \le z_n$, 那么$y_n$极限存在的一个条件就是:

$$
\lim_{n \to \infty}x_n = \lim_{n \to \infty} z_n = Y
$$

我们引入这个思想, 试着改变$\xi_i$的选取方式, 求出黎曼和在每个划分下的最大值和最小值(也就是我们后面要说的达布大和和达布小和), 然后证明$\lambda \to 0$的条件下最大值和最小值会相互无限逼近. 下面我们就是要用严谨的数学语言给出推导和证明:

回顾一下定义: 
$$
\int_{a}^{b} f(x) dx =\lim_{\lambda \to 0} \sum_{i=1}^{n} f(\xi_i)\Delta x_i
$$
极限过程和性质的关键在于 $\xi_i$ 取值的任意性. 因此, 我们考虑极端情况: 函数 $f(x)$ 在区间 $[x_{i-1},x_i]$ 上的上确界和下确界, 分别记为 $M_i$ 和 $m_i$. 于是我们得到两个极限: 

$$
M = \lim_{\lambda \to 0} \sum_{i=1}^{n}M_i \cdot \Delta x_i
$$
$$
m = \lim_{\lambda \to 0} \sum_{i=1}^{n}m_i \cdot \Delta x_i
$$
如果极限 $M$ 和 $m$ 都收敛且收敛于同一个值, 我们可以断言定积分存在, 因为: 
$$
\lim_{\lambda \to 0} \sum_{i=1}^{n}m_i \cdot \Delta x_i = m \leq \int_{a}^{b} f(x) dx =\lim_{\lambda \to 0} \sum_{i=1}^{n} f(\xi_i)\Delta x_i \leq M = \lim_{\lambda \to 0} \sum_{i=1}^{n}M_i \cdot \Delta x_i
$$
通过这种方式, 我们可以用函数 $f(x)$ 的上确界和下确界代替 $\xi_i$ 的随机选择, 这比原始定义更具可操作性. 下面我们将给出上述思想的严谨表述及证明. 定义 (达布和, Darboux Sum)对于一个划分 $P$ 及其每一个子区间 $[x_{i-1},x_i]$, 我们做如下标记: 
$$
M_i = \sup\{f(x)|x \in [x_{i-1},x_i]\}, \quad m_i = \inf\{f(x)|x \in [x_{i-1},x_i]\}
$$
显然它们与划分的选择有关. 选定划分 $P$ 后, 我们定义: 
$$
\overline{S}(P) = \sum_{i=1}^{n} M_i \cdot \Delta x_i , \quad \underline{S}(P) = \sum_{i=1}^{n} m_i \cdot \Delta x_i
$$
其中 $\overline{S}(P)$ 称为 达布大和 (Darboux upper sum), $\underline{S}(P)$ 称为 达布小和 (Darboux lower sum). 显而易见: 
$$
\underline{S}(P) \leq \sum_{i=1}^{n} f(\xi_i) \Delta x_i \leq \overline{S}(P)
$$
下一步是证明: 如果极限 $\lim_{\lambda \to 0} \overline{S}(P)$ 和 $\lim_{\lambda \to 0} \underline{S}(P)$ 存在且收敛于同一值, 则定积分存在. （其中 $\lambda = \max \{\Delta x_i\}$）引理在原有划分中增加分点形成新的划分；达布大和不会增加, 达布小和不会减少. 

**证明:**

假设 $\overline{S}(P)$ 和 $\underline{S}(P)$ 对应于某个划分 $P$, 且 $P: \{x_i\}_{i=1}^n$. 当增加一个新的分点后, 我们得到一个新的划分 $P'$, 其达布大和与达布小和分别为 $\overline{S}(P')$ 和 $\underline{S}(P')$. 我们需要证明的是: 

$$
\overline{S}(P') \leq \overline{S}(P), \quad \underline{S}(P) \leq \underline{S}(P')
$$

假设增加的点 $x'$ 落在区间 $(x_{i-1},x_i)$ 内, 我们记: 

$$
M_i = \sup \{f(x)|x \in (x_{i-1},x_i)\}, \quad M_i' = \sup \{f(x)|x \in (x_{i-1},x')\}, \quad M_i'' = \sup \{f(x)| x \in (x', x_i)\}
$$

因为 $(x_{i-1},x') \subset (x_{i-1},x_i)$ 且 $(x', x_i) \subset (x_{i-1},x_i)$, 所以有: 

$$
M_i' \leq M_i, \quad M_i'' \leq M_i
$$
$$
M_i'(x'-x_{i-1}) + M_i''(x_i-x') \leq M_i(x_i - x_{i-1})
$$
增加一个分点不会影响其他区间, 因此我们有 $\overline{S}(P') \leq \overline{S}(P)$. 同理可证 $\underline{S}(P) \leq \underline{S}(P')$. 由此我们可以推导出 $m(b-a) \leq \underline{S}(P_2) \leq \overline{S}(P_1) \leq M(b-a)$. 根据单调有界收敛定理, 我们可以断言极限 $\lim_{\lambda \to 0} \overline{S}(P)$ 和 $\lim_{\lambda \to 0} \underline{S}(P)$ 存在. 记: 
$$
\lim_{\lambda \to 0} \overline{S}(P)=L, \quad \lim_{\lambda \to 0} \underline{S}(P)=l
$$
现在我们要证明对于所有有界函数 $f(x)$, $L = \inf \{\overline{S}(P)|\overline{S}(P) \in \overline{\textbf{S}}\}$ 和 $l = \sup \{\underline{S}(P)|\underline{S}(P) \in \underline{\textbf{S}}\}$ 成立. 

**引理 (达布定理, Darboux Theorem):**
$$
\lim_{\lambda \to 0} \overline{S}(P) = \inf \{\overline{S}(P)|\overline{S}(P) \in \overline{\textbf{S}}\}
$$
$$
\lim_{\lambda \to 0} \underline{S}(P) = \sup \{\underline{S}(P)|\underline{S}(P) \in \underline{\textbf{S}}\}
$$
证明: 我们要给出达布大和的证明. 达布小和的情况类似. 基本思想是使用 $\epsilon - \delta$ 语言, 选取一个满足极限条件的达布大和, 并证明 $\forall P, \lambda = \max_{1 \leq i \leq n} (\Delta x_i) < \delta$, 都有 $0 \leq \overline{S}(P)-L < \epsilon$. 假设我们有一个划分 $P'$ 满足 $0 \leq \overline{S}(P') - L < \frac{\epsilon}{2}$. 且: 
$$
P' : a = x_0' <x_1' < x_2' < \cdots < x_p' = b
$$
我们要选取 $\delta = \min \{\Delta x_1', \Delta x_2', \cdots , \Delta x_p', \frac{\epsilon}{2(p-1)(M-m)}\}$. 现在假设我们有另一个划分 $P$ 满足 $\lambda = \max_{1 \leq i \leq n} (\Delta x_i) < \delta$: 
$$
P: a = x_0 < x_1 < x_2 < \cdots <x_n = b
$$
其达布大和为 $\overline{S}(P)$. 我们将 $P' = \{x_j'\}^p_{j=0}$ 插入到 $P = \{x_i\}^n_{i=0}$ 中形成一个新的划分 $P*$. 同样, 记其达布大和为 $\overline{S}(P*)$. 根据前面的引理, 我们有: 
$$
\overline{S}(P*)-\overline{S}(P') \leq 0
$$
对于所有区间 $(x_{i-1},x_i)$, 至多有 $p-1$ 个区间被插入了分点. 对于其他区间, 没有任何变化. 对于被插入分点的区间, 利用证明中用过的符号, 我们有: 
$$
M_i(x_i-x_{i-1})-[M_i'(x_j'-x_{i-1})+M_i''(x_i-x_j')] \leq (M-m) (x_i-x_{i-1}) < (M-m) \delta
$$
所以现在我们有: 
$$
0 \leq \overline{S}(P)-\overline{S}(P*)<(p-1)(M-m)\delta \leq \frac{\epsilon}{2}
$$
综上所述, 我们得出结论: 
$$
0 \leq \overline{S}(P)-L = [\overline{S}(P)-\overline{S}(P*)]+[\overline{S}(P*)-\overline{S}(P')]+[\overline{S}(P')-L]<\frac{\epsilon}{2}+\frac{\epsilon}{2}=\epsilon
$$
现在我们得到了可积的充要条件. 定理区间 $[a,b]$ 上的有界函数 $f(x)$ 可积的充要条件是: 对于任意划分 $P$, 当 $\lambda = \max_{1 \leq i \leq n} \Delta x_i \to 0$ 时, 有: 
$$
\lim_{\lambda \to 0} \overline{S}(P) = L = l = \lim_{\lambda \to 0} \underline{S}(P)
$$
证明: 现在我们完成定理的证明. 设 $f$ 为 $[a,b]$ 上的有界函数, 定义: 
$$
L = \lim_{\lambda \to 0} \overline{S}(P), \quad l = \lim_{\lambda \to 0} \underline{S}(P)
$$
由达布定理可知: 
$$
L = \inf \left\{ \overline{S}(P) \right\}, \quad l = \sup \left\{ \underline{S}(P) \right\}.
$$
必要性:  如果 $f$ 在 $[a,b]$ 上可积, 则存在一个数 $I$, 使得对于任意 $\epsilon > 0$, 存在 $\delta > 0$, 使得对于任何 $\lambda < \delta$ 的划分 $P$ 以及任意选取的样点 $\xi_i \in [x_{i-1}, x_i]$, 都有: 
$$
\left| \sum_{i=1}^{n} f(\xi_i) \Delta x_i - I \right| < \epsilon.
$$
特别地, 对于任意这样的划分 $P$, 我们可以选择样点使得 $f(\xi_i)$ 任意接近 $M_i$, 从而得到: 
$$
\left| \overline{S}(P) - I \right| \leq \epsilon.
$$
同理, 通过选择点使得 $f(\xi_i)$ 任意接近 $m_i$, 我们得到: 
$$
\left| \underline{S}(P) - I \right| \leq \epsilon.
$$
因此, 当 $\lambda \to 0$ 时, 我们有: 
$$
\overline{S}(P) \to I \quad \underline{S}(P) \to I
$$
这意味着 $L = l = I$. 充分性:  反之, 假设 $L = l = I$. 那么对于任意 $\epsilon > 0$, 存在 $\delta > 0$, 使得对于任何 $\lambda < \delta$ 的划分 $P$, 有: 
$$
\left| \overline{S}(P) - I \right| < \epsilon \quad \text{且} \quad \left| \underline{S}(P) - I \right| < \epsilon.
$$
对于对应于 $P$ 的任意黎曼和 $\sum_{i=1}^{n} f(\xi_i) \Delta x_i$, 我们有: 
$$
\underline{S}(P) \leq \sum_{i=1}^{n} f(\xi_i) \Delta x_i \leq \overline{S}(P).
$$
因此, 
$$
I - \epsilon < \underline{S}(P) \leq \sum_{i=1}^{n} f(\xi_i) \Delta x_i \leq \overline{S}(P) < I + \epsilon,
$$
这意味着: 
$$
\left| \sum_{i=1}^{n} f(\xi_i) \Delta x_i - I \right| < \epsilon.
$$
因此, $f$ 在 $[a,b]$ 上可积且积分为 $I$. 证明完毕. 从上述定理中, 我们可以推导出一个涉及函数振幅 (oscillation) 的更实用的判别法. 定义子区间 $[x_{i-1}, x_i]$ 上的振幅为 $\omega_i = M_i - m_i$. 条件 $L=l$ 等价于: 
$$
\lim_{\lambda \to 0} \sum_{i=1}^n \omega_i \Delta x_i = 0
$$
这个判别法依旧在说明可积性上依旧是充分必要的.

总体来说, 我们现在有三类判别法:

1. 定义判别法: 常用于否定可积性.
2. 达布和判别法: 常用于肯定可积性.
3. 振幅判别法: 肯定和否定可积性均可使用.

下面展示一些推论:

**推论**: 闭区间上的连续函数必可积.

证明:

由于闭区间上的连续函数必然一直连续, 那么存在$\delta>0$, 对任意$x', x'' \in [a,b]$, 只要$|x'-x''|<\delta$, 必有$|f(x')-f(x'')| < \frac{\epsilon}{b-a}$.  

所以对于划分$P$, 倘若$\lambda < \delta$, 必有$\omega_i < \frac{\epsilon}{b-a}$.  

所以$\sum_{i=1}^{n} \omega_i\Delta x_i < \epsilon$.

**推论**: 闭区间上的单调函数必可积.

证明:  
类似上面的证法, 只是需要取$\delta = \frac{\epsilon}{f(b)-f(a)} >0$, 假设$f(x)$单增的话. 后面推导一致. 这里省略不谈.

**推论**: 闭区间上仅有有限个不连续点的有界函数必可积.

我们给出这个定理的详细证明.

证明:

记$f(x)$在定义域上的不连续点有$k$个, 记为$a \le p_1' < \cdots < p_k' \le b$, 不妨设不连续点都在区间内. $M$和$m$为函数在全定义域上的上确界和下确界.

对$\forall \epsilon >0$, 取$\delta = \min \{\frac{p_1'-a}{2},\frac{b-p_k'}{2},\frac{d}{3},\frac{\epsilon}{4k(M-m)}\}$

>说明: 这里$\delta$的取法兼顾几个要素, 后面我们会划分出一些连续区段, 我们要保证这些连续区段既不能超出定义域, 也不能相互交叉, 还得有利于后面判定敛散性.

我们遍历每个不连续点, 先以$p_j'$的$\delta$领域的两个端点$p_j'-\delta,p_j'+\delta$为一个划分点, 将$[a,b]$(定义域)划分为$2k+1$个区段, 所以f(x)在$D^{(1)} = [a, p'_1-\delta]$, $D^{(k+1)} = [p_k'+\delta,b]$, $D^{(t)} = [p_{j-1}'+\delta , p_j'-\delta]$上连续($k+1$个连续区间), 我们在上面取分点, 使得:

$$
\sum_{i=1}^{l_j} \omega_i^{j} \Delta x_i^{j} < \frac{\epsilon}{2(k+1)}
$$

然后将所有小区间的分点合在一块看作是$[a,b]$上的一个分点.

我们考虑函数在全定义域上的划分情况, 我们可以看到连续区段对于表达式$\sum_{i=1}^n \omega_i \Delta x_i$的"贡献"不大于$(k+1) \cdot \frac{\epsilon}{2(k+1)}$, 而不连续区间的个数为$k$, 每个区间的长度满足$\text{lenth} = 2\delta < \frac{2\epsilon}{4k(M-m)}$, 每个区间的振幅一定小于函数的振幅. 所以我们有:

$$
\sum_{i=1}^{l_j} \omega_i^{j} \Delta x_i^{j} < \frac{\epsilon}{2(k+1)} + \frac{2\epsilon}{4k(M-m)} \cdot k(M-m) = \epsilon
$$

到这里便完成了证明. 可以发现在证明函数可积性的时候关键在$\delta$的选取.

### 定积分的性质

在讨论了可积性的判定之后, 我们假设函数已经满足可积条件. 定积分作为一种特殊的极限 (或者说是线性泛函), 具有许多优良的代数和序性质.

#### 1. 线性性质

定积分是线性的, 这意味着积分运算对加法和数乘封闭.

**定理**: 若 $f(x), g(x)$ 在 $[a,b]$ 上可积, 且 $k_1, k_2$ 为常数, 则:
$$
\int_a^b [k_1 f(x) + k_2 g(x)] dx = k_1 \int_a^b f(x) dx + k_2 \int_a^b g(x) dx
$$

这一性质直接由黎曼和 $\sum [k_1 f(\xi_i) + k_2 g(\xi_i)] \Delta x_i$ 的线性性取极限得到.

#### 2. 乘积的可积性与注意事项

**定理**: 若 $f(x), g(x)$ 在 $[a,b]$ 上可积, 则它们的乘积 $f(x)g(x)$ 也在 $[a,b]$ 上可积.

> **警示 (Warning)**: 
> 虽然乘积函数是可积的, 但定积分**不满足**乘法的分配律. 即通常情况下:
> $$
> \int_a^b f(x)g(x) dx \neq \left( \int_a^b f(x) dx \right) \cdot \left( \int_a^b g(x) dx \right)
> $$
> 这一点必须时刻牢记, 这是初学者极易犯的错误.

#### 3. 保序性 (Monotonicity)

定积分能够保持函数之间的大小关系.

**定理**: 若在 $[a,b]$ 上 $f(x) \le g(x)$, 则:
$$
\int_a^b f(x) dx \le \int_a^b g(x) dx
$$

**推论 (绝对值不等式)**:
若 $f(x)$ 在 $[a,b]$ 上可积, 则 $|f(x)|$ 也可积, 且成立:
$$
\left| \int_a^b f(x) dx \right| \le \int_a^b |f(x)| dx
$$
这个不等式在进行积分估值分析 (Estimate) 时非常有用.

积分第一中值定理

积分中值定理是将积分问题转化为函数值问题的重要桥梁, 它体现了积分作为“平均值”的某种推广意义.

**定理 (积分第一中值定理)**:
设 $f(x)$ 在 $[a,b]$ 上连续, $g(x)$ 在 $[a,b]$ 上可积且**不变号** (即在区间上始终 $\ge 0$ 或始终 $\le 0$), 则在 $[a,b]$ 上至少存在一点 $\xi$, 使得:
$$
\int_a^b f(x)g(x) dx = f(\xi) \int_a^b g(x) dx
$$

特别地, 当 $g(x) \equiv 1$ 时, 这就是我们熟悉的平均值公式:
$$
\int_a^b f(x) dx = f(\xi)(b-a)
$$

**证明**:
不妨假设 $g(x) \ge 0$.
因为 $f(x)$ 在闭区间 $[a,b]$ 上连续, 由最值定理, 存在 $m, M$ 分别为 $f(x)$ 的最小值和最大值.
即 $m \le f(x) \le M$.
由于 $g(x) \ge 0$, 我们可以同乘 $g(x)$ 而不改变不等号方向:
$$
m g(x) \le f(x)g(x) \le M g(x)
$$
根据定积分的保序性, 两边同时积分:
$$
m \int_a^b g(x) dx \le \int_a^b f(x)g(x) dx \le M \int_a^b g(x) dx
$$
1. 若 $\int_a^b g(x) dx = 0$, 则不等式变为 $0 \le \int f g \le 0$, 等式显然成立 (此时两边均为0).
2. 若 $\int_a^b g(x) dx > 0$, 则除以该积分值, 得:
$$
m \le \frac{\int_a^b f(x)g(x) dx}{\int_a^b g(x) dx} \le M
$$
根据**介值定理 (Intermediate Value Theorem)**, 连续函数 $f(x)$ 可以取到介于最小值 $m$ 和最大值 $M$ 之间的任意值. 因此, 必存在 $\xi \in [a,b]$, 使得:
$$
f(\xi) = \frac{\int_a^b f(x)g(x) dx}{\int_a^b g(x) dx}
$$
整理即得证.

Holder 不等式 (Hölder's Inequality)

Holder 不等式是柯西-施瓦茨不等式 (Cauchy-Schwarz Inequality) 的推广, 也是泛函分析中 $L^p$ 空间理论的基石. 在处理积分的估值和收敛性问题时极具威力.

**定理**: 
设 $p, q$ 为共轭指数, 即 $p>1, q>1$ 且满足 $\frac{1}{p} + \frac{1}{q} = 1$. 若 $|f(x)|^p$ 和 $|g(x)|^q$ 在 $[a,b]$ 上可积, 则 $|f(x)g(x)|$ 也可积, 且满足:
$$
\int_a^b |f(x)g(x)| dx \le \left( \int_a^b |f(x)|^p dx \right)^{\frac{1}{p}} \left( \int_a^b |g(x)|^q dx \right)^{\frac{1}{q}}
$$

特别地, 当 $p=q=2$ 时, 这就是著名的 **Cauchy-Schwarz 不等式**:
$$
\int_a^b |fg| dx \le \sqrt{\int_a^b f^2 dx} \cdot \sqrt{\int_a^b g^2 dx}
$$

**证明**:
证明的核心在于利用 **Young 不等式**: 对于 $a, b \ge 0$, 有 $ab \le \frac{a^p}{p} + \frac{b^q}{q}$.

记 $A = \left( \int_a^b |f(x)|^p dx \right)^{\frac{1}{p}}$, $B = \left( \int_a^b |g(x)|^q dx \right)^{\frac{1}{q}}$.

如果 $A=0$ 或 $B=0$, 则 $f(x)$ 或 $g(x)$ 几乎处处为0, 不等式两边均为0, 显然成立.
现假设 $A > 0, B > 0$.

对任意 $x \in [a,b]$, 令 $a = \frac{|f(x)|}{A}, b = \frac{|g(x)|}{B}$, 代入 Young 不等式:
$$
\frac{|f(x)g(x)|}{AB} \le \frac{1}{p} \frac{|f(x)|^p}{A^p} + \frac{1}{q} \frac{|g(x)|^q}{B^q}
$$
对两边在 $[a,b]$ 上积分:
$$
\frac{1}{AB} \int_a^b |f(x)g(x)| dx \le \frac{1}{p} \frac{\int_a^b |f(x)|^p dx}{A^p} + \frac{1}{q} \frac{\int_a^b |g(x)|^q dx}{B^q}
$$
注意到 $A^p = \int_a^b |f(x)|^p dx$, $B^q = \int_a^b |g(x)|^q dx$, 代入上式右边:
$$
\text{右边} = \frac{1}{p} \cdot 1 + \frac{1}{q} \cdot 1 = 1
$$
因此:
$$
\frac{1}{AB} \int_a^b |f(x)g(x)| dx \le 1
$$
$$
\int_a^b |f(x)g(x)| dx \le AB = \left( \int_a^b |f(x)|^p dx \right)^{\frac{1}{p}} \left( \int_a^b |g(x)|^q dx \right)^{\frac{1}{q}}
$$
以上就是定积分的性质的全部内容

### 微积分基本定理

对于定积分问题, 我们针对其可积性问题进行了深入的讨论, 下面我们将对定积分如何求解的问题进行深入探讨. 在讨论积分值的求解的过程中, 我们必须借助一类辅助函数, 也就是变限函数, 即上限或者下限为变量的函数.

**定义**设$f(x)$在$[a,b]$上可积, 作函数:

$$
F(x) = \int_a^x f(t) dt, x \in [a,b]
$$

显然$F(x)$在定义域上连续(**在计算的时候这是一个强制性的要求**). 倘若$f(x)$在定义域上连续, 则$F(x)$可导. 我们下面给出其导数的表达式:

$$
F'(x) = \lim_{\Delta x \to 0}\frac{F(x+\Delta x)-F(x)}{\Delta x} = \lim_{\Delta x \to 0} \frac{1}{\Delta x}(\int_a^{x+\Delta x}f(t)-\int_a^xf(t)) = \lim_{\Delta \to 0} f(\xi)
$$

由积分中值定理$\xi \in (x, x+\Delta x)$. 当$\Delta \to 0$时, 我们一定可以得到:

$$
F'(x) = \lim_{\Delta \to 0}f(\xi) = f(x)
$$

也就是说, 变上限函数$F(x)$本质上是$f(x)$的原函数. 我们根据不定积分的定义:

$$
\int_a^x f(t) dt = F(x) + C
$$

取$x=a$, 我们可以求出$C= - F(a)$. 所以:

$$
\int_a^x f(t) dt = F(x) - F(a) 
$$

进一步的, 我们取$x=b$, 我们得到一个表达式:

$$
\int_a^b f(t) dt = F(b) - F(a) = F(x) |^{b}_{a}
$$

这个公式被称为Newton-Leibniz公式, 也被称作微积分基本定理, 它优雅的把导数, 不定积分, 定积分三者结合起来了, 是数学分析和微积分学中非常优雅的结论.

微积分基本定理是求解定积分的最佳武器.

由Newton-Leibniz公式可以推出以下规律:

设$f(x)$, $g(x)$分别为奇函数和偶函数, $a>0$, 那么对于对称区间上的积分:

$$
\int_{-a}^a f(x)dx = 0 \quad \int_{-a}^{a}g(x)dx = 2 \int_0^a g(x)dx
$$

设$h(x)$是以$T$为周期的可积函数, 那么对任意$a$, 都有:

$$
\int_a^{a+T}h(x)dx = \int_0^Th(x)dx
$$

这两个定理的证明略.

在应用微积分基本定理将定积分转化为不定积分问题时, 我们依旧可以采用分部积分法和换元积分法来解决问题, 而且换元积分时我们反而不需要关注单调性问题, 这是因为我们无需再通过求反函数代回积分后的表达式, 而是直接换上下限就可以.

最后再来看一个例子: 求定积分:

$$
\int_0^2\frac{(x-1)^2+1}{(x-1)^2+x^2(x-2)^2}dx
$$

观察到:

$$
\int \frac{(x-1)^2+1}{(x-1)^2+x^2(x-2^2)}dx = \arctan \frac{x(x-2)}{x-1} = F(x)
$$

所以我们便得到:

$$
\int_0^2\frac{(x-1)^2+1}{(x-1)^2+x^2(x-2)^2}dx = \arctan \frac{x(x-2)}{x-1} \bigg|_0^2 = 0
$$

但是这是不可能, 因为被积函数在定义域上恒正, 是哪里出了问题呢?

经过观察, 我们发现经过不定积分得到的函数$F(x)$在$x=1$处竟然是不连续的. 这就是导致问题的所在.

因为$\{1\}$是一个$\mathbb{R}$上的零测集, 所以我们可以在$x=1$的两侧分别积分:

$$
\int_0^2\frac{(x-1)^2+1}{(x-1)^2+x^2(x-2)^2}dx = \arctan \frac{x(x-2)}{x-1} \bigg|_0^1+ \arctan \frac{x(x-2)}{x-1} \bigg|_1^2=\pi
$$

即为所求. 这提示我们在计算的时候务必关注微积分基本定理的适用条件.

### 微元法与几何计算

让我们看看一元函数微积分在几何计算中的应用

#### 求平面图形的面积

由定积分的几何意义我们可以轻易推出平面图形的面积的表达式.

$S_1$是$f(x)$和x轴围成的面积, $S_2$是$f(x)$和$g(x)$围成的面积

$$
S_1 = \int_a^b |f(x)| dx \quad S_2=\int_a^b|f(x)-g(x)|dx
$$

倘若$f(x)$是用参数方程形式写成的: 那么:

$$
\begin{cases}
    x = x(t) \\
    y = y(t)
\end{cases}

\quad t \in [T_1,T_2]

\quad S_1 = \int_{T_1}^{T_2}|y(t) \cdot x'(t)|dt
$$

而若曲线是由极坐标方程$r = r(\theta)$表示的, 那么它和两条边界极径$\theta = \alpha, \theta = \beta$围成的图形面积可以表示为:

$$
S = \frac{1}{2} \int_{\alpha}^{\beta}r^2(\theta)d\theta
$$

#### 求光滑曲线的弧长

我们在曲线上取一小段弧长, 我们可以近似的把它看作是一段直线. 那么由勾股定理, 我们可以得到: $\Delta s = \sqrt{\Delta^2 x+\Delta^2y}$. 进而得到:

倘若$f(x)$是由参数方式写成的, 那么:

$$
\begin{cases}
    x = x(t) \\
    y = y(t)
\end{cases}

\quad t \in [T_1,T_2]

\quad L=\int_{T_1}^{T_2}\sqrt{[x'(t)]^2+[y'(t)]^2} dt

$$

用$f(x)$显性表示则可以写作:

$$
L = \int_a^b\sqrt{1+[f'(x)]^2}dx
$$

用$r = r(\theta)$表示则可以写作:

$$
L = \int_{\alpha}^{\beta} \sqrt{[r(\theta)]^2+[r'(\theta)]^2}d\theta
$$

#### 求旋转体的体积

考虑平面曲线 $y = f(x)$ 在区间 $[a, b]$ 上绕 $x$ 轴旋转一周所形成的旋转体。利用微元法，取微小区间 $[x, x+dx]$，对应薄片体积近似为 $\pi [f(x)]^2 dx$，因此总体积为：

$$
V_x = \pi \int_a^b [f(x)]^2 dx
$$

类似地，若曲线绕 $y$ 轴旋转，且由 $x = g(y)$ 表示，$y \in [c, d]$，则体积为：

$$
V_y = \pi \int_c^d [g(y)]^2 dy
$$

对于参数方程 $\begin{cases} x = x(t) \\ y = y(t) \end{cases}$，$t \in [T_1, T_2]$，绕 $x$ 轴旋转的体积公式为（假设 $x(t)$ 单调变化）：

$$
V_x = \pi \int_{T_1}^{T_2} [y(t)]^2 \cdot x'(t) \, dt
$$

注意，实际计算时需根据旋转轴和参数范围确定积分表达式.

#### 求旋转曲面的面积

旋转曲面面积是指曲线旋转一周所形成曲面的侧面积。对于曲线 $y = f(x)$ 在 $[a, b]$ 上绕 $x$ 轴旋转, 我们进行如下推导:

将光滑曲线上一段无穷小的弧长 $ds$ 绕坐标轴旋转一周，所得曲面可近似视为一个圆台的侧面。圆台的侧面积公式为：

$$ S_{\text{侧}} = \pi (r_1 + r_2) l $$

其中 $r_1$、$r_2$ 是上下底半径，$l$ 是母线长。当弧长趋于无穷小时，$r_1 \approx r_2 \approx r$（旋转半径），且母线长 $l = ds$，因此面积微元为：

$$ dA = 2\pi r \cdot ds $$

这里 $r$ 是弧上点到旋转轴的垂直距离，$ds$ 是弧长微元。

**具体情形推导**

1. 曲线 $y = f(x)$ 绕 $x$ 轴旋转

- **旋转半径**：点 $(x, f(x))$ 到 $x$ 轴的距离为 $|f(x)|$，故 $r = |f(x)|$。
- **弧长微元**：$ds = \sqrt{1 + \left( \frac{dy}{dx} \right)^2} dx = \sqrt{1 + [f'(x)]^2} dx$。
- **面积微元**：代入 $dA = 2\pi r \cdot ds$ 得：

$$ dA = 2\pi |f(x)| \sqrt{1 + [f'(x)]^2} dx $$

2. 曲线 $x = g(y)$ 绕 $y$ 轴旋转

- **旋转半径**：点 $(g(y), y)$ 到 $y$ 轴的距离为 $|g(y)|$，故 $r = |g(y)|$。
- **弧长微元**：$ds = \sqrt{1 + \left( \frac{dx}{dy} \right)^2} dy = \sqrt{1 + [g'(y)]^2} dy$。
- **面积微元**：代入 $dA = 2\pi r \cdot ds$ 得：

$$ dA = 2\pi |g(y)| \sqrt{1 + [g'(y)]^2} dy $$

3. 参数方程 $\begin{cases} x = x(t) \\ y = y(t) \end{cases}$ 绕 $x$ 轴旋转

- **旋转半径**：点 $(x(t), y(t))$ 到 $x$ 轴的距离为 $|y(t)|$，故 $r = |y(t)|$。
- **弧长微元**：$ds = \sqrt{ \left( \frac{dx}{dt} \right)^2 + \left( \frac{dy}{dt} \right)^2 } dt = \sqrt{ [x'(t)]^2 + [y'(t)]^2 } dt$。
- **面积微元**：代入 $dA = 2\pi r \cdot ds$ 得：

$$ dA = 2\pi |y(t)| \sqrt{ [x'(t)]^2 + [y'(t)]^2 } dt $$

4. 参数方程 $\begin{cases} x = x(t) \\ y = y(t) \end{cases}$ 绕 $y$ 轴旋转

- **旋转半径**：点 $(x(t), y(t))$ 到 $y$ 轴的距离为 $|x(t)|$，故 $r = |x(t)|$。
- **弧长微元**：同上，$ds = \sqrt{ [x'(t)]^2 + [y'(t)]^2 } dt$。
- **面积微元**：代入 $dA = 2\pi r \cdot ds$ 得：

$$ dA = 2\pi |x(t)| \sqrt{ [x'(t)]^2 + [y'(t)]^2 } dt $$

所有公式统一为 $dA = 2\pi r \cdot ds$，其中 $r$ 是旋转半径，$ds$ 是弧长微元，具体表达式取决于曲线方程和旋转轴。推导基于几何直观的圆台近似，并假设曲线光滑且旋转时不自交。下面给出部分的积分表达式.

$$
A_x = 2\pi \int_a^b |f(x)| \sqrt{1 + [f'(x)]^2} \, dx
$$

类似地，绕 $y$ 轴旋转，由 $x = g(y)$ 表示，$y \in [c, d]$，则：

$$
A_y = 2\pi \int_c^d |g(y)| \sqrt{1 + [g'(y)]^2} \, dy
$$

对于参数方程 $\begin{cases} x = x(t) \\ y = y(t) \end{cases}$，$t \in [T_1, T_2]$，绕 $x$ 轴旋转的曲面面积为：

$$
A_x = 2\pi \int_{T_1}^{T_2} |y(t)| \sqrt{[x'(t)]^2 + [y'(t)]^2} \, dt
$$

绕 $y$ 轴旋转时，公式类似，只需交换 $x$ 和 $y$ 的角色。这些公式均假设曲线光滑，且旋转过程中无自交.

## 广义积分

在前面的章节中, 我们讨论了定积分的定义和性质. 然而, 在实际应用中, 我们经常会遇到一些函数在某些点上不满足有界性, 或者积分区间是无限的. 这些情况下, 我们需要引入广义积分的概念.

### 第一类广义积分的定义与审敛法

**定义**: 设 $f(x)$ 在区间 $[a, +\infty)$ 上有定义. 如果对于任意 $A > a$, $f(x)$ 在 $[a, A]$ 上可积, 并且极限:
$$
\lim_{A \to +\infty} \int_a^A f(x) dx
$$
存在(有限), 则称该极限为 $f(x)$ 在 $[a, +\infty)$ 上的广义积分, 广义积分收敛, 其积分值为:
$$
\int_a^{+\infty} f(x) dx = \lim_{A \to +\infty} \int_a^A f(x) dx
$$
对于区间 $(-\infty, b]$ 和 $(-\infty, +\infty)$ 上的广义积分, 定义类似:
$$
\int_{-\infty}^b f(x) dx = \lim_{A \to -\infty} \int_A^b f(x) dx
$$
$$
\int_{-\infty}^{+\infty} f(x) dx = \int_{-\infty}^c f(x) dx + \int_c^{+\infty} f(x) dx
$$
注意, 我们这里在计算 $(-\infty, +\infty)$ 上的广义积分时, 需要选择一个中间点 $c$ 将积分区间分成两个部分, 分别计算后再相加. 不能直接用下面的方法计算:
$$
\int_{-\infty}^{+\infty} f(x) dx = \lim_{A \to +\infty} \int_{-A}^{A} f(x) dx
$$
因为后者的存在并不意味着前者的存在. 极限的计算对于无穷大的选取是任意的, 如果我们发现改变无穷大的阶数和选取方式会影响极限的值, 那么我们就可以断定该广义积分发散. 反之, 如果无论如何选取无穷大, 极限值都相同, 那么我们就可以断定该广义积分收敛. 然而, 上面这种极限并非毫无价值, 它被称作**柯西主值 (Cauchy Principal Value)**, 在某些情形下具有重要的应用价值, 其定义为:
$$
\text{(cpv)} \int_{-\infty}^{+\infty} f(x) dx = \lim_{A \to +\infty} \int_{-A}^{A} f(x) dx
$$

显然有: 广义积分存在 $\Rightarrow$ 柯西主值存在, 反之不成立.

**定理**: 两个反常积分的和收敛当且仅当各自收敛. 证明略.

**定理**: 设 $f(x)$ 在 $[a, +\infty)$ 上有定义. 则 $f(x)$ 在 $[a, +\infty)$ 上的广义积分收敛的充分必要条件是: 对任意 $\epsilon > 0$, 存在 $\delta > 0$, 使得对于任意 $A', A'' > \delta$, 有:
$$
\left| \int_{A'}^{A''} f(x) dx \right| < \epsilon
$$
**证明**: 必要性: 设 $f(x)$ 在 $[a, +\infty)$ 上的广义积分收敛, 记其积分值为 $I$. 那么对于任意 $\epsilon > 0$, 存在 $\delta > 0$, 使得对于任意 $A > \delta$, 有:
$$
\left| \int_a^A f(x) dx - I \right| < \frac{\epsilon}{2}
$$
对于任意 $A', A'' > \delta$, 我们有:
$$
\left| \int_{A'}^{A''} f(x) dx \right| = \left| \int_a^{A''} f(x) dx - \int_a^{A'} f(x) dx \right| \leq \left| \int_a^{A''} f(x) dx - I \right| + \left| \int_a^{A'} f(x) dx - I \right| < \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon
$$
充分性: 设对于任意 $\epsilon > 0$, 存在 $\delta > 0$, 使得对于任意 $A', A'' > \delta$, 有:
$$
\left| \int_{A'}^{A''} f(x) dx \right| < \epsilon
$$
对于任意 $A > \delta$, 取 $A' = \delta, A'' = A$, 则有:
$$
\left| \int_{\delta}^{A} f(x) dx \right| < \epsilon
$$
因此, $\int_a^A f(x) dx$ 在 $A \to +\infty$ 时是柯西列, 故存在极限 $I$. 于是, $f(x)$ 在 $[a, +\infty)$ 上的广义积分收敛且积分值为 $I$. 证明完毕.

这一定理的叙述本质上是柯西收敛准则在广义积分情形下的应用. 我们在这里称之为**广义积分的柯西判别法**.

**定义**: 设$f(x)$在任意有限区间$[a,b]$上可积, 且$\int_a^{+\infty} |f(x)|dx$收敛, 则称$f(x)$在$[a,+\infty)$上**绝对可积**. 否则称为**条件可积**.

显然, 绝对可积$\Rightarrow$ 可积, 反之不成立.

#### 非负函数第一类广义积分的审敛法

1. **比较审敛法**: 设$f(x)$和$g(x)$在$[a,+\infty)$上有定义, 且$0 \le f(x) \le K \cdot g(x)$. 则:

- 若$\int_a^{+\infty} g(x) dx$收敛, 则$\int_a^{+\infty} f(x) dx$收敛.
- 若$\int_a^{+\infty} f(x) dx$发散, 则$\int_a^{+\infty} g(x) dx$发散.

2. **极限比较审敛法**: 设$f(x)$和$g(x)$在$[a,+\infty)$上有定义, 且:

$$
\lim_{x \to +\infty} \frac{f(x)}{g(x)} = L, \quad 0 < L < +\infty
$$
- 若$\int_a^{+\infty} g(x) dx$收敛, 则$\int_a^{+\infty} f(x) dx$收敛.
- 若$\int_a^{+\infty} g(x) dx$发散, 则$\int_a^{+\infty} f(x) dx$发散.
  
注: 在这里我们允许$x=+\infty$的写法.

3. **Cauchy判别法**: 设在$[a, +\infty) \subset (0, +\infty)$ 上恒有$f(x) \ge 0$, 且 $K$ 为常数. 则:
- 若$f(x) \leq \frac{K}{x^p}$, 且$p>1$, 则$\int_a^{+\infty} f(x) dx$收敛.
- 若$f(x) \geq \frac{K}{x^p}$, 且$p \leq 1$, 则$\int_a^{+\infty} f(x) dx$发散.

4. **Cauchy判别法的极限形式**: 设在$[a, +\infty) \subset (0, +\infty)$ 上恒有$f(x) \ge 0$. 且:
$$
\lim_{x \to +\infty} f(x) x^p = L
$$
- 若$0 \leq L < +\infty$, 且$p>1$, 则$\int_a^{+\infty} f(x) dx$收敛.
- 若$0 < L \leq +\infty$, 且$p \leq 1$, 则$\int_a^{+\infty} f(x) dx$发散.

#### 一般函数第一类广义积分的审敛法

**引理**: 第二积分中值定理: 设$f(x)$在$[a,b]$上可积, $g(x)$在$[a,b]$上单调, 则存在$\xi \in [a,b]$, 使得下式成立:
$$
\int_a^b f(x)g(x) dx = g(a) \int_a^{\xi} f(x) dx + g(b) \int_{\xi}^b f(x) dx
$$

证明: 我们这里仅对$f(x)$在$[a,b]$上连续, g(x)在$[a,b]$上单调$, $g'(x)$在定义域上可积的情形进行证明, 其他情形的证明类似.

对于$\int_a^b f(x)g(x) dx$，先进行分部积分, 然后运用第一积分中值定理, 记:

$$F(x) = \int_a^x f(t) dt$$

$$\int_a^b f(x)g(x) dx = \int_a^b g(x) dF(x) = g(b)\int_a^bf(x)dx - \int_a^b F(x) g'(x) dx$$

$$= g(b)\int_a^bf(x)dx - [g(b)-g(a)]\int_a^{\xi} f(x) dx$$

$$= g(a)\int_a^{\xi} f(x) dx + g(b)\int_{\xi}^b f(x) dx$$

**Abel判别法**: 设$f(x)$在$[a,+\infty)$上可积, 且$\int_a^{+\infty} f(x) dx$收敛. $g(x)$在$[a,+\infty)$上单调且有界, 则$\int_a^{+\infty} f(x)g(x) dx$收敛.

证明: 运用第二积分中值定理, 对任意$A > a$, 存在$\xi \in [a,A]$, 使得:
$$
\int_a^A f(x)g(x) dx = g(a) \int_a^{\xi} f(x) dx + g(A) \int_{\xi}^A f(x) dx
$$
由于$\int_a^{+\infty} f(x) dx$收敛, 故对于任意$\epsilon > 0$, 存在$\delta > 0$, 使得对于任意$A', A'' > \delta$, 有:
$$
\left| \int_{A'}^{A''} f(x) dx \right|
    < \epsilon
$$
又由于$g(x)$在$[a,+\infty)$上有界,
故存在常数$K$, 使得对于任意$x \in [a,+\infty)$, 有$|g(x)| \le K$. 于是, 对于任意$A', A'' > \delta$, 我们有:
$$
\left| \int_{A'}^{A''} f(x)g(x) dx \right| \leq |g(a)| \left| \int_{A'}^{\xi} f(x) dx \right| + |g(A'')| \left| \int_{\xi}^{A''} f(x) dx \right| < (|g(a)| + K) \epsilon
$$
由广义积分的柯西判别法, 可知$\int_a^{+\infty} f(x)g(x) dx$收敛. 证明完毕.

**Dirichlet判别法**: 设$f(x)$在$[a,+\infty)$上连续, 且对于任意$A > a$, $\left| \int_a^A f(x) dx \right| \le K$, $g(x)$在$[a,+\infty)$上单调且$\lim_{x \to +\infty} g(x) = 0$, 则$\int_a^{+\infty} f(x)g(x) dx$收敛.

证明: 运用第二积分中值定理, 对任意$A > a$, 存在$\xi \in [a,A]$, 使得:
$$
\int_a^A f(x)g(x) dx = g(a) \int_a^{\xi} f(x) dx + g(A) \int_{\xi}^A f(x) dx
$$
由于对于任意$A > a$, $\left| \int_a^A f(x) dx \right| \le K$, 故对于任意$A', A'' > a$, 我们有:
$$
\left| \int_{A'}^{A''} f(x)g(x) dx \right| \leq |g(a)| \left| \int_{A'}^{\xi} f(x) dx \right| + |g(A'')| \left| \int_{\xi}^{A''} f(x) dx \right| \leq |g(a)| \cdot 2K + |g(A'')| \cdot 2K
$$
由于$\lim_{x \to +\infty} g(x) = 0$, 故对于任意$\epsilon > 0$, 存在$\delta > 0$, 使得对于任意$A'' > \delta$, 有$|g(A'')| < \frac{\epsilon}{2K}$. 于是, 对于任意$A', A'' > \delta$, 我们有:
$$
\left| \int_{A'}^{A''} f(x)g(x) dx \right| < |g(a)| \cdot 2K + \frac{\epsilon}{2K} \cdot 2K = |g(a)| \cdot 2K + \epsilon \leq \epsilon'
$$
由广义积分的柯西判别法, 可知$\int_a^{+\infty} f(x)g(x) dx$收敛. 证明完毕.

上述两类积分判别法统称为**Dirichlet-Abel判别法**.

### 第二类广义积分的定义与审敛法
**定义**: 设 $f(x)$ 在区间 $(a, b]$ 上有定义. 如果对于任意 $A \in (a, b]$, $f(x)$ 在 $[A, b]$ 上可积, 并且极限:
$$
\lim_{\epsilon \to 0^+} \int_{a+\epsilon}^b f(x) dx
$$
存在(有限), 则称该极限为 $f(x)$ 在 $(a, b]$ 上的广义积分, 广义积分收敛, 其积分值为:
$$
\int_a^b f(x) dx = \lim_{\epsilon \to 0^+} \int_{a+\epsilon}^b f(x) dx
$$

对于区间 $[a, b)$ 上的广义积分, 定义类似.

类似于第一类广义积分, 第二类广义积分也有对应的柯西主值的概念:
$$
\text{(cpv)} \int_a^b f(x) dx = \lim_{\epsilon \to 0^+} \int_{a+\epsilon}^{b-\epsilon} f(x) dx
$$
显然有: 广义积分存在 $\Rightarrow$ 柯西主值存在, 反之不成立.

**定理**: 两个反常积分的和收敛当且仅当各自收敛. 证明略.

**定理**: 设 $f(x)$ 在 $(a, b]$ 上有定义. 则 $f(x)$ 在 $(a, b]$ 上的广义积分收敛的充分必要条件是: 对任意 $\epsilon > 0$, 存在 $\delta > 0$, 使得对于任意 $0 < \epsilon', \epsilon'' < \delta$, 有:
$$
\left| \int_{a+\epsilon'}^{a+\epsilon''} f(x) dx \right| < \epsilon
$$
**证明**: 

必要性: 设 $f(x)$ 在 $(a, b]$ 上的广义积分收敛, 记其积分值为 $I$. 那么对于任意 $\epsilon > 0$, 存在 $\delta > 0$, 使得对于任意 $0 < \epsilon < \delta$, 有:
$$
\left| \int_{a+\epsilon}^b f(x) dx - I \right| < \frac{\epsilon}{2}
$$

对于任意 $0 < \epsilon', \epsilon'' < \delta$, 我们有:
$$
\left| \int_{a+\epsilon'}^{a+\epsilon''} f(x) dx \right| = \left| \int_{a+\epsilon''}^b f(x) dx - \int_{a+\epsilon'}^b f(x) dx \right| \leq \left| \int_{a+\epsilon''}^b f(x) dx - I \right| + \left| \int_{a+\epsilon'}^b f(x) dx - I \right| < \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon
$$
充分性: 设对于任意 $\epsilon > 0$, 存在 $\delta > 0$, 使得对于任意 $0 < \epsilon', \epsilon'' < \delta$, 有:
$$
\left| \int_{a+\epsilon'}^{a+\epsilon''} f(x) dx \right| < \epsilon
$$
对于任意 $0 < \epsilon < \delta$, 取 $\epsilon' = \delta, \epsilon'' = \epsilon$, 则有:
$$
\left| \int_{a+\delta}^{a+\epsilon} f(x) dx \right| < \epsilon
$$
因此, $\int_{a+\epsilon}^b f(x) dx$ 在 $\epsilon \to 0^+$ 时是柯西列, 故存在极限 $I$. 于是, $f(x)$ 在 $(a, b]$ 上的广义积分收敛且积分值为 $I$. 证明完毕.

这一定理的叙述本质上是柯西收敛准则在广义积分情形下的应用. 我们在这里称之为**广义积分的柯西判别法**.

#### 非负函数第二类广义积分的审敛法

1. **比较审敛法**: 设$f(x)$和$g(x)$在$(a,b]$上有定义, 且$0 \le f(x) \le K \cdot g(x)$. 则:
- 若$\int_a^{b} g(x) dx$收敛, 则$\int_a^{b} f(x) dx$收敛.
- 若$\int_a^{b} f(x) dx$发散, 则$\int_a^{b} g(x) dx$发散.
  
2. **极限比较审敛法**: 设$f(x)$和$g(x)$在$(a,b]$上有定义, 且:
$$
\lim_{x \to a^+} \frac{f(x)}{g(x)} = L, \quad 0 < L < +\infty
$$
- 若$\int_a^{b} g(x) dx$收敛, 则$\int_a^{b} f(x) dx$收敛.
- 若$\int_a^{b} g(x) dx$发散, 则$\int_a^{b} f(x) dx$发散.

3. **Cauchy判别法**: 设在$(a, b] \subset (0, +\infty)$ 上恒有$f(x) \ge 0$, 且 $K$ 为常数. 则:
- 若$f(x) \leq \frac{K}{(x-a)^p}$, 且$p<1$, 则$\int_a^{b} f(x) dx$收敛.
- 若$f(x) \geq \frac{K}{(x-a)^p}$, 且$p \geq 1$, 则$\int_a^{b} f(x) dx$发散.

4. **Cauchy判别法的极限形式**: 设在$(a, b] \subset (0, +\infty)$ 上恒有$f(x) \ge 0$. 且:
$$
\lim_{x \to a^+} f(x) (x-a)^p = L
$$
- 若$0 \leq L < +\infty$, 且$p<1$, 则$\int_a^{b} f(x) dx$收敛.
- 若$0 < L \leq +\infty$, 且$p \geq 1$, 则$\int_a^{b} f(x) dx$发散.

#### 一般函数第二类广义积分的审敛法

**Abel判别法**: 设$f(x)$在$(a,b]$上可积, 且$\int_a^{b} f(x) dx$收敛. $g(x)$在$(a,b]$上单调且有界, 则$\int_a^{b} f(x)g(x) dx$收敛. 证明从略.

**Dirichlet判别法**: 设$f(x)$在$(a,b]$上连续, 且对于任意$A \in (a,b]$, $\left| \int_A^b f(x) dx \right| \le K$, $g(x)$在$(a,b]$上单调且$\lim_{x \to a^+} g(x) = 0$, 则$\int_a^{b} f(x)g(x) dx$收敛. 证明从略.

上述两类积分判别法统称为**Dirichlet-Abel判别法**.

## 级数理论

### 数项级数

#### 基本概念与性质

**定义**: 设$x_1, x_2, \cdots, x_n, \cdots$为一无穷可列个实数, 我们定义$\{x_n\}$为数列的**通项**.

数列的部分和序列为:
$$
S_n = x_1 + x_2 + \cdots + x_n
$$

无穷项级数(简称级数)定义为:
$$
S= x_1 + x_2 + \cdots + x_n + \cdots = \sum_{n=1}^{\infty} x_n
$$

若数列$\{S_n\}$收敛, 则称级数$S$收敛, 且其和为:
$$
S = \lim_{n \to \infty} S_n
$$
否则称级数$S$发散. 这就是相关概念的定义

**定理**: 级数$\sum_{n=1}^{\infty} x_n$收敛的必要条件是: $\lim_{n \to \infty} x_n = 0$.

本定理显然, 这里不予证明.

下面列举几种常见的级数:

1. **几何级数**: 形如$\sum_{n=0}^{\infty} ar^n$的级数, 其中$a$和$r$为常数. 当$|r| < 1$时, 该级数收敛, 且其和为:
$$
S = \frac{a}{1-r}
$$
2. **调和级数**: 形如$\sum_{n=1}^{\infty} \frac{1}{n}$的级数. 该级数发散.
3. **p级数**: 形如$\sum_{n=1}^{\infty} \frac{1}{n^p}$的级数, 其中$p$为常数.
   
   当$p > 1$时, 该级数收敛; 当$p \leq 1$时, 该级数发散.

**性质**: 下面列举无穷级数的几个性质:
- 若级数$\sum_{n=1}^{\infty} x_n$收敛, 则其任意加括号的级数也收敛, 且级数和相等.
- 若级数$\sum_{n=1}^{\infty} x_n$收敛, 则其任意有限项被去掉后的级数也收敛.
- 线性性质: 若级数$\sum_{n=1}^{\infty} x_n$和$\sum_{n=1}^{\infty} y_n$均收敛, 则对于任意常数$a$和$b$, 级数$\sum_{n=1}^{\infty} (a x_n + b y_n)$也收敛, 且有:
$$
\sum_{n=1}^{\infty} (a x_n + b y_n) = a \sum_{n=1}^{\infty} x_n + b \sum_{n=1}^{\infty} y_n
$$

#### 上下极限

研究级数敛散性需要借助数列的敛散性, 但是有些数列并不收敛, 这时我们可以借助数列的上下极限来研究数列的性质.

先考虑有界数列的情形:

**定义**: 设$\{x_n\}$为有界数列, 若在这个数列中存在一个子列$\{x_{n_k}\}$, 使得:
$$
\lim_{k \to \infty} x_{n_k} = \xi
$$
则称$\xi$为数列$\{x_n\}$的一个**极限点**.

记$E$为数列$\{x_n\}$的全部极限点所组成的集合, 则E是一个非空有界集合.

**定理**: $E$的上确界$H$和下确界$h$都在集合$E$中, 即存在数列的子列$\{x_{n_k}\}$和$\{x_{m_k}\}$, 使得:
$$\lim_{k \to \infty} x_{n_k} = H, \quad \lim_{k \to \infty} x_{m_k} = h$$

**定义**: 数列$\{x_n\}$的上极限和下极限分别定义为:
$$
\overline{\lim_{n \to \infty}} x_n = H, \quad \underline{\lim_{n \to \infty}} x_n = h
$$
其中$H$和$h$分别为数列$\{x_n\}$的极限点集合的上确界和下确界.

**定理**: 设$\{x_n\}$为有界数列, 则数列收敛的充分必要条件是:
$$
\overline{\lim_{n \to \infty}} x_n = \underline{\lim_{n \to \infty}} x_n
$$

我们可以从这个定义出发定义无界数列的上下极限:

**定义**: 设$\{x_n\}$为数列, 若存在一个子列$\{x_{n_k}\}$, 使得:
$$
\lim_{k \to \infty} x_{n_k} = \xi, \quad \xi \in \mathbb{R} \cup \{+\infty, -\infty\}
$$
则称$\xi$为数列$\{x_n\}$的一个**极限点**.

记$E$为数列$\{x_n\}$的全部极限点所组成的集合, 则E是一个非空集合.

**定义**: 数列$\{x_n\}$的上极限和下极限分别定义为:
$$
\overline{\lim_{n \to \infty}} x_n = \sup E, \quad \underline{\lim_{n \to \infty}} x_n = \inf E
$$
其中$\sup E$和$\inf E$分别为数列$\{x_n\}$的极限点集合的上确界和下确界. 当$\sup E = +\infty$或$\inf E = -\infty$时, 我们约定$\overline{\lim_{n \to \infty}} x_n = +\infty$或$\underline{\lim_{n \to \infty}} x_n = -\infty$.

上下极限的运算和普通代数运算有所不同:

- 加法: 设$\{x_n\}$和$\{y_n\}$为数列, 则有:
$$
\overline{\lim_{n \to \infty}} (x_n + y_n) \leq \overline{\lim_{n \to \infty}} x_n + \overline{\lim_{n \to \infty}} y_n
$$
$$
\underline{\lim_{n \to \infty}} (x_n + y_n) \geq \underline{\lim_{n \to \infty}} x_n + \underline{\lim_{n \to \infty}} y_n
$$
- 乘法: 设$\{x_n\}$和$\{y_n\}$为数列, 则有:
$$
\overline{\lim_{n \to \infty}} (x_n y_n) \leq \overline{\lim_{n \to \infty}} x_n \cdot \overline{\lim_{n \to \infty}} y_n
$$
$$
\underline{\lim_{n \to \infty}} (x_n y_n) \geq \underline{\lim_{n \to \infty}} x_n \cdot \underline{\lim_{n \to \infty}} y_n
$$

注意, 上述四个式子在$x_n$和$y_n$有一者收敛时取等.

其证明可以通过下面这个结论完成:

**定理**: 设$\{x_n\}$为数列, 则$\overline{\lim_{n \to \infty}} x_n = H$的充分必要条件为:
- 对任意$\epsilon > 0$, 存在$N_1$, 当$n > N_1$时, 有$x_n < H + \epsilon$;
- 对任意$\epsilon > 0$, $\{x_n\}$中有无穷多项,  $x_n > H - \epsilon$.

#### 正项级数的审敛法

**定义**: 设$\{a_n\}$为非负数列, 则级数$\sum_{n=1}^{\infty} a_n$称为**正项级数**.

根据单增数列必有上界, 我们可以立即得到下面的定理:

**定理**: 正项级数$\sum_{n=1}^{\infty} a_n$收敛的充分必要条件是其部分和序列$\{S_n\}$有上界.

下面给出正项级数的几种常用审敛法:

1. 比较审敛法: 设$\{a_n\}$和$\{b_n\}$为非负数列, 且存在常数$K > 0$, 使得对于任意$n \in \mathbb{N}$, 有$a_n \leq K b_n$. 则:
- 若级数$\sum_{n=1}^{\infty} b_n$收敛, 则级数$\sum_{n=1}^{\infty} a_n$收敛.
- 若级数$\sum_{n=1}^{\infty} a_n$发散, 则级数$\sum_{n=1}^{\infty} b_n$发散.
  
2. 极限比较审敛法: 设$\{a_n\}$和$\{b_n\}$为非负数列, 且:
   $$
   \lim_{n \to \infty} \frac{a_n}{b_n} = L, \quad 0 \leq L \leq +\infty
   $$
   - 若$0 < L < +\infty$, 则级数$\sum_{n=1}^{\infty} a_n$和$\sum_{n=1}^{\infty} b_n$同敛散.
   - 若$L = 0$, 且级数$\sum_{n=1}^{\infty} b_n$收敛, 则级数$\sum_{n=1}^{\infty} a_n$收敛.
   - 若$L = +\infty$, 且级数$\sum_{n=1}^{\infty} b_n$发散, 则级数$\sum_{n=1}^{\infty} a_n$发散.

3. $p$-级数判别法: 设$\{a_n\}$为非负数列, 且$K$为常数. 则:
   - 若$a_n \leq \frac{K}{n^p}$, 且$p>1$, 则级数$\sum_{n=1}^{\infty} a_n$收敛.
   - 若$a_n \geq \frac{K}{n^p}$, 且$p \leq 1$, 则级数$\sum_{n=1}^{\infty} a_n$发散.

4. Cauchy根值判别法: 设$\{a_n\}$为非负数列, 则:
   - 若$\lim_{n \to \infty} \sqrt[n]{a_n} = L < 1$, 则级数$\sum_{n=1}^{\infty} a_n$收敛.
   - 若$\lim_{n \to \infty} \sqrt[n]{a_n} = L > 1$, 则级数$\sum_{n=1}^{\infty} a_n$发散.
   - 若$\lim_{n \to \infty} \sqrt[n]{a_n} = 1$, 则该判别法无法判断级数$\sum_{n=1}^{\infty} a_n$的敛散性.

5. D'Alembert比值判别法: 设$\{a_n\}$为非负数列, 则:
   - 若$\lim_{n \to \infty} \frac{a_{n+1}}{a_n} = L < 1$, 则级数$\sum_{n=1}^{\infty} a_n$收敛.
   - 若$\lim_{n \to \infty} \frac{a_{n+1}}{a_n} = L > 1$, 则级数$\sum_{n=1}^{\infty} a_n$发散.
   - 若$\lim_{n \to \infty} \frac{a_{n+1}}{a_n} = 1$, 则该判别法无法判断级数$\sum_{n=1}^{\infty} a_n$的敛散性.

证明: 本定理的证明需要一个引理:

**引理**: 设$\{x_n\}$为数列, 那么一定存在:
$$
\underline{\lim_{n \to \infty}} \frac{x_{n+1}}{x_n} \leq \underline{\lim_{n \to \infty}} \sqrt[n]{x_n} \leq \overline{\lim_{n \to \infty}} \sqrt[n]{x_n} \leq \overline{\lim_{n \to \infty}} \frac{x_{n+1}}{x_n}
$$

**证明**: 设$\overline{r} = \overline{\lim_{n \to \infty}} \frac{x_{n+1}}{x_n}$, 则对于任意$\epsilon > 0$, 存在$N$, 当$n > N$时, 有:
$$
\frac{x_{n+1}}{x_n} < \overline{r} + \epsilon
$$
因此, 对于任意$m > n > N$, 有:
$$
x_m = \frac{x_m}{x_{m-1}} \cdot \frac{x_{m-1}}{x_{m-2}} \cdots \frac{x_{n+1}}{x_n} x_n < (\overline{r} + \epsilon)^{m-n} x_n
$$
即:
$$
\sqrt[m]{x_m} < \sqrt[m]{(\overline{r} + \epsilon)^{m-n} x_n} = (\overline{r} + \epsilon)^{1 - \frac{n}{m}} \sqrt[m]{x_n}
$$
令$m \to \infty$, 则有:
$$
\overline{\lim_{n \to \infty}} \sqrt[n]{x_n} \leq \overline{r} + \epsilon
$$
由于$\epsilon$任意, 故有:
$$
\overline{\lim_{n \to \infty}} \sqrt[n]{x_n} \leq \overline{\lim_{n \to \infty}} \frac{x_{n+1}}{x_n}
$$

类似地, 可以证明下极限部分的不等式.

利用上述引理, 我们可以证明D'Alembert比值判别法:

**证明**: 设$\lim_{n \to \infty} \frac{a_{n+1}}{a_n} = L < 1$, 则由引理可知:
$$
\lim_{n \to \infty} \sqrt[n]{a_n} = L < 1
$$
由Cauchy根值判别法可知, 级数$\sum_{n=1}^{\infty} a_n$收敛.

同理, 若$\lim_{n \to \infty} \frac{a_{n+1}}{a_n} = L > 1$, 则由引理可知:
$$
\lim_{n \to \infty} \sqrt[n]{a_n} = L > 1
$$
由Cauchy根值判别法可知, 级数$\sum_{n=1}^{\infty} a_n$发散. 证明完毕.

6. Raabe判别法: 设$\{a_n\}$为非负数列, 则:
   - 若存在常数$r > 1$, 且对于下面这个极限表达式:
   $$
   \lim_{n \to \infty} n \left( \frac{a_n}{a_{n+1}} - 1 \right) = r 
   $$
   * 当$r > 1$时, 级数$\sum_{n=1}^{\infty} a_n$收敛.
   * 当$r < 1$时, 级数$\sum_{n=1}^{\infty} a_n$发散.
   * 当$r = 1$时, 该判别法无法判断级数$\sum_{n=1}^{\infty} a_n$的敛散性.

Raabe判别法是D'Alembert比值判别法的推广. 主要思想是对比$\frac{a_{n+1}}{a_n}$与$1 - \frac{1}{n}$的大小关系, 因为$\sum_{n=1}^{\infty} \frac{1}{n}$发散, 而$\sum_{n=1}^{\infty} \frac{1}{n^p}$在$p > 1$时收敛. 若$\frac{a_{n+1}}{a_n}$与$1 - \frac{1}{n}$的差距足够大, 则可以判断级数的敛散性.

**证明**:

先证明第一个结论: 

$$ \because r > 1, \therefore \exists s,t \in \mathbb{R}, r > s > t > 1 $$
$$ \therefore \exists N \in \mathbb{N}, \text{s.t. } \forall n > N, n\left(\frac{a_n}{a_{n+1}} - 1\right) > s $$
$$ \therefore \forall n > N, \frac{a_n}{a_{n+1}} > 1 + \frac{s}{n} $$
$$ \because 1 + \frac{s}{n} > \left(1 + \frac{1}{n}\right)^t, \therefore \forall n > N, \frac{a_n}{a_{n+1}} > \left(1 + \frac{1}{n}\right)^t = \left(\frac{n+1}{n}\right)^t $$

所以我们得到: $a_n n^t > a_{n+1} (n+1)^t$.

因此, $a_n n^t$递减, 必有上界, 设其上界为$M$, 则对于任意$n \in \mathbb{N}$, 有$a_n n^t \leq M$, 即$a_n \leq \frac{M}{n^t}$. 由于$t > 1$, 故级数$\sum_{n=1}^{\infty} a_n$收敛.

对于第二个结论:

$$ \because r < 1, \therefore \exist n > N, \text{s.t. } < 1+\frac{r}{n} < 1 + \frac{1}{n}
$$

$$
\therefore \frac{x_n}{x_{n+1}} < \frac{n+1}{n}, \quad x_n n < x_{n+1} (n+1)
$$

因此, $x_n n$递增, 故级数$\sum_{n=1}^{\infty} a_n$发散. 证明完毕.

1. 积分判别法: 设$f(x)$在$[a,+\infty)$上有定义, 且对任意$A\in (a,+\infty)$, $f(x)$在$[a,A]$上Riemann可积, 那么我们取一单增且发散的数列, 同时定义:
   $$
   \{a_n\} \quad \text{s.t.} \quad a = a_1 < a_2 < \cdots < a_n < \cdots,  \quad
   u_n = \int_{a_n}^{a_{n+1}}f(x)dx
   $$
   那么$\sum_{n=1}^{\infty} u_n$和$\int_{a}^{+\infty}f(x)dx$敛散性相同.

   特别的, 若$f(x)$单调下降, 取$a_n = n$, 那么反常积分$\int_a^{+\infty} f(x)dx$ 与正项技术$\sum_{n=N}^{\infty}, N = [a]+1$敛散性相同.

   **证明提示***: 设$S_k = \sum_{i=1}^{k} u_i$, 对下面这个式子取极限:
   $$\forall A > a, \exist n, \text{s.t.} S_{n-1} \leq \int_a^Af(x)dx < S_{n+1}$$

   本定理也可以反向证明反常积分的敛散性.

#### 任意级数的审敛法

*交错级数的审敛法*

**定义**: 设$\{a_n\}$为非负数列, 则级数$\sum_{n=1}^{\infty} (-1)^{n-1} a_n$称为**交错级数**.

1. Leibniz判别法: 设$\{a_n\}$为单调递减且趋于零的非负数列, 则交错级数$\sum_{n=1}^{\infty} (-1)^{n-1} a_n$收敛.

**证明**: 设$S_n = \sum_{k=1}^{n} (-1)^{k-1} a_k$为交错级数的部分和序列, 则对于任意$n \in \mathbb{N}$, 有:
$$
S_{2n} = (a_1 - a_2) + (a_3 - a_4) + \cdots + (a_{2n-1} - a_{2n}) \leq a_1
$$
$$
S_{2n+1} = S_{2n} + a_{2n+1} \geq S_{2n}
$$
因此, $\{S_{2n}\}$为单调递增且有上界的数列, 故存在极限$S_{2n} \to S$. 由于$\{S_{2n+1}\}$为单调递减且有下界的数列, 故存在极限$S_{2n+1} \to S'$. 由于$a_n \to 0$, 故$S' = S$. 因此, 部分和序列$\{S_n\}$收敛, 故交错级数$\sum_{n=1}^{\infty} (-1)^{n-1} a_n$收敛. 证明完毕.

2. 绝对收敛与条件收敛: 设$\sum_{n=1}^{\infty} x_n$为级数, 若级数$\sum_{n=1}^{\infty} |x_n|$收敛, 则称级数$\sum_{n=1}^{\infty} x_n$**绝对收敛**; 若级数$\sum_{n=1}^{\infty} |x_n|$发散, 但级数$\sum_{n=1}^{\infty} x_n$收敛, 则称级数$\sum_{n=1}^{\infty} x_n$**条件收敛**.

**定理**: 绝对收敛的级数必收敛.

**A-D判别法**: 若下列两个条件之一成立, 则级数$\sum_{n=1}^{\infty} x_n y_n$收敛:
1. 数列$\{x_n\}$的部分和序列$\{S_n\}$有界, 且数列$\{y_n\}$单调且趋于零.
2. 数列$\{x_n\}$单调有界, 且数列$\{y_n\}$的部分和序列$\{T_n\}$收敛.
   
   这两个条件分别称为Dirichlet判别法和Abel判别法.

证明: 先证明Abel引理, 先推出一个Abel变换公式:
$$
\sum_{k=1}^{p} a_k b_k = a_p B_p - \sum_{k=1}^{p-1} B_k (a_{k+1} - a_k)
$$

其中$B_k = \sum_{i=1}^{k} b_i$.

这个公式可以如下推出:

$$
\sum_{k=1}^{p} a_k b_k = a_1B_1 + \sum_{k=2}^{p}a_kb_k = a_1B_1 + \sum_{k=2}^p a_k (B_k-B_{k-1}) = a_1B_1 + \sum_{k=2}^p a_k B_k - \sum_{k=2}^p a_k B_{k-1}
$$
$$= a_1B_1 + \sum_{k=2}^p a_k B_k - \sum_{k=1}^{p-1} a_{k+1} B_k = a_p B_p - \sum_{k=1}^{p-1} B_k (a_{k+1} - a_k)
$$

**Abel引理**: $\{a_k\}$为单调数列, $\{B_k\}$为有界数列, 则存在常数$M > 0$, 使得$\forall p \in \mathbb{N}$:
$$
\left| \sum_{k=1}^{p} a_k b_k \right| \leq M (|a_1|+2|a_p|)
$$

**证明**: 由Abel变换公式, 有:
$$
\left| \sum_{k=1}^{p} a_k b_k \right| = \left| a_p B_p - \sum_{k=1}^{p-1} B_k (a_{k+1} - a_k) \right| \leq |a_p||B_p| + \sum_{k=1}^{p-1} |B_k| |a_{k+1} - a_k|
$$
由于$\{B_k\}$有界, 故存在常数$M > 0$, 使得对于任意$k \in \mathbb{N}$, 有$|B_k| \leq M$. 因此, 上式右端继续估计:
$$
\leq M |a_p| + M \sum_{k=1}^{p-1} |a_{k+1} - a_k| = M |a_p| + M (|a_1 - a_2| + |a_2 - a_3| + \cdots + |a_{p-1} - a_p|)
$$
$$
= M |a_p| + M (|a_1| + |a_p|) = M (|a_1| + 2 |a_p|)
$$

利用Abel引理, 我们可以证明A-D判别法. 这里不再赘述.

#### 任意项级数和更序数列

**定义**: 我们给出$x_n^+$和$x_n^-$的定义:

1. $x_n^+ = \begin{cases} x_n, & x_n > 0 \\ 0, & x_n \leq 0 \end{cases}$
2. $x_n^- = \begin{cases} -x_n, & x_n < 0 \\ 0, & x_n \geq 0 \end{cases}$

则有$x_n = x_n^+ - x_n^-$且$|x_n| = x_n^+ + x_n^-$. 由此, 我们可以将任意级数$\sum_{n=1}^{\infty} x_n$拆分为两个正项级数$\sum_{n=1}^{\infty} x_n^+$和$\sum_{n=1}^{\infty} x_n^-$.

**定理**: 级数$\sum_{n=1}^{\infty} x_n$绝对收敛的充分必要条件是级数$\sum_{n=1}^{\infty} x_n^+$和$\sum_{n=1}^{\infty} x_n^-$均收敛.

**定理**: 若级数$\sum_{n=1}^{\infty} x_n$条件收敛, 则$\{x_n^+\}$和$\{x_n^-\}$均发散到$+\infty$.

**定义**: 更序列: 设$\sum_{n=1}^{\infty} x_n$为级数, 若存在一个双射$\pi: \mathbb{N} \to \mathbb{N}$, 使得级数$\sum_{n=1}^{\infty} x_{\pi(n)}$收敛, 则称级数$\sum_{n=1}^{\infty} x_{\pi(n)}$为级数$\sum_{n=1}^{\infty} x_n$的一个**重排**.

**定理**: 设级数$\sum_{n=1}^{\infty} x_n$绝对收敛, 则对于任意重排$\sum_{n=1}^{\infty} x_{\pi(n)}$, 都有:
$$\sum_{n=1}^{\infty} x_{\pi(n)} = \sum_{n=1}^{\infty} x_n$$

**定理(Riemann重排定理)**: 设级数$\sum_{n=1}^{\infty} x_n$条件收敛, 则对于任意$S \in \mathbb{R} \cup \{+\infty, -\infty\}$, 都存在级数$\sum_{n=1}^{\infty} x_{\pi(n)}$, 使得:
$$\sum_{n=1}^{\infty} x_{\pi(n)} = S$$

本定理的证明略, 可参考相关教材.

期末考试内容截止于此. 这部分内容除了正常的不定积分和黎曼积分外, 重点是对**无穷**的认知. 需要建立一个足够严谨的直觉, 来理解无穷小和无穷大的概念, 以及它们在极限、连续、导数、积分和级数中的应用.

**级数的乘法**: 设$\sum_{n=0}^{\infty} a_n$和$\sum_{n=0}^{\infty} b_n$为两个级数, 则它们的乘积定义为:
$$
\left( \sum_{n=0}^{\infty} a_n \right) \left( \sum_{n=0}^{\infty} b_n \right) = \sum_{n=0}^{\infty} c_n
$$

这一定义的本质, 就是下面这个矩阵中所有元素的和:

$$\begin{pmatrix}
    a_1 b_1 & a_1 b_2 & a_1 b_3 & a_1 b_4 & \cdots \\
    a_2 b_1 & a_2 b_2 & a_2 b_3 & a_2 b_4 & \cdots \\
    a_3 b_1 & a_3 b_2 & a_3 b_3 & a_3 b_4 & \cdots \\
    a_4 b_1 & a_4 b_2 & a_4 b_3 & a_4 b_4 & \cdots \\
    \vdots   & \vdots   & \vdots   & \vdots   & \ddots
\end{pmatrix}
$$

我们知道, 对于两个有限部分和的乘积, 他们最终的结果与相加的次序没有关联, 那么对于无穷级数的乘积, 他们的结果是否也与相加的次序无关呢? 非常不幸, 它们的结果不一定与顺序无关. 我们需要规定一种或者几种相加的次序, 这里我们采用**对角线相加法**:

$$
\sum_{i=1}^{\infty} a_i \cdot \sum_{j=1}^{\infty} b_j = \sum_{n=2}^{\infty} \sum_{k=1}^{n-1} a_k b_{n-k} = a_1 b_1 + (a_1 b_2 + a_2 b_1) + (a_1 b_3 + a_2 b_2 + a_3 b_1) + \cdots
$$

这种乘积也叫做**Cauchy乘积**.

另一种常见的乘积方式定义如下:

$$
\sum_{i=1}^{\infty} a_i \cdot \sum_{j=1}^{\infty} b_j = \sum_{n=1}^{\infty} \left(\sum_{i=1}^{n}(a_i b_n+ a_n b_i) - a_n b_n \right)
$$

这种乘积被称为**正方形乘积**.

**定理**: 只要级数$\sum_{n=0}^{\infty} a_n$和$\sum_{n=0}^{\infty} b_n$收敛, 则他们的正方形乘积收敛.

然而Cauchy乘积并不一定满足上述的性质, 下面给出一个反例:

**反例**: 设$a_n = b_n = \frac{(-1)^{n+1}}{\sqrt{n}}$, 则级数$\sum_{n=1}^{\infty} a_n$和$\sum_{n=1}^{\infty} b_n$均收敛(根据莱布尼茨判别法). 但是他们的Cauchy乘积的一般项为:

$$
c_n = (-1)^{n+1} \sum_{i+j= n+1} \frac{1}{\sqrt{ij}} \geq (-1)^{n+1} \sum_{i+j=n+1} \frac{2}{i+j} = (-1)^{n+1} \sum_{i+j=n+1} \frac{2}{n+1} = (-1)^{n+1} n \cdot \frac{2}{n+1}
$$

由于通项不趋近于0, 必然发散.

**定理**: 设级数$\sum_{n=0}^{\infty} a_n$和$\sum_{n=0}^{\infty} b_n$绝对收敛, 则他们的Cauchy乘积和正方形乘积(甚至任意方式进行加法)均绝对收敛, 且乘积均等于:

$$
\left( \sum_{n=0}^{\infty} a_n \right) \left( \sum_{n=0}^{\infty} b_n \right) 
$$

证明: 设$a_{i_k} b_{j_k}$是所有$a_i b_j$的一个排列, 则有对任意的$n$, 取:

$$N = \max_{1 \leq k \leq n} \{i_k, j_k\}$$

$$\sum_{k=1}^n |a_{i_k} b_{j_k}| \leq \sum_{i=1}^N \sum_{j=1}^N |a_i b_j| = \left( \sum_{i=1}^N |a_i| \right) \left( \sum_{j=1}^N |b_j| \right) \leq \left( \sum_{i=1}^{\infty} |a_i| \right) \left( \sum_{j=1}^{\infty} |b_j| \right)
$$

因为$\sum_{i=1}^{\infty} |a_i|$和$\sum_{j=1}^{\infty} |b_j|$均收敛, 故存在常数$M > 0$, 使得对于任意$n \in \mathbb{N}$, 有:
$$\sum_{k=1}^n |a_{i_k} b_{j_k}| \leq M$$

所以任意排列的部分乘积序列的绝对值一定单增有上界, 必然绝对收敛. 证明完毕.

由d'Alembert比值判别法, 我们可以得到下面这个定理:

**定理**: 对任意$x \in \mathbb{R}$, 我们一定有:
$$
T = \sum_{n=0}^{\infty} \frac{x^n}{n!}
$$
这个级数$T$必然收敛. 且根据后面的知识我们可以知道, 这个级数的和就是$e^x$.

证明: 我们采用Cauchy乘积, 由于其绝对收敛, 我们可以得到:

$$
\left( \sum_{n=1}^{\infty} \frac{x^n}{n!} \right) \left( \sum_{n=1}^{\infty} \frac{y^n}{n!} \right) = \sum_{n=0}^{\infty} \sum_{k=0}^{n} \frac{x^k}{k!} \cdot \frac{y^{n-k}}{(n-k)!} = \sum_{n=0}^{\infty} \frac{(x+y)^n}{n!}
$$

也就是$f(x+y) = f(x)f(y)$, 满足这个式子的只有$f(x) = e^x$. 所以收敛.

#### 无穷乘积

**定义**: 设$\{p_n\}$为无穷可列个非零实数, 我们称他们的积:

$$
p_1 \cdot p_2 \cdot p_3 \cdots p_n \cdots = \prod_{n=1}^{\infty} p_n
$$

为无穷乘积, $p_n$称为通项, 我们可以类似的定义部分积$\{P_n\}$:

$$
P_n = p_1 \cdot p_2 \cdot p_3 \cdots p_n = \prod_{k=1}^{n} p_k
$$

若部分积数列$\{P_n\}$收敛于一个非零的有限数$P$(**也就是说如果收敛到$0$, 我们称此数列发散**), 则称无穷乘积$\prod_{n=1}^{\infty} p_n$收敛, 且其积为:
$$
\prod_{n=1}^{\infty} p_n = \lim_{n \to \infty} P_n = P
$$

否则称无穷乘积$\prod_{n=1}^{\infty} p_n$发散(包括收敛到$0$的情况).

**定理**: 无穷乘积收敛的必要条件如下:

$$\lim_{n \to \infty} p_n = 1 \quad \quad$$

$$\lim_{n\to \infty} \prod_{k=n+1}^{\infty} p_k = 1$$

这个判别法和级数和的定义类似.

证明: 我们永远可以写出这个表达式: 取极限即可.

$$
\lim_{k \to \infty} p_k = \lim_{k \to \infty}\frac{\prod_{n=1}^k p_n}{\prod_{n=1}^{k-1} p_n} =\lim_{k \to \infty} \frac{P_k}{P_{k-1}} = 1
$$

第二个必要条件的证法类似, 这里不再赘述.

**提示**: 我们经常把$p_n = 1+ a_n$, 这个表达式更利于分析问题.

显然我们可以得到:$\prod_{n=1}^{\infty} (1+a_n)$收敛的必要条件是: $\lim_{n \to \infty} a_n = 0$

例: 设$p_n = 1 - \frac{1}{(2n)^2}$, 判断无穷乘积的敛散性.

$$
P_n = \prod_{k=1}^n[1-\frac{1}{(2k)^2}] = \prod_{k=1}^n \frac{(2k-1)(2k+1)}{2k \cdot 2k} = \frac{1 \cdot 3 \cdot 3 \cdot 5 \cdots (2n-1)(2n+1)}{2 \cdot 2 \cdot 4 \cdot 4 \cdots (2n)(2n)}
$$

$$
\therefore P_n =\frac{(2n-1)!!}{(2n)!!}(2n+1)!! = \frac{2}{\pi} \frac{I_{2n}}{I_{2n+1}} 
$$

其中, $I_n = \int_0^{\frac{\pi}{2}} \sin^n x dx$, 因为$I_{2n+1} < I_{2n} <I_{2n-1}$:

$$
1 < \frac{I_{2n}}{I_{2n+1}} < \frac{I_{2n-1}}{I_{2n+1}} = \frac{2n+1}{2n}
\therefore \lim_{n \to \infty} P_n = \frac{2}{\pi}
$$

**Wallice**公式: 设$p_n = \frac{(2n)^2}{(2n-1)(2n+1)}$, 则无穷乘积:
$$
\prod_{n=1}^{\infty} \frac{(2n)^2}{(2n-1)(2n+1)} = \frac{\pi}{2}
$$
$$
\frac{2 \cdot 2 \cdot 4 \cdot 4 \cdots (2n) \cdot (2n)}{1 \cdot 3 \cdot 3 \cdot 5 \cdots (2n-1)(2n+1)} = \frac{\pi}{2}
$$

例: 设$p_n = \cos \frac{x}{2^n}$

$$
\sin x = 2 \cos \frac{x}{2} \sin \frac{x}{2} = 2^2 \cos \frac{x}{2} \cos \frac{x}{2^2} \sin \frac{x}{2^2} = \cdots = 2^n \left( \prod_{k=1}^n \cos \frac{x}{2^k} \right) \sin \frac{x}{2^n}
$$

$$
P_n = \prod_{k=1}^n \cos \frac{x}{2^k} = \frac{\sin x}{2^n \sin \frac{x}{2^n}}
$$

$$
\therefore \lim_{n \to \infty} P_n =\lim_{n \to \infty} \frac{\sin x}{2^n \sin \frac{x}{2^n}} =\lim_{n \to \infty} \frac{\sin x}{x} = 1
$$

**Viete**公式: 设$p_n = \cos \frac{\pi}{2^{n+1}}$, 对上式, 令$x = \frac{\pi}{2}$, 则无穷乘积:
$$
\prod_{n=1}^{\infty} \cos \frac{\pi}{2^{n+1}} = \frac{2}{\pi}
$$

**定理**: 设$p_n = 1 - a_n$, 且$a_n \geq 0$, 则无穷乘积$\prod_{n=1}^{\infty} p_n$收敛的充分必要条件是级数$\sum_{n=1}^{\infty} a_n$收敛. 这个转化的过程就是在无穷乘积等式两侧取对数.

**证明**: 设$P_n = \prod_{k=1}^{n} p_k$, 则有:
$$
\ln P_n = \ln \left( \prod_{k=1}^{n} p_k \right) = \sum_{k=1}^{n} \ln p_k
$$

**推论**: 设$p_n = 1 + a_n$, 且$a_n$不变号, 则无穷乘积$\prod_{n=1}^{\infty} p_n$收敛的充分必要条件是级数$\sum_{n=1}^{\infty} a_n$收敛. 本推论的证明略.

**推论**: 设$p_n = 1 + a_n$, 若$\sum_{n=1}^{\infty}a_n$收敛, 那么无穷乘积$\prod_{n=1}^{\infty} p_n$收敛的充分必要条件是$\sum_{n=1}^{\infty}a_n^2$收敛. 下面给出本推论的证明:

**证明**: 设$P_n = \prod_{k=1}^{n} p_k$, 则有:
$$
\ln P_n = \ln \left( \prod_{k=1}^{n} p_k \right) = \sum_{k=1}^{n} \ln (1 + a_k)
$$
由于$\sum_{n=1}^{\infty} a_n$收敛, 故$a_n \to 0$. 因此, 对于充分大的$n$, 有:
$$
\ln (1 + a_n) = a_n - \frac{a_n^2}{2} + o(a_n^2)
$$
因此, 当$n$充分大时, 有:
$$
\ln P_n = \sum_{k=1}^{n} \left( a_k - \frac{a_k^2}{2} + o(a_k^2) \right) = \sum_{k=1}^{n} a_k - \frac{1}{2} \sum_{k=1}^{n} a_k^2 + \sum_{k=1}^{n} o(a_k^2)
$$
由于$\sum_{n=1}^{\infty} a_n$收敛, 故$\sum_{n=1}^{\infty} o(a_n^2)$也收敛. 因此, 无穷乘积$\prod_{n=1}^{\infty} p_n$收敛的充分必要条件是级数$\sum_{n=1}^{\infty} a_n^2$收敛. 证明完毕.

**注意**: 我们要求$\sum_{k=1}^{\infty} a_n^2$收敛, 而不是$\sum_{k=1}^{\infty} a_n$收敛, 因为这样可以推出$a_n^k$均收敛, 进而保证对数级数的收敛性.

**绝对收敛**: 当级数$\sum_{n=1}^{\infty} |a_n|$收敛时, 称级数$\prod_{n=1}^{\infty} p_n$**绝对收敛**; 否则称为**条件收敛**.

绝对数列的无穷乘积具有交换性, 任意重排后的无穷乘积均收敛且等于原无穷乘积的值. 而收敛但是不绝对收敛的无穷乘积则不具有交换性, 任意重排后的无穷乘积可能收敛到不同的值, 甚至发散.

**定理**: 若$a_n > -1$, 下面三个定理等价:
- $\prod_{n=1}^{\infty} (1+a_n)$绝对收敛.
- $\prod_{n=1}^{\infty} (1+|a_n|)$收敛.
- $\sum_{n=1}^{\infty} a_n$收敛.

**Stirling公式**: 当$n \to \infty$, 有近似公式:

$$
n! \sim \sqrt{2 \pi n} \left( \frac{n}{e} \right)^n \quad n \to \infty 
$$

证明提示: 设$p_n = \frac{(n+1)! e^{n+1}}{(n+1)^{n+1} n! e^n} = \frac{e}{(1 + \frac{1}{n})^{n+1}}$

至此, 课程MATH1203数学分析I的内容全部结束. 


$$
F(x) = \int_0^{x^3} t^3 \sin t dt - x^3 \int_0^x t^3 \sin t dt
$$

$$
\begin{aligned}
    \frac{d}{dx}F(x) &= \frac{d}{dx} \int_0^{x^3} t^3 \sin t dt - \frac{d}{dx} \left( x^3 \int_0^{x^3} t^3 \sin t dt \right) \\
    &= 3x^2 \cdot (x^3)^3 \sin (x^3) - 3x^2 \int_0^{x^3} \sin t dt - 3x^2 \cdot x^3 \sin x \\
    &= 3x^5(x^6-1) \sin (x^3) - 3x^2 \int_0^{x^3} \sin t dt \\
    &= 3x^5(x^6-1) \sin (x^3) - 3x^2 \cdot (-\cos x^3 + 1) \\
    &= 3x^5(x^6-1) \sin (x^3) + 3x^2 \cos x^3 - 3x^2
\end{aligned}
$$