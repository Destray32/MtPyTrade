# this file will be responsible for importing other classes and libraries that will be essantial for the program to run
import MetaTrader5 as mt5
from trader import Trader
from strategy import Strategy
from strategies.MACD import MACD


def main():
    # connect to MetaTrader 5
    if not mt5.initialize():
        print("initialize() failed, error code =", mt5.last_error())
        quit()
    
    # create strategy
    strategy = Strategy("long")
    strategy.set_algorithm(MACD(12, 26, 9))

    # create trader
    trader = Trader("EURUSD.pro", 0.01, 100, 100, strategy)
    trader.run()

if __name__ == "__main__":
    main()