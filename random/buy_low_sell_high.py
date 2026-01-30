import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Config
TICKER = "GOOG"
START_DATE = "2014-01-01"
END_DATE = "2018-01-01"
INITIAL_CAPITAL = 1000.0

# Fetch data
goog_data = yf.download(TICKER, start=START_DATE, end=END_DATE, progress=False)
if isinstance(goog_data.columns, pd.MultiIndex):
    goog_data.columns = goog_data.columns.get_level_values(0)

# Build signals: 1 when price goes up, 0 when down
goog_data_signal = pd.DataFrame(index=goog_data.index)
goog_data_signal["price"] = goog_data["Close"]
goog_data_signal["daily_difference"] = goog_data_signal["price"].diff()
goog_data_signal["signal"] = np.where(goog_data_signal["daily_difference"] > 0, 1, 0)
goog_data_signal["position"] = goog_data_signal["signal"].diff()

# Plot price with buy/sell markers
fig, ax = plt.subplots(figsize=(10, 5))
ax.set_ylabel(f"{TICKER} price ($)")
ax.plot(goog_data_signal["price"], color="r", linewidth=2)

buys = goog_data_signal[goog_data_signal["position"] == 1.0]
sells = goog_data_signal[goog_data_signal["position"] == -1.0]
ax.plot(buys.index, buys["price"], "^", markersize=5, color="m")
ax.plot(sells.index, sells["price"], "v", markersize=5, color="k")

# Portfolio simulation
positions = pd.DataFrame(index=goog_data_signal.index, columns=["GOOG"]).fillna(0.0)
portfolio = pd.DataFrame(index=goog_data_signal.index).fillna(0.0)

positions["GOOG"] = goog_data_signal["signal"]
portfolio["position"] = positions["GOOG"] * goog_data_signal["price"]
portfolio["cash"] = INITIAL_CAPITAL - (
    positions["GOOG"].diff() * goog_data_signal["price"]
).cumsum()
portfolio["total"] = portfolio["position"] + portfolio["cash"]

portfolio.plot()
plt.tight_layout()
plt.show()
