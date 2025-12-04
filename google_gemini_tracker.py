import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 1. SETUP
ticker = "GOOGL"
launch_day = "2025-11-18"
data = yf.download(ticker, start="2025-10-01", end="2025-12-05")

if isinstance(data.columns, pd.MultiIndex):
    data.columns = data.columns.droplevel(1)
data.index = pd.to_datetime(data.index)

# 2. SELECT SPECIFIC DATES
wanted_dates = [
    "2025-10-01", "2025-10-20", 
    "2025-11-05", "2025-11-18", "2025-11-28", 
    "2025-12-01"
]
subset = data[data.index.isin(wanted_dates)]

# 3. PREPARE COLORS & DATA
x_positions = np.arange(len(subset))
prices = subset["Close"]
dates = [d.strftime('%Y-%m-%d') for d in subset.index]

# Google Brand Colors (Blue, Red, Yellow, Green)
google_colors = ['#4285F4', '#EA4335', '#FBBC04', '#34A853']
# Create a list of colors for our 6 bars by repeating the pattern
bar_colors = [google_colors[i % 4] for i in range(len(subset))]

# 4. PLOT
plt.figure(figsize=(11, 6))

# Plot the bars with Google colors
bars = plt.bar(x_positions, prices, color=bar_colors, width=0.6)

# 5. ADD LABELS
# Find the launch day index
try:
    launch_idx = list(subset.index).index(pd.Timestamp(launch_day))
    
    # Add the "Gemini Launch Day" text ON the bar
    # We place it slightly inside the top of the bar, rotated
    plt.text(launch_idx, prices.iloc[launch_idx] - 10, "Gemini Launch Day", 
             rotation=90, color='white', ha='center', va='top', fontweight='bold', fontsize=12)
except ValueError:
    pass

# Standard polish
plt.xticks(x_positions, dates, rotation=15)
plt.title(f"Gemini Impact: Google Price Levels ({ticker})", fontsize=14)
plt.ylabel("Stock Price ($)")

# Zoom y-axis to make bars look good
plt.ylim(prices.min() * 0.9, prices.max() * 1.05)

# Add price numbers on top of bars
for x, price in zip(x_positions, prices):
    plt.text(x, price + 2, f"${price:.0f}", ha='center', fontsize=10, fontweight='bold', color='black')

plt.grid(True, axis='y', alpha=0.3)
plt.tight_layout()
plt.show()
