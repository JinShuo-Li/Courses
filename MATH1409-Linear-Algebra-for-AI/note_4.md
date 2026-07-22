## 矩阵的谱分解和奇异值分解

### 矩阵的谱分解

**定义**: 可对角化的矩阵称为半单矩阵.

**定义**: 矩阵的所有特征值称为矩阵的**谱**, 记为$\sigma(A) = \{\lambda_1, \lambda_2, \cdots, \lambda_n\}$. 记$\rho(A) = \max\{|\lambda|: \lambda \in \sigma(A)\}$为矩阵的**谱半径**.

**定理**(谱分解定理): 设$A_n$是一个$n$阶半单矩阵, $A$的谱为$\sigma(A) = \{\lambda_1, \lambda_2, \cdots, \lambda_n\}$, 则存在唯一一组$P_1, P_2, \cdots, P_n$使得
$$
A = \lambda_1 P_1 + \lambda_2 P_2 + \cdots + \lambda_n P_n.
, \quad
\sum_{i=1}^n P_i = I
, \quad
P_i^2 = P_i
, \quad
P_i P_j = 0 \quad (i \neq j).
$$

对于这组唯一的矩阵$P_1, P_2, \cdots, P_n$, 称$P_i$为**成分矩阵**, 因为它成功的把矩阵分成了不同的"单纯变换"的加权求和.

**推论**: 设$A=\sum_{i=1}^n \lambda_i P_i$, 那么我们可以得到:

$$
A^m = \sum_{i=1}^n \lambda_i^m P_i
$$

$$
f(A) = \sum_{i=1}^n f(\lambda_i) P_i
$$

### SVD分解

