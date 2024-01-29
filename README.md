# Python Trading Bot

This project is a Python script that connects to MetaTrader5 and allows trading with a specified strategy. The script uses object-oriented programming to create an instance that has the strategy passed to it. The script can use different indicators and models to generate signals, such as MACD, Hawkes Process, RSI, etc.

## Installation

To run this script, you need to have Python 3.7 or higher installed on your machine. You also need to install the following packages:

- MetaTrader5: `pip install MetaTrader5`
- numpy: `pip install numpy`

## Usage

To use this script, you need to have a MetaTrader5 account and a trading strategy. You can modify the parameters of the strategy in the `main.py` file, such as the indicator, period, threshold, direction, symbol, lot, stop loss, take profit, etc. You can also change the algorithm used by the strategy in the `strategy.py` file, by creating a new class that inherits from the `Algorithm` class and implementing the `get_signal` method. You can then pass an object of that class to the `set_algorithm` method of the `Strategy` class.

To run the script, simply execute the `main.py` file:

`python main.py`

The script will connect to MetaTrader5 and start trading according to the strategy. It will print the details of the trades on the console.
