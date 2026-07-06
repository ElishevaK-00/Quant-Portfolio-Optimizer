# Quant-Portfolio-Optimizer
Python-based script utilizing data analytics to maximize the Sharpe Ratio and optimize equity asset allocation.
# Quantitative Portfolio Optimization & Risk Analysis

## Project Overview
This repository contains a quantitative financial analytics script designed to evaluate the historical performance, volatility, and risk-adjusted returns of a multi-asset equity portfolio. Using historical market data pulled via API, the model utilizes matrix calculus and statistical analysis to calculate foundational modern portfolio theory metrics.

## Methodology
- **Data Sourcing:** Extracts historical adjusted close pricing via Yahoo Finance API (`yfinance`).
- **Statistical Aggregation:** Computes annualized logarithmic asset returns and creates an annualized variance-covariance matrix.
- **Risk Assessment:** Implements matrix multiplication ($w^T \Sigma w$) to compute overall portfolio volatility and determines the overall **Sharpe Ratio** against a fixed risk-free benchmark.

## Core Technical Skills Displayed
- Quantitative Programming (Python, Pandas, NumPy)
- Modern Portfolio Theory & Statistical Modelling
- Linear Algebra Application in Finance
