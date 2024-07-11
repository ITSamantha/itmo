from Exceptions.IncorrectValueException import IncorrectValueException
from Validation.Validator import Validator
from Equations import EQUATIONS, METHODS
from DifferentialEquationsMethods import DifferentialEquationsMethods
import matplotlib.pyplot as plt

class Terminal:

    def work(self):
        try:
            print('\t\tЧисленное решение обыкновенных дифференциальных уравнений')
            function_number = self.enterFunctionNumber()
            method_number = self.enterMethodNumber()
            print('Введите y0 = y(x0)')
            x0 = self.enterArgument('x0')
            y0 = self.enterArgument('y0')
            xn = self.enterInterval(x0)
            h = self.enterH()
            eps = self.enterEpsilon()
            diff = DifferentialEquationsMethods(x0, y0, xn, h, eps)
            if method_number == 1:
                results = diff.methodModifiedEiler(function_number)
            elif method_number == 2:
                results = diff.methodRungeCutta4(function_number)
            else:
                results = diff.methodAdams(function_number)
            plt.plot(diff.getArrayX(), results, color='blue', label='Найденные')
            plt.legend()
            plt.grid()
        except IncorrectValueException as e:
            print(e.message)
            return
        except RuntimeWarning:
            pass

    def enterInterval(self, x0):
        try:
            print('Введите границу интервала xn (x0 задано):')
            print('xn = ', end='')
            xn = Validator.validateNumber(input())
            Validator.validateBorders(x0, xn)
            return xn
        except IncorrectValueException as e:
            print(e.message)
            return self.enterInterval()

    def enterH(self):
        try:
            print('Введите шаг h:')
            n = Validator.validateH()
            return n
        except IncorrectValueException as e:
            print(e.message)
            return self.enterH()

    def enterArgument(self, arg):
        try:
            print(f'Введите значение {arg}:')
            number = Validator.validateNumber(input())
            return number
        except IncorrectValueException as e:
            print(e.message)
            return self.enterArgument(arg)

    def enterFunctionNumber(self):
        try:
            print(f'Введите значение функции:')
            for i in range(len(EQUATIONS)):
                print(f'{i + 1}.{EQUATIONS[i+1]}')
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
            return self.enterMethodNumber()

    def enterEpsilon(self):
        try:
            print('Введите точность epsilon:')
            eps = Validator.validateEpsilon(input())
            return eps
        except IncorrectValueException as e:
            print(e.message)
            return self.enterEpsilon()
