# 第11章作业

## 胡其图教材

### 11.22

#### (1) 球壳内、外表面上的电荷

在球壳材料内部做一个包围空腔的闭合球面作为高斯免$S$. 因为导体内部电场为零，根据高斯定理:

$$
\oint_S E \cdot dA = \frac{\sum q_{inside}}{\epsilon_0} = 0
$$

所以高斯面内包围的净电荷为零. 由于高斯面内包含点电荷和内表面感应电荷, 则:

$$
q + q_{in} = 0 \implies q_{in} = -q
$$

由电荷守恒, 球壳总电荷为 $Q$, 则球壳外表面电荷为:

$$
q_{out} = Q - q_{in} = Q + q
$$

#### (2) 球心$O$处, 球壳内表面电荷产生的电势

由电势的标量叠加原理:

$$
V_{in} = \int_{S_{in}} \frac{d q_{in}}{4 \pi \epsilon_0 a} = \frac{q_{in}}{4 \pi \epsilon_0 a} = -\frac{q}{4 \pi \epsilon_0 a}
$$

#### (3) 球心$O$处总电势

球心$O$处的总电势为内表面电荷和外表面电荷再加上点电荷产生的电势之和:

$$
V = V_{in} + V_{out} + V_{dot} = -\frac{q}{4 \pi \epsilon_0 a} + \frac{Q + q}{4 \pi \epsilon_0 b} + \frac{q}{4 \pi \epsilon_0 r} = \frac{1}{4 \pi \epsilon_0} \left( -\frac{q}{a} + \frac{Q + q}{b} + \frac{q}{r} \right)
$$

### 11.23

$$
F = Q E_{single} = \frac{1}{2} QE = \frac{QV}{2d} = \frac{\epsilon_0 S V^2}{2d^2}
$$

代入数据计算得:

$$
F = 4.425 \times 10^{-8} N
$$

### 11.24

#### (1) 水滴半径

电荷均匀分布在球形水滴表面上, 球外及表面的电场分布与电荷集中在球心处的情况等价, 由点电荷电势公式:

$$
V = \frac{q}{4 \pi \epsilon_0 R}, \quad R = \frac{q}{4 \pi \epsilon_0 V}
$$

代入计算得:

$$
R \approx 5.4 \times 10^{-4} m
$$

#### (2) 大水滴表面电势

由已知: $R' = 2^{\frac{1}{3}} R$, $q' = 2q$, 则大水滴表面电势为:

$$
V' = 2^{\frac{2}{3}} V \approx 793.7 V
$$

### 11.29

#### (1) 球心$O$处的电势为

雷同 11.22(3), 由电势的标量叠加原理:

$$
V = V_{in} + V_{out} + V_{dot} = -\frac{q}{4 \pi \epsilon_0 a} + \frac{Q + q}{4 \pi \epsilon_0 b} + \frac{q}{4 \pi \epsilon_0 r} = \frac{1}{4 \pi \epsilon_0} \left( -\frac{q}{a} + \frac{Q + q}{b} + \frac{q}{r} \right)
$$

#### (2) 金属球壳外距球心 $O$ 为 $R$ 处 $P$ 点的电场强度

由于静电屏蔽, 金属球壳内部及内表面的电荷电场被屏蔽在导体内部, 不会穿透到球壳外侧. 在球壳外 ($R > b$), 电场完全由外表面均匀分布的电荷 $Q + q$ 产生. 由于其电荷分布具有球对称性, 选取以球心 $O$ 为中心, 半径为 $R$ 的同心球面为高斯面 $S$:

根据高斯定理:

$$\oint_S \vec{E} \cdot d\vec{A} = E \cdot 4\pi R^2 = \frac{\sum q_{\text{around}}}{\varepsilon_0} = \frac{Q + q}{\varepsilon_0}$$

$$\vec{E}_P = \frac{Q + q}{4\pi\varepsilon_0 R^2} \hat{e}_r$$

### 11.31

(1) A带$q$, B不带电

$$
E = \frac{q}{2\epsilon_0 S}, \quad V_A - V_B = Ed = \frac{qd}{2\epsilon_0 S}
$$

(2) A带$q$, B带$3q$

$$
E = \frac{q}{\epsilon_0 S}, \quad V_A - V_B = -Ed = -\frac{qd}{\epsilon_0 S}
$$

(3) A带$q$, B接地

$$
E = \frac{q}{\varepsilon_0 S}, \quad V_A - V_B = E d = \frac{qd}{\varepsilon_0 S}
$$

## 系列化习题

### 12.4

#### (1) B 和 C 两板上的电荷

平行板电场强度近似为匀强电场:

$$
U_{AC} = \frac{q_1 d_{CA}}{\epsilon_0 S} \quad U_{AB} = \frac{q_2 d_{BA}}{\epsilon_0 S}
$$

$$\frac{q_1 d_{CA}}{\varepsilon_0 S} = \frac{q_2 d_{AB}}{\varepsilon_0 S} \implies q_1 d_{CA} = q_2 d_{AB}$$

$$
q_1 = 2 q_2 = 2.0 \times 10^{-7} C
$$

$$
\therefore Q_C = -q_1 = -2.0 \times 10^{-7} C, \quad Q_B = -q_2 = -1.0 \times 10^{-7} C
$$

#### (2) A板的电势

$$V_A = U_{AC} = \frac{q_1 d_{CA}}{\varepsilon_0 S}$$

代入计算得:

$$
V_A = 2.26 \times 10^3 V
$$

### 12.8

#### (1) A, C 圆柱面上的电荷

根据电荷守恒定律: $Q_1 + Q_2 = Q$

由静电感应和高斯定律:

$$
Q_A = -Q_1, \quad Q_C = -Q_2
$$

