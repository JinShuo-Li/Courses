# 第一章 运动学

## 第一章: 质点运动学

### 矢量函数

**标量与矢量**: 标量是只有大小没有方向的物理量, 如温度、质量等；矢量则具有大小和方向, 如位移、速度等.

矢量记作 $\vec{A}$, 其分量可以表示为 $A_x$ 和 $A_y$. 矢量的大小记作 $|\vec{A}|$, 称为矢量的模.

**矢量的加法**: 两个矢量 $\vec{A}$ 和 $\vec{B}$ 的和 $\vec{C} = \vec{A} + \vec{B}$ 可以通过平行四边形法则或三角形法则来求得.

**矢量的减法**: 两个矢量 $\vec{A}$ 和 $\vec{B}$ 的差 $\vec{D} = \vec{A} - \vec{B}$ 可以通过将 $\vec{B}$ 反向后与 $\vec{A}$ 相加来求得.

**矢量的数乘**: 数量 $k$ 与矢量 $\vec{A}$ 的积 $k\vec{A}$ 是一个新的矢量, 其大小为 $|k||\vec{A}|$, 方向与 $\vec{A}$ 相同（如果 $k > 0$）或相反（如果 $k < 0$）.

**矢量的叉乘**: 两个矢量 $\vec{A}$ 和 $\vec{B}$ 的叉乘 $\vec{C} = \vec{A} \times \vec{B}$ 是一个新的矢量, 其大小为 $|\vec{A}||\vec{B}|\sin\theta$, 方向垂直于 $\vec{A}$ 和 $\vec{B}$ 所在的平面, 遵循右手定则. 用线性代数中的行列式来计算叉乘的分量:
$$\vec{C} = \begin{vmatrix}\hat{i} & \hat{j} & \hat{k} \\
A_x & A_y & A_z \\
B_x & B_y & B_z\end{vmatrix}$$

**矢量函数的微商**: 矢量函数 $\vec{r}(t)$ 的导数 $\frac{d\vec{r}}{dt}$ 表示矢量函数的变化率, 称为矢量函数的微商. 如果 $\vec{r}(t) = x(t)\hat{i} + y(t)\hat{j} + z(t)\hat{k}$, 则:

$$\frac{d\vec{r}}{dt} = \frac{dx}{dt}\hat{i} + \frac{dy}{dt}\hat{j} + \frac{dz}{dt}\hat{k}$$

考虑物理含义, 矢量函数的微分还是矢量函数, 其方向与矢量函数的变化方向相同, 大小表示矢量函数的变化率.

矢量函数微分适用以下几条运算律:

1. **线性运算律**: $\frac{d}{dt}(k\vec{A}) = k\frac{d\vec{A}}{dt}$, 其中 $k$ 是常数.

2. **加法运算律**: $\frac{d}{dt}(\vec{A} + \vec{B}) = \frac{d\vec{A}}{dt} + \frac{d\vec{B}}{dt}$.
3. **乘积运算律**: $\frac{d}{dt}(\vec{A} \cdot \vec{B}) = \frac{d\vec{A}}{dt} \cdot \vec{B} + \vec{A} \cdot \frac{d\vec{B}}{dt}$.
4. **叉乘运算律**: $\frac{d}{dt}(\vec{A} \times \vec{B}) = \frac{d\vec{A}}{dt} \times \vec{B} + \vec{A} \times \frac{d\vec{B}}{dt}$.

### 质点运动学

#### 参考系和质点

**参考系**: 参考系是观察和描述物体运动的坐标系统. 质点运动学通常在惯性参考系中进行分析. 坐标系是参考系的数学抽象. 为了具体描述质点的运动规律, 我们通常需要建立特定的坐标系. 

**质点**: 质点是一个理想化的物体, 具有质量但没有尺寸和形状. 在质点运动学中, 我们将物体视为质点来简化分析. 

描述质点运动的基本物理量包括: 
- **位矢 $\vec{r}$**: 从坐标系原点（参考点）指向质点当前位置的矢量. 
- **位移 $\Delta \vec{r}$**: 质点位置的改变, 定义为末位矢减去初位矢: $\Delta \vec{r} = \vec{r}_f - \vec{r}_i$. 
- **速度 $\vec{v}$**: 质点位置对时间的变化率, 定义为位矢的微商: $\vec{v} = \frac{d\vec{r}}{dt}$. 
- **加速度 $\vec{a}$**: 质点速度对时间的变化率, 定义为速度的微商: $\vec{a} = \frac{d\vec{v}}{dt} = \frac{d^2\vec{r}}{dt^2}$. 

---

#### 常见坐标系下的运动学描述

为了适应不同特性的运动, 物理学中常采用三种不同的坐标系来展开推导: 直角坐标系、自然坐标系与极坐标系. 我们要在这些坐标系中保持对位移、速度、加速度的统一认识. 

