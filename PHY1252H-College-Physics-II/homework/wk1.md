# 第11章作业

## 胡其图教材

### 11.2

(1) 细棒中垂线上距离为$L$处的电场强度

直接使用库仑定律计算:

由已知: $d\vec{E} = k \frac{dq}{r^3} \vec{r}$

且: $r = \sqrt{(x-\frac{L}{2})^2 + L^2}$

我们分别求$x, y$分量:

$$
\begin{aligned}
E_x &= k \lambda_0 \int_0^L \frac{x(\frac{L}{2} - x)}{\left[ (x-\frac{L}{2})^2 + L^2 \right]^{3/2}} dx \\
&= -k \lambda_0 \int_{-L/2}^{L/2} \frac{x^2}{(x^2 + L^2)^{3/2}} dx \\
&= -2k \lambda_0 \left( \ln \frac{1+\sqrt{5}}{2} - \frac{\sqrt{5}}{5} \right)
\end{aligned}
$$

同理不难求得$E_y$:

$$
E_y = k \lambda_0 L \int_0^L \frac{x dx}{\left[ (x-\frac{L}{2})^2 + L^2 \right]^{3/2}} = \frac{k \lambda_0}{\sqrt{5}}
$$

因我们得到:

$$
\vec{E} = k \lambda_0 \left[ -2 \left( \ln \frac{1+\sqrt{5}}{2} - \frac{\sqrt{5}}{5} \right) \hat{i} + \frac{1}{\sqrt{5}} \hat{j} \right]
$$

(2) 细棒延长线上$2L$处的电场强度

由对称性, $E_y = 0$.

我们只需要利用积分计算$E_x$:

$$
d\vec{E} = k \frac{dq}{r^3} \vec{r}, \quad r = 2L + x
$$

$$
E_x = - k \lambda_0 \int_0^L \frac{x}{(x+2L)^2} dx = -k \lambda_0 \left( \ln \frac{3}{2} - \frac{1}{3} \right)
$$

$$
\therefore \vec{E} = -k \lambda_0 \left( \ln \frac{3}{2} - \frac{1}{3} \right) \hat{i}
$$

### 11.3

由对称性: $E_x = 0$, 我们只需要求出来$E_y$:

$$
d \vec{E} = - k b \sin \phi R \frac{\vec{r}}{r^3} \cdot d \phi
$$

$$
d \vec{E_y} = - k b \sin \phi R \frac{1}{R^2} \sin \phi \cdot d \phi
$$

$$
\begin{aligned}
    E_y &= - \frac{kb}{R} \int_0^{\pi} \sin^2 \phi d \phi \\
    &= - \frac{kb}{R} \left[ \frac{\phi}{2} - \frac{\sin 2\phi}{4} \right]_0^{\pi} \\
    &= - \frac{kb \pi}{2R}
\end{aligned}
$$

$$
\therefore \vec{E} = - \frac{kb \pi}{2R} \hat{j}
$$

### 11.4

我们先在圆环所在平面构造平面直角坐标系, 然后在空间中构造右手的直角坐标系, $xOy$平面在圆环所在平面, $z$轴垂直于圆环所在平面, 并且过圆环的圆心. $x$轴指向$\phi = 0$的方向, $y$轴指向$\phi = \pi/2$的方向.

(1) 圆环轴线上任意一点处的电场强度

由对称性, $E_y = 0$, $E_x = 0$, 我们需要求解$E_z$.

$$
d \vec{E} = k \frac{dq}{r^3} \vec{r}, \quad r = \sqrt{R^2 + z^2}
$$

$$
d q = \lambda (\phi) R d \phi = b \cos \phi R d \phi
$$

我们下面求解$E_x$:

$$
E_x = - \int_0^{2\pi} k \frac{b \cos \phi R d \phi}{R^2 + z^2} \cdot \frac{R \cos \phi}{\sqrt{R^2 + z^2}} = - \frac{k b R^2}{(R^2 + z^2)^{3/2}} \int_0^{2\pi} \cos^2 \phi d \phi = - \frac{k b R^2}{(R^2 + z^2)^{3/2}} \cdot \pi
$$

$$
\vec{E} = - \frac{k b \pi R^2}{(R^2 + z^2)^{3/2}} \hat{i}
$$

(2) 证明远处是电偶极子场, 并求偶极矩

当$z \gg R$, 我们有:

$$
\vec{E} \approx - \frac{k b \pi R^2}{z^3} \hat{i}
$$

和偶极子的电场公式对比, 我们可以得到该偶极子的偶极矩为:

$$
\vec{p} = b \pi R^2 \hat{i}
$$

### 11.6

由已知:

$$
\rho (r) = \rho_0 \left( 1 - \frac{r}{R} \right)
$$

计算空间中任意一点的电场强度: 我们需要分类讨论, 对于$r < R$的情况, 根据高斯定理, 我们有:

$$
\oint \vec{E} \cdot d \vec{A} = \frac{Q_{in}}{\epsilon_0}
$$

$$
Q_{\text{in}} = 4 \pi \rho_0 \int_0^r \left( 1 - \frac{r'}{R} \right) r'^2 dr' = 4 \pi \rho_0 \left( \frac{r^3}{3} - \frac{r^4}{4R} \right)
$$

$$
E(r) = \frac{\rho_0}{\epsilon_0} \left( \frac{r}{3} - \frac{r^2}{4R} \right)
$$

对于$r > R$的情况, 我们先计算总电荷

$$
Q = 4 \pi \rho_0 \int_0^R \left( 1 - \frac{r'}{R} \right) r'^2 dr' = 4 \pi \rho_0 \left( \frac{R^3}{3} - \frac{R^3}{4} \right) = \frac{\pi R^3}{3} \rho_0
$$

$$
E(r) = \frac{Q}{4 \pi \epsilon_0 r^2} = \frac{\pi R^3 \rho_0}{12 \pi \epsilon_0 r^2} = \frac{R^3 \rho_0}{12 \epsilon_0 r^2}
$$

所以在整个空间内, 电场为:

$$
\vec{E}(R) = \begin{cases}
\frac{\rho_0}{\epsilon_0} \left( \frac{r}{3} - \frac{r^2}{4R} \right) \hat{r}, & r < R \\
\frac{R^3 \rho_0}{12 \epsilon_0 r^2} \hat{r}, & r \geq R
\end{cases}
$$

