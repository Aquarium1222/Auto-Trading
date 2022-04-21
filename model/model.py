import abc


class Model(abc.ABC):
    def __init__(self, dataset):
        self._dataset = dataset

    @abc.abstractmethod
    def train(self):
        return NotImplemented

    @abc.abstractmethod
    def predict(self, x):
        return NotImplemented
