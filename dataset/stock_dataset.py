import pandas as pd
import torch.utils.data as data
from sklearn.preprocessing import MinMaxScaler

from config import *


class StockDataset(data.Dataset):
    def __init__(self, path, method):
        self.__datas = pd.read_csv(path, header=None)
        self.__x, self.__y = self.__preprocessing(method)

    def __preprocessing(self, method):
        def svr_preproc():
            x, y = [], []
            scaler = MinMaxScaler()
            scaler.fit(self.__datas)
            datas = scaler.transform(self.__datas)[:, 0]
            for i in range(Hp.X_LEN, len(datas)):
                x.append(datas[i - Hp.X_LEN:i])
                y.append(datas[i])
            return x, y

        def ma_preproc():
            x, y = [], []
            # ma preprocessing method
            return x, y

        if method == Constant.Method['SVR']:
            x, y = svr_preproc()
        elif method == Constant.Method['MA']:
            x, y = ma_preproc()
        else:
            raise Exception('No such method.')
        return x, y

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
