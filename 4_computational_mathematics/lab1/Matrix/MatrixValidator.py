from Exceptions.IncorrectValueException import IncorrectValueException


class MatrixValidator:
    MIN_DIMENSION = 1
    MAX_DIMENSION = 20
    MIN_EPSILON = 0

    @staticmethod
    def validateDimension(dimension: str):
        try:
            dimension = int(dimension)
            if MatrixValidator.MIN_DIMENSION <= dimension <= MatrixValidator.MAX_DIMENSION:
                return dimension
            else:
                raise IncorrectValueException(f'Размерность матрицы должна находится в промежутке '
                                              f'{MatrixValidator.MIN_DIMENSION} и {MatrixValidator.MAX_DIMENSION}.')
        except ValueError:
            raise IncorrectValueException('Размерность матрицы - целое число.')

    @staticmethod
    def validateEpsilon(epsilon: str):
        try:
            epsilon = float(epsilon)
            if epsilon >= MatrixValidator.MIN_EPSILON:
                return epsilon
            else:
                raise IncorrectValueException(f'Точность (эпсилон) должна быть больше или равна 0.')
        except ValueError:
            raise IncorrectValueException(f'Точность (эпсилон) - число с плавающей точкой.')
