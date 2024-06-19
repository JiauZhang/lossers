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
&= log \bigg( \frac {\sigma_2} {\sigma_1} \bigg)
+ \int_{-\infty}^{+\infty} p(x)\frac {(x-\mu_2)^2} {2 \sigma_2^2}dx
- \int_{-\infty}^{+\infty} p(x)\frac {(x-\mu_1)^2} {2 \sigma_1^2}dx 
\end{aligned}
$$

其中

$$
\begin{aligned}
\int_{-\infty}^{+\infty} p(x)\frac {(x-\mu_1)^2} {2 \sigma_1^2}dx &= \int_{-\infty}^{+\infty} \frac {(x-\mu_1)^2} {2 \sigma_1^2} \frac {1} {\sqrt{2 \pi \sigma_1^2}} e^{-\frac {(x-\mu_1)^2} {2 \sigma_1^2}}dx \\
&= \frac {1} {2\sigma_1^3\sqrt{2\pi}} \int_{-\infty}^{+\infty} (x_1-\mu_1)^2e^{-\frac {(x-\mu_1)^2} {2 \sigma_1^2}}dx \\
&= \frac {1} {2\sigma_1^3\sqrt{2\pi}} \int_{-\infty}^{+\infty} y^2e^{-\frac {y^2} {2 \sigma_1^2}}dy \\
&= \frac {1} {2\sigma_1^3\sqrt{2\pi}} \times \frac {(\sqrt{2}\sigma_1)^3} {2} \sqrt{\pi} \\
&= \frac {1} {2}
\end{aligned}
$$

另外

$$
\begin{aligned}
\int_{-\infty}^{+\infty} p(x)\frac {(x-\mu_2)^2} {2 \sigma_2^2}dx
&= \frac {1} {2\sigma_2^2} \int_{-\infty}^{+\infty} p(x)(x^2-2x\mu_2+\mu_2^2-2x\mu_1+\mu_1^2+2x\mu_1-\mu_1^2)dx \\
&= \frac {1} {2\sigma_2^2} \int_{-\infty}^{+\infty} p(x)\bigg[(x-\mu_1)^2+2x(\mu_1-\mu_2)+(\mu_2^2-\mu_1^2) \bigg]dx \\
&= \frac {1} {2\sigma_2^2}\bigg[\int_{-\infty}^{+\infty} p(x)(x-\mu_1)^2dx + 2(\mu_1-\mu_2)\int_{-\infty}^{+\infty} xp(x)dx
+ (\mu_2^2-\mu_1^2) \int_{-\infty}^{+\infty} p(x)dx \bigg] \\
&= \frac {1} {2\sigma_2^2}\bigg[\int_{-\infty}^{+\infty} p(y)y^2dy
+ 2(\mu_1-\mu_2)E[x] + (\mu_2^2-\mu_1^2) \bigg] \\
&= \frac {1} {2\sigma_2^2}\bigg[\sigma_1^2 + 2\mu_1^2 - 2\mu_1\mu_2 + \mu_2^2 - \mu_1^2  \bigg] \\
&= \frac {\sigma_1^2 + (\mu_1-\mu_2)^2} {2\sigma_2^2}
\end{aligned}
$$

带入可得：

$$
D_{KL}(p||q)
= log \bigg( \frac {\sigma_2} {\sigma_1} \bigg)
+ \frac {\sigma_1^2 + (\mu_1-\mu_2)^2} {2\sigma_2^2}
- \frac {1} {2} 
$$
