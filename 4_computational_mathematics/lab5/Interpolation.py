class Interpolation:

    def __init__(self, x_array, y_array, x):
        self.__x_array = x_array
        self.__y_array = y_array
        self.__x = x

    def getX(self):
        return self.__x

    def getArrayX(self):
        return self.__x_array

    def getArrayY(self):
        return self.__y_array

    def setX(self, x):
        self.__x = x
