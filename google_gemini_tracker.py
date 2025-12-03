import yfinance as yf
import matplotlib.pyplot as plt
#1. Define the Ticker and the Timeframe
ticker = "GOOGL"
start_date = "2025-10-01" #Pre-launch hype
end_date = "2025-12-03" #Today (Post-launch)
#2. Download the Data
print(f "Downloading {ticker} data from {start_date} to {end_date}...")
data = yf.download(ticker, start = start_date, end = end_date)
#3. Check the "Launch Day" Price
launch_day = "2025-11-18"
#Check if we have data for that specific day (markets are closed weekends)
if launch_day in data.index:price = data.loc[launch_day]
  ["Close"]
  print(f"Closing Price on Launch day ({launch_day}): ${price:2f}")
else:
  print(f"Launch day {launch_day} might be a weekend/holiday. Checking next trading day...")
  #4. Create the Chart
  plt.figure(figsize=(10,5))
  plt.plot(data["Close"], label="Google Stock Price", color="blue", marker='0')
  #Add a vertical line for the Launch Day
  plt.axvline(x=data.index.get_loc(launch_day) if launch_day in data.index else 0, color='red', linestyle='--', label=f"Gemini 3 Launch ({launch_day})")
  plt.title(f"The 'Gemini 3' Spike:Google Stock (Nov-Dec 2025)")
  plt.xlabel("Date")
  plt.ylabel("Price($)")
  plt.legend ()
  plt.grid(True)
  plt.show()
