import MetaTrader5 as mt5
from time import sleep

class Trader:
    def __init__(self, symbol, lot, stop_loss, take_profit, strategy):
        self.symbol = symbol
        self.lot = lot
        self.stop_loss = stop_loss
        self.take_profit = take_profit
        self.strategy = strategy
        self.position = None

    def open_position(self, direction):
        # open a buy or sell position
        point = mt5.symbol_info(self.symbol).point
        # get the current price
        price = mt5.symbol_info_tick(self.symbol).ask if direction == mt5.ORDER_TYPE_BUY else mt5.symbol_info_tick(self.symbol).bid

        if direction == "buy":
            sl = price - self.stop_loss * point
            tp = price + self.take_profit * point

        elif direction == "sell":
            sl = price + self.stop_loss * point
            tp = price - self.take_profit * point
        else:
            print("Invalid direction")
            return False
        
        # prepare the buy request structure
        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": self.symbol,
            "volume": self.lot,
            "type": mt5.ORDER_TYPE_BUY if direction == "buy" else mt5.ORDER_TYPE_SELL,
            "price": price,
            "sl": sl,
            "tp": tp,
            "magic": 234000,
            "comment": "python script open",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_FOK,
        }

        # send a trading request
        result = mt5.order_send(request)
        if result.retcode == mt5.TRADE_RETCODE_DONE:
            #trade successfully executed
            print(f"Opened {direction} position for {self.symbol} at {price}")
            return True
        else:
            #trade execution failed
            print(f"Failed to open {direction} position for {self.symbol} at {price}: {result.comment}")
            print(f"Error code: {result.retcode}")
            return False
        
    def close_position(self):
        # close current position
        if self.position is None:
            # no position to close
            return False
        # getting the current position details
        position = mt5.positions_get(symbol=self.symbol)[0]
        # prepare the close order request structure
        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": self.symbol,
            "volume": position.volume,
            "type": mt5.ORDER_TYPE_SELL if position.type == mt5.ORDER_TYPE_BUY else mt5.ORDER_TYPE_BUY,
            "position": position.ticket,
            "price": position.price_current,
            "magic": 234000, # magic number
            "comment": "Python script trade", # comment
            "type_time": mt5.ORDER_TIME_GTC, # good till canceled
            "type_filling": mt5.ORDER_FILLING_FOK, # return order if not filled
        }
        # send the trade request
        result = mt5.order_send(request)
        if result.retcode == mt5.TRADE_RETCODE_DONE:
            # trade successful
            print(f"Closed position of {position.volume} {self.symbol} at {position.price_current}")
            self.position = None # clear the order number
            return True
        else:
            # trade failed
            print(f"Failed to close position of {position.volume} {self.symbol} at {position.price_current}")
            print(f"Error code: {result.retcode}")
            return False

    def check_signal(self):
        # check the signal from the strategy object
        return self.strategy.get_signal(self.symbol)

    def run(self):
        # run the main loop
        while True:
            # check the signal
            signal = self.check_signal()
            if signal:
                # signal is True, open a position in the direction of the strategy
                self.open_position(self.strategy.direction)
            else:
                # signal is False, close the current position if any
                self.close_position()
            # wait for some time
            sleep(1000)