# 第11章作业

## 胡其图教材

### 11.2

#### (1) 细棒中垂线上距离为 \(L\) 处的电场强度

直接使用库仑定律计算：

\[
d\vec E=k\frac{dq}{r^3}\vec r
\]

且

\[
r=\sqrt{\left(x-\frac L2\right)^2+L^2}.
\]

分别求 \(x,y\) 分量：

\[
\begin{aligned}
E_x
&=
k\lambda_0
\int_0^L
\frac{x\left(\frac L2-x\right)}
{\left[\left(x-\frac L2\right)^2+L^2\right]^{3/2}}dx\\
&=
-k\lambda_0
\int_{-L/2}^{L/2}
\frac{x^2}{(x^2+L^2)^{3/2}}dx\\
&=
-2k\lambda_0
\left(
\ln\frac{1+\sqrt5}{2}
-\frac{\sqrt5}{5}
\right).
\end{aligned}
\]

同理，

\[
E_y
=
k\lambda_0L
\int_0^L
\frac{x\,dx}
{\left[\left(x-\frac L2\right)^2+L^2\right]^{3/2}}
=
\frac{k\lambda_0}{\sqrt5}.
\]

因此

\[
\boxed{
\vec E=
k\lambda_0
\left[
-2\left(
\ln\frac{1+\sqrt5}{2}
-\frac{\sqrt5}{5}
\right)\hat i
+
\frac1{\sqrt5}\hat j
\right]
}
\]

#### (2) 细棒延长线上 \(2L\) 处的电场强度

由对称性，

\[
E_y=0.
\]

且

\[
d\vec E=k\frac{dq}{r^3}\vec r,
\qquad r=2L+x.
\]

所以

\[
E_x
=
-k\lambda_0
\int_0^L
\frac{x}{(x+2L)^2}dx
=
-k\lambda_0
\left(
\ln\frac32-\frac13
\right).
\]

因此

\[
\boxed{
\vec E
=
-k\lambda_0
\left(
\ln\frac32-\frac13
\right)\hat i
}
\]

---

### 11.3

由对称性：

\[
E_x=0.
\]

只需求 \(E_y\)。

\[
d\vec E
=
-kb\sin\phi R
\frac{\vec r}{r^3}d\phi.
\]

因此

\[
dE_y
=
-\frac{kb}{R}\sin^2\phi\,d\phi.
\]

于是

\[
\begin{aligned}
E_y
&=
-\frac{kb}{R}
\int_0^\pi\sin^2\phi\,d\phi\\
&=
-\frac{kb}{R}
\left[
\frac\phi2-\frac{\sin2\phi}{4}
\right]_0^\pi\\
&=
-\frac{kb\pi}{2R}.
\end{aligned}
\]

所以

\[
\boxed{
\vec E
=
-\frac{kb\pi}{2R}\hat j
}
\]

---

### 11.4

建立直角坐标系，圆环位于 \(xOy\) 平面，\(z\) 轴通过圆心并垂直于圆环平面。

电荷线密度为

\[
\lambda(\phi)=b\cos\phi.
\]

#### (1) 圆环轴线上任意一点处的电场强度

由对称性，

\[
E_y=0,\qquad E_z=0.
\]

有

\[
dq=b\cos\phi R\,d\phi,
\qquad
r=\sqrt{R^2+z^2}.
\]

于是

\[
\begin{aligned}
E_x
&=
-\int_0^{2\pi}
k\frac{bR\cos\phi\,d\phi}{(R^2+z^2)^{3/2}}
R\cos\phi\\
&=
-\frac{kbR^2}{(R^2+z^2)^{3/2}}
\int_0^{2\pi}\cos^2\phi\,d\phi\\
&=
-\frac{kb\pi R^2}{(R^2+z^2)^{3/2}}.
\end{aligned}
\]

因此

\[
\boxed{
\vec E
=
-\frac{kb\pi R^2}{(R^2+z^2)^{3/2}}\hat i
}
\]

#### (2) 证明远处为电偶极子场，并求偶极矩

当

\[
z\gg R
\]

时，

\[
\vec E
\approx
-\frac{kb\pi R^2}{z^3}\hat i.
\]

