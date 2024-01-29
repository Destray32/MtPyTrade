import numpy
import MetaTrader5 as mt5

from strategy import Algorithm

class MACD(Algorithm):
    # class for MACD algorithm

    def __init__(self, fast_period, slow_period, signal_period):
        self.fast_period = fast_period
        self.slow_period = slow_period
        self.signal_period = signal_period


    def get_signal(self, symbol):
        # get MACD data
        macd = mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_D1, 0, 250)
        # calculate MACD
        macd = numpy.array(macd)
        macd = macd['close']
        macd = numpy.mean(macd)
        # get MACD signal data
        macd_signal = mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_D1, 0, 250)
        # calculate MACD signal
        macd_signal = numpy.array(macd_signal)
        macd_signal = macd_signal['close']
        macd_signal = numpy.mean(macd_signal)
        # compare MACD and MACD signal
        if macd > macd_signal:
            return True
        else:
            return False