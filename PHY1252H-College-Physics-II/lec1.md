# 静电场

> 场是用空间位置函数来表述的, 如果物理量是标量则是标量场, 如果物理量是矢量则是矢量场.

## 电力和电荷

### 基本性质

> 电力是非常强的长程力(与引力相比约强 $10^{36}$ 倍), 存在于原子内部和宇宙天体之间, 存在吸引与排斥两种形式.
>
> 电荷是物质的性质, 具有正负两种, 且具有量子性: 任何带电体的电量都是元电荷 $e$ 的整数倍. 由于 $e$ 极小, 宏观电量总是包含极大量的元电荷, 因此可以认为电量是连续分布的. 夸克模型指出还存在着带分数电荷的粒子. 电荷是守恒的, 即$\sum_i q_i = \text{const.}$ 电荷具有运动不变性(即在不同惯性系中测量到的电荷值相同). 当带电体的线度远小于它到考察点的距离时, 我们采用点电荷模型.

### 库仑定律 & 电力叠加原理

**库仑定律**: 在真空中, 两个静止点电荷间的相互作用电力的方向沿着它们的连线. 同号电荷相互排斥, 异号电荷相互吸引. 电力的大小与两电荷的乘积成正比, 与它们之间距离的平方成反比. 公式为:

$$
F = k \frac{q_1 q_2}{r^2}, \quad k = \frac{1}{4\pi \epsilon_0} \approx 8.9875 \times 10^9 \ \text{N}\cdot\text{m}^2/\text{C}^2
$$

$$
\epsilon_0 \approx 8.85 \times 10^{-12} \ \text{C}^2/(\text{N}\cdot\text{m}^2)
$$

矢量表达式为: $\vec{F} = k \frac{q_1 q_2}{r^2} \vec{e}_r = k \frac{q_1 q_2}{r^2} \frac{\vec{r}}{r} = k \frac{q_1 q_2}{r^3} \vec{r}$

其中 $\vec{r}$ 为由施力电荷 $q_1$ 指向受力电荷 $q_2$ 的矢量, $r = |\vec{r}|$, $\vec{e}_r = \vec{r}/r$ 为该方向的单位矢量. 按此约定上式给出的是 $q_2$ 所受的电力: 当 $q_1 q_2 > 0$ 时力沿 $\vec{e}_r$ 方向(排斥), 当 $q_1 q_2 < 0$ 时力沿 $-\vec{e}_r$ 方向(吸引).

**适用条件**: 只适用于真空中的两个静止点电荷. 对于运动电荷, 电力不再严格满足该式(还需考虑磁力等效应).

当然我们如果把$k = \frac{1}{4\pi \epsilon_0}$代入, 就会在分母上看到球面面积$4\pi r^2$, 这和后续的高斯定律有很大关系.

**电力叠加原理**: 在真空中, 多个静止点电荷间的相互作用电力是各个点电荷之间相互作用电力的矢量和. 一个点电荷系对点电荷的总电力的公式为:

$$
\vec{F} = \sum_i \vec{F}_i = k \sum_i \frac{q q_i}{r_i^2} \vec{e}_{r_i} = k q \sum_i \frac{q_i}{r_i^2} \vec{e}_{r_i}
$$

其中 $\vec{e}_{r_i}$ 为由 $q_i$ 指向 $q$ 的单位矢量.

掌握了**库仑定律**和**电力叠加原理**, 我们就可以计算任意点电荷系对某个点电荷的总电力了. 对于连续带电体, 如果我们已知其电荷密度分布$\rho(\vec{r}')$, 那么我们可以把它看作是由无数个点电荷组成的, 于是就可以把上式改写为积分形式:

$$
\vec{F} = k q \int \frac{\rho(\vec{r}')}{|\vec{r} - \vec{r}'|^2} \frac{\vec{r} - \vec{r}'}{|\vec{r} - \vec{r}'|} dV' = k q \int \frac{\rho(\vec{r}') (\vec{r} - \vec{r}')}{|\vec{r} - \vec{r}'|^3} dV'
$$

其中 $\vec{r}$ 为场点(受力电荷 $q$ 所在处)的位置矢量, $\vec{r}'$ 为源点(电荷元 $dq = \rho(\vec{r}') dV'$ 所在处)的位置矢量, 积分遍及整个带电体.

### 电场强度

**电场和静电场**: 电场是电荷周围存在、并传递电荷间相互作用的特殊物质. 静电场是静止点电荷(系)产生的电场. 电场是矢量场, 其方向定义为在该点放置一个正电荷时所受电力的方向.

**电场强度**: 描述场中各点电场的大小和方向的物理量, 单位为 $\text{N/C}$(也即 $\text{V/m}$).   
用于借助库仑力测定电场强度的电荷叫做试验电荷(记为 $q_0$), 要求:
- 试验电荷的电量要足够小, 以免影响原有电场的分布
- 试验电荷必须足够小, 可以近似的看作是点电荷, 以便于计算

定义式为:

$$
\vec{E} = \lim_{q_0 \to 0} \frac{\vec{F}}{q_0}
$$

对于点电荷$q$产生的电场, 结合库仑定律, 其电场强度为:

