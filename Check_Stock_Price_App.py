import requests

def check_stock_price(symbol):
    url = f'https://api.polygon.io/v1/open-close/{symbol}/2023-02-09?adjusted=false&apiKey=nrvGL4xwuciY3nX_QsmbypmmM8U_Nbnj'
    r = requests.get(url)
    data = r.json()
    stock_price = data["close"]
    print(f"Closed price of {ticker} is {stock_price} USD")


ticker = input("Enter a valid stock symbol: ")
try:
    check_stock_price(ticker)
except:
    print("Enter a valid stock symbol!")
    ticker = input("Enter a valid stock symbol: ")
    check_stock_price(ticker)


