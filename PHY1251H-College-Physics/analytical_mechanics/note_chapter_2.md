# 守恒定律

物理学一直在追寻守恒律和守恒量. 本章我们将从最小作用量原理出发, 推出常见的几种守恒定律: 能量守恒、动量守恒和角动量守恒.

**定义**(运动积分): 对于一个具有$s$个自由度的系统, 其运动积分是一个函数:

$$F(q_1, q_2, \ldots, q_s, p_1, p_2, \ldots, p_s)$$

若$F$在系统的运动过程中保持不变, 即$\frac{dF}{dt} = 0$. 则$F$被称为系统的一个运动积分.

由前置数学知识(常微分方程理论)可知, 这样一个系统可以得到$2s-1$个独立的运动积分. 每一个运动积分都对应着一个守恒量. 但是并不是所有的运动积分都有相同的重要性和物理意义. 我们需要寻找源自本征性质的守恒量.

换言之, 我们需要寻找反映**时间均匀性**, **空间均匀性**和**空间各向同性**的守恒量. 这三个性质分别对应着能量守恒、动量守恒和角动量守恒.

## 能量守恒

能量守恒直接来自于时间均匀性. 也就是说, 如果一个孤立系统的物理规律不随时间改变, 那么系统的能量将保持不变. 下面我们将从最小作用量原理出发, 推导出能量守恒定律.

我们先对拉格朗日函数求导:

$$
\frac{dL}{dt} = \sum_{i} \frac{\partial L}{\partial q_i} \dot{q}_i + \sum_{i} \frac{\partial L}{\partial \dot{q}_i} \ddot{q}_i
$$

根据拉格朗日方程:

$$
\frac{d}{dt} \left( \frac{\partial L}{\partial \dot{q}_i} \right) - \frac{\partial L}{\partial q_i} = 0
$$

我们代换掉$\frac{\partial L}{\partial q_i}$:

$$
\frac{dL}{dt} = \sum_{i} \frac{\partial L}{\partial \dot{q}_i} \ddot{q}_i + \sum_{i} \frac{d}{dt} \left( \frac{\partial L}{\partial \dot{q}_i} \right) \dot{q}_i
$$

我们观察到上式右侧的两项可以合并成一个总导数:

$$
\frac{dL}{dt} = \frac{d}{dt} \left(\sum_{i} \frac{\partial L}{\partial \dot{q}_i} \dot{q}_i \right)
$$

由于时间具有均匀性, 最终得到:

$$
\frac{d}{dt} \left( \sum_{i} \frac{\partial L}{\partial \dot{q}_i} \dot{q}_i - L \right) = 0, \quad \sum_{i} \frac{\partial L}{\partial \dot{q}_i} \dot{q}_i - L = E = \text{Const}
$$

我们把上述得到的"能量$E$"的表达式用质点系的拉格朗日函数验证一下:

$$
E = \sum_{i=1}^N \frac{\partial L}{\partial \dot{q}_i} \dot{q}_i - L = \sum_{i=1}^N m_i v_i^2 - \left( \sum_{i=1}^N \frac{1}{2} m_i v_i^2 - U(q_1, q_2, \ldots, q_N) \right) = \sum_{i=1}^N \frac{1}{2} m_i v_i^2 + U(q_1, q_2, \ldots, q_N)
$$

换言之, 能量$E$就是系统的动能与势能之和. 这就是我们在牛顿力学中所知的能量的定义.

## 动量守恒

动量守恒来源于空间均匀性. 也就是说, 如果一个孤立系统的物理规律在空间中是均匀的, 那么系统的动量将保持不变. 下面我们将从最小作用量原理出发, 推导出动量守恒定律.

根据空间均匀性, 当封闭力学系统在空间中整体平移的时候, 其性质保持不变, 因此我们研究一个无穷小的平移$\epsilon$, 讨论使拉格朗日函数不变的条件.

$$
\delta L = \sum_{i} \frac{\partial L}{\partial q_i} \cdot \delta q_i = \epsilon \cdot \sum_{i} \frac{\partial L}{\partial q_i} = 0
$$

因为$\epsilon$是任意的, 所以我们可以得出结论:

$$
\sum_{i} \frac{\partial L}{\partial q_i} = 0
$$

根据拉格朗日方程:

$$
\frac{d}{dt} \left( \frac{\partial L}{\partial \dot{q}_i} \right) - \frac{\partial L}{\partial q_i} = 0
$$

因此我们可以得到:

$$\frac{d}{dt} \left( \sum_{i} \frac{\partial L}{\partial \dot{q}_i} \right) = 0$$

进而我们可以知道$\sum_{i} \frac{\partial L}{\partial \dot{q}_i}$是一个守恒量. 这个守恒量被称为**系统的动量**:

