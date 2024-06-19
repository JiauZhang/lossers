### 前置
$$
\begin{aligned}
f^2(x) &= \int_{-\infty}^{+\infty}e^{-\frac {x^2} {a^2}}dx\int_{-\infty}^{+\infty}e^{-\frac {y^2} {a^2}}dy \\
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
f(x) = \int_{-\infty}^{+\infty}e^{-\frac {x^2} {a^2}}dx = a \sqrt {\pi}
$$

进一步

$$
\begin{aligned}
x^2f(x) &= \int_{-\infty}^{+\infty}x^2e^{-\frac {x^2} {a^2}}dx
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
