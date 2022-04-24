import abc

from config import *


class StockState(abc.ABC):
    def action(self, context, tdy_stock, tmr_stock, atmr_stock):
        # tdy_stock:    today stock price
        # tmr_stock:    tomorrow stock price
        # atmr_stock:   the day after tomorrow stock price
        cur_stock = tdy_stock if context.state == Constant.State.Nothing else context.stock_price
        cond_list = [
            cur_stock < tmr_stock < atmr_stock,
            cur_stock < atmr_stock < tmr_stock,
            atmr_stock < cur_stock < tmr_stock,
            atmr_stock < tmr_stock < cur_stock,
            tmr_stock < atmr_stock < cur_stock,
            tmr_stock < cur_stock < atmr_stock
        ]
        return self._state_action(context, cond_list)

    def _do_strategy(self, context, cond_list, action_list):
        if len(cond_list) != len(action_list):
            raise Exception('Condition list must as long as Action list.')

        for cond, action in zip(cond_list, action_list):
            if cond:
                if isinstance(self, NothingState):
                    if action == Constant.Action.Buy:
                        context.state = HoldState()
                    elif action == Constant.Action.Sell:
                        context.state = ShortState()
                elif isinstance(self, ShortState):
                    if action == Constant.Action.Buy:
                        context.state = NothingState()
                elif isinstance(self, HoldState):
                    if action == Constant.Action.Sell:
                        context.state = NothingState()
                return action
        return Constant.Action.NoAction

    @abc.abstractmethod
    def _state_action(self, context, cond_list):
        return NotImplemented

    @abc.abstractmethod
    def __repr__(self):
        return NotImplemented

    @property
    @abc.abstractmethod
    def state(self):
        return NotImplemented


class NothingState(StockState):
    def _state_action(self, context, cond_list):
        action_list = [
            Constant.Action.Buy,
            Constant.Action.Sell,
            Constant.Action.Sell,
            Constant.Action.Sell,
            Constant.Action.Buy,
            Constant.Action.Buy,
        ]
        # action_list = [
        #     Constant.Action.Buy,
        #     Constant.Action.Buy,
        #     Constant.Action.Buy,
        #     Constant.Action.Sell,
        #     Constant.Action.Sell,
        #     Constant.Action.Sell,
        # ]
        return self._do_strategy(context, cond_list, action_list)

    def __repr__(self):
        return 'Nothing'

    @property
    def state(self):
        return Constant.State.Nothing


class HoldState(StockState):
    def _state_action(self, context, cond_list):
        action_list = [
            Constant.Action.NoAction,
            Constant.Action.Sell,
            Constant.Action.Sell,
            Constant.Action.NoAction,
            Constant.Action.NoAction,
            Constant.Action.NoAction,
        ]
        # action_list = [
        #     Constant.Action.NoAction,
        #     Constant.Action.NoAction,
        #     Constant.Action.NoAction,
        #     Constant.Action.Sell,
        #     Constant.Action.Sell,
        #     Constant.Action.Sell,
        # ]
        return self._do_strategy(context, cond_list, action_list)

    def __repr__(self):
        return 'Hold'

    @property
    def state(self):
        return Constant.State.Hold


class ShortState(StockState):
    def _state_action(self, context, cond_list):
        action_list = [
            Constant.Action.NoAction,
            Constant.Action.NoAction,
            Constant.Action.NoAction,
            Constant.Action.NoAction,
            Constant.Action.Buy,
            Constant.Action.Buy,
        ]
        # action_list = [
        #     Constant.Action.Buy,
        #     Constant.Action.Buy,
        #     Constant.Action.Buy,
        #     Constant.Action.NoAction,
        #     Constant.Action.NoAction,
        #     Constant.Action.NoAction,
        # ]
        return self._do_strategy(context, cond_list, action_list)

    def __repr__(self):
        return 'Short'

    @property
    def state(self):
        return Constant.State.Short
