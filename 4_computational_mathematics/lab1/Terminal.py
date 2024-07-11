import random

from Exceptions.IncorrectValueException import IncorrectValueException
from Matrix.Matrix import Matrix
from Matrix.MatrixMethods import MatrixMethods


class Terminal:

    def __init__(self):
        self.__isFromFile: bool = False
        self.__isGenerated: bool = False

    @staticmethod
    def isFile() -> bool:
        print("Выберите формат ввода(c клавиатуры - k или из файла - f):")
        is_file = input()
        if is_file.__eq__('k'):
            return False
        elif is_file.__eq__('f'):
            return True
        else:
            return Terminal.isFile()

    @staticmethod
    def isGenerated():
        is_generated = input()
        if is_generated.__eq__('y'):
            return True
        elif is_generated.__eq__('n'):
            return False
        else:
            return Terminal.isGenerated()

    def getMatrixParameters(self) -> Matrix:
        try:
            if self.__isFromFile:
                f = open(input('Введите путь к файлу:'), 'r')
                parameters = f.read().split(';')
            else:
                parameters = input().split(';')
            if len(parameters) != 2:
                raise IncorrectValueException('Количество аргументов должно быть строго 2: размерность матрицы '
                                              'и точность вычислений.')
            matrix: Matrix = Matrix(parameters[0], parameters[1])
            return matrix
        except IncorrectValueException as e:
            print(e.message)
            return self.getMatrixParameters()
        except FileNotFoundError as e:
            print(e.strerror)
            return self.getMatrixParameters()

    @staticmethod
    def getMatrixRows(matrix: Matrix):
        print("Введите значения элементов матрицы для каждой строки в виде :{a1;a2;...;an;bn}")
        dimension = matrix.getDimension()
        extended_dimension = matrix.getExtendedDimension()
        temp_matrix = []
        for row in range(dimension):
            print(f'Строка №{(row + 1)}')
            elements = input().strip().split(';')
            temp_matrix.append([])
            for column in range(extended_dimension):
                try:
                    temp_matrix[row].append(float(elements[column]))
                except ValueError:
                    print(f'Элемент матрицы должен быть числом. '
                          f'Некорректный ввод элемента [{row}][{column}].')
                    return Terminal.getMatrixRows(matrix)
                except IndexError:
                    print()(f'Количество элементов введено некорректно. ')
                    return Terminal.getMatrixRows(matrix)

        matrix.setMatrix(temp_matrix)

    @staticmethod
    def getMatrixRowsFromFile(matrix: Matrix):
        try:
            f = open(input('\nВведите путь к файлу:'), 'r')
            dimension = matrix.getDimension()
            extended_dimension = matrix.getExtendedDimension()
            temp_matrix = []
            for row in range(dimension):
                elements = f.readline().strip().split(';')
                temp_matrix.append([])
                for column in range(extended_dimension):
                    temp_matrix[row].append(float(elements[column]))
        except ValueError:
            print(f'Элемент матрицы должен быть числом. '
                  f'Некорректный ввод элемента [{row}][{column}].')
            return Terminal.getMatrixRowsFromFile(matrix)
        except IndexError:
            print()(f'Количество элементов введено некорректно. ')
            return Terminal.getMatrixRowsFromFile(matrix)
        except FileNotFoundError as e:
            return Terminal.getMatrixRowsFromFile(matrix)

        matrix.setMatrix(temp_matrix)

    @staticmethod
    def getRandomRows(matrix: Matrix):
        dimension = matrix.getDimension()
        extended_dimension = matrix.getExtendedDimension()
        matrix.setMatrix(
            [[round(random.random() + random.randint(-1000, 1000), 3) for i in range(extended_dimension)] for x in
             range(dimension)])

    def work(self):
        self.__isFromFile = self.isFile()
        if not self.__isFromFile:
            print('Введите параметры матрицы в виде: "Размерность (n);Точность (eps)": ')
        matrix: Matrix = self.getMatrixParameters()
        print(f'Матрица, n = {matrix.getDimension()}. Эпсилон, eps = {matrix.getEpsilon()}\n')
        self.__isFromFile = self.isFile()
        if not self.__isFromFile:
            print('Сгенерировать коэффициенты автоматически? y/n')
            self.__isGenerated = Terminal.isGenerated()
            if not self.__isGenerated:
                Terminal.getMatrixRows(matrix)
            else:
                Terminal.getRandomRows(matrix)
        else:
            Terminal.getMatrixRowsFromFile(matrix)
        print(matrix.createViewStrSLAE())
        methods = MatrixMethods(matrix)
        methods.solve()

    def refresh(self):
        self.__isFromFile = False
        self.__isGenerated = False