$$
\vec{E} = k \frac{q}{r^2} \vec{e}_r = k \frac{q}{r^2} \frac{\vec{r}}{r} = k \frac{q}{r^3} \vec{r}
$$

同样, 我们也可以使用积分形式来计算连续带电体产生的电场强度:

$$
\vec{E} = k \int \frac{\rho(\vec{r}')}{|\vec{r} - \vec{r}'|^2} \frac{\vec{r} - \vec{r}'}{|\vec{r} - \vec{r}'|} dV' = k \int \frac{\rho(\vec{r}') (\vec{r} - \vec{r}')}{|\vec{r} - \vec{r}'|^3} dV'
$$

**e.g.1: 求均匀带电直线的电场分布**

**模型**: 长为 $L$ 的均匀带电直线, 线电荷密度为 $\lambda$(设 $\lambda > 0$), 求距直线距离为 $a$ 的场点 $P$ 处的电场强度.

**取坐标系**: 以 $P$ 到直线的垂足为原点 $O$, 沿直线取 $y$ 轴, 由 $O$ 指向 $P$ 的方向取 $x$ 轴. 直线上坐标为 $y$ 处取电荷元 $dq = \lambda dy$, 它到场点 $P$ 的位置矢量为 $\vec{r} = a\vec{e}_x - y\vec{e}_y$, 距离为 $r = |\vec{r}| = \sqrt{a^2+y^2}$.

**电荷元的场**: 由点电荷的场强公式,

$$
d\vec{E} = k\frac{dq}{r^2}\vec{e}_r = k\frac{\lambda dy}{a^2+y^2}\cdot\frac{a\vec{e}_x - y\vec{e}_y}{\sqrt{a^2+y^2}} = \frac{k\lambda}{(a^2+y^2)^{3/2}}(a\vec{e}_x - y\vec{e}_y)dy
$$

即

$$
dE_x = \frac{k\lambda a}{(a^2+y^2)^{3/2}}dy, \qquad dE_y = -\frac{k\lambda y}{(a^2+y^2)^{3/2}}dy
$$

**积分**: 设直线两端坐标为 $y_1, y_2$, 利用 $\displaystyle\int\frac{dy}{(a^2+y^2)^{3/2}} = \frac{y}{a^2\sqrt{a^2+y^2}}$ 与 $\displaystyle\int\frac{y\,dy}{(a^2+y^2)^{3/2}} = -\frac{1}{\sqrt{a^2+y^2}}$,

$$
E_x = k\lambda a\int_{y_1}^{y_2}\frac{dy}{(a^2+y^2)^{3/2}} = \frac{k\lambda}{a}\left[\frac{y}{\sqrt{a^2+y^2}}\right]_{y_1}^{y_2} = \frac{k\lambda}{a}(\sin\theta_2 - \sin\theta_1)
$$

$$
E_y = -k\lambda\int_{y_1}^{y_2}\frac{y\,dy}{(a^2+y^2)^{3/2}} = \frac{k\lambda}{a}\left[\frac{1}{\sqrt{a^2+y^2}}\right]_{y_1}^{y_2} = \frac{k\lambda}{a}(\cos\theta_2 - \cos\theta_1)
$$

其中 $\theta_1, \theta_2$ 分别为直线下端、上端到场点 $P$ 的连线与垂线($x$ 轴)的夹角, 取偏向 $y$ 轴正向时为正, 于是 $\sin\theta_i = \dfrac{y_i}{\sqrt{a^2+y_i^2}}$, $\cos\theta_i = \dfrac{a}{\sqrt{a^2+y_i^2}}$.

**讨论**:

1. **中垂线上** ($y_1 = -\frac{L}{2}, y_2 = \frac{L}{2}$, 即 $\theta_1 = -\theta, \theta_2 = \theta$): 由对称性 $E_y = 0$, 场强沿垂线背离直线,

$$
E = E_x = \frac{2k\lambda\sin\theta}{a} = \frac{\lambda L}{4\pi\epsilon_0 a\sqrt{a^2 + (L/2)^2}} = \frac{q}{4\pi\epsilon_0 a\sqrt{a^2 + (L/2)^2}}
$$

其中 $q = \lambda L$ 为直线总电量. 当 $a \gg L$ 时 $E \approx \dfrac{q}{4\pi\epsilon_0 a^2}$, 退化为点电荷的场.

2. **无限长直线** ($\theta_1 \to -\frac{\pi}{2}, \theta_2 \to \frac{\pi}{2}$): $E_y = 0$,

$$
E = \frac{2k\lambda}{a} = \frac{\lambda}{2\pi\epsilon_0 a}
$$

方向垂直于直线($\lambda > 0$ 时背离直线). 可见无限长均匀带电直线的场强与距离的一次方成反比, 而不是与平方成反比.

3. **半无限长直线的端点处** ($\theta_1 = 0, \theta_2 = \frac{\pi}{2}$):

$$
E_x = \frac{k\lambda}{a}, \quad E_y = -\frac{k\lambda}{a}, \quad E = \sqrt{E_x^2 + E_y^2} = \frac{\sqrt{2}\lambda}{4\pi\epsilon_0 a}
$$

场强方向与直线成 $45^\circ$ 角, 指向背离直线的一侧.