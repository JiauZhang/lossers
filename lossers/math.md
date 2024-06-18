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
&=\sum_x p(x) log \frac {q(x)} {p(x)} \\
&=-E_{p(x)}\Bigg[ log \frac {q(x)} {p(x)} \Bigg] \\
&\ge -log E_{p(x)}\Bigg[\frac {q(x)} {p(x)} \Bigg] \\
&=-log \sum_x p(x) \frac {q(x)} {p(x)} \\
&=-log \sum_x {q(x)} \\
&=-log(1) = 0
\end{aligned}
$$