$$
P = \sum_{i} \frac{\partial L}{\partial \dot{q}_i} = \text{Const}
$$

因此我们可以得出结论: 在一个空间均匀的系统中, 系统的动量是守恒的. 将上述动量的定义代入质点系的拉格朗日函数, 可以得到:

$$P = \sum_{i=1}^N m_i v_i$$

这就是我们在牛顿力学中所熟知的动量的定义. 因此我们可以得出结论: 在一个空间均匀的孤立系统中, 系统的动量是守恒的. 这就是我们在牛顿力学中所熟知的动量守恒定律.

## 角动量守恒

我们下面将直接从空间各向同性出发, 推导出角动量守恒定律. 根据空间各向同性, 当封闭力学系统在空间中整体旋转的时候, 其性质保持不变, 因此我们研究一个无穷小的旋转$\delta \theta$, 讨论使拉格朗日函数不变的条件.

我们如此变可以得到径矢端点的线位移与转角的关系:

$$
|\delta \vec{r} | = r \sin \theta \cdot \delta \phi, 
\quad \delta \vec{r} = \delta \vec{\phi} \times \vec{r}
$$

同理, 我们可以得到速度矢量的线位移与转角的关系:
$$
|\delta \vec{v} | = v \sin \theta \cdot \delta \phi,
\quad \delta \vec{v} = \delta \vec{\phi} \times \vec{v}
$$

计算拉格朗日函数的变分:

$$
\delta L = \sum_{i} \frac{\partial L}{\partial q_i} \cdot \delta q_i + \sum_{i} \frac{\partial L}{\partial \dot{q}_i} \cdot \delta \dot{q}_i = \sum_{i} \frac{\partial L}{\partial q_i} \cdot (\delta \vec{\phi} \times \vec{r}_i) + \sum_{i} \frac{\partial L}{\partial \dot{q}_i} \cdot (\delta \vec{\phi} \times \vec{v}_i)
$$

我们根据前面在动量的讨论中的定义, 我们给出:

$$
\vec{p_i} = \frac{\partial L}{\partial \dot{q}_i}, \quad \dot{\vec{p_i}} = \frac{\partial L}{\partial q_i}
$$

更进一步的, 根据混合积的性质, 我们可以得到:

$$\delta L = \delta \vec{\phi} \cdot \sum_{i} (\vec{r}_i \times \dot{\vec{p_i}} + \vec{v}_i \times \vec{p_i})$$

因为$\delta \vec{\phi}$是任意的, 因此我们可以得出结论:
$$\sum_{i} (\vec{r}_i \times \dot{\vec{p_i}} + \vec{v}_i \times \vec{p_i}) = 0$$

实际上括号里的内容可以写成一个全微分的形式:

$$\sum_{i} (\vec{r}_i \times \dot{\vec{p_i}} + \vec{v}_i \times \vec{p_i}) = \sum_{i} \frac{d}{dt} (\vec{r}_i \times \vec{p_i}) = \frac{d}{dt} \sum_{i} (\vec{r}_i \times \vec{p_i})=0$$

对于上式中的$\sum_{i} (\vec{r}_i \times \vec{p_i})$, 我们给出一个专门的名称, 叫做**系统的角动量**:

$$L = \sum_{i} (\vec{r}_i \times \vec{p_i}) = \text{Const}$$

因此我们可以得出结论: 在一个空间各向同性的系统中, 系统的角动量是守恒的. 将上述角动量的定义代入质点系的拉格朗日函数, 可以得到:

$$L = \sum_{i=1}^N (\vec{r}_i \times m_i \vec{v}_i)$$

这就是我们在牛顿力学中所熟知的角动量的定义. 因此我们可以得出结论: 在一个空间各向同性的孤立系统中, 系统的角动量是守恒的. 这就是我们在牛顿力学中所熟知的角动量守恒定律.

然而, 由于角动量守恒中出现了径矢, 这意味着角动量的总量和系统的参考点有关. 因此我们需要选择一个合适的参考点来定义系统的角动量. 通常我们选择系统的质心作为参考点, 这样就可以得到一个与参考点无关的角动量定义:

$$L = \sum_{i=1}^N ((\vec{r}_i - \vec{R}) \times m_i \vec{v}_i)$$

参考系的质心的位置$\vec{R}$定义为:

$$\vec{R} = \frac{1}{M} \sum_{i=1}^N m_i \vec{r}_i, \quad M = \sum_{i=1}^N m_i$$

因此我们可以得出结论: 在一个空间各向同性的孤立系统中, 系统的角动量是守恒的. 这就是我们在牛顿力学中所熟知的角动量守恒定律.

## 力学相似性

