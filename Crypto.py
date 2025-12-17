import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

CSV_FILE = "crypto_top10.csv"

# CoinGecko API URL for top 10 coins by market cap
url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 10,
    "page": 1,
    "sparkline": "false"
}

# Fetch data
response = requests.get(url, params=params)
data = response.json()

# Parse data into DataFrame
coins = []
for coin in data:
    coins.append([
        coin['name'],
        coin['symbol'].upper(),
        coin['current_price'],
        coin['price_change_percentage_24h']
    ])

df = pd.DataFrame(coins, columns=["Name", "Symbol", "Price (USD)", "24h Change (%)"])

# Save to CSV
df.to_csv(CSV_FILE, index=False)
print(f"✅ Top 10 cryptocurrencies saved to '{CSV_FILE}'")
print(df)

# -----------------------------
# Plot: Top 10 coins by price
plt.figure(figsize=(10,6))
sns.barplot(x='Price (USD)', y='Name', data=df, palette="viridis")
plt.title("Top 10 Cryptocurrencies by Price (USD)")
plt.xlabel("Price (USD)")
plt.ylabel("Coin")
plt.tight_layout()
plt.show()

# Plot: 24h % change
plt.figure(figsize=(10,6))
sns.barplot(x='24h Change (%)', y='Name', data=df, palette="magma")
plt.title("Top 10 Cryptocurrencies: 24h % Change")
plt.xlabel("24h Change (%)")
plt.ylabel("Coin")
plt.tight_layout()
plt.show()
