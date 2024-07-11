import Equations
from Exceptions.IncorrectValueException import IncorrectValueException

MIN_EPSILON = 0


class Validator:

    @staticmethod
    def validateNumber(number: str):
        try:
            number = float(number)
            return number
        except ValueError:
            raise IncorrectValueException(f'Необходимо ввести число.')

    @staticmethod
    def validateEpsilon(epsilon: str):
        try:
            epsilon = float(epsilon)
            if epsilon >= MIN_EPSILON:
                return epsilon
            else:
                raise IncorrectValueException(f'Точность (эпсилон) должна быть больше или равна 0.')
        except ValueError:
            raise IncorrectValueException(f'Точность (эпсилон) - число с плавающей точкой.')

    @staticmethod
    def validateFunctionNumber():
        try:
            number = Validator.validateNumber(input())
            if 0 > number > len(Equations.EQUATIONS):
                raise IncorrectValueException('Введите число из диапазона. Такой функции не существует.')
            return number
        except ValueError:
            raise IncorrectValueException(f'Необходимо ввести число.')

    @staticmethod
    def validateMethodNumber():
        try:
            number = Validator.validateNumber(input())
            if -1 > number > len(Equations.METHODS):
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
    def validateH():
        n = float(Validator.validateNumber(input()))
        if n > 0:
            return n
        else:
            raise IncorrectValueException(
                'Неверное введен шаг h. Число должно быть строго больше 0. Попробуйте еще раз.')
