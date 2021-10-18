# :chart_with_upwards_trend: Value at Risk - Variance Covariance Method.
In this project, we are going to calculate value at risk with variance-covariance method using Python.

## :file_folder: Folders
| Folder Name                             | Description    |
|-----------------------------------------|----------------|
| [Images](https://github.com/radianlukman/Value-at-Risk-Variance-Covariance/tree/main/Images)  | Images for README.md and Notebook |

## :card_index: Files

| File   Name                             | Description    |
|-----------------------------------------|----------------|
| [Value_at_Risk_Variance_Covariance_Method.ipynb](https://github.com/radianlukman/Value-at-Risk-Variance-Covariance/blob/main/Value_at_Risk_Variance_Covariance_Method.ipynb)  | Full Project (Python Notebook) |
| [Value at Risk - Variance Covariance Method.py](https://github.com/radianlukman/Value-at-Risk-Variance-Covariance/blob/main/Value%20at%20Risk%20-%20Variance%20Covariance%20Method.py)  | Python Script |

## :hammer_and_wrench: Project Details

![](https://github.com/radianlukman/Value-at-Risk-Variance-Covariance/blob/main/Images/Saham%20Properti.jpg)

Here, we will measure the VaR value of the property and real estate companies included in the LQ45 Index. There are four property and real estate companies in the LQ45 Index, they are: Alam Sutera Reality, Sentul City, Bumi Serpong Damai, and Lippo Karawaci. The portfolio to be formed contains the four companies with a weight of 25% each. I will use Python for this case and use steps from the video by a YouTube channel: [Financial Programming with Ritvik](https://www.youtube.com/watch?v=hdEp8A90RdM) and sources from the [Quantinsti](https://blog.quantinsti.com/calculating-covariance-matrix-portfolio-variance/) blog.

You can view the full project (steps) [here](https://github.com/radianlukman/Value-at-Risk-Variance-Covariance/blob/main/Value_at_Risk_Variance_Covariance_Method.ipynb).

## :pushpin: Conclusion
The portfolio contains four companies of the property and real estate sector (ASRI, BKSL, BSDE, and LPKR) with a weight of 25% each. Here, the Value at Risk value is calculated using the variance-covariance method. The daily VaR for this portfolio is 4.039%. This means that if the initial fund invested in the portfolio is 10,000 dollars, then there is a 95% confidence that the loss to be received by the investor will not exceed 403.9 dollars. The VaR value for 30 days is 22.121%, so the loss that investors will receive will not exceed 2,212.1 dollars if they invest 10,000 dollars in the portfolio for 30 days.
