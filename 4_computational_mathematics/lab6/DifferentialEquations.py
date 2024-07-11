import numpy as np


class DifferentialEquations:

    def __init__(self, x0, y0, xn, h, eps):
        self.__x0 = x0
        self.__y0 = y0
        self.__xn = xn
        self.__h = h
        self.__eps = eps
        self.__x_array = list(np.arange(x0, xn + 0.00001, h))

    def getY0(self):
        return self.__y0

    def getX0(self):
        return self.__x0

    def getXN(self):
        return self.__xn

    def getH(self):
        return self.__h

    def getEps(self):
        return self.__eps

    def getArrayX(self):
        return self.__x_array

    def ruleRunge(self, I_h, I_h2, k, eps):
        delta = abs(I_h2 - I_h) / (2 ** k - 1)
        print(
            f'Погрешность вычислений между значениями {I_h2} и {I_h} составляет {delta} {"<" if delta < eps else ">"} {eps}.')
        if delta <= eps:
            return True
        else:
            return False
