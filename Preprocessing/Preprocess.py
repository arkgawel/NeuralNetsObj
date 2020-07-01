from sklearn.model_selection import train_test_split
from sklearn.preprocessing import scale


class Preprocess:
    def scale_and_split(self, input, output, file):
        x = file[input]
        y = file[output]
        scaled = scale(self.__to_float(x))
        return train_test_split(scaled, y, test_size=0.2, random_state=5)

    def __to_float(self, input):
        return input.astype(float)
