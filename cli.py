from bot.orders import place_market_order, place_limit_order
from bot.client import get_market_price, get_account_balance
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)
from bot.logging_config import logger


def main():
    print("=" * 50)
    print("      Binance Futures Trading Bot")
    print("=" * 50)

    symbol = validate_symbol(input("Enter Symbol (e.g. BTCUSDT): "))

    current_price = get_market_price(symbol)
    print(f"\nCurrent Market Price: ${current_price}")

    print("\nAccount Balance:")
    balances = get_account_balance()

    for balance in balances:
        if balance["asset"] == "USDT":
            print(f"USDT Balance : {balance['balance']}")
            print(f"Available    : {balance['availableBalance']}")
            break

    side = validate_side(input("Enter Side (BUY/SELL): "))
    order_type = validate_order_type(input("Enter Order Type (MARKET/LIMIT): "))
    quantity = validate_quantity(input("Enter Quantity: "))

    if order_type == "MARKET":
        result = place_market_order(symbol, side, quantity)
    else:
        price = validate_price(input("Enter Price: "))
        result = place_limit_order(symbol, side, quantity, price)

    logger.info(result)

    print("\n========== ORDER SUMMARY ==========")

    if "error" in result:
        print("Status      : Failed")
        print("Error       :", result["error"])
    else:
        print("Order ID    :", result.get("orderId"))
        print("Symbol      :", result.get("symbol"))
        print("Side        :", result.get("side"))
        print("Type        :", result.get("type"))
        print("Status      :", result.get("status"))
        print("Quantity    :", result.get("origQty"))
        print("Executed Qty:", result.get("executedQty"))
        print("Price       :", result.get("price"))

    print("===================================")


if __name__ == "__main__":
    main()