和电偶极子在垂直于偶极矩方向上的电场比较：

\[
\vec E=-k\frac{\vec p}{z^3},
\]

可得

\[
\boxed{
\vec p=b\pi R^2\hat i
}
\]

---

### 11.6

已知

\[
\rho(r)=\rho_0\left(1-\frac rR\right).
\]

对于 \(r<R\)，根据高斯定理，

\[
\oint\vec E\cdot d\vec A
=
\frac{Q_{\text{in}}}{\varepsilon_0}.
\]

包围的电荷为

\[
\begin{aligned}
Q_{\text{in}}
&=
4\pi\rho_0
\int_0^r
\left(1-\frac{r'}R\right)r'^2dr'\\
&=
4\pi\rho_0
\left(
\frac{r^3}{3}-\frac{r^4}{4R}
\right).
\end{aligned}
\]

因此

\[
E(r)
=
\frac{\rho_0}{\varepsilon_0}
\left(
\frac r3-\frac{r^2}{4R}
\right).
\]

对于 \(r>R\)，先计算总电荷：

\[
Q
=
4\pi\rho_0
\int_0^R
\left(1-\frac{r'}R\right)r'^2dr'
=
\frac{\pi R^3\rho_0}{3}.
\]

所以

\[
E(r)
=
\frac{Q}{4\pi\varepsilon_0r^2}
=
\frac{R^3\rho_0}{12\varepsilon_0r^2}.
\]

故整个空间中的电场为

\[
\boxed{
\vec E(r)=
\begin{cases}
\dfrac{\rho_0}{\varepsilon_0}
\left(
\dfrac r3-\dfrac{r^2}{4R}
\right)\hat r,
& r<R,\\[8pt]
\dfrac{R^3\rho_0}{12\varepsilon_0r^2}\hat r,
& r\ge R.
\end{cases}
}
\]

---

### 11.7

将无限长圆柱面分解为宽度为 \(dz\) 的带电圆环。

圆柱面上的面积元为

\[
dS=R\,d\phi\,dz.
\]

因此

\[
dq
=
\sigma dS
=
b\cos\phi\,R\,d\phi\,dz.
\]

对于轴线上的场点，

\[
r=\sqrt{R^2+z^2}.
\]

电荷元到场点的位移矢量在 \(x\) 方向的分量为

\[
r_x=-R\cos\phi.
\]

因此

\[
dE_x
=
-k
\frac{bR^2\cos^2\phi}
{(R^2+z^2)^{3/2}}
\,dz\,d\phi.
\]

于是

\[
E_x
=
-kbR^2
\int_{-\infty}^{+\infty}
\frac{dz}{(R^2+z^2)^{3/2}}
\int_0^{2\pi}\cos^2\phi\,d\phi.
\]

其中

\[
\int_0^{2\pi}\cos^2\phi\,d\phi=\pi,
\]

且

\[
\int_{-\infty}^{+\infty}
\frac{dz}{(R^2+z^2)^{3/2}}
=
\frac2{R^2}.
\]

所以

\[
E_x=-2\pi kb.
\]

因此

\[
\boxed{
\vec E=-2\pi kb\,\hat i
}
\]

---

### 11.9

设无限大带电平板沿 \(y,z\) 方向无限延伸，其范围为

\[
0\le x\le b,
\]

电荷体密度为

\[
\rho=kx.
\]

将整个带电平板看作由无数个厚度为 \(dx\) 的无限大带电薄平面叠加而成。

对于位于 \(x\) 处、厚度为 \(dx\) 的薄层，

\[
d\sigma=\rho\,dx=kx\,dx.
\]

无限大带电平面在两侧产生的电场强度大小为

\[
dE=\frac{d\sigma}{2\varepsilon_0}
=
\frac{kx}{2\varepsilon_0}dx.
\]

#### (1) 平板外两侧任一点处的电场强度

对于 \(x_0<0\)，

\[
E_x
=
-\int_0^b
\frac{kx}{2\varepsilon_0}dx
=
-\frac{kb^2}{4\varepsilon_0}.
\]

故

\[
\boxed{
\vec E
=
-\frac{kb^2}{4\varepsilon_0}\hat i,
\qquad x_0<0
}
\]

对于 \(x_0>b\)，

\[
E_x
=
\int_0^b
\frac{kx}{2\varepsilon_0}dx
=
\frac{kb^2}{4\varepsilon_0}.
\]

故

\[
\boxed{
\vec E
=
\frac{kb^2}{4\varepsilon_0}\hat i,
\qquad x_0>b
}
\]

#### (2) 平板内任一点处的电场强度

设

\[
0<x_0<b.
\]

位于场点左侧的薄层产生的电场沿 \(+x\) 方向，位于场点右侧的薄层产生的电场沿 \(-x\) 方向，因此

\[
E_x
=
\int_0^{x_0}
\frac{kx}{2\varepsilon_0}dx
-
\int_{x_0}^{b}
\frac{kx}{2\varepsilon_0}dx.
\]

所以

\[
E_x
=
\frac{k}{4\varepsilon_0}
\left(2x_0^2-b^2\right).
\]

故

\[
\boxed{
\vec E
=
\frac{k}{4\varepsilon_0}
\left(2x_0^2-b^2\right)\hat i,
\qquad 0<x_0<b
}
\]

#### (3) 电场强度为零的点

令

\[
2x_0^2-b^2=0,
\]

得

\[
\boxed{
x_0=\frac b{\sqrt2}
}
\]

---

### 11.12

点电荷通过圆平面的电通量可直接利用立体角计算：

\[
\Phi
=
\frac{q}{4\pi\varepsilon_0}\Omega.
\]

圆面在点电荷处所张的立体角为

\[
\Omega
=
2\pi(1-\cos\theta).
\]

由几何关系，

\[
\cos\theta
=
\frac{x}{\sqrt{x^2+R^2}}.
\]

因此

\[
\Omega
=
2\pi
\left(
1-\frac{x}{\sqrt{x^2+R^2}}
\right).
\]

故通过圆平面的电通量大小为

\[
\boxed{
\Phi
=
\frac{q}{2\varepsilon_0}
\left(
1-\frac{x}{\sqrt{x^2+R^2}}
\right)
}
\]

若所取面法向与电场穿过圆面的方向相反，则通量取负号。

---

### 11.13

将圆锥侧面与底面组成闭合曲面。

点电荷位于圆锥内部，由高斯定理，

\[
\Phi_{\text{侧}}+\Phi_{\text{底}}
=
\frac q{\varepsilon_0}.
\]

点电荷到底面圆心的距离为

\[
\frac h2.
\]

底面圆在点电荷处张的立体角为

\[
\Omega
=
2\pi
\left(
1-
\frac{h/2}{\sqrt{R^2+h^2/4}}
\right)
=
2\pi
\left(
1-\frac{h}{\sqrt{h^2+4R^2}}
\right).
\]

所以

\[
\Phi_{\text{底}}
=
\frac{q}{2\varepsilon_0}
\left(
1-\frac{h}{\sqrt{h^2+4R^2}}
\right).
\]

因此

\[
\boxed{
\Phi_{\text{侧}}
=
\frac{q}{2\varepsilon_0}
\left(
1+\frac{h}{\sqrt{h^2+4R^2}}
\right)
}
\]

---

### 11.15

立方体边长为

\[
a=100\,\mathrm m.
\]

由于电场竖直向下，只有上下两个水平面有电通量。

上表面的外法向向上，因此

\[
\Phi_{\text{上}}
=
-60\times100^2.
\]

下表面的外法向向下，因此

\[
\Phi_{\text{下}}
=
100\times100^2.
\]

所以总电通量为

\[
\Phi
=
(100-60)\times100^2
=
4.0\times10^5
\ \mathrm{N\,m^2/C}.
\]

由高斯定理，

\[
Q=\varepsilon_0\Phi.
\]

所以

\[
Q
=
8.85\times10^{-12}
\times4.0\times10^5.
\]

故

\[
\boxed{
Q\approx3.54\times10^{-6}\ \mathrm C
}
\]

---

### 11.16

已知

\[
\rho(r)=\rho_0\frac rR.
\]

总电荷为

\[
\begin{aligned}
Q
&=
4\pi
\int_0^R
\rho_0\frac rRr^2dr\\
&=
\frac{4\pi\rho_0}{R}
\int_0^Rr^3dr\\
&=
\pi\rho_0R^3.
\end{aligned}
\]

因此

\[
\boxed{
Q=\pi\rho_0R^3
}
\]

对于 \(r<R\)，

\[
Q_{\text{in}}
=
\frac{4\pi\rho_0}{R}
\int_0^r r'^3dr'
=
\frac{\pi\rho_0r^4}{R}.
\]

由高斯定理，

\[
E\cdot4\pi r^2
=
\frac{Q_{\text{in}}}{\varepsilon_0}.
\]

所以

\[
\boxed{
\vec E
=
\frac{\rho_0r^2}{4\varepsilon_0R}\hat r,
\qquad r<R
}
\]

对于 \(r\ge R\)，

\[
E
=
\frac{Q}{4\pi\varepsilon_0r^2},
\]

所以

\[
\boxed{
\vec E
=
\frac{\rho_0R^3}{4\varepsilon_0r^2}\hat r,
\qquad r\ge R
}
\]

综上，

\[
\boxed{
\vec E(r)=
\begin{cases}
\dfrac{\rho_0r^2}{4\varepsilon_0R}\hat r,
& r<R,\\[8pt]
\dfrac{\rho_0R^3}{4\varepsilon_0r^2}\hat r,
& r\ge R.
\end{cases}
}
\]

---

### 11.17

设无限大带电平面位于

\[
z=0.
\]

其两侧电场为

\[
\vec E
=
\begin{cases}
\dfrac{\sigma}{2\varepsilon_0}\hat z,
&z>0,\\[6pt]
-\dfrac{\sigma}{2\varepsilon_0}\hat z,
&z<0.
\end{cases}
\]

选带电平面为电势零点，

\[
V(0)=0.
\]

对于 \(z>0\)，

\[
V(z)
=
-\int_0^z
\frac{\sigma}{2\varepsilon_0}dz'
=
-\frac{\sigma z}{2\varepsilon_0}.
\]

对于 \(z<0\)，

\[
V(z)
=
\frac{\sigma z}{2\varepsilon_0}.
\]

因此统一写为

\[
\boxed{
V(z)
=
-\frac{\sigma}{2\varepsilon_0}|z|
}
\]

---

### 11.20

将有圆孔的无限大带电平面看成

\[
\text{完整无限大平面}
-
\text{半径为 }R\text{ 的均匀带电圆盘}.
\]

设轴线上场点到平面的距离为 \(z\)。

无限大平面的电场为

\[
E_{\text{平面}}
=
\frac{\sigma}{2\varepsilon_0}.
\]

均匀带电圆盘轴线上的电场为

\[
E_{\text{圆盘}}
=
\frac{\sigma}{2\varepsilon_0}
\left(
1-\frac{|z|}{\sqrt{z^2+R^2}}
\right).
\]

两者相减得

\[
\boxed{
\vec E(z)
=
\frac{\sigma}{2\varepsilon_0}
\frac{z}{\sqrt{z^2+R^2}}
\hat z
}
\]

又因为

\[
V(z)-V(0)
=
-\int_0^zE(z')dz',
\qquad
V(0)=0,
\]

所以

\[
V(z)
=
-\frac{\sigma}{2\varepsilon_0}
\int_0^z
\frac{z'}{\sqrt{z'^2+R^2}}dz'.
\]

得到

\[
\boxed{
V(z)
=
-\frac{\sigma}{2\varepsilon_0}
\left(
\sqrt{z^2+R^2}-R
\right)
}
\]

---

### 11.21

电荷体密度为

\[
\rho=Ar,
\qquad r\le R.
\]

#### (1) 圆柱体内、外的电场强度

对于 \(r<R\)，取半径为 \(r\)、长度为 \(L\) 的高斯柱面。

包围的电荷为

\[
\begin{aligned}
Q_{\text{in}}
&=
\int_0^r Ar'\cdot2\pi r'L\,dr'\\
&=
\frac{2\pi ALr^3}{3}.
\end{aligned}
\]

由高斯定理，

\[
E\cdot2\pi rL
=
\frac{Q_{\text{in}}}{\varepsilon_0}.
\]

所以

\[
\boxed{
\vec E
=
\frac{Ar^2}{3\varepsilon_0}\hat r,
\qquad r<R
}
\]

对于 \(r\ge R\)，单位长度内总电荷为

\[
\lambda
=
\frac{2\pi AR^3}{3}.
\]

因此

\[
\boxed{
\vec E
=
\frac{AR^3}{3\varepsilon_0r}\hat r,
\qquad r\ge R
}
\]

#### (2) 圆柱体内、外的电势

选

\[
V(l)=0,
\qquad l>R.
\]

对于 \(R\le r\le l\)，

\[
V(r)
=
-\int_l^r
\frac{AR^3}{3\varepsilon_0r'}dr',
\]

因此

\[
\boxed{
V(r)
=
\frac{AR^3}{3\varepsilon_0}
\ln\frac lr,
\qquad r\ge R
}
\]

在 \(r=R\) 处，

\[
V(R)
=
\frac{AR^3}{3\varepsilon_0}
\ln\frac lR.
\]

对于 \(r<R\)，

\[
V(r)
=
V(R)
-
\int_R^r
\frac{Ar'^2}{3\varepsilon_0}dr'.
\]

所以

\[
\boxed{
V(r)
=
\frac{AR^3}{3\varepsilon_0}
\ln\frac lR
+
\frac{A}{9\varepsilon_0}
\left(R^3-r^3\right),
\qquad r<R
}
\]

---

### 11.25

给定电势

\[
V(r)
=
\frac Ar e^{-\mu r}.
\]

由泊松方程，

\[
\nabla^2V
=
-\frac{\rho}{\varepsilon_0}.
\]

对于 \(r>0\)，由于球对称，

\[
\nabla^2V
=
\frac1{r^2}
\frac d{dr}
\left(
r^2\frac{dV}{dr}
\right).
\]

有

\[
\frac{dV}{dr}
=
-Ae^{-\mu r}
\left(
\frac{\mu}{r}
+
\frac1{r^2}
\right),
\]

因此

\[
\nabla^2V
=
A\mu^2\frac{e^{-\mu r}}r.
\]

所以在 \(r>0\) 处，

\[
\boxed{
\rho(r)
=
-\varepsilon_0A\mu^2
\frac{e^{-\mu r}}r
}
\]

另一方面，由于

\[
V(r)\underset{r\to0}{\sim}\frac Ar,
\]

原点处还存在一个点电荷。由

\[
\frac{q_0}{4\pi\varepsilon_0r}
=
\frac Ar
\]

得

\[
q_0=4\pi\varepsilon_0A.
\]

因此完整电荷分布为

\[
\boxed{
\rho(\vec r)
=
4\pi\varepsilon_0A\,
\delta^{(3)}(\vec r)
-
\varepsilon_0A\mu^2
\frac{e^{-\mu r}}r
}
\]

---

## 系列化习题

### 11.4

真空中有两个正交的无限大均匀带电平面，面电荷密度分别为 \(+\sigma\) 与 \(-\sigma\)。

单个无限大带电平面两侧产生的电场大小均为

\[
E_0=\frac{\sigma}{2\varepsilon_0}.
\]

设 \(\hat n_+\) 与 \(\hat n_-\) 分别为两个平面的单位法向量，两者互相垂直；\(u,v\) 分别为场点到两个平面的有向距离。

则两个平面的电场叠加为

\[
\boxed{
\vec E
=
\frac{\sigma}{2\varepsilon_0}
\left[
\operatorname{sgn}(u)\hat n_+
-
\operatorname{sgn}(v)\hat n_-
\right]
}
\]

因为

\[
\hat n_+\perp\hat n_-,
\]

所以四个区域内电场强度的大小均为

\[
\boxed{
E
=
\sqrt{E_0^2+E_0^2}
=
\frac{\sigma}{\sqrt2\,\varepsilon_0}
}
\]

方向均沿两个平面的角平分线，由 \(+\sigma\) 平面指向 \(-\sigma\) 平面。

因此电场线在各区域内均为相互平行的直线，方向沿相应角平分线；电场线从 \(+\sigma\) 平面出发，终止于 \(-\sigma\) 平面。

---

### 11.8

已知立方体边长为 \(a\)，电场为

\[
\vec E=bx\,\hat i.
\]

#### (1) 通过 \(S_1,S_2\) 面的电通量

右侧 \(S_1\) 面位于

\[
x=2a,
\]

其外法向沿 \(+x\) 方向，所以

\[
\Phi_1
=
E(2a)a^2
=
2ba\cdot a^2.
\]

因此

\[
\boxed{
\Phi_1=2ba^3
}
\]

上方 \(S_2\) 面的法向沿 \(y\) 方向，与电场垂直，因此

\[
\boxed{
\Phi_2=0
}
\]

#### (2) 立方体内的电荷量

左侧面位于 \(x=a\)，其外法向沿 \(-x\) 方向，因此

\[
\Phi_{\text{左}}
=
-ba^3.
\]

其他四个与 \(x\) 方向平行的面通量均为零。

故总电通量为

\[
\Phi
=
2ba^3-ba^3
=
ba^3.
\]

由高斯定理，

\[
Q=\varepsilon_0\Phi.
\]

所以

\[
\boxed{
Q=\varepsilon_0ba^3
}
\]

---

### 11.11

设无限长均匀带电圆柱体半径为 \(R\)，体电荷密度为 \(\rho\)。

#### (1) 圆柱体内任一点处的电场强度

取半径为 \(r<R\)、长度为 \(L\) 的同轴高斯柱面。

包围的电荷为

\[
Q_{\text{in}}
=
\rho\pi r^2L.
\]

由高斯定理，

\[
E\cdot2\pi rL
=
\frac{\rho\pi r^2L}{\varepsilon_0}.
\]

因此

\[
\boxed{
\vec E
=
\frac{\rho r}{2\varepsilon_0}\hat r
}
\]

#### (2) 偏心圆柱形空腔内的电场强度

设原圆柱轴线到空腔轴线的位移矢量为

\[
\vec d.
\]

利用叠加原理，将空腔看成：

\[
\text{密度为 }\rho\text{ 的完整圆柱}
+
\text{密度为 }-\rho\text{ 的空腔圆柱}.
\]

对于空腔内任一点 \(P\)，设它相对于原圆柱轴线的位置矢量为 \(\vec r\)，相对于空腔轴线的位置矢量为 \(\vec r'\)，则

\[
\vec r=\vec d+\vec r'.
\]

两部分产生的电场分别为

\[
\vec E_1
=
\frac{\rho}{2\varepsilon_0}\vec r,
\]

\[
\vec E_2
=
-\frac{\rho}{2\varepsilon_0}\vec r'.
\]

所以

\[
\vec E
=
\frac{\rho}{2\varepsilon_0}
(\vec r-\vec r')
=
\frac{\rho}{2\varepsilon_0}\vec d.
\]

故空腔内为匀强电场：

\[
\boxed{
\vec E
=
\frac{\rho}{2\varepsilon_0}\vec d
}
\]

其方向由原圆柱轴线指向空腔轴线。

---

### 11.14

设无限大带电平面位于 \(x=0\)，取由左向右为 \(+x\) 方向。把左右两侧总电场沿 \(+x\) 的有向分量分别记为

\[
E_L,\qquad E_R.
\]

带电平面自身产生的电场在左右两侧分别为

\[
-\frac{\sigma}{2\varepsilon_0},
\qquad
+\frac{\sigma}{2\varepsilon_0}.
\]

设外电场为 \(E_0\)，则

\[
E_L
=
E_0-\frac{\sigma}{2\varepsilon_0},
\]

\[
E_R
=
E_0+\frac{\sigma}{2\varepsilon_0}.
\]

两式相加、相减可得

\[
\boxed{
E_0=\frac{E_L+E_R}{2}
}
\]

以及

\[
\boxed{
\sigma
=
\varepsilon_0(E_R-E_L)
}
\]

因此外电场的方向由 \(E_0\) 的正负决定。

若题图中的 \(E_1,E_2\) 表示左右两侧电场的有向分量，则

\[
\boxed{
\sigma=\varepsilon_0(E_2-E_1)
}
\]

\[
\boxed{
E_0=\frac{E_1+E_2}{2}
}
\]

若 \(A,B\) 分别位于平面左、右两侧，距平面的距离分别为 \(a,b\)，则

\[
V_B-V_A
=
-\int_A^B\vec E\cdot d\vec l.
\]

由于左右两侧电场均为匀强场，

\[
\boxed{
V_B-V_A
=
-(E_1a+E_2b)
}
\]

其中 \(E_1,E_2\) 均按 \(+x\) 方向取有向值。

若 \(A,B\) 到平面的距离相等，均为 \(d\)，则

\[
\boxed{
V_B-V_A
=
-d(E_1+E_2)
=
-2E_0d
}
\]

---

## 其他习题

### 无限大均匀带电厚板

有一块 \(x\) 方向厚度为 \(l\)，沿 \(y,z\) 方向无限延伸的均匀带电板，体电荷密度为 \(\rho\)。取原点位于板的中央，因此

\[
-\frac l2<x<\frac l2.
\]

由于平面对称性，电场只能沿 \(x\) 方向：

\[
\vec E=E_x(x)\hat i.
\]

由高斯定理的微分形式，

\[
\nabla\cdot\vec E
=
\frac{\rho}{\varepsilon_0},
\]

可得

\[
\frac{dE_x}{dx}
=
\frac{\rho}{\varepsilon_0}.
\]

积分，

\[
E_x
=
\frac{\rho}{\varepsilon_0}x+C.
\]

由对称性，

\[
E_x(0)=0,
\]

所以

\[
C=0.
\]

故板内电场为

\[
\boxed{
\vec E
=
\frac{\rho x}{\varepsilon_0}\hat i,
\qquad
|x|<\frac l2
}
\]

---

## 附加题

### 正 \(N\) 边形均匀带电面的中心电势

正 \(N\) 边形面上均匀分布面电荷密度为 \(\sigma\)，中心到一边中点的距离为 \(a\)，以无穷远为电势零点。

将正 \(N\) 边形分成 \(N\) 个完全相同的三角形。

令

\[
\alpha=\frac{\pi}{N}.
\]

在其中一个三角形内使用极坐标，其边界满足

\[
r_{\max}
=
\frac a{\cos\theta},
\qquad
-\alpha\le\theta\le\alpha.
\]

中心处的电势为

\[
V
=
k\sigma
\int\frac{dS}{r}.
\]

因为

\[
dS=r\,dr\,d\theta,
\]

所以一个三角形产生的电势为

\[
V_1
=
k\sigma
\int_{-\alpha}^{\alpha}
\int_0^{a/\cos\theta}
dr\,d\theta.
\]

于是

\[
V_1
=
k\sigma a
\int_{-\alpha}^{\alpha}
\sec\theta\,d\theta.
\]

利用

\[
\int\sec\theta\,d\theta
=
\ln|\sec\theta+\tan\theta|,
\]

得到

\[
V_1
=
2k\sigma a
\ln
\left(
\sec\alpha+\tan\alpha
\right).
\]

因此总电势为

\[
\boxed{
V
=
2Nk\sigma a
\ln
\left[
\sec\left(\frac\pi N\right)
+
\tan\left(\frac\pi N\right)
\right]
}
\]

即

\[
\boxed{
V
=
\frac{N\sigma a}{2\pi\varepsilon_0}
\ln
\left[
\sec\left(\frac\pi N\right)
+
\tan\left(\frac\pi N\right)
\right]
}
\]

当

\[
N\to\infty
\]

时，

\[
\ln(\sec x+\tan x)\sim x,
\]

因此

\[
N
\ln
\left[
\sec\left(\frac\pi N\right)
+
\tan\left(\frac\pi N\right)
\right]
\to\pi.
\]

故

\[
\boxed{
\lim_{N\to\infty}V
=
\frac{\sigma a}{2\varepsilon_0}
}
\]

这正是半径为 \(a\) 的均匀带电圆盘在圆心处的电势。
