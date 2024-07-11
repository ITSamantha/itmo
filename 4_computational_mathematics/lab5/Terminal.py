from InterpolationMethods import InterpolationMethods
from Exceptions.IncorrectValueException import IncorrectValueException
from Validation.Validator import Validator
from Functions import FUNCTIONS, METHODS
import numexpr as ne
import numpy as np
import matplotlib.pyplot as plt


class Terminal:
    def __init__(self):
        self.__inputMode = ''

    def chooseInputMode(self) -> str:
        print("Выберите формат ввода(c клавиатуры - k, файла - f, выбрать функцию - c):")
        input_mode = input()
        if input_mode == 'k' or input_mode == 'c' or input_mode == 'f':
            return input_mode
        else:
            return self.chooseInputMode()

    def refresh(self):
        self.__inputMode = ''

    def work(self):
        try:
            print('\t\t\tИнтерполяция функции')
            self.__inputMode = self.chooseInputMode()
            if self.__inputMode == 'k':
                x_array, y_array = self.enterArraysFromKeyboard()
            elif self.__inputMode == 'f':
                x_array, y_array = self.enterArraysFromFile()
            elif self.__inputMode == 'c':
                x_array, y_array = self.enterArraysFromFunctions()
            x = self.enterArgumentX()
            interpolation = InterpolationMethods(x_array, y_array, x)
            method = self.enterMethodNumber()
            x_arr = np.arange(min(x_array), max(x_array), 0.0001)
            if method == 1:
                y = []
                for val in x_arr:
                    interpolation.setX(val)
                    y_i = interpolation.methodLagrange1()
                    y.append(y_i)
                interpolation.setX(x)
                answer = interpolation.methodLagrange()
            elif method == 2:
                y = []
                for val in x_arr:
                    interpolation.setX(val)
                    y_i = interpolation.methodNewton1()
                    y.append(y_i)
                interpolation.setX(x)
                answer = interpolation.methodNewton()
            else:
                y = []
                for val in x_arr:
                    interpolation.setX(val)
                    y_i = interpolation.methodStirling1()
                    y.append(y_i)
                interpolation.setX(x)
                answer = interpolation.methodStirling()
            plt.plot(x_arr, y, color='black', label='fi(x)')
            plt.plot(x_array, y_array, color='blue', label='f(x)')
            plt.scatter(x_array, y_array, color='orange', label='f(x)')
            plt.scatter(x, answer, color='red')
            plt.legend()
            plt.grid()
        except IncorrectValueException as e:
            print(e.message)
            return
        except RuntimeWarning:
            pass
        finally:
            plt.show()

    def enterArray(self, variable) -> object:
        try:
            print(f'Введите значения {variable} (через ;):')
            arr = [Validator.validateNumber(x) for x in input().split(';')]
            return arr
        except IncorrectValueException as e:
            print(e.message)
            return self.enterArray(variable)

    def enterArraysFromKeyboard(self):
        x_array = self.enterArray('x')
        y_array = self.enterArray('y')
        Validator.validateEqualityLengths(x_array, y_array)
        x_array = Validator.validateNumbersInArray(x_array)
        return x_array, y_array

    def enterArraysFromFile(self):
        try:
            f = open(input('Введите путь к файлу:'), 'r')
            x_array = [Validator.validateNumber(x) for x in f.readline().split(';')]
            y_array = [Validator.validateNumber(x) for x in f.readline().split(';')]
            Validator.validateEqualityLengths(x_array, y_array)
            x_array = Validator.validateNumbersInArray(x_array)
            return x_array, y_array
        except IncorrectValueException as e:
            print(e.message)
            return self.enterArraysFromFile()
        except FileNotFoundError as e:
            print(e.strerror)
            return self.enterArraysFromFile()

    def enterArraysFromFunctions(self):
        try:
            print('Доступные функции')
            for i in range(len(FUNCTIONS)):
                print(f'{i + 1}.{FUNCTIONS[i + 1]}')
            number = self.enterFunctionNumber()
            a, b = self.enterInterval()
            n = self.enterNumberOfDots()
            return self.reformatFunction(FUNCTIONS[number], a, b, n)
        except IncorrectValueException as e:
            print(e.message)
            return self.enterArraysFromFile()

    def reformatFunction(self, function, a, b, n):
        h = (b - a) / n
        x_array = list(np.arange(a, b, h))
        y_array = [ne.evaluate(function.split('=')[1], local_dict={'x': x}) for x in x_array]
        return x_array, y_array

    def enterInterval(self):
        try:
            print('Введите границы интервала a и b:')
            print('a = ', end='')
            a = Validator.validateNumber(input())
            print('b = ', end='')
            b = Validator.validateNumber(input())
            Validator.validateBorders(a, b)
            return a, b
        except IncorrectValueException as e:
            print(e.message)
            return self.enterInterval()

    def enterNumberOfDots(self):
        try:
            print('Введите начальное число точек для разбиения:')
            n = Validator.validateN()
            return n
        except IncorrectValueException as e:
            print(e.message)
            return self.enterNumberOfDots()

    def enterArgumentX(self):
        try:
            print(f'Введите значение аргумента x:')
            number = Validator.validateNumber(input())
            return number
        except IncorrectValueException as e:
            print(e.message)
            return self.enterArgumentX()

    def enterFunctionNumber(self):
        try:
            print(f'Введите значение функции:')
            number = Validator.validateFunctionNumber()
            return number
        except IncorrectValueException as e:
            print(e.message)
            return self.enterFunctionNumber()

    def enterMethodNumber(self):
        try:
            print('Методы для решения задачи интерполяции')
            for i in range(len(METHODS)):
                print(f'{i + 1}. {METHODS[i]}')
            print(f'Введите номер метода:')
            number = Validator.validateMethodNumber()
            return number
        except IncorrectValueException as e:
            print(e.message)
            return self.enterMethodNumber(self)
