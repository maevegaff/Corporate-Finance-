import pandas as pd
import numpy as np

# Load the Excel file
file_path = r"C:\Users\maeve\Downloads\EA1 5 year financials (1).xlsx"
df = pd.read_excel(file_path, sheet_name="Volatility")

#  Define initial project value V0
V0 = 33298.32   # EA3 initial project value

# Extract simulated terminal project values
VT = df["EA3 Value"].dropna()

# Remove non-positive values (BS requires lognormality)
VT = VT[VT > 0]

# Compute log returns
log_returns = np.log(VT / V0)

# Compute volatility
T = 1  # time horizon in years
sigma = log_returns.std(ddof=1) / np.sqrt(T)

#  Output
print(f"Black–Scholes volatility (σ): {sigma:.3f}")
print(f"Volatility (%): {sigma * 100:.1f}%")
