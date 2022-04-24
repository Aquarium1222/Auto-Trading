import numpy as np

from config import *
from model.model import Model
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error


class SVRStock(Model):
    def train(self):
        # training
        self._model = SVR(kernel='rbf', C=Hp.SVR_C, gamma='scale')
        self._model.fit(self._train_x, self._train_y)

        # testing
        test_x_step1, test_y_step1 = self._test_x, self._test_y
        pred_step1 = self._model.predict(test_x_step1)
        test_x_step2 = np.delete(test_x_step1, 0, axis=1)
        test_x_step2 = np.insert(test_x_step2, Hp.SVR_X_LEN - 1, pred_step1, axis=1)
        test_x_step2 = test_x_step2[:-1]
        test_y_step2 = test_y_step1[1:]
        pred_step2 = self._model.predict(test_x_step2)
        rmse_step1 = np.sqrt(mean_squared_error(pred_step1, test_y_step1))
        rmse_step2 = np.sqrt(mean_squared_error(pred_step2, test_y_step2))
        print('SVR RMSE: \n\tstep1: {}\n\tstep2: {}'.format(rmse_step1, rmse_step2))
    
    def predict(self, x):
        return self._model.predict(x)
