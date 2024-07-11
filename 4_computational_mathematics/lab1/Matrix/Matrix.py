import random

from Matrix.MatrixValidator import MatrixValidator


class Matrix:

    def __init__(self, dimension: str, epsilon: str):
        self.__dimension = MatrixValidator.validateDimension(dimension)
        self.__extended_dimension = self.__dimension + 1;
        self.__epsilon = MatrixValidator.validateEpsilon(epsilon)
        self.__matrix = [[0 for x in range(self.__extended_dimension)] for i in range(self.__dimension)]
        self.__converted_matrix = [[0 for x in range(self.__extended_dimension)] for x in range(self.__dimension)]

    def getDimension(self):
        return self.__dimension

    def getExtendedDimension(self):
        return self.__extended_dimension

    def getEpsilon(self):
        return self.__epsilon

    def getMatrix(self):
        return self.__matrix

    def getConvertedMatrix(self):
        return self.__converted_matrix

    def setMatrix(self, matrix: []):
        self.__matrix = matrix

    def setConvertedMatrix(self, converted_matrix: []):
        self.__converted_matrix = converted_matrix

    def createViewStrConvertedMatrix(self):
        result = "Конвертированная матрица:\n"
        for row in range(self.__dimension):
            result += f"x_{(row + 1)}= "
            firstAppending = True
            for column in range(self.__extended_dimension):
                if row == column:
                    continue;
                if column == self.__extended_dimension - 1:
                    if self.__converted_matrix[row][column] >= 0:
                        result += f" +{self.__matrix[row][column]}"
                    else:
                        result += f" {self.__converted_matrix[row][column]}"
                    continue
                if not firstAppending:
                    if self.__converted_matrix[row][column] >= 0:
                        result += f" +{self.__matrix[row][column]}*x_{column + 1}"
                    else:
                        result += f" {self.__converted_matrix[row][column]}*x_{column + 1}"
                else:
                    result += f" {self.__converted_matrix[row][column]}*x_{column + 1}"
                    firstAppending = False
            result += ";\n"
        return result


    def createViewStrMatrix(self):
        result = ''
        for i in range(self.__dimension):
            result += '('
            for j in range(self.__extended_dimension):
                if j == self.__extended_dimension - 1:
                    result += f')   (x{(i + 1)})    =  ({self.__matrix[i][j]}'
                    break
                result += f' {self.__matrix[i][j]} '
            result += ')\n'
        return result


    def createViewStrSLAE(self):
        result = f'Матрица, n = {self.__dimension}. Эпсилон, eps = {self.__epsilon}\n'
        for i in range(self.__dimension):
            for j in range(self.__extended_dimension):
                if j == self.__extended_dimension - 1:
                    result += f' =  {self.__matrix[i][j]}\n'
                    break
                if self.__matrix[i][j] >= 0:
                    if j != 0:
                        result += '+'
                result += f' {self.__matrix[i][j]}x{j + 1} '

        return result