实际上, 除去上述提及的三个守恒定律, 物理学中最普适的一条规律就是**力学相似性**. 力学相似性是指在满足一定条件的情况下, 不同系统之间的运动规律是相似的. 这意味着我们可以通过研究一个系统的运动规律, 来推断另一个系统的运动规律. 不同系统之间的差异可能是**尺寸**差异, 也可能是**时间尺度**差异. 下面我们将从最小作用量原理出发, 推导出力学相似性的规律.

下面给出一系列有趣的推导.

由于**拉格朗日函数**乘以任意常数不影响运动学规律, 所以我们现在必须凑出一个乘以定常的拉格朗日函数.

考虑如下的坐标变换:

$$
\vec{r}_{\alpha} \to \alpha \vec{r}_{\alpha}, \quad t \to \beta t
$$

我们记势能函数$U(\vec{r_1}, \cdots \vec{r_n})$的齐次次数为$k$, 也就是说:

$$U(\alpha \vec{r_1}, \cdots \alpha \vec{r_n}) = \alpha^k U(\vec{r_1}, \cdots \vec{r_n})$$

同理, 根据上述坐标变换, 我们可以得到动能函数$T$的变换规律:

$$\vec{v} \to \frac{\alpha}{\beta} \vec{v}, \quad T \to \alpha^2 \beta^{-2} T$$

根据前面我们讨论得到的质点系的拉格朗日函数的定义:

$$L = T - U$$

要想使得$L$在上述变化下只乘常数, 我们需要满足如下的关系:

$$\alpha^2 \beta^{-2} = \alpha^k$$

换言之, 就是要满足:

$$
\beta = \alpha^{1- \frac{k}{2}}
$$

换言之, 具有上述变换的系统在运动轨迹上是相似的, 也就是说, 如果一个系统的坐标和时间满足上述变换关系, 那么这个系统的运动轨迹将与原系统相似. 这就是力学相似性的规律.

由力学相似性的规律我们可以直接推出**开普勒第三定律**. 开普勒第三定律是指在一个中心力场中, 行星的轨道周期$T$与轨道半长轴$a$之间的关系为:

$$T^2 \propto a^3$$

我们考虑一个行星绕着一个中心天体运动的系统. 这个系统的势能函数是一个齐次函数, 其次数为$k = -1$. 因此根据前面我们推导得到的力学相似性的规律, 我们可以得到:

$$\beta = \alpha^{1 - \frac{-1}{2}} = \alpha^{\frac{3}{2}}$$

换言之, 我们可以考虑到如下的情况:

$$
\frac{t'}{t} = \left( \frac{l'}{l} \right)^{\frac{3}{2}}
$$

其中$t$和$t'$分别是原系统和变换后的系统的轨道周期, $l$和$l'$分别是原系统和变换后的系统的轨道半长轴. 因此我们可以得出结论:

$$T^2 \propto a^3$$

### 位力定理

如果力学系统在有限空间中做速度有限的运动, 势能是坐标的$k$次齐次函数, 我们可以逐步推出**位力定理**:

$$\overline{T} = \frac{k}{2} \overline{U}, \quad \overline{U} = \frac{2}{k+2} E, \quad \overline{T} = \frac{k}{k+2} E$$

我们先从**欧拉齐次函数定理**出发, 得到最初级的结论:

$$
2T = \sum_i \vec{v_i} \cdot \frac{\partial U}{\partial \vec{v_i}} = \sum_i \vec{v_i} \cdot \vec{p_i} = \sum_i \left( \frac{d}{dt} \vec{p_i} \cdot \vec{r_i} - \dot{\vec{p_i}} \cdot \vec{v_i} \right)
$$

我们考虑对时间的平均:

$$
\overline{f} = \frac{1}{\tau} \int_0^{\tau} f(t) dt= \frac{1}{\tau} \int_0^{\tau} \frac{dF(t)}{dt} \cdot dt = \frac{1}{\tau} (F(\tau) - F(0))
$$

我们对上述表达式做对时间的在无穷区间上的平均:

$$
2\overline{T} = \sum_i \vec{v_i} \cdot \frac{\partial \overline{U}}{\partial \vec{v_i}} = k \overline{U}
$$

这就是位力定理的第一个结论. 由于系统的总能量$E$是动能和势能之和, 因此我们可以得到:

$$E = \overline{T} + \overline{U} = \frac{k}{2} \overline{U} + \overline{U} = \frac{k+2}{2} \overline{U}, \quad \overline{U} = \frac{2}{k+2} E, \quad \overline{T} = E - \overline{U} = E - \frac{2}{k+2} E = \frac{k}{k+2} E$$

至此, 本章内容结束. 通过最小作用量原理, 我们推导出了能量守恒定律、动量守恒定律、角动量守恒定律以及力学相似性的规律. 这些定律和规律是物理学中最基本的定律和规律, 它们在各种物理现象中都得到了验证和应用.