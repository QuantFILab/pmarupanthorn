---
title: "ตัวอย่างของมาร์ติงเกล"
summary: "โครงการนี้คือ WorldQuant University ในวิชา MScFE 622 Continuous-time Stochastic Processes."
date: 2020-07-21
math: true
authors:
  - admin
tags:
  - Stochastic Processes
  - Brownian Motion
image:
  caption: ''
---

<div style="font-size: 16px;">

## หมายเหตุ

โครงการนี้คือมหาวิทยาลัย WorldQuant ในหลักสูตร MScFE 622 เรื่องกระบวนการเชิงสุ่มเวลาต่อเนื่อง 

## คําถามที่ 1

ให้ $W = \{W_t : t \geq 0\}$ เป็นการเคลื่อนที่แบบบราวเนียนบน $(\omega, \mathcal{F}, \mathbb{F} = (\mathcal{F}_t)_{t \geq 0}, \mathbb{P})$

### คําถามที่ 1.1

แสดงว่า $W$ เป็น $\mathbb{F}$-martingale 

### ตอบ

เราพิจารณาข้อมูลที่สถานะ $s$ โดยที่ $s \leq t$จากสมมติฐานว่า $W$ เป็นการเคลื่อนที่แบบบราวเนียน ซึ่งบ่งชี้ว่า $W_t \sim N(0,t)$ และ $W_s \sim N(0,s)$ค่าคาดหวังแบบมีเงื่อนไขที่กําหนดสถานะข้อมูล $s$ ของการเคลื่อนที่แบบบราวเนียนคือ 

$$
\begin{align*}
\mathbb{E}[W_t|\mathcal{F}_s] &= \mathbb{E}[(W_t - W_s + W_s)|\mathcal{F}_s] & \text{Include and exclude rules} \\
&   = \mathbb{E}[(W_t - W_s)|\mathcal{F}_s]  + \mathbb{E}[W_s|\mathcal{F}_s] & \text{Linear property of the expectation } \\
& = \mathbb{E}[(W_t - W_s)] +  W_s & \text{$W_t - W_s \sim N(0,t-s)$ and it is independent of $\mathcal{F}_s$}\\
&   = \mathbb{E}[W_t] - \mathbb{E}[W_s] + W_s & \text{Linear property of the expectation} \\
& = 0 - 0+ W_s & \text{$W_t \sim N(0,t)$ and $W_s \sim N(0,s)$} \\
& = W_s.
\end{align*} 
$$

ดังนั้น $W$ จึงเป็น $\mathbb{F}-$martingale  

### คําถามที่ 1.2
แสดงว่าสําหรับทุก $\alpha \ใน \mathbb{R}$ กระบวนการ

$$X_t^{\alpha} =: \exp(\alpha W_t - \frac{1}{2}\alpha^2t)$$
เป็น $\mathbb{F}$-martingale

### ตอบเราทราบว่า $W_t \sim N(0,t)$จากการสร้างโมเมนต์ของการแจกแจงปกติ ($X \sim N(\mu,\sigma^2)$ แล้ว $M_X(\alpha) = \exp(\alpha\mu + \frac{1}{2}\sigma^2\alpha^2)$ ความสัมพันธ์ระหว่าง $W_t-W_s \sim N(0,s-t)$ กับฟังก์ชันการสร้างโมเมนต์ของมันถูกกําหนดโดย

$$
\begin{align}
M_{W_t-W_s}(\alpha) &= \mathbb{E}(\exp(\alpha(W_t-W_s))) \nonumber\\
 &=  \exp(\alpha\mu +  \frac{1}{2}\sigma^2\alpha^2) & W_t - W_s \sim N(0,s-t) \nonumber\\
