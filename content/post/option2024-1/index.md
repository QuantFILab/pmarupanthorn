---
title: Why the Lookback Option is More Expensive Than the Asian Option, A Simulation Approach
summary: 
date: 2024-04-22
math: true
authors:
  - admin
tags:
  - Option
  - Monte Carlo Simulation
image:
  caption: 'Lookback Option Versus Asian Option'
---

<div style="font-size: 16px;">
  
## Introduction

Asian and lookback options, two distinct types of exotic options, differ fundamentally in their payoff structures, each designed to meet specific financial needs and risk profiles. Asian options, encompassing average price and average strike varieties, calculate their payoffs based on the average price of the underlying asset over a designated period. This averaging reduces the effects of volatility, often making these options less costly than standard options, which makes them particularly suitable for hedging in markets characterized by high volatility but indeterminate price trends.

In contrast, lookback options derive their payoffs from the highest or lowest price of the underlying asset during the life of the option. This feature ensures that the holder benefits from the most favorable price achieved during the option period, providing an optimal payoff scenario. Due to these characteristics, lookback options are generally more expensive than both standard and Asian options and are favored by investors anticipating significant market movements who aim to fully capitalize on these fluctuations.

In a complete market framework, the expected value of the discounted payoff under the risk-neutral probability measure \(Q\) for any derivative's price \(V(S, t)\) can be mathematically formulated as:

$$
    V(S, t) = e^{r(T-t)} \mathbb{E}^Q[\Lambda(S_T)]
$$

where $r$ is the risk-free rate, $T$ is the time of expiry, $t$ is the current time, $S_T$ is the stock price at expiry, and $\Lambda(S_T)$ denotes the option's specific payoff function.

Path-dependent options such as the arithmetic average-type call Asian option demonstrate the influence of the underlying asset's historical prices on the payoff:
$$
    \Lambda_{asian}(t) = (\bar{S} - K)^+, \ \text{where} \ \bar{S} = \frac{1}{m}\sum_{j = 1}^m S(t_j),
$$
with $m$ representing the number of observation periods. Similarly, the fixed-strike lookback option's payoff is determined by:
$$
    \Lambda_{lookback}(t) = (S_{\text{max}} - K)^+
$$
where $S_{\text{max}}$ is the maximum price reached during the option's duration. Both option payoffs can be readily found in the literature textbook such as the standard book by Hull and Basu \cite{hull2016options}. 

While these options cannot be priced analytically within the traditional Black-Scholes framework, alternative analytical methods such as spectral theory have been employed to estimate the prices of Asian options \cite{linetsky2001exact}. However, this discussion will primarily focus on using the standard Euler-Maruyama scheme for approximating the prices of these options and explaination mathematically why the lockback option more expensive than the Asian option at the equivalent parameters in the subsequent section.

</div>
