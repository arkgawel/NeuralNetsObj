import pandas as pd
from sklearn.utils import shuffle
from pandas.tests.reshape.test_pivot import dropna


class DataLoader:
    def __init__(self, path, separator, decimal):
        self.path = path
        self.separator = separator
        self.decimal=decimal


    def read_file(self):
        loaded = pd.read_csv(self.path, sep=self.separator, decimal=self.decimal)
        loaded = shuffle(loaded)
        return loaded.dropna(axis=0, how='any')


    def pick_x_y(x, y):
        input = x
        output = y



