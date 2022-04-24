import abc


class Model(abc.ABC):
    def __init__(self, dataset, slicer):
        self._dataset = dataset
        self._train_x, self._train_y = slicer.train_datas
        self._test_x, self._test_y = slicer.test_datas
        self._model = None

    @abc.abstractmethod
    def train(self):
        return NotImplemented

    @abc.abstractmethod
    def predict(self, x):
        return NotImplemented
