import MetaTrader5 as mt5
import numpy as numpy
from abc import ABC, abstractmethod

class Strategy:
    
    def __init__(self, direction):
        self.direction = direction
        self.algorithm = None

    def set_algorithm(self, algorithm):
        self.algorithm = algorithm

    def get_signal(self, symbol):
        if self.algorithm is not None:
            return self.algorithm.get_signal(symbol)
        else:
            # algorithm is not set
            return False
        
    
class Algorithm(ABC):
    # base class for all algorithms

    @abstractmethod
    def get_signal(self, symbol):
        pass
