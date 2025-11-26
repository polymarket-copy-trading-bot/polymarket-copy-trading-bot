import requests
import pandas as pd
import os

POLY_API = os.getenv("POLYMARKET_API", "https://api.polymarket.com")

def get_markets(limit=10):
    """Fetch active markets from Polymarket"""
    url = f"{POLY_API}/markets?limit={limit}"
    resp = requests.get(url)
    data = resp.json()
    markets = pd.DataFrame(data)
    return markets[["question", "outcomePrices", "endDate"]]
