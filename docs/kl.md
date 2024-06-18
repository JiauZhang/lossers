### 信息熵(Information Entropy)
信息论中，某个信息$x_i$出现的不确定性的大小定义为$x_i$所携带的信息量，用$I(x_i)$表示：

$$
I(x_i) = log \frac {1} {p(x_i)} = -log(p(x_i))
$$

进一步可得平均信息量为：

$$
H(x)
=-\sum_x{p(x) log(p(x))}
=-\sum_{i=1}^{n}{p(x_i) log(p(x_i))}
$$

由于$H(x)$与热力学中熵的定义类似，故又称为**信息熵**。

### 交叉熵(Cross Entropy)

$$
H(p, q)
=-\sum_x{p(x) log(q(x))}
=-\sum_{i=1}^{n}{p(x_i) log(q(x_i))}
$$

### 詹森不等式(Jensen Inequality)
定义$X$为随机变量，$\varphi$是凸函数，则有：

$$
\varphi (E[X]) \le E[\varphi (X)]
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
&= \int_{-\infty}^{+\infty} y^2 \frac {1} {\sqrt{2 \pi \sigma^2}} e^{-\frac {y^2} {2 \sigma^2}}dy \\
&= \sigma^2
\end{aligned}
$$

### 相对熵(Relative entropy) or KL散度(Kullback-Leibler Divergence)
$p(x)$是目标分布，$q(x)$是模型预测分布

$$
D_{KL}(p||q)=KL[p(x)||q(x)]
={\sum}_{x \in X} p(x) log \frac {p(x)} {q(x)}
=E_{x \in p(x)}[log \frac {p(x)} {q(x)}]
$$

性质：
- 当两个分布$p(x)$和$q(x)$相同时，$D_{KL}(p||q)=0$
- 非对称性：$D_{KL}(p||q) \neq D_{KL}(q||p)$
- 非负性：$D_{KL}(p||q) \ge 0$

$$
\begin{aligned}
D_{KL}(p||q)
&=\sum_x p(x) log \frac {p(x)} {q(x)} \\
&=-\sum_x p(x) log \frac {q(x)} {p(x)} \\
&=-E_{p(x)}\Bigg[ log \frac {q(x)} {p(x)} \Bigg] \\
&\ge -log E_{p(x)}\Bigg[\frac {q(x)} {p(x)} \Bigg] \\
&=-log \sum_x p(x) \frac {q(x)} {p(x)} \\
&=-log \sum_x {q(x)} \\
&=-log(1) = 0
\end{aligned}
$$

#### 两个高斯分布的KL散度
设$log(\cdot)=ln(\cdot)$，且$p(x)$、$q(x)$的概率密度函数分别为：

$$p(x) = \frac {1} {\sqrt{2 \pi \sigma_1^2}} e^{-\frac {(x-\mu_1)^2} {2 \sigma_1^2}}$$

$$q(x) = \frac {1} {\sqrt{2 \pi \sigma_2^2}} e^{-\frac {(x-\mu_2)^2} {2 \sigma_2^2}}$$

带入$D_{KL}(p||q)$可得：

$$
\begin{aligned}
D_{KL}(p||q) &= \int_{-\infty}^{+\infty} p(x) log \frac {p(x)} {q(x)} \\
&=\int_{-\infty}^{+\infty} p(x) \bigg[
    \frac {(x-\mu_2)^2} {2 \sigma_2^2} -
    \frac {(x-\mu_1)^2} {2 \sigma_1^2} +
    log \bigg( \frac {\sigma_2} {\sigma_1} \bigg)
\bigg] \\
&=
\end{aligned}
$$