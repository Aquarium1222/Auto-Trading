import pandas as pd
import numpy as np
import torch.utils.data as data


class StockDataset(data.Dataset):
    def __init__(self, preprocessor, train_path, test_path):
        preprocessor = preprocessor
        train_datas = pd.read_csv(train_path, header=None)
        test_datas = pd.read_csv(test_path, header=None)
        datas = pd.concat([train_datas, test_datas], axis=0).reset_index(drop=True)
        self.__x, self.__y = preprocessor.preprocessing(datas)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __getitem__(self, item):
        return self.__x[item], self.__y[item]

    def __len__(self):
        return len(self.__y)
