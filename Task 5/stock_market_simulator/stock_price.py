import random

# Stock market with initial prices
stocks = {"AAPL": 150, "TSLA": 700, "GOOGL": 2800, "AMZN": 3500}
portfolio = {}
balance = 10000  # User's starting balance

def update_prices():
    """Randomly update stock prices within a range."""
    for stock in stocks:
        stocks[stock] += random.randint(-10, 10)  # Prices fluctuate randomly

def buy_stock(stock, quantity):
    global balance
    if stock in stocks:
        cost = stocks[stock] * quantity
        if cost <= balance:
            balance -= cost
            portfolio[stock] = portfolio.get(stock, 0) + quantity
            print(f"Bought {quantity} shares of {stock}.")
        else:
            print("Insufficient balance!")
    else:
        print("Stock not found!")

def sell_stock(stock, quantity):
    global balance
    if stock in portfolio and portfolio[stock] >= quantity:
        balance += stocks[stock] * quantity
        portfolio[stock] -= quantity
        if portfolio[stock] == 0:
            del portfolio[stock]
        print(f"Sold {quantity} shares of {stock}.")
    else:
        print("Not enough shares to sell!")

def show_portfolio():
    print("\nYour Portfolio:")
    for stock, qty in portfolio.items():
        print(f"{stock}: {qty} shares @ {stocks[stock]} each")
    print(f"Balance: ${balance}\n")

# Simulation loop
while True:
    update_prices()
    print("\nStock Prices:", stocks)
    action = input("Enter action (buy/sell/show/exit): ").lower()

    if action == "buy":
        stock = input("Enter stock symbol: ").upper()
        qty = int(input("Enter quantity: "))
        buy_stock(stock, qty)
    elif action == "sell":
        stock = input("Enter stock symbol: ").upper()
        qty = int(input("Enter quantity: "))
        sell_stock(stock, qty)
    elif action == "show":
        show_portfolio()
    elif action == "exit":
        break
    else:
        print("Invalid action! Try again.")
