定义扩散模型逆过程是马尔科夫链，则有：

$$
\begin{aligned}
p_\theta(x_{0:T}) &= p_\theta(x_0 | x_{1:T}) p_\theta(x_{1:T}) = p_\theta(x_0 | x_1) p_\theta(x_{1:T}) \\
&= p_\theta(x_0 | x_1) p_\theta(x_1 | x_{2:T}) p_\theta(x_{2:T}) \\
&= p_\theta(x_0 | x_1) p_\theta(x_1 | x_2) p_\theta(x_{2:T}) \\
&= \cdots = p_\theta(x_0 | x_1) p_\theta(x_1 | x_2) \cdots p_\theta(x_{T-1} | x_T) p_\theta(x_T) \\
&= p_\theta(x_T) \prod_{t=1}^{T} p_\theta(x_{t-1} | x_t)
\end{aligned}
$$

定义前向过程同样是马尔科夫链过程，则有：

$$
q(x_{0:T}) = q(x_0) \prod_{t=1}^{T} q(x_{t} | x_{t-1})
$$

定义前向过程和逆过程概率分布均为高斯分布：

$$
q(x_{t} | x_{t-1}) = \mathcal{N}(x_t;\sqrt{1-\beta_t}x_{t-1},\beta_t I) \\
p_\theta(x_{t-1} | x_t) = \mathcal{N}(x_{t-1};\bm\mu_{\theta}(x_t, t),\bm\Sigma_{\theta}(x_t, t)) \\
$$

根据贝叶斯定理及马尔科夫性质：

$$
\begin{aligned}
q(x_{t} | x_{t-1}) &= q(x_{t} | x_{t-1}, x_0) = \frac {q(x_t, x_{t-1}, x_0)} {q(x_{t-1}, x_0)} \\
&= \frac {q(x_{t-1} | x_t, x_0) q(x_t, x_0)} {q(x_{t-1}, x_0)} = \frac {q(x_{t-1} | x_t, x_0) q(x_t | x_0) q(x_0)} {q(x_{t-1} | x_0) q(x_0)} \\
&= \frac {q(x_{t-1} | x_t, x_0) q(x_t | x_0)} {q(x_{t-1} | x_0)}
\end{aligned}
$$

根据VAE中ELBO的结论可得：

$$
\begin{aligned}
\mathbb{E}[-\mathrm{log}p_\theta(x_0)] & \le \mathbb{E}_q\bigg[-\mathrm{log}\frac{p_\theta(x_{0:T})}{q(x_{1:T}|x_0)}\bigg] = \mathbb{E}_q\bigg[-\mathrm{log}p_\theta(x_T) - \sum_{t \ge 1} \mathrm{log} \frac{p_\theta(x_{t-1} | x_t)}{q(x_{t} | x_{t-1})}\bigg] \\
&= \mathbb{E}_q\bigg[-\mathrm{log}p_\theta(x_T) - \mathrm{log} \frac{p_\theta(x_0 | x_1)}{q(x_1 | x_0)} - \sum_{t > 1} \mathrm{log} \frac{p_\theta(x_{t-1} | x_t)}{q(x_{t} | x_{t-1})}\bigg] \\
&= \mathbb{E}_q\bigg[-\mathrm{log}p_\theta(x_T) - \mathrm{log} \frac{p_\theta(x_0 | x_1)}{q(x_1 | x_0)} - \sum_{t > 1} \mathrm{log} \frac{p_\theta(x_{t-1} | x_t)}{q(x_{t} | x_{t-1},x_0)}\bigg] \\
&= \mathbb{E}_q\bigg[-\mathrm{log}p_\theta(x_T) - \mathrm{log} \frac{p_\theta(x_0 | x_1)}{q(x_1 | x_0)} - \sum_{t > 1} \mathrm{log} \frac{p_\theta(x_{t-1} | x_t)}{q(x_{t-1} | x_t,x_0)} \cdot \frac{q(x_{t-1} | x_0)}{q(x_t | x_0)} \bigg] \\
&= \mathbb{E}_q\bigg[-\mathrm{log}p_\theta(x_T) - \mathrm{log} \frac{p_\theta(x_0 | x_1)}{q(x_1 | x_0)} - \sum_{t > 1} \mathrm{log} \frac{p_\theta(x_{t-1} | x_t)}{q(x_{t-1} | x_t,x_0)} - \sum_{t > 1} \mathrm{log} \frac{q(x_{t-1} | x_0)}{q(x_t | x_0)} \bigg] \\
&= \mathbb{E}_q\bigg[-\mathrm{log}p_\theta(x_T) - \mathrm{log} \frac{p_\theta(x_0 | x_1)}{q(x_1 | x_0)} - \sum_{t > 1} \mathrm{log} \frac{p_\theta(x_{t-1} | x_t)}{q(x_{t-1} | x_t,x_0)} - \mathrm{log} \frac{q(x_1 | x_0)}{q(x_T | x_0)} \bigg] \\
&= \mathbb{E}_q\bigg[-\mathrm{log}p_\theta(x_T) - \mathrm{log} \frac{p_\theta(x_0 | x_1)}{q(x_T | x_0)} - \sum_{t > 1} \mathrm{log} \frac{p_\theta(x_{t-1} | x_t)}{q(x_{t-1} | x_t,x_0)} \bigg] \\
&= \mathbb{E}_q\bigg[-\mathrm{log} \frac {p_\theta(x_T)} {q(x_T | x_0)} - \mathrm{log} {p_\theta(x_0 | x_1)} - \sum_{t > 1} \mathrm{log} \frac{p_\theta(x_{t-1} | x_t)}{q(x_{t-1} | x_t,x_0)} \bigg] \\
&= \mathbb{E}_q\bigg[D_{KL}(q(x_T | x_0) \parallel p_\theta(x_T)) - \mathrm{log} {p_\theta(x_0 | x_1)} + \sum_{t > 1} D_{KL} (q(x_{t-1} | x_t,x_0) \parallel p_\theta(x_{t-1} | x_t)) \bigg] \\
& = \mathbb{E}_q\bigg[L_T - L_0 + \sum_{t > 1} L_{t-1} \bigg]
\end{aligned}
$$
