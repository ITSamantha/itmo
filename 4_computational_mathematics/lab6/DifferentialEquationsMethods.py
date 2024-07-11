import math

import numpy as np

from DifferentialEquations import DifferentialEquations
from Equations import calculateFunction, calculateAnswer
from Exceptions.IncorrectValueException import IncorrectValueException

EILER_COLS = 6
RUNGE_COLS = 9
ADAMS_COLS = 8


class DifferentialEquationsMethods(DifferentialEquations):

    def methodModifiedEiler(self, function_number):
        results = self._calculateModifiedEilerMethod(function_number)
        self.__printEilerModifiedTable(results)
        return results[:][2]

    def _calculateModifiedEilerMethod(self, function_number):
        x_arr = self.getArrayX()
        n = len(x_arr)
        h = self.getH()
        x0=self.getX0()
        y0 = self.getY0()
        iterations = [[0.0 for x in range(EILER_COLS)] for i in range(n)]
        for i in range(n):
            iterations[i][0] = i
            iterations[i][1] = round(float(x_arr[i]), 5)
            if i == 0:
                iterations[i][2] = y0
            function = round(calculateFunction(x_arr[i], iterations[i][2], function_number), 5)
            if i != n - 1:
                iterations[i + 1][2] = round(iterations[i][2] + h / 2 * (
                        function + calculateFunction(x_arr[i + 1], iterations[i][2] + h * function,
                                                        function_number)),
                                                5)  # yi+1
                if np.isnan(iterations[i + 1][2]) or np.isinf(iterations[i + 1][2]):
                    raise IncorrectValueException('Невозможно вычислить.')
                iterations[i][3] = function  # f(xi,yi)
                function_2 = calculateFunction(x_arr[i + 1], iterations[i][2] + h * function, function_number)
                iterations[i][4] = function_2  # f(xi+1,yi+hf(xi,yi))
            iterations[i][5] = calculateAnswer(x0, y0, x_arr[i],function_number )
        return iterations

    def __printEilerModifiedTable(self, iterations):
        print('\t\tМодифицированный метод Эйлера')
        print('i  |  x  |   y   | f(xi, yi)  | f(xi+1, yi+1) | Точное решение |')
        n = len(iterations)
        for i in range(n):
            print(f'{iterations[i][0]}  |{iterations[i][1]}  | {iterations[i][2]}  | {iterations[i][3]}  |'
                  f'{iterations[i][4]}  |{iterations[i][5]}  |')

    def methodRungeCutta4(self, function_number):
        results = self._calculateRungeCutta4(function_number)
        self.__printRungeCuttaTable(results, len(results))
        return results[:][2]

    def _calculateRungeCutta4(self, function_number):
        x_arr = self.getArrayX()
        n = len(x_arr)
        h = self.getH()
        y0 = self.getY0()
        x0 = self.getX0()
        iterations = [[0.0 for x in range(RUNGE_COLS)] for i in range(n)]
        for i in range(n):
            iterations[i][0] = i
            iterations[i][1] = round(float(x_arr[i]), 5)
            if i == 0:
                iterations[i][2] = y0
            iterations[i][3] = round(h * calculateFunction(x_arr[i], iterations[i][2], function_number), 5)
            iterations[i][4] = round(
                h * calculateFunction(x_arr[i] + h / 2, iterations[i][2] + iterations[i][3] / 2, function_number),
                5)
            iterations[i][5] = round(
                h * calculateFunction(x_arr[i] + h / 2, iterations[i][2] + iterations[i][4] / 2, function_number),
                5)
            iterations[i][6] = round(
                h * calculateFunction(x_arr[i] + h, iterations[i][2] + iterations[i][5], function_number),
                5)
            fun = round(1 / 6 * (iterations[i][3] + 2 * iterations[i][4] + 2 * iterations[i][5] + iterations[i][6]), 5)
            if i != n - 1:
                iterations[i + 1][2] = round(iterations[i][2] + fun, 5)  # yi+1
                if np.isnan(iterations[i + 1][2]) or np.isinf(iterations[i + 1][2]):
                    raise IncorrectValueException('Невозможно вычислить.')
            iterations[i][7] = fun
            iterations[i][8] = calculateAnswer(x0, y0, x_arr[i],function_number )
        return iterations

    def __printRungeCuttaTable(self, iterations, num):
        print('\t\tМетод Рунге-Кутта 4 порядка')
        print('i  |  x  |   y   | k1 | k2 | k3 | k4 | delta | Точное решение |')
        for i in range(num):
            print(f'{iterations[i][0]}  |{iterations[i][1]}  | {iterations[i][2]}  | {iterations[i][3]}  |'
                  f'{iterations[i][4]}  |{iterations[i][5]}  |{iterations[i][6]} |{iterations[i][7]} |{iterations[i][8]}')

    def methodAdams(self, function_number):
        results = self._calculateRungeCutta4(function_number)
        self.__printRungeCuttaTable(results, 4)
        iterations = self.__calculateAdams(function_number, results[:4])
        self.__printAdamsTable(iterations)
        return iterations[:][2]

    def __calculateAdams(self, function_number, results):
        x_arr = self.getArrayX()
        n = len(x_arr)
        h = self.getH()
        y0 = self.getY0()
        x0=self.getX0()
        iterations = [[0.0 for x in range(ADAMS_COLS)] for i in range(n)]
        for i in range(4):
            iterations[i][0] = i
            iterations[i][1] = round(float(x_arr[i]), 5)
            iterations[i][2] = results[i][2]
            fi = round(results[i - 1][3] / h, 5)
            iterations[i][3] = fi
            delta_fi = fi - round(results[i - 2][3] / h, 5)
            iterations[i][4] = delta_fi
            delta_fi_2 = fi - round(2 * results[i - 2][3] / h, 5) + round(results[i - 3][3] / h, 5)
            iterations[i][5] = delta_fi_2
            delta_fi_3 = fi - round(3 * results[i - 2][3] / h, 5) + round(3 * results[i - 3][3] / h, 5) - round(
                results[i - 4][3] / h, 5)
            iterations[i][6] = delta_fi_3
        for i in range(3, n):
            if i != 3:
                iterations[i][0] = i
                iterations[i][1] = round(float(x_arr[i]), 5)
                fi = calculateFunction(x_arr[i], iterations[i][2], function_number)
                iterations[i][3] = fi
                delta_fi = fi - iterations[i - 2][3]
                iterations[i][4] = delta_fi
                delta_fi_2 = fi - 2 * iterations[i - 2][3] + iterations[i - 3][3]
                iterations[i][5] = delta_fi_2
                delta_fi_3 = fi - 3 * iterations[i - 2][3] + 3 * iterations[i - 3][3] - iterations[i - 4][3]
                iterations[i][6] = delta_fi_3
            if i != n - 1:
                iterations[i + 1][2] = iterations[i][2] + h * iterations[i][3] + h ** 2 / 2 * iterations[i][
                    4] + 5 / 12 * h ** 3 * iterations[i][5] + h ** 4 * 3 / 8 * iterations[i][6]
            iterations[i][7] = calculateAnswer(x0, y0, x_arr[i],function_number )
        return iterations

    def __printAdamsTable(self, iterations):
        print('\t\tМногошаговый метод Адамса')
        print('i  |  x  |   y   | fi | delta fi | delta2 fi| delta3 fi | Точное решение |')
        n = len(iterations)
        for i in range(n):
            print(f'{iterations[i][0]}  |{iterations[i][1]}  | {iterations[i][2]}  | {iterations[i][3]}  |'
                  f'{iterations[i][4]}  |{iterations[i][5]}  |{iterations[i][6]} |{iterations[i][7]} ')
