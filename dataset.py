import pandas as pd


class Dataset:
    def __init__(self, path):
        self.__data = pd.read_csv(path, header=None)
        print(self.__data)

    @property
    def open_price(self):
        return self.__data.iloc[:, 0]
