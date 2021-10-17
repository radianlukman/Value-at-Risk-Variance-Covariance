# Install yfinance
!pip install yfinance

# Import Packages
import yfinance as yf
import numpy as np, datetime as dt
import matplotlib.pyplot as plt
from scipy.stats import norm

# Membuat Portofolio
stocks = ['ASRI.JK','BKSL.JK','BSDE.JK','LPKR.JK']
weights = np.array([0.25,0.25,0.25,0.25])

# Mengunduh Data Harga Saham Harian
mulai = dt.datetime(2020,1,1)
akhir = dt.datetime.now()
yf.download('ASRI.JK',mulai,akhir)
data = yf.download(stocks, mulai, akhir)['Adj Close']
print(data)

# Menghitung Nilai return
returns = data.pct_change()
print(returns)

# Membuat Matriks Varians-Kovarians
cov_matrix = returns.cov()
print(cov_matrix)

# Menghitung Expected Return Portofolio
avg_returns = returns.mean()
print(avg_returns)

port_mean = avg_returns @ weights
print("Expected Return Portofolio Harian Sebesar = {}".format(port_mean))

# Menghitung Varians dan Standar Deviasi Portofolio
port_var = weights.T @ cov_matrix @ weights
print("Expected Variance Portofolio Sebesar = {}".format(port_var))

port_std = np.sqrt(port_var)
print("Standar Deviasi / Volatilitas Portofolio Sebesar = {}".format(port_std))

# Membuat Kurva Distribusi Normal Portofolio
dist = np.arange(-0.05, 0.05, 0.001)
norm_dist = norm.pdf(dist, port_mean, port_std)
plt.plot(dist, norm_dist, color = 'b')
plt.title('Distribusi Normal Portofolio')
plt.show()

# Nilai Value at Risk Harian
significance_level = 0.05
VaR = norm.ppf(significance_level, port_mean, port_std)
print("Value at Risk Portofolio Harian Sebesar = {}".format(VaR))

# Nilai Value at Risk dalam n-hari
jumlah_hari = 30
VaR_30 = VaR * np.sqrt(jumlah_hari)
print("Value at Risk Portofolio Selama 30 hari Sebesar = {}".format(VaR_30))