##### 1. 直角坐标系 (Cartesian Coordinate System)
直角坐标系是最基础的坐标系, 其核心推导优势在于**基矢量 $\hat{i}, \hat{j}, \hat{k}$ 的方向和大小全都不随时间和空间改变**. 

- **位矢与位移**:
  由于单位矢量固定不变, 位矢可以直接按分量展开: 
  $$\vec{r}(t) = x(t)\hat{i} + y(t)\hat{j} + z(t)\hat{k}$$
  位移表现为分量增量的叠加: 
  $$\Delta \vec{r} = \Delta x\hat{i} + \Delta y\hat{j} + \Delta z\hat{k}$$

- **速度**:
  因为 $\frac{d\hat{i}}{dt} = \frac{d\hat{j}}{dt} = \frac{d\hat{k}}{dt} = \textbf{0}$, 我们可以直接对标量系数求导: 
  $$\vec{v} = \frac{d\vec{r}}{dt} = \dot{x}\hat{i} + \dot{y}\hat{j} + \dot{z}\hat{k} = v_x\hat{i} + v_y\hat{j} + v_z\hat{k}$$

- **加速度**:
  同理, 对速度微商: 
  $$\vec{a} = \frac{d\vec{v}}{dt} = \ddot{x}\hat{i} + \ddot{y}\hat{j} + \ddot{z}\hat{k} = a_x\hat{i} + a_y\hat{j} + a_z\hat{k}$$
  各分量完全解耦, 运动在各正交方向上独立. 这种线性叠加是直角坐标系独有的性质. 


##### 2. 自然坐标系 (Intrinsic / Natural Coordinate System)
**自然坐标系**是直接以质点运动的**实际轨迹**为基础建立的局部参考系. 

在任意时刻, 我们在质点所在位置建立两个局部单位矢量: 
- 切向单位矢量 $\hat{\tau}$: 沿轨迹切线方向, 指向质点前进方向. 
- 法向单位矢量 $\hat{n}$: 垂直于 $\hat{\tau}$, 指向轨迹所在的局部曲率中心. 

自然系下通常使用路程（弧长） $s$ 来代替位移. 注意, $\hat{\tau}$ 和 $\hat{n}$ 是随质点运动而**不断改变方向**的. 

- **速度**:
  沿轨迹切线方向, 自然系下速度具有极其简洁的形式: 
  $$\vec{v} = v\hat{\tau}$$
  速度大小 $v = \frac{ds}{dt}$ 即为速率. 

- **加速度**:
  对上式应用乘积法则求微商: 
  $$\vec{a} = \frac{d\vec{v}}{dt} = \frac{dv}{dt}\hat{\tau} + v\frac{d\hat{\tau}}{dt}$$
  由于 $\hat{\tau}$ 是单位向量, 质点在 $dt$ 内移动微小弧长 $ds$ 时, $\hat{\tau}$ 转过微小角度 $d\theta$, 它的增量 $d\hat{\tau}$ 垂直于 $\hat{\tau}$ (即沿着 $\hat{n}$ 方向). 大小上 $|d\hat{\tau}| = |\hat{\tau}|d\theta = d\theta$. 所以:
  $$d\hat{\tau} = d\theta \hat{n} \implies \frac{d\hat{\tau}}{ds} = \frac{d\theta}{ds} \hat{n} = \frac{1}{\rho}\hat{n}$$
  其中 $\rho$ 是曲率半径. 再根据链式法则: 
  $$\frac{d\hat{\tau}}{dt} = \frac{d\hat{\tau}}{ds} \frac{ds}{dt} = \frac{1}{\rho}\hat{n} \cdot v = \frac{v}{\rho}\hat{n}$$
  代入加速度公式: 
  $$\vec{a} = \frac{dv}{dt}\hat{\tau} + \frac{v^2}{\rho}\hat{n} = a_\tau \hat{\tau} + a_n \hat{n}$$
  - **切向加速度 $a_\tau = \frac{dv}{dt}$**: 反映速度**大小**改变快慢. 
  - **法向加速度 $a_n = \frac{v^2}{\rho}$**: 反映速度**方向**改变快慢. 


##### 3. 极坐标系 (Polar Coordinate System)
涉及复杂有心力（如引力引起的旋转）, 我们引入**极坐标系**. 质点位置由极距 $r$ 和极角 $\theta$ 给出. 

