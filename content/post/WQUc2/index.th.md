---
title: "ตัวอย่างการแก้สมการเชิงอนุพันธ์เชิงสุ่ม"
summary: "โครงการนี้เป็นการบ้านของมหาวิทยาลัย WorldQuant ในรายวิชา MScFE 622 Continuous-time Stochastic Processes"
date: 2020-08-10
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

โครงการนี้คือการบ้านของมหาวิทยาลัย WorldQuant ในวิชา MScFE 622 เรื่องกระบวนการสุ่มต่อเนื่อง 


## คําถาม 

ให้ $W = \{W_t: t \geq 0\}$ เป็นการเคลื่อนที่แบบบราวเนียนบน $(\Omega, \mathcal{F}, \mathbb{F} = (\mathcal{F}_t)_{t \geq 0}, \mathbb{P})$.กําหนด $\alpha, \ \beta \ใน \mathbb{R}$ และพิจารณา SDE ดังนี้: 

$$
d X_t = \frac{\beta - X_t}{T-t}dt + d W_t, \ \ \ 0< t < T, \ (E1)
$$

และ 

$$X_0 = \alpha, \ X_T = \beta.$$

คําตอบของ SDE นี้ที่มีเงื่อนไขขอบเขตที่กําหนด เรียกว่า บราวเนียนบริดจ์โดยการนําบทนิยามของอิโตะไปใช้กับ $Y_t := f(t,X_t) = \frac{X_t}{T-t}$ ให้แก้ SDE นี้และหาการแจกแจง ค่าเฉลี่ย และความแปรปรวนของ $X_t$ โดยที่ $0 < t < T.$\\\ 


## ตอบ

เรานําเลมมา Ito มาใช้กับกระบวนการ $Y_t =\frac{X_t}{T-t}$,  

$$
\begin{align}
d Y_t &= \pdv{f(t,X_t)}{t}dt + \pdv{f(t,X_t)}{X_t} d X_t + \frac{1}{2}\pdv[2]{f(t,X_t)}{X_t} d X_t^2 & \text{Ito's Lemma}\\
&= \frac{X_t}{(T-t)^2}dt + \frac{1}{(T-t)}d X_t + 0   & \text{Differentiating}  \\
&= \frac{X_t}{(T-t)^2}dt + \frac{1}{(T-t)}\left(\frac{\beta - X_t}{T-t}dt + d W_t\right)   & \text{Using (\ref{BB})}  \\
&= \frac{\beta}{(T-t)^2}dt + \frac{1}{(T-t)}d W_t   & \text{Rearranging} \ (E3).
\end{align}
$$

ต่อไปเราจะหาคําตอบของกระบวนการ $Y_t$ ใน (E3) โดยการอินทิเกรต 

$$
\begin{align}
Y_t &= Y_0 + \int_0^t \frac{\beta}{(T-s)^2}ds + \int_0^t \frac{1}{(T-s)}d W_s & \text{Integrating (\ref{DYR})}  \nonumber\\
      &= Y_0 + \frac{2\beta}{T-t} -\frac{2\beta}{T} + \int_0^t \frac{1}{(T-s)}d W_s &   \nonumber \\
      &= \frac{\alpha}{T-t} + \frac{2\beta}{T-t} -\frac{2\beta}{T} + \int_0^t \frac{1}{(T-s)}d W_s & Y_0 = \frac{X_0}{T-t} =  \frac{\alpha}{T-t}  \nonumber  \\
      &= \frac{\alpha+2\beta}{T-t} -\frac{2\beta}{T} + \int_0^t \frac{1}{(T-s)}d W_s &  \nonumber
\end{align}
$$

ดังนั้น  

$$
\begin{align}
X_t &=  (T-t)\left(\frac{\alpha+2\beta}{T-t} -\frac{2\beta}{T} + \int_0^t \frac{1}{(T-s)}d W_s \right)\nonumber \\
&=  \alpha+2\beta \left( \frac{t}{T }\right) + (T-t)\int_0^t \frac{1}{(T-s)}d W_s  \ (E4).\\
\end{align}
$$

โดยใช้เงื่อนไขขอบเขต $X_T = \beta$, 

$$
\begin{align}
  \beta &= \alpha+2\beta \left( \frac{T}{T }\right) + (T-T)\int_0^T \frac{1}{(T-s)}d W_s \\
            & = -\alpha.
\end{align}
$$ดังนั้นคําตอบใน (E4) สามารถเขียนใหม่เป็น 

$$
X_t = \alpha \left( 1 -\frac{2t}{T }\right) + (T-t)\int_0^t \frac{1}{(T-s)}d W_s.
$$

ดังนั้น $X_t$ จึงมีการแจกแจงปกติโดยมีค่าเฉลี่ย 

$$\mathbb{E}(X_t) = \alpha \left( 1 -\frac{2t}{T }\right),$$

และความแปรปรวน 

$$\text{Var}(X_t) = \text{Var}\left((T-t)\int_0^t \frac{1}{(T-s)}d W_s\right)= (T-t)^2\int_0^t \frac{1}{(T-s)^2}ds  =2(T-t)^2\left(\frac{1}{T-t}  - \frac{1}{T}\right),$$
เช่น $X_t \sim N\left(\alpha \left( 1 -\frac{2t}{T }\right),2(T-t)^2\left(\frac{1}{T-t} - \frac{1}{T}\right)\right)$. 

</div>
