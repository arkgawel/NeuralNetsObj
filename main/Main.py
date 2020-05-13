#import numpy as np
#import pandas as pd
#from sklearn import preprocessing
#from sklearn.model_selection import train_test_split
#from sklearn.utils import shuffle
#from sklearn.metrics import confusion_matrix
#from keras.models import Sequential
#from keras.layers import Dense

from Preprocessing.DataLoader import DataLoader

#data_loader1 = DataLoader('./forestfires.csv', ';', ',')
#print(data_loader1.read_file())

print(DataLoader('./forestfires.csv', ';', ',').read_file())





#print(data_loader1.dtypes())
