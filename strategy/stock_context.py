from config import *
from strategy.stock_state import *


class StockContext:
    def __init__(self):
        self.__state = NothingState()
        self.__stock_price = 0
        self.__profit = 0

    def action(self, today_price, tmr_price, atmr_price):
        return self.__state.action(self, today_price, tmr_price, atmr_price)

    @property
    def state(self):
        return self.__state.state

    @state.setter
    def state(self, nstate):
        self.__state = nstate

    @property
    def stock_price(self):
        return self.__stock_price

    @stock_price.setter
    def stock_price(self, nstock_price):
        self.__stock_price = nstock_price
