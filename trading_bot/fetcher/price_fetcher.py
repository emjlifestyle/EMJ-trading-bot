import requests

def fetch_price(symbol="bitcoin"):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd"
    try:
        response = requests.get(url)
        data = response.json()
        return data[symbol]["usd"]
    except Exception as e:
        print(f"Error fetching price: {e}")
        return None
