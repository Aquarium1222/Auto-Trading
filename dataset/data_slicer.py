from config import *


class DataSlicer:
    def __init__(self, dataset):
        self.__dataset = dataset
        print(len(self.__dataset))
        self.__train_end = int((len(dataset) - Constant.N_VAL) * Constant.TRAIN_SIZE)
        self.__test_end = len(dataset) - Constant.N_VAL + 1
        self.__val_end = len(dataset)

    @property
    def train_datas(self):
        x, y = self.__dataset.x, self.__dataset.y
        return x[:self.__train_end], y[:self.__train_end]

    @property
    def test_datas(self):
        x, y = self.__dataset.x, self.__dataset.y
        return x[self.__train_end:self.__test_end], y[self.__train_end:self.__test_end]

    @property
    def val_datas(self):
        x, y = self.__dataset.x, self.__dataset.y
        return x[self.__test_end:self.__val_end], y[self.__test_end:self.__val_end]
