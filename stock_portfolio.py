stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

portfolio = {}
total_investment = 0

print("===== Stock Portfolio Tracker =====")
print("Available Stocks:")

for stock, price in stock_prices.items():
    print(f"{stock} : ${price}")

while True:
    stock_name = input("\nEnter Stock Name (or type 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Stock not available!")
        continue

    quantity = int(input(f"Enter quantity of {stock_name}: "))

    portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity
print("\n------ Portfolio Summary ------")

report = "Stock Portfolio Report\n"
report += "=========================\n"

for stock, quantity in portfolio.items():
    investment = stock_prices[stock] * quantity
    total_investment += investment

    print(f"{stock} - {quantity} shares = ${investment}")

    report += f"{stock} - {quantity} shares = ${investment}\n"

print("-------------------------------")
print(f"Total Investment = ${total_investment}")

report += "-------------------------\n"
report += f"Total Investment = ${total_investment}"

with open("investment_report.txt", "w") as file:
    file.write(report)
