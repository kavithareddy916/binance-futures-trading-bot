from binance.client import Client
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

client = Client(API_KEY, API_SECRET)
client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

def get_client():
    return client


def get_account_balance():
    balances = client.futures_account_balance()
    return balances

def get_market_price(symbol):
    ticker = client.futures_symbol_ticker(symbol=symbol)
    return float(ticker["price"])