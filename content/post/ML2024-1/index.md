---
title: Support Vector Machines for Classification on SET100 Returns
summary: The project was the CQF exam in Monte Carlo simulation for option pricing.
date: 2024-06-17
math: true
authors:
  - admin
tags:
  - Machine Learning
  - Classification
  - SET100
image:
  caption: 'Confuse Matrix'
---

<div style="font-size: 16px;">

## Note

The project was the CQF exam in Machine Learning in Finance.

## Problem Understanding

The SET100 index, representing the top 100 stocks on the Stock Exchange of Thailand (SET), serves as a critical benchmark for Thailand's equity market. Unlike established indices in developed markets such as the S\&P 500 or the FTSE 100, the SET100 is exposed to the dynamic economic landscape of an emerging market. Emerging markets like Thailand offer higher growth potential due to industrialization, urbanization, and favorable demographics. However, this growth comes with increased volatility and higher risks, influenced by political instability, economic fluctuations, and global economic shocks.

The SET100 provides unique investment opportunities across diverse sectors, including finance, energy, consumer goods, and industrials. The inclusion of small to medium-sized enterprises in the index underscores its potential for significant growth. These features, along with the challenges and opportunities inherent in emerging markets, make the SET100 an intriguing subject for financial analysis and return prediction.

Accurately predicting stock returns is crucial for informed investment decisions. The volatile and complex nature of financial markets, with factors like market sentiment, economic indicators, and geopolitical events, poses significant challenges for return prediction. Traditional statistical methods often fail to capture the non-linear relationships within the data, necessitating more advanced machine learning techniques. In this project, we employ Support Vector Machines (SVM) to classify the daily returns of SET100 stocks, leveraging the algorithm's capability to handle high-dimensional data and model complex patterns. Our goal is to enhance predictive accuracy, providing valuable insights for investors and portfolio managers.


## Data Retrieving

The data for this study, including the open, high, low, and close (OHLC) prices of the SET100 stocks, was retrieved from [Investing.com](https://www.investing.com/). The dataset spans from January 3, 2018, to May 30, 2024, providing a comprehensive range of historical price data. All prices are adjusted for dividends and are presented in Thai Baht (THB). Upon retrieval, the data underwent a thorough cleaning process to ensure its quality and reliability. This process involved handling missing values, removing any duplicates, and ensuring consistency in the date formats. 

</div>
