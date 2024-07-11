import Functions
from Exceptions.IncorrectValueException import IncorrectValueException
from Functions import FUNCTIONS


class Validator:

    @staticmethod
    def validateNumber(number: str):
        try:
            number = float(number)
            return number
        except ValueError:
            raise IncorrectValueException(f'Необходимо ввести число.')

    @staticmethod
    def validateFunctionNumber():
        try:
            number = Validator.validateNumber(input())
            if 0 > number > len(FUNCTIONS):
                raise IncorrectValueException('Введите число из диапазона. Такой функции не существует.')
            return number
        except ValueError:
            raise IncorrectValueException(f'Необходимо ввести число.')

    @staticmethod
    def validateMethodNumber():
        try:
            number = Validator.validateNumber(input())
            if -1 > number > len(Functions.METHODS):
                raise IncorrectValueException('Введите число из диапазона. Такого метода не существует.')
            return number
        except ValueError:
            raise IncorrectValueException(f'Необходимо ввести число.')

    @staticmethod
    def validateBorders(border_left: float, border_right: float):
        if border_left < border_right:
            return True
        else:
            raise IncorrectValueException(f'Левая граница должна быть строго меньше правой.')

    @staticmethod
    def validateEqualityLengths(arr_1, arr_2):
        if len(arr_1) != len(arr_2):
            raise IncorrectValueException('Длины массивов не равны.')

    @staticmethod
    def validateNumbersInArray(arr_1):
        visited = set()
        dup = [i for i in range(len(arr_1)) if arr_1[i] in visited or (visited.add(arr_1[i]) or False)]
        for i in range(len(arr_1)):
            if i in dup:
                arr_1[i] -= 0.001
        return arr_1

    @staticmethod
    def validateN():
        n = int(Validator.validateNumber(input()))
        if n > 0:
            return n
        else:
            raise IncorrectValueException(
                'Неверное введено значение числа разбиения интервала . Число должно быть строго больше 0. Попробуйте еще раз.')