由已知: $E_1(r) = \frac{Q_1}{2 \pi \epsilon_0 L r}$

$$V_B - V_A = \int_{R}^{2R} \frac{Q_1}{2\pi\varepsilon_0 L r} dr = \frac{Q_1}{2\pi\varepsilon_0 L} \ln\left(\frac{2R}{R}\right) = \frac{Q_1 \ln 2}{2\pi\varepsilon_0 L}$$

$$V_B - V_C = \int_{2R}^{4R} \frac{Q_2}{2\pi\varepsilon_0 L r} dr = \frac{Q_2}{2\pi\varepsilon_0 L} \ln\left(\frac{4R}{2R}\right) = \frac{Q_2 \ln 2}{2\pi\varepsilon_0 L}$$

$$
\because V_B - V_A = V_B - V_C \implies Q_1 = Q_2 = \frac{Q}{2}
$$

$$
\therefore Q_A = Q_C = -\frac{Q}{2}
$$

#### (2) B 圆柱面的电势

$$V_B = \frac{Q_1 \ln 2}{2\pi\varepsilon_0 L} = \frac{\frac{Q}{2} \ln 2}{2\pi\varepsilon_0 L} = \frac{Q \ln 2}{4\pi\varepsilon_0 L}$$

#### (3) 整个导体组的电容

$$C = \frac{Q}{\frac{Q \ln 2}{4\pi\varepsilon_0 L}} = \frac{4\pi\varepsilon_0 L}{\ln 2}$$

## 补充习题

### 补充习题 1

导体球表面电荷均匀分布，面电荷密度为

$$
\sigma=\frac{Q}{4\pi R^2}
$$

导体表面的静电压力为

$$
p=\frac{\sigma^2}{2\varepsilon_0}
=\frac{Q^2}{32\pi^2\varepsilon_0R^4}
$$

取上半球，静电斥力沿对称轴方向的合力为

$$
F=\int_S p\cos\theta\,\mathrm dS
$$

由于 $\mathrm dS=2\pi R^2\sin\theta\,\mathrm d\theta$，故

$$
\begin{aligned}
F&=2\pi R^2p\int_0^{\pi/2}\sin\theta\cos\theta\,\mathrm d\theta\\
&=\pi R^2p
\end{aligned}
$$

因此，保持两半球结合所需的最小外力为

$$
F_{\min}=\frac{Q^2}{32\pi\varepsilon_0R^2}
$$

### 补充习题 2

设内、外球壳的感应电荷总量分别为 $Q_1,Q_2$。

由于两球壳均接地，外部电场为零，由高斯定理得

$$
q+Q_1+Q_2=0
$$

在内球壳表面取电势的球面平均值，由于球壳电势为零，有

$$
\frac{1}{4\pi\varepsilon_0}
\left(\frac{q}{l}+\frac{Q_1}{r}+\frac{Q_2}{R}\right)=0
$$

联立两式：

$$
\begin{cases}
Q_1+Q_2=-q\\
\displaystyle\frac{Q_1}{r}+\frac{Q_2}{R}=-\frac{q}{l}
\end{cases}
$$

解得内球壳感应电荷总量

$$
\boxed{Q_1=-\frac{qr(R-l)}{l(R-r)}}
$$

外球壳感应电荷总量

$$
Q_2=-\frac{qR(l-r)}{l(R-r)}
$$

### 补充习题 3

设内、外球壳的总电荷量分别为 $Q_A,Q_B$。由于外球壳绝缘且原来不带电，有

$$
Q_B=0
$$

利用球面电势平均值性质：球外点电荷 $q$ 在球面上的平均电势为 $\dfrac{q}{4\pi\varepsilon_0d}$。

#### (1) A 球壳的感应电荷量**

由于 A 球壳接地，电势为零，故

$$
V_A=\frac{1}{4\pi\varepsilon_0}
\left(\frac{q}{d}+\frac{Q_A}{R_A}+\frac{Q_B}{R_B}\right)=0
$$

代入 $Q_B=0$，得

$$
\boxed{Q_A=-\frac{qR_A}{d}}
$$

#### (2) 外球壳 B 的电势

对 B 球面取电势平均值：

$$
V_B=\frac{1}{4\pi\varepsilon_0}
\left(\frac{q}{d}+\frac{Q_A+Q_B}{R_B}\right)
$$

代入 $Q_A=-\dfrac{qR_A}{d}$、$Q_B=0$，得

$$
\boxed{V_B=\frac{q}{4\pi\varepsilon_0d}
\left(1-\frac{R_A}{R_B}\right)}
$$

## 附加题

设 $r$ 为圆盘上距圆心的距离，$\sigma(r)$ 为单侧表面电荷密度。

由导体表面为等势面，求解拉普拉斯方程可得

$$
\sigma(r)=\frac{C}{\sqrt{R^2-r^2}}
$$

圆盘两面均带电，由电荷守恒：

$$
Q=2\int_0^R \sigma(r)\cdot 2\pi r\,\mathrm dr
$$

代入得

$$
Q=4\pi C\int_0^R\frac{r}{\sqrt{R^2-r^2}}\,\mathrm dr
=4\pi CR
$$

因此

$$
\boxed{\sigma(r)=\frac{Q}{4\pi R\sqrt{R^2-r^2}}}
$$

圆盘两面电荷分布相同，均占总电荷的一半。

**分布特点：**

1. 圆心处电荷密度最小：

   $$
   \sigma(0)=\frac{Q}{4\pi R^2}
   $$

2. 随 $r$ 增大，电荷密度逐渐增大。

3. 当 $r\to R^-$ 时，$\sigma(r)\to\infty$，即电荷集中于圆盘边缘（理想零厚度模型）.