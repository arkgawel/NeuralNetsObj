#import numpy as np
#import pandas as pd
#from sklearn import preprocessing
#from sklearn.model_selection import train_test_split
#from sklearn.utils import shuffle
#from sklearn.metrics import confusion_matrix
#from keras.models import Sequential
#from keras.layers import Dense

from Preprocessing.DataLoader import DataLoader, Preprocess, Analize

data_loader1 = DataLoader('./forestfires.csv', ';', ',')
file = data_loader1.read_file()
print(file)

x = ['temp','RH', 'wind','rain']
y = ['fire']

X_train, X_test, y_train, y_test= Preprocess().scale_and_split(x, y, file)

print(X_train)
print(y_train)

analize = Analize(len(x))
analize.evaluate_model(X_train, y_train, X_test, y_test)


#print(DataLoader('./forestfires.csv', ';', ',').read_file())







#print(data_loader1.dtypes())