& = \exp(\alpha (\mathbb{E}(W_t) - \mathbb{E}(W_s)) +  \frac{1}{2}(s-t)\alpha^2) & \mu = \mathbb{E}(x),\ \sigma^2 = s-t  \nonumber\\
& =  \exp(\frac{1}{2}(s-t)\alpha^2) & \mathbb{E}(W_t) = \mathbb{E}(W_s) = 0. \ (E3)
\end{align}
$$

อีกครั้ง เราพิจารณาค่าคาดหวังแบบมีเงื่อนไขของกระบวนการ $X_t^\alpha$, 

$$
\begin{align*}
\mathbb{E}[X_t^{\alpha}|\mathcal{F}_s]  &= \mathbb{E}\left[\exp(\alpha W_t - \frac{1}{2}\alpha^2t)\Bigg|\mathcal{F}_s\right] &\text{Given information} \\
& = \mathbb{E}\left[\exp(\alpha(W_t - W_s) + \alpha W_s- \frac{1}{2}\alpha^2t) \Bigg|\mathcal{F}_s\right] &  \text{Include and exclude rules} \\
& =  \mathbb{E}\left[\exp(\alpha(W_t - W_s))\exp(\alpha W_s -\frac{1}{2}\alpha^2t) \Bigg|\mathcal{F}_s\right] &\text{Exponential function's property} \\
& =  \exp(\alpha W_s -\frac{1}{2}\alpha^2t)  \mathbb{E}\left[\exp(\alpha(W_t - W_s)) \Bigg|\mathcal{F}_s\right] &\text{$W_s$ is measurable with respect to $\mathcal{F}_s$} \\
& =  \exp(\alpha W_s -\frac{1}{2}\alpha^2t) \mathbb{E}[\exp(\alpha(W_t - W_s))]&\text{$W_t - W_s \sim N(0,t-s)$ independent of $\mathcal{F}_s$}\\
& =   \exp(\alpha W_s -\frac{1}{2}\alpha^2t)\exp(\frac{1}{2}(s-t)\alpha^2)  &\text{Using MGF (E3)} \\
& =    \exp(\alpha W_s - \frac{1}{2}\alpha^2s)  &\text{Simplifying} \\
& =   X_s^\alpha &\text{From Definition of $X_s^\alpha$} 
\end{align*}
$$

ดังนั้น $X_t^\alpha$ เป็น $\mathbb{F}-$martingale สําหรับทุก $\alpha \ใน \mathbb{R}$\\ 


## คําถามที่ 2

กําหนดพหุนาม $H_n(x,y);\ n = 0,1,2,\dots$ โดย

$$H_n(x,y) = \frac{\partial^n}{\partial \alpha^n} \exp(\alpha x - \frac{1}{2}\alpha^2y) \ \text{at} \ \alpha = 0$$

ตัวอย่างเช่น 

$$H_0(x,y) = 1, \ H_(x,y) =x, \ H_2(x,y) = x^2-y, \ H_3(x,y) = x^3-3xy,\ H_4(x,y) = x^4-6x^2y+3y^3, \ \text{etc.}$$

สามารถแสดงได้ (โดยใช้ชุด Taylor) ว่า

$$X_t^\alpha = \exp(\alpha W_t - \frac{1}{2}\alpha^2t) = \sum_{n = 0}^{\infty} \frac{\alpha^n}{n!}H_n(W_t,t)$$

ตอนนี้เราแสดงให้เห็นว่า $H_n(W_t,t)$ เป็นมาร์ติงเกลสําหรับแต่ละ $n$

### คําถามที่ 2.1

ให้ $0 \leq s \leq t$ และ $\alpha \in \mathbb{R}$อธิบายว่าทําไมสําหรับแต่ละ$F \ใน \mathcal{F}_s$


$$\int_{F} X_t^\alpha d \mathbb{P} = \int_{F} X_s^\alpha d\mathbb{P}$$

### ตอบข้อความนี้สามารถอธิบายได้ง่ายโดยนิยามของค่าคาดหวังแบบมีเงื่อนไข 

$$\mathbb{E}(X|F) = \int_F X d\mathbb{P},$$

สําหรับ $F \ใน \mathcal{F}$เราใช้ค่าคาดหวังแบบมีเงื่อนไขของกระบวนการ $X_t^\alpha$,  

$$
X_s^\alpha = \mathbb{E}[(X_t^\alpha|F)]=  \int_{F} X_s^\alpha d\mathbb{P} \ (E1.), 
$$

เนื่องจาก $\mathbb{F}$-martingale ของ $X_t^\alpha$ และนิยามของค่าคาดหวังแบบมีเงื่อนไขเรายังทราบว่า $\mathbb{E}(X_t^\alpha) < \infty$จากนั้นเราพิจารณาอีกครั้ง $X_s^\alpha$, 

$$
X_s^\alpha = \mathbb{E}[(X_s^\alpha|F)]=  \int_{F} X_s^\alpha d\mathbb{P} \ (E2.), 
$$

เนื่องจาก $X_s$ เป็น $\mathcal{F}_s$-วัดได้ และเป็นนิยามของค่าคาดหวังแบบมีเงื่อนไขการตั้งค่า $E 1 = E2$,  

$$\int_{F} X_t^\alpha d \mathbb{P} = \int_{F} X_s^\alpha d\mathbb{P}$$

### คําถามที่ 2.2

โดยการหาอนุพันธ์ (3a) ทั้งสองด้าน $n$ คูณกับ $\alpha$ และสลับอนุพันธ์กับอินทิกรัล (ไม่จําเป็นต้องอธิบายขั้นตอนนี้) แสดงว่า 

$$\mathbb{E}(H_n(W_t,t)|\mathcal{F}_s) = H_n(W_s,s),$$

### ตอบ

เมื่อพิจารณาอนุพันธ์เวลา $n$ ตาม $\alpha$ เราจะได้

$$
\begin{align*}
\pdv[n]{}{\alpha}\int_{F} X_t^\alpha d \mathbb{P} &= \pdv[n]{}{\alpha}\int_{F} X_s^\alpha d\mathbb{P} &\text{From (3a)}  \\
\int_{F} \pdv[n]{}{\alpha} X_t^\alpha d \mathbb{P} &=\int_{F}  \pdv[n]{}{\alpha} X_s^\alpha d\mathbb{P} & \text{Interchange between} \\
&& \text{derivative and integral} \\
\int_{F} \pdv[n]{}{\alpha}\exp(\alpha W_t - \frac{1}{2}\alpha^2t) d \mathbb{P} &=\int_{F}  \pdv[n]{}{\alpha} \exp(\alpha W_s - \frac{1}{2}\alpha^2s) d \mathbb{P} &\text{Definition of $X_{\cdot}^\alpha$}\\
\int_{F} H_n(W_t,t)  d \mathbb{P} &=\int_{F} H_n(W_s,s)  d\mathbb{P} &\text{Definition of $H_n(x,y)$}\\
\mathbb{E}(H_n(W_t,t)|F)  &= \mathbb{E}(H_n(W_s,s)|F) &\text{Definition of}\\
&&\text{the conditional expectation}\\
\mathbb{E}(H_n(W_t,t)|F)  &=  H_n(W_s,s) &\text{$W_s$ is $F$-measurable}
\end{align*} 
$$

เนื่องจาก $F \ใน \mathcal{F}_s$,  

$$
\mathbb{E}(H_n(W_t,t)|\mathcal{F}_s)  =  H_n(W_s,s)
$$


### คําถามที่ 2.3สรุปว่า $\{ H_n(W_t,t) : t \geq 0 \}$ เป็นมาร์ติงเกล 


### ตอบ

จากสมการ (\ref{4}) กระบวนการ $\{ H_n(W_t,t) : t \geq 0 \}$ เป็น $\mathcal{F}_s$-martingale 

</div>
