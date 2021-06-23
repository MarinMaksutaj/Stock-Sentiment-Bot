import pandas as pd
import matplotlib.pyplot as plt
import stock_data_collector


def graph_stock(symbol, period, interval):
    print(stock_data_collector.get_stock_data(symbol, period, interval))
    df = stock_data_collector.get_stock_data(symbol, period, interval)
    df['Open'].plot()
    plt.figure(figsize=(10, 10))
    plt.plot(df.index, df['Open'])
    plt.xlabel("date")
    plt.ylabel("$ price")
    plt.title(symbol + " Stock Price")
    plt.draw()
    plt.savefig(fname='plot', dpi=100)
    plt.close()