极坐标基矢量 $\hat{e}_r$ 和 $\hat{e}_\theta$ 与直角坐标系的联系: 
$$
\begin{cases}
\hat{e}_r = \cos\theta \hat{i} + \sin\theta \hat{j} \\
\hat{e}_\theta = -\sin\theta \hat{i} + \cos\theta \hat{j}
\end{cases}
$$
由于它也是随动坐标系, 对时间 $t$ 求导得单位矢量的变化率（$\omega = \dot{\theta}$ 为角速度）: 
$$
\begin{cases}
\frac{d\hat{e}_r}{dt} = (-\sin\theta \dot{\theta})\hat{i} + (\cos\theta \dot{\theta})\hat{j} = \dot{\theta} \hat{e}_\theta = \omega \hat{e}_\theta \\
\frac{d\hat{e}_\theta}{dt} = (-\cos\theta \dot{\theta})\hat{i} - (\sin\theta \dot{\theta})\hat{j} = -\dot{\theta} \hat{e}_r = -\omega \hat{e}_r
\end{cases}
$$

- **位矢与微小位移**:
  位矢非常简洁: 
  $$\vec{r} = r\hat{e}_r$$
  微小位移 $d\vec{r}$ 包括沿径向伸长的 $dr \hat{e}_r$ 和横向扫过的弧长 $r d\theta \hat{e}_\theta$. 

- **速度**:
  对方位矢求微商, 运用乘积法则: 
  $$\vec{v} = \frac{d\vec{r}}{dt} = \frac{dr}{dt}\hat{e}_r + r\frac{d\hat{e}_r}{dt}$$
  代入 $\frac{d\hat{e}_r}{dt} = \dot{\theta}\hat{e}_\theta$ 即得极坐标速度: 
  $$\vec{v} = \dot{r}\hat{e}_r + r\dot{\theta}\hat{e}_\theta = v_r \hat{e}_r + v_\theta \hat{e}_\theta$$
  其中, 径向速度 $v_r = \dot{r}$, 横向速度 $v_\theta = r\dot{\theta} = r\omega$. 

- **加速度**:
  继续对速度式求微商: 
  $$\vec{a} = \frac{d\vec{v}}{dt} = \frac{d}{dt}(\dot{r}\hat{e}_r) + \frac{d}{dt}(r\dot{\theta}\hat{e}_\theta)$$
  展开得到: 
  $$\vec{a} = (\ddot{r}\hat{e}_r + \dot{r}\frac{d\hat{e}_r}{dt}) + (\dot{r}\dot{\theta}\hat{e}_\theta + r\ddot{\theta}\hat{e}_\theta + r\dot{\theta}\frac{d\hat{e}_\theta}{dt})$$
  代入 $\frac{d\hat{e}_r}{dt} = \dot{\theta}\hat{e}_\theta$ 和 $\frac{d\hat{e}_\theta}{dt} = -\dot{\theta}\hat{e}_r$, 合并同类基向量, 得出: 
  $$\vec{a} = (\ddot{r} - r\dot{\theta}^2)\hat{e}_r + (r\ddot{\theta} + 2\dot{r}\dot{\theta})\hat{e}_\theta = a_r \hat{e}_r + a_\theta \hat{e}_\theta$$
  各个分量的物理意义极强: 
  - **纯径向加速度 $\ddot{r}$**: 由径向距离变化的快慢引起. 
  - **向心加速度 $-r\dot{\theta}^2$**: 由于速度横向分量方向改变而产生, 始终指向极点. 
  - **横向切向加速度 $r\ddot{\theta}$**: 由于角速度大小的改变而引起. 
  - **科里奥利加速度 (Coriolis) $2\dot{r}\dot{\theta}$**: 动学耦合项. 一方面因为质点径向运动导致到达不同横向速度区域所需线速度增量（$\dot{r}\dot{\theta}$）, 另一方面因横向速度导致原有径向单位矢量发生旋转所产生的补充（$\dot{r}\dot{\theta}$）. 

## 补充知识 (单位和量纲)

在力学体系中, 所有物理量都可以分成两类: 基本量和导出量. 基本量是无法通过其他物理量定义的, 如长度、时间、质量等. 导出量则是通过基本量定义的, 如速度、加速度、力等.

基本量的单位称为基本单位. 在国际单位制SI中, 基本单位包括:

| 物理量 | 单位名称 | 符号 |
| --- | --- | --- |
| 长度 | 米 | m |
| 质量 | 千克 | kg |
| 时间 | 秒 | s |
| 电流 | 安培 | A |
| 温度 | 开尔文 | K |
| 物质的量 | 摩尔 | mol |
| 发光强度 | 坎德拉 | cd |

其中前三个量 (长度、质量、时间) 是力学中最常用的基本量. 导出量的单位可以通过基本单位组合得到, 如速度的单位是米每秒 (m/s), 加速度的单位是米每二次方秒 (m/s²), 力的单位是牛顿 (N), 其中1牛顿等于1千克·米每二次方秒 (kg·m/s²).

我们用如下方式表示量纲:

$$[Q] = L^{\alpha} M^{\beta} T^{\gamma}$$

**物理方程的量纲必须平衡**: 根据这点可以进行定性/半定量的分析.

