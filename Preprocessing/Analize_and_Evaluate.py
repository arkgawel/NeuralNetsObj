from keras import Sequential
from keras.layers import Dense, np
from sklearn.metrics import confusion_matrix
import pandas as pd
import numpy as np


class Analize:
    def __init__(self, input_size):
        self.__nnet = Sequential()
        self.__nnet.add(Dense(input_size * 2, input_dim=input_size, activation='relu'))
        self.__nnet.add(Dense(input_size + 2, activation='relu'))
        self.__nnet.add(Dense(1, activation='sigmoid'))
        self.__nnet.summary()
        self.__nnet.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    def evaluate_model(self, X_train, y_train, X_test, y_test):
        #evo = self.__nnet.evaluate(X_train, y_train)
        _, accuracy = self.__nnet.evaluate(X_train, y_train)
        evo = ' Accuracy: %.2f' % (accuracy*100)
        self.__nnet.fit(X_test, y_test, epochs=150, batch_size=10)
        predictions = self.__nnet.predict_classes(X_test)
        labels = np.unique(y_test)
        a = confusion_matrix(y_test, predictions, labels=labels)
        result = pd.DataFrame(a, index=labels, columns=labels)
        return result, evo
