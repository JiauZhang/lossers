### 前置
$$
\begin{aligned}
\int_{-\infty}^{+\infty} \int_{-\infty}^{+\infty} f^2(x) &= \int_{-\infty}^{+\infty}e^{-\frac {x^2} {a^2}}dx\int_{-\infty}^{+\infty}e^{-\frac {y^2} {a^2}}dy \\
&= \int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty} e^{-\frac {x^2+y^2} {a^2}}dxdy
\end{aligned}
$$

换元$(x,y)=(rcos\theta,rsin\theta)$，则$dxdy=|J|drd\theta=rdrd\theta$，带入换元可得：

$$
\begin{aligned}
&= \int_{0}^{2\pi}\int_{0}^{+\infty} e^{-\frac {r^2} {a^2}}rdrd\theta \\
&= \int_{0}^{2\pi} d\theta \int_{0}^{+\infty} e^{-\frac {r^2} {a^2}}rdr \\
&= 2\pi \times (-\frac {a^2} {2}) e^{-\frac {r^2} {a^2}}\bigg |_0^{+\infty} \\
&= a^2\pi
\end{aligned}
$$

由此可得：

$$
\int_{-\infty}^{+\infty} f(x) = \int_{-\infty}^{+\infty}e^{-\frac {x^2} {a^2}}dx = a \sqrt {\pi}
$$

进一步

$$
\begin{aligned}
\int_{-\infty}^{+\infty} x^2f(x) &= \int_{-\infty}^{+\infty}x^2e^{-\frac {x^2} {a^2}}dx
= \int_{-\infty}^{+\infty} -\frac {xa^2} {2} d(e^{-\frac {x^2} {a^2}})dx \\
&= \frac {a^2} {2} \bigg[ -xe^{-\frac {x^2} {a^2}}\bigg|_{-\infty}^{+\infty} - \int_{-\infty}^{+\infty} -e^{-\frac {x^2} {a^2}}dx \bigg] \\
&= \frac {a^2} {2} \times a\sqrt{\pi} = \frac {a^3} {2} \sqrt{\pi}
\end{aligned}
$$

### 高斯分布
$$
f(x) = \frac {1} {\sqrt{2 \pi \sigma^2}} e^{-\frac {(x-\mu)^2} {2 \sigma^2}}
$$

#### 高斯分布的均值
$$
\begin{aligned}
E(x) &= \int_{-\infty}^{+\infty} xf(x)dx = \int_{-\infty}^{+\infty} x\frac {1} {\sqrt{2 \pi \sigma^2}} e^{-\frac {(x-\mu)^2} {2 \sigma^2}}dx \\
&= \int_{-\infty}^{+\infty} (x-\mu)\frac {1} {\sqrt{2 \pi \sigma^2}} e^{-\frac {(x-\mu)^2} {2 \sigma^2}}dx + \mu \int_{-\infty}^{+\infty} \frac {1} {\sqrt{2 \pi \sigma^2}} e^{-\frac {(x-\mu)^2} {2 \sigma^2}}dx \\
&= \mu
\end{aligned}
$$

由于高斯分布$f(x)$是一个关于$(x-\mu)$偶函数，而公式中第一项$(x-\mu)$是一个奇函数，因此第一项积分为$0$；第二项中$\mu$与积分无关，故概率密度函数的积分为$1$。

#### 高斯分布的方差
$$
\begin{aligned}
Var(x) &= E((x-E(x))^2) =\int_{-\infty}^{+\infty} (x-\mu)^2 f(x)dx = \int_{-\infty}^{+\infty} (x-\mu)^2 \frac {1} {\sqrt{2 \pi \sigma^2}} e^{-\frac {(x-\mu)^2} {2 \sigma^2}}dx \\
&= \int_{-\infty}^{+\infty} y^2 \frac {1} {\sqrt{2 \pi \sigma^2}} e^{-\frac {y^2} {2 \sigma^2}}dy = \frac {1} {\sqrt{2 \pi \sigma^2}}
\int_{-\infty}^{+\infty} -y\sigma^2 d(e^{-\frac {y^2} {2 \sigma^2}})dy \\
&= \frac {\sigma} {\sqrt{2 \pi}} \bigg[ -ye^{-\frac {y^2} {2 \sigma^2}}\bigg |_{-\infty}^{+\infty} - \int_{-\infty}^{+\infty} -e^{-\frac {y^2} {2 \sigma^2}}dy \bigg] = \frac {\sigma} {\sqrt{2 \pi}} \int_{-\infty}^{+\infty} e^{-\frac {y^2} {2 \sigma^2}}dy \\
&= \frac {\sigma} {\sqrt{2 \pi}} \times \sqrt{2\pi}\sigma  \\
&= \sigma^2
\end{aligned}
$$

