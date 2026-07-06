import numpy as np
import pandas as pd
import yfinance as yf

# 1. Define the assets to analyze (e.g., Apple, Microsoft, Google, Amazon)
assets = ["AAPL", "MSFT", "GOOGL", "AMZN"]
print(f"Fetching historical data for: {assets}")

# 2. Pull 3 years of daily historical closing prices using Yahoo Finance API
data = yf.download(assets, start="2023-01-01", end="2026-01-01")["Adj Close"]

# 3. Calculate daily percentage returns
daily_returns = data.pct_change().dropna()

# 4. Calculate Annualized Mean Returns and the Covariance Matrix
# (Assuming 252 trading days in a year)
annual_returns = daily_returns.mean() * 252
covariance_matrix = daily_returns.cov() * 252

print("\n--- Annualized Expected Returns ---")
print(annual_returns)

# 5. Simulate a basic equally-weighted portfolio allocation (25% each)
weights = np.array([0.25, 0.25, 0.25, 0.25])

# Calculate expected portfolio return
portfolio_return = np.sum(annual_returns * weights)

# Calculate expected portfolio volatility (risk) using linear algebra matrix multiplication
portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(covariance_matrix, weights)))

# Assuming a risk-free rate of 4% (0.04), calculate the Sharpe Ratio
risk_free_rate = 0.04
sharpe_ratio = (portfolio_return - risk_free_rate) / portfolio_volatility

print("\n--- Equally Weighted Portfolio Baseline ---")
print(f"Expected Annual Return: {portfolio_return:.2%}")
print(f"Expected Volatility (Risk): {portfolio_volatility:.2%}")
print(f"Calculated Sharpe Ratio: {sharpe_ratio:.2f}")
