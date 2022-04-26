from enum import Enum


class Constant:
    class Method(Enum):
        SVR = 0
        RF = 1

    class State(Enum):
        Nothing = 0
        Hold = 1
        Short = 2

    class Action(Enum):
        Buy = 1
        NoAction = 0
        Sell = -1

    TRAIN_SIZE = 0.9
    N_VAL = 20


class Hp:
    SVR_X_LEN = 3
    SVR_C = 11
    Y_LEN = 2
