import csv
from datetime import datetime

def log_decision(symbol, price, rsi, sma, decision, filename="trade_log.csv"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    row = [timestamp, symbol, price, rsi, sma, decision]

    try:
        with open(filename, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(row)
        print(f"Logged decision: {row}")
    except Exception as e:
        print(f"Error logging decision: {e}")
