import numpy as np

from config import *
from model.model import Model
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error


class SVRStock(Model):
    def train(self):
        # training
        train_size = int(self._length * Constant.TRAIN_SIZE)
        train_x, train_y = self._dataset.x[:train_size], self._dataset.y[:train_size]
        self._model = SVR(kernel='rbf', C=Hp.SVR_C, gamma='scale')
        self._model.fit(train_x, train_y)

        # testing
        test_x, test_y = self._dataset.x[train_size:], self._dataset.y[train_size:]
        pred = self._model.predict(test_x)
        rmse = np.sqrt(mean_squared_error(pred, test_y))
        print('SVR RMSE: {}'.format(rmse))
    
    def predict(self, x):
        return self._model.predict(x)
