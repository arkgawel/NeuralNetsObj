import pandas as pd
from keras import Sequential
from keras.layers import Dense, np
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
from sklearn import preprocessing
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

class Preprocess:
    def scale_and_split(self, input, output, file):
        x = file[input]
        y = file[output]
        scaled = preprocessing.scale(self.__to_float(x))
        return train_test_split(scaled, y, test_size=0.2, random_state=5)

    def __to_float(self, input):
        return input.astype(float)


class Analize:
    def __init__(self, input_size):
        self.__nnet = Sequential()
        self.__nnet.add(Dense(input_size * 2, input_dim=input_size, activation='relu'))
        self.__nnet.add(Dense(input_size + 2, activation='relu'))
        self.__nnet.add(Dense(1, activation='sigmoid'))
        self.__nnet.summary()
        self.__nnet.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])


    def evaluate_model(self, X_train, y_train, X_test, y_test):
        evo=self.__nnet.evaluate(X_train, y_train)
        self.__nnet.fit(X_test, y_test, epochs=150, batch_size=10)
        predictions = self.__nnet.predict_classes(X_test)
        labels = np.unique(y_test)
        a = confusion_matrix(y_test, predictions, labels=labels)
        result = pd.DataFrame(a, index=labels, columns=labels)
        return print(result, evo )
