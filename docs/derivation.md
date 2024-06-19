### 积的导数
$$
\begin{aligned}
[u(x)v(x)]^{'} &= \lim\limits_{\varDelta x \to 0} \frac {u(x+\varDelta x)v(x+\varDelta x) - u(x)v(x)} {\varDelta x} \\
&= \lim\limits_{\varDelta x \to 0} \frac {u(x+\varDelta x)v(x+\varDelta x) - u(x+\varDelta x)v(x) + u(x+\varDelta x)v(x) - u(x)v(x)} {\varDelta x} \\
&= \lim\limits_{\varDelta x \to 0} \frac {u(x+\varDelta x)v(x+\varDelta x) - u(x+\varDelta x)v(x)} {\varDelta x} +
\lim\limits_{\varDelta x \to 0} \frac {u(x+\varDelta x)v(x) - u(x)v(x)} {\varDelta x} \\
&= \lim\limits_{\varDelta x \to 0} \frac {v(x+\varDelta x) - v(x)} {\varDelta x} u(x+\varDelta x) +
\lim\limits_{\varDelta x \to 0} \frac {u(x+\varDelta x) - u(x)} {\varDelta x} v(x) \\
&= v^{'}(x)u(x) + u^{'}(x)v(x)
\end{aligned}
$$

### 分部积分
根据积的导数可知，两边同时积分接的分部积分的结论。

$$
\int u(x)v^{'}(x)dx = u(x)v(x) - \int u^{'}(x)v(x)dx
$$

### 二重积分换元
对二重积分来说，换元其实就是底面积的变化，要想换元前后$(u,v) \rightarrow (x(u,v), y(u, v))$的结果不变，需要保证换元前后底面积不变。

<div align="center">
<img src="./images/derivation-01.png" />
</div>

根据上图可得：

$$
\begin{aligned}
\overrightarrow m &= (x(u_0+du, v_0) - x(u_0, v_0), y(u_0+du, v_0) - y(u_0, v_0)) \\
&= x_u^{'}du + y_u^{'}du
\end{aligned}
$$

$$
\begin{aligned}
\overrightarrow l &= (x(v_0+dv, u_0) - x(u_0, v_0), y(v_0+dv, u_0) - y(u_0, v_0)) \\
&= x_v^{'}dv + y_v^{'}dv
\end{aligned}
$$

进一步可得：

$$
\begin{aligned}
|\overrightarrow u \times \overrightarrow v| &= dudv =dA_1=dA_2=dxdy=
|\overrightarrow m \times \overrightarrow l| \\
&=|x_u^{'}y_v^{'}-y_u^{'}x_v^{'}|dudv =
\begin{vmatrix}
x_u^{'} & x_v^{'} \\ 
y_u^{'} & y_v^{'}
\end{vmatrix} dudv \\
&= |J|dudv
\end{aligned}
$$
