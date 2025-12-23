import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# === Load Excel File ===
# Replace 'data.xlsx' with your actual file name
df = pd.read_excel(R"C:\Users\maeve\Downloads\EA1RevenueProb.xlsx")

# Ensure the columns exist
df.columns = df.columns.str.strip().str.lower()
if 'year' not in df.columns or 'revenue' not in df.columns:
    raise ValueError("Excel file must have 'Year' and 'Revenue' columns. Please check the column names for typos or formatting issues.")

# Extract the revenue data
revenues = df['revenue'].dropna()

# === Fit a Normal Distribution ===
mean, std = norm.fit(revenues)

# Create a range of values for the probability curve
x = np.linspace(min(revenues), max(revenues), 1000)
pdf = norm.pdf(x, mean, std)
# === Summary Statistics ===
percentiles = np.percentile(revenues, [25, 50, 75])

print("Summary Statistics:")
print(f"Mean (μ): {mean:.2f}")
print(f"Standard Deviation (σ): {std:.2f}")
print(f"Minimum Revenue: {min(revenues):.2f}")
print(f"Maximum Revenue: {max(revenues):.2f}")
print(f"Range: {max(revenues) - min(revenues):.2f}")
print(f"25th Percentile: {percentiles[0]:.2f}")
print(f"50th Percentile (Median): {percentiles[1]:.2f}")
print(f"75th Percentile: {percentiles[2]:.2f}")

# === Plot ===
plt.figure(figsize=(10, 6))
plt.hist(revenues, bins=15, density=True, alpha=0.6, color='skyblue', edgecolor='black')
plt.plot(x, pdf, 'r-', linewidth=2, label=f'Normal PDF\nμ={mean:.2f}, σ={std:.2f}')
plt.title('Probability Distribution of Revenue')
plt.xlabel('Revenue')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
