import yfinance as yf


def get_stock_data(symbol, p, i):
    stock = yf.Ticker(symbol)
    return stock.history(period=p, interval=i)



