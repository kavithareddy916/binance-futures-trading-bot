from bot.client import get_client

client = get_client()

try:
    account = client.futures_account()
    print("✅ Connected successfully!")
    print("Account connection successful.")
except Exception as e:
    print("❌ Connection failed")
    print(e)