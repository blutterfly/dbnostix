# Strangle Strategy

## What is

A Strangle is an options trading strategy that involves buying or selling both a call option and a put option with the same expiration date but different strike prices. It is used to take advantage of expected volatility in the underlying asset.

### Option Strangle Strategy

### Types of Strangle Strategies

1. Long Strangle (Buying a Strangle)
   - Buy an out-of-the-money (OTM) call option.
   - Buy an out-of-the-money (OTM) put option.
   - Used when a trader expects high volatility but is unsure of the direction.

2. Short Strangle (Selling a Strangle)
   - Sell an out-of-the-money (OTM) call option.
   - Sell an out-of-the-money (OTM) put option.
   - Used when a trader expects low volatility and wants to collect premium.

---

### Long Strangle Strategy

- Objective: Profit from a significant price move in either direction.
- Max Loss: Limited to the total premium paid.
- Max Profit: Unlimited (if the stock moves significantly beyond the strike prices).
- Breakeven Points:
  - Upper BEP = Call strike price + Premium paid.
  - Lower BEP = Put strike price - Premium paid.

✅ Best for: Volatile markets, earnings reports, major news events.

🔴 Risk: If the stock remains within the strike prices, the options expire worthless.

---

### Short Strangle Strategy

- Objective: Profit from low volatility and time decay.
- Max Profit: Limited to the premium collected.
- Max Loss: Potentially unlimited if the stock moves sharply.
- Breakeven Points:
  - Upper BEP = Call strike price + Premium received.
  - Lower BEP = Put strike price - Premium received.

✅ Best for: Stable or low-volatility markets.

🔴 Risk: Large losses if the stock price moves sharply in either direction.

---

### Example of a Long Strangle

Stock: XYZ trading at $100  

- Buy 110 Call at $2.00
- Buy 90 Put at $2.00  
- Total Cost: $4.00

Breakeven Points:

- Upper BEP = $110 + $4 = $114
- Lower BEP = $90 - $4 = $86

Profit Scenarios:

- If stock moves above $114, the call option gains value.
- If stock moves below $86, the put option gains value.
- If stock stays between $90 and $110, both options expire worthless, and you lose the $4 premium.

---

### Example of a Short Strangle

Stock: XYZ trading at $100  

- Sell 110 Call for $2.00
- Sell 90 Put for $2.00  
- Total Premium Collected: $4.00

Breakeven Points:

- Upper BEP = $110 + $4 = $114
- Lower BEP = $90 - $4 = $86

Profit Scenarios:

- If stock stays between $90 and $110, both options expire worthless, and you keep the premium.
- If stock moves above $114 or below $86, you face unlimited risk.

---

### Key Takeaways

✔️ Long Strangle: Limited risk, unlimited profit potential, best for high volatility.  
✔️ Short Strangle: Limited profit, unlimited risk, best for low volatility.  
✔️ Breakeven Points: Critical to manage risk and set exit points.  
✔️ Implied Volatility (IV): Higher IV makes long strangles more expensive, while lower IV makes short strangles more profitable.  

## Script to backtest this strategy 🚀

~~~python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# Define parameters for the strangle strategy
ticker = "AAPL"
start_date = "2023-01-01"
end_date = "2024-01-01"
strike_diff = 5  # Difference from ATM for Call and Put
premium_paid = 4  # Estimated cost of buying both options
premium_received = 4  # Estimated premium collected for short strangle

# Fetch historical stock data
data = yf.download(ticker, start=start_date, end=end_date)
data["MidPrice"] = (data["High"] + data["Low"]) / 2

# Define breakeven points
data["Upper_BEP_Long"] = data["MidPrice"] + strike_diff + premium_paid
data["Lower_BEP_Long"] = data["MidPrice"] - strike_diff - premium_paid
data["Upper_BEP_Short"] = data["MidPrice"] + strike_diff + premium_received
data["Lower_BEP_Short"] = data["MidPrice"] - strike_diff - premium_received

# Calculate long strangle profit/loss
data["Long_Strangle_PL"] = np.where(
    (data["MidPrice"] > data["Upper_BEP_Long"]) | (data["MidPrice"] < data["Lower_BEP_Long"]),
    abs(data["MidPrice"] - data["Upper_BEP_Long"]) - premium_paid,
    -premium_paid
)

# Calculate short strangle profit/loss
data["Short_Strangle_PL"] = np.where(
    (data["MidPrice"] > data["Upper_BEP_Short"]) | (data["MidPrice"] < data["Lower_BEP_Short"]),
    -abs(data["MidPrice"] - data["Upper_BEP_Short"]) + premium_received,
    premium_received
)


# Display first few rows using pprint
pprint(data[["MidPrice", "Long_Strangle_PL", "Short_Strangle_PL"]].head())

~~~
