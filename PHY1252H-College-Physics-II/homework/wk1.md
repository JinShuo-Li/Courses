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

### 11.7

我们只需要先算一下宽为 $dz$ 的带电圆环对圆柱轴线上任意一点的电场强度，然后再沿 $z$ 方向积分即可。根据对称性不难知道：

$$
E_z=0,\qquad E_y=0.
$$

记宽为 $dz$ 的带电圆环半径为 $R$，且

$$
dl=R\,d\phi.
$$

圆柱面上的面积元为

$$
dS=R\,d\phi\,dz,
$$

因此电荷元为

$$
dq=\sigma dS=b\cos\phi\cdot R\,d\phi\,dz.
$$

对于轴线上的场点，有

$$
r=\sqrt{R^2+z^2}.
$$

电场元满足

$$
d\vec E=k\frac{dq}{r^3}\vec r.
$$

其中电荷元到场点的位移矢量在 $x$ 方向的分量为

$$
r_x=-R\cos\phi.
$$

因此

$$
dE_x
=
k\frac{dq}{r^3}(-R\cos\phi)
=
-k\frac{bR^2\cos^2\phi}{(R^2+z^2)^{3/2}}\,dz\,d\phi.
$$

于是

$$
E_x
=
\int_{-\infty}^{+\infty}
\int_0^{2\pi}
-k\frac{bR^2\cos^2\phi}{(R^2+z^2)^{3/2}}
\,d\phi\,dz.
$$

即

$$
E_x
=
-kbR^2
\int_{-\infty}^{+\infty}
\frac{dz}{(R^2+z^2)^{3/2}}
\int_0^{2\pi}\cos^2\phi\,d\phi.
$$

其中

$$
\int_0^{2\pi}\cos^2\phi\,d\phi=\pi,
$$

且

$$
\int_{-\infty}^{+\infty}
\frac{dz}{(R^2+z^2)^{3/2}}
=
\frac{2}{R^2}.
$$

因此

$$
E_x
=
-kbR^2\cdot\frac{2}{R^2}\cdot\pi
=
-2\pi kb.
$$

### 11.9

设无限大带电平板沿 $y,z$ 方向无限延伸，厚度方向为 $x$，其范围为

$$
0\le x\le b,
$$

电荷体密度为

$$
\rho=kx.
$$

可以将整个带电平板看成由无数个厚度为 $dx$ 的无限大带电薄平面叠加而成。

对于位于 $x$ 处、厚度为 $dx$ 的薄层，其等效面电荷密度为

$$
d\sigma=\rho\,dx=kx\,dx.
$$

无限大带电平面在两侧产生的电场强度大小为

$$
dE=\frac{d\sigma}{2\varepsilon_0}
=\frac{kx}{2\varepsilon_0}dx,
$$

方向均背离该带电平面。


#### (1) 平板外两侧任一点处的电场强度

对于平板左侧，即 $x_0<0$，所有带电薄层产生的电场方向均沿 $-x$ 方向，因此

$$
E_x
=
-\int_0^b\frac{kx}{2\varepsilon_0}dx.
$$

于是

$$
E_x
=
-\frac{k}{2\varepsilon_0}\frac{b^2}{2}
=
-\frac{kb^2}{4\varepsilon_0}.
$$

故

$$
\boxed{
\vec E
=
-\frac{kb^2}{4\varepsilon_0}\vec e_x,
\qquad x_0<0
}
$$

对于平板右侧，即 $x_0>b$，所有带电薄层产生的电场方向均沿 $+x$ 方向，因此

$$
E_x
=
\int_0^b\frac{kx}{2\varepsilon_0}dx
=
\frac{kb^2}{4\varepsilon_0}.
$$

故

$$
\boxed{
\vec E
=
\frac{kb^2}{4\varepsilon_0}\vec e_x,
\qquad x_0>b
}
$$

可见平板外部的电场强度与场点到平板的距离无关。


#### (2) 平板内任一点处的电场强度

设场点位于

$$
0<x_0<b.
$$

位于场点左侧，即 $0<x<x_0$ 的薄层产生的电场沿 $+x$ 方向；位于场点右侧，即 $x_0<x<b$ 的薄层产生的电场沿 $-x$ 方向。

因此

$$
E_x
=
\int_0^{x_0}\frac{kx}{2\varepsilon_0}dx
-
\int_{x_0}^b\frac{kx}{2\varepsilon_0}dx.
$$

计算得到

$$
E_x
=
\frac{k}{2\varepsilon_0}
\left(
\frac{x_0^2}{2}
-
\frac{b^2-x_0^2}{2}
\right).
$$

所以

$$
E_x
=
\frac{k}{4\varepsilon_0}
\left(2x_0^2-b^2\right).
$$

故平板内部任一点的电场为

$$
\boxed{
\vec E
=
\frac{k}{4\varepsilon_0}
\left(2x_0^2-b^2\right)\vec e_x,
\qquad 0<x_0<b
}
$$

---

#### (3) 电场强度为零的点

令

$$
E_x=0,
$$

即

$$
2x_0^2-b^2=0.
$$

因此

$$
x_0^2=\frac{b^2}{2}.
$$

由于 $0\le x_0\le b$，故

$$
\boxed{
x_0=\frac{b}{\sqrt2}
}
$$

所以电场强度为零的点位于平板内部距离 $x=0$ 一侧

$$
\boxed{\frac{b}{\sqrt2}}
$$

处。