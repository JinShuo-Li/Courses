# 数学分析期末

范围: 多元函数的积分学

时间: 2026年6月22日

作者: 李谨硕

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