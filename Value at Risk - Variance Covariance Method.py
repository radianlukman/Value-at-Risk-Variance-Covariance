# Install yfinance Package
!pip install yfinance

# Import Packages
import yfinance as yf
import numpy as np, datetime as dt
import matplotlib.pyplot as plt
from scipy.stats import norm

# Make Stock Portfolio
stocks = ['ASRI.JK','BKSL.JK','BSDE.JK','LPKR.JK']
weights = np.array([0.25,0.25,0.25,0.25])

# Download Daily Stock Price
start = dt.datetime(2020,1,1)
end = dt.datetime.now()

yf.download('ASRI.JK',start,end)

data = yf.download(stocks, start, end)['Adj Close']
print(data)

# Calculate Stock Returns
returns = data.pct_change()
print(returns)

# Make Variance-Covariance Matrix
cov_matrix = returns.cov()
print(cov_matrix)

# Calculate Portfolio Expected Return
avg_returns = returns.mean()
print(avg_returns)

port_mean = avg_returns @ weights
print("Daily Expected Return of the Portfolio = {}".format(port_mean))

# Calculate Portfolio Variance and Standard Deviation
port_var = weights.T @ cov_matrix @ weights
print("Portfolio's Expected Variance = {}".format(port_var))

port_std = np.sqrt(port_var)
print("Portfolio's Standard Deviation / Volatility = {}".format(port_std))

# Make Normal Distributin Curve of the Portfolio
dist = np.arange(-0.05, 0.05, 0.001)
norm_dist = norm.pdf(dist, port_mean, port_std)
plt.plot(dist, norm_dist, color = 'b')
plt.title('Portfolio Normal Distribution')
plt.show()

# Daily Value at Risk
significance_level = 0.05
VaR = norm.ppf(significance_level, port_mean, port_std)
print("Daily Value at Risk of the Portfolio = {}".format(VaR))

# Value at Risk in n-days
number_days = 30
VaR_30 = VaR * np.sqrt(number_days)
print("Value at Risk for 30 days of the Portfolio = {}".format(VaR_30))