import statistics
from math import factorial, ceil, floor

import numpy
from numpy import delete

from Interpolation import Interpolation


class InterpolationMethods(Interpolation):

    def _calculateLagrangeInterpolation(self):
        x_array = self.getArrayX()
        y_array = self.getArrayY()
        length = len(x_array)
        x = self.getX()
        L = []
        for i in range(length):
            l_i = 1
            for j in range(length):
                if i != j:
                    l_i *= (x - x_array[j]) / (x_array[i] - x_array[j])
            l_i *= y_array[i]
            L.append(l_i)
        return L

    def _calculateSumLagrange(self, l):
        return sum(l)

    def methodLagrange(self):
        print(f'Поиск значения функции c помощью многочлена Лагранжа с аргументом x = {self.getX()}')
        L = self._calculateLagrangeInterpolation()
        y_array = self.getArrayY()
        x = self.getX()
        for i in range(len(L)):
            print(f'l{i}(x) = {L[i]}, y{i} = {y_array[i]}')
        print(
            f' Значение функции с аргументом x = {x}\n\t L{len(y_array) - 1} = y({x}) = {self._calculateSumLagrange(L)}')
        return self._calculateSumLagrange(L)

    def methodLagrange1(self):
        L = self._calculateLagrangeInterpolation()
        y_array = self.getArrayY()
        x = self.getX()
        return self._calculateSumLagrange(L)
    def methodNewton(self):
        print('\n\tМногочлен Ньютона для интерполяции')
        table = self.formulateTableOfFiniteDifferences()
        n = len(self.getArrayX())
        print('\n\tТаблица конечных разностей\n x |', end='')
        for i in range(n + 1):
            print(f'y({i})', end='|')
        print()
        for row in range(n):
            for column in range(n + 1):
                print(table[row][column], end='|')
            print()
        median = self._findMiddle()
        index = self._findIndexForT()
        if self._defineRule(median):
            N = self._firtsRuleNewton(index, table)
            print(f'Используем правило №1. Ответ y{self.getX()} = {N}')
        else:
            N = self._secondRuleNewton(table)
            print(f'Используем правило №2. Ответ y{self.getX()} = {N}')
        return N

    def methodNewton1(self):
        table = self.formulateTableOfFiniteDifferences()
        n = len(self.getArrayX())
        median = self._findMiddle()
        index = self._findIndexForT()
        if self._defineRule(median):
            N = self._firtsRuleNewton(index, table)
        else:
            N = self._secondRuleNewton(table)
        return N

    def formulateTableOfFiniteDifferences(self):
        x_array = self.getArrayX()
        y_array = self.getArrayY()
        n = len(x_array)
        table = [['-' for _ in range(n + 1)] for _ in range(n)]
        for column in range(n + 1):
            for row in range(n):
                if column == 1:
                    table[row][column] = y_array[row]
                elif column == 0:
                    table[row][column] = x_array[row]
                else:
                    if row < n + 1 - column:
                        table[row][column] = round(table[row + 1][column - 1] - table[row][column - 1], 4)
        return table

    def _findMiddle(self):
        return statistics.median(self.getArrayX())

    def _defineRule(self, median):
        x = self.getX()
        return x < median

    def _firtsRuleNewton(self, index, table):
        n = len(self.getArrayX())
        t = self._findT(index)
        N = 0
        for i in range(2, n + 2):
            try:
                y_i = table[index][i - 1]
                f = 1
                for j in range(i - 2):
                    f *= (t - j)
                y_i = y_i * f / float(factorial(i - 2))
                N += y_i
            except:
                continue
        return N

    def _secondRuleNewton(self, table):
        n = len(self.getArrayX())
        t = self._findT(n - 1)
        N = 0
        coefficient = 0
        for i in range(n - 1, -1, -1):
            try:
                y_i = table[i][coefficient + 1]
                f = 1
                for j in range(coefficient):
                    f *= (t + j)
                y_i *= f / factorial(coefficient)
                N += y_i
                coefficient += 1
            except:
                continue
        return N

    def _findIndexForT(self):
        x_array = self.getArrayX()
        n = len(x_array)
        x = self.getX()
        for i in range(n):
            if x_array[i] > x:
                return i - 1

    def _findT(self, index):
        x = self.getX()
        x_array = self.getArrayX()
        return (x - x_array[index]) / self._findH()

    def _findH(self):
        x_array = self.getArrayX()
        return x_array[1] - x_array[0]

    def methodStirling(self):
        print('\n\tСхема Стирлинга для интерполяции')
        table = self.formulateTableOfFiniteDifferences()
        n = len(self.getArrayX())
        print('\n\tТаблица разделенных разностей\n x |', end='')
        for i in range(n + 1):
            print(f'y({i})', end='|')
        print()
        for row in range(n):
            for column in range(n + 1):
                print(table[row][column], end='|')
            print()
        result = self._calculateStrirling(table)
        print(f'Ответ y{self.getX()} = {result} по схеме Стирлинга.')
        return result

    def methodStirling1(self):
        table = self.formulateTableOfFiniteDifferences()
        n = len(self.getArrayX())
        result = self._calculateStrirling(table)
        return result

    def _calculateStrirling(self, table):
        y_array = self.getArrayY()
        factors = self.create_factorial(len(y_array))
        table = list(delete(table, [0], 1))
        middle = len(self.getArrayX()) // 2
        t = self._findT(middle)
        result = y_array[middle]
        for i in range(1, middle + 1):
            try:
                mul = 1
                for j in range(1, i):
                    mul *= (t * t - j * j)
                result += 1 / factors[2 * i - 1] * t * mul * \
                          (float(table[-(i - 1) + middle][2 * i - 1]) + float(table[-i + middle][2 * i - 1])) / 2
                result += 1 / factors[2 * i] * t * t * mul * (float(table[-i + middle][2 * i]))
            except:
                continue
        return result


    def create_factorial(self, n):
        result = []
        for i in range(n + 1):
            fact = 1
            for j in range(1, i + 1):
                fact *= j
            result.append(fact)
        return result
