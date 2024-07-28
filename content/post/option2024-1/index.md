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
##Introduction

Asian and lookback options, two distinct types of exotic options, differ fundamentally in their payoff structures, each designed to meet specific financial needs and risk profiles. Asian options, encompassing average price and average strike varieties, calculate their payoffs based on the average price of the underlying asset over a designated period. This averaging reduces the effects of volatility, often making these options less costly than standard options, which makes them particularly suitable for hedging in markets characterized by high volatility but indeterminate price trends.

In contrast, lookback options derive their payoffs from the highest or lowest price of the underlying asset during the life of the option. This feature ensures that the holder benefits from the most favorable price achieved during the option period, providing an optimal payoff scenario. Due to these characteristics, lookback options are generally more expensive than both standard and Asian options and are favored by investors anticipating significant market movements who aim to fully capitalize on these fluctuations.

In a complete market framework, the expected value of the discounted payoff under the risk-neutral probability measure \(Q\) for any derivative's price \(V(S, t)\) can be mathematically formulated as:

$$
    V(S, t) = e^{r(T-t)} \mathbb{E}^Q[\Lambda(S_T)]
$$

where $r$ is the risk-free rate, $T$ is the time of expiry, $t$ is the current time, $S_T$ is the stock price at expiry, and $\Lambda(S_T)$ denotes the option's specific payoff function.
</div>