### 多元高斯分布的KL散度
定义$X$是一个$n\times1$为的随机向量，当$X$是一个具有均值$\mu$和方差$\Sigma$时，定义：

$$
X \sim \mathcal{N}(\bm\mu, \bm\Sigma) = \frac{1}{\sqrt{(2 \pi)^D |\bm\Sigma|}} \cdot \exp \left[ -\frac{1}{2} (\bm{x}-\bm\mu)^T \bm\Sigma^{-1} (\bm{x}-\bm\mu) \right]
$$

其中$\Sigma$是$n \times n$的正定矩阵。

现在先假设 $\bm{\Sigma^{-1}} = \bm{\Lambda}$ 是最简单的对角阵形式:

$$
\bm{\Lambda} = \begin{bmatrix}
 \lambda_1 & 0 & \cdots & 0 \\
 0 & \lambda_2 & \cdots & 0 \\
 \vdots & \vdots & \ddots & 0 \\
 0 & 0 & \cdots & \lambda_D \\
\end{bmatrix}_{D \times D}
$$

带入可得：

$$
\begin{aligned}
\int f(\bm{x}) &= \int e^{- \frac {1} {2} (\bm{x}-\bm\mu)^T \bm{\Lambda} (\bm{x}-\bm\mu)}d\bm{x} \\
&= \int e^{- \frac {1} {2} \bm{y}^T \bm{\Lambda} \bm{y}}d\bm{y} \\
&= \int dy_1 \int dy_2 \cdots \int e^{- \frac {1} {2} \sum_{i=1}^D\lambda_i y_i^2} dy_n \\
&= \int e^{- \frac {1} {2} \lambda_1 y_1^2} dy_1 \int e^{- \frac {1} {2} \lambda_2 y_2^2} dy_2 \cdots \int e^{- \frac {1} {2} \lambda_D y_D^2} dy_D \\
&= \sqrt{\frac {2\pi} {\lambda_1}} \sqrt{\frac {2\pi} {\lambda_2}} \cdots \sqrt{\frac {2\pi} {\lambda_D}} \\
&= \sqrt{\frac {(2\pi)^D} {\lambda_1 \lambda_1 \cdots \lambda_D}} \\
&= \sqrt{\frac {(2\pi)^D} {det(\bm{\Lambda})}}
\end{aligned}
$$

根据正定矩阵定理可知： $ \bm{A} = \bm{C}^T \bm{\Lambda} \bm{C}, \bm{A}^{-1} = \bm{C}^T \bm{\Lambda}^{-1} \bm{C} $ ，其中 $ \bm{C} $ 是正交阵 $ \bm{C}^T\bm{C} = \bm{C} \bm{C}^T = \bm{I}, \bm{C}^{-1} = \bm{C}^T $ ，带入更一般的概率密度函数：

$$
\begin{aligned}
\int f(\bm{x}) &= \int e^{- \frac {1} {2} \bm{(x-\mu)}^T \bm{A} \bm{(x-\mu)}} d\bm{x} = \int e^{- \frac {1} {2} \bm{(x-\mu)}^T \bm{C}^T \bm{\Lambda} \bm{C} \bm{(x-\mu)}} d\bm{x} \\
&= \int e^{- \frac {1} {2} (\bm{C(x-\mu)})^T \bm{\Lambda} (\bm{C(x-\mu)})} d\bm{x} \\
&= |det^{-1}(\bm{C})| \int e^{- \frac {1} {2} (\bm{y})^T \bm{\Lambda} (\bm{y})} d\bm{y} \\
&= |det^{-1}(\bm{C})| \sqrt{\frac {(2\pi)^D} {det(\bm{\Lambda})}}
= |det(\bm{C})| \sqrt{\frac {(2\pi)^D} {det(\bm{\Lambda})}} \\
&= \sqrt{\frac {(2\pi)^D det^2(\bm{C})} {det(\bm{\Lambda})}} = \sqrt{{(2\pi)^D det(\bm{C^T \Lambda^{-1} C})}} \\
&= \sqrt{{(2\pi)^D det(\bm{A^{-1}})}}
\end{aligned}
$$

令 $\bm{\Sigma} = \bm{A^{-1}}$ ，则有：

$$
\int_{-\infty}^{+\infty} f(\bm{x}) = \sqrt{{(2\pi)^D det(\bm{\Sigma})}}
$$


> [多元高斯分布的相关证明](https://www.jianshu.com/p/20341c1d9d47)
