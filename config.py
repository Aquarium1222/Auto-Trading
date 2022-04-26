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
<<<<<<< HEAD
    SVR_C = 0.05
=======
    SVR_C = 11
>>>>>>> 9f5ca70ee5e6d9d0e14596bcbb82e3ff633c1493
    Y_LEN = 2
