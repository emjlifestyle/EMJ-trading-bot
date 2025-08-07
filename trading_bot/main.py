from fetcher.price_fetcher import fetch_price
from analyzer.indicator_calculator import calculate_rsi, calculate_sma
from logger.decision_logger import log_decision

# Simulated price history (15 days)
prices = [100, 102, 101, 103, 105, 107, 106, 108, 110, 109, 111, 113, 115, 114, 116]

symbol = "bitcoin"
price = fetch_price(symbol)
prices.append(price)

sma = calculate_sma(prices)
rsi = calculate_rsi(prices)

# Simple decision logic
if rsi and rsi < 30:
    decision = "BUY"
elif rsi and rsi > 70:
    decision = "SELL"
else:
    decision = "HOLD"

print(f"Price: ${price}")
print(f"SMA: {sma}")
print(f"RSI: {rsi}")
print(f"Decision: {decision}")

# Log to CSV
log_decision(symbol, price, rsi, sma, decision)
from analyzer.indicator_calculator import calculate_rsi, calculate_sma

# Simulated price history (15 days)
prices = [100, 102, 101, 103, 105, 107, 106, 108, 110, 109, 111, 113, 115, 114, 116]

sma = calculate_sma(prices)
rsi = calculate_rsi(prices)

print(f"Sample SMA: {sma}")
print(f"Sample RSI: {rsi}")
from fetcher.price_fetcher import fetch_price

price = fetch_price("bitcoin")
print(f"Bitcoin price: ${price}")
