import numpy as np
from sklearn.preprocessing import MinMaxScaler

from config import *


class Preprocessor:
    def __init__(self, method):
        self.__method = method
        self.__scaler = None

    def preprocessing(self, datas):
        if self.__method == Constant.Method.SVR:
            x, y = self._svr_preproc(datas)
        elif self.__method == Constant.Method.RF:
            x, y = self._rf_preproc(datas)
        else:
            raise Exception('No such method.')
        return x, y

    def _svr_preproc(self, datas):
        x, y = [], []
        datas = np.expand_dims(np.array(datas.iloc[:, 0].values.tolist()), axis=1)
        self.__scaler = MinMaxScaler()
        self.__scaler.fit(datas)
        datas = self.__scaler.transform(datas)
        for i in range(Hp.SVR_X_LEN, len(datas)):
            x.append(np.squeeze(datas[i - Hp.SVR_X_LEN:i]))
            y.append(np.squeeze(datas[i]))
        return x, y

    def _rf_preproc(self, datas):
        x, y = [], []
        # ma preprocessing method
        return x, y

    def reverse(self, datas):
        return self.__scaler.inverse_transform(datas)
