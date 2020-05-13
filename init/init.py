
from Preprocessing.DataLoader import DataLoader
from Preprocessing.Preprocess import Preprocess
from Preprocessing.Analize_and_Evaluate import Analize

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
