from Matrix.Matrix import Matrix


class MatrixMethods:

    def __init__(self, matrix: Matrix):
        self.__matrix = matrix

    def solve(self):
        print("Проверка доминирования диагонали. ")
        if not self.checkDiagonalDominance():
            print("Матрица не удовлетворяет тербованию доминирования диагонали.  "
                  "Пытаемся исправить ситуацию перестановкой.")
            self.correctDiagonalDominance()
            if not self.checkDiagonalDominance():
                print("Невозможно добиться доминирования диагонали матрицы.")
            else:
                print("Матрица соответствует требованию доминирования диагонали.")
        else:
            print("Матрица соответствует требованию доминирования диагонали.")
        self.createConvertedMatrix()
        try:
            self.algorithmGaussZeidel()
        except MemoryError as e:
            print("Memory Error.")

    def checkDiagonalDominance(self) -> bool:
        dimension = self.__matrix.getDimension()
        matrix = self.__matrix.getMatrix()
        for row in range(dimension):
            row_sum = 0
            for column in range(dimension):
                if row != column:
                    row_sum += abs(matrix[row][column])
            if abs(matrix[row][row]) > row_sum:
                continue
            return False
        return True

    def correctDiagonalDominance(self):
        """Исправить матрицу в соответствии с правилом преобладания диагональных элементов."""
        matrix: Matrix = self.__matrix.getMatrix()
        dimension: int = self.__matrix.getDimension()
        for column in range(dimension):
            diagonal_element = matrix[column][column]
            dominance_row_number = column
            for row in range(column, dimension):
                if abs(matrix[row][column]) > abs(diagonal_element):
                    diagonal_element = abs(matrix[row][column])
                    dominance_row_number = row
            matrix[dominance_row_number], matrix[column] = matrix[column], matrix[dominance_row_number]
        self.__matrix.setMatrix(matrix)
        print("Новая матрица имеет вид:")
        print(self.__matrix.createViewStrMatrix())

    def createConvertedMatrix(self):
        matrix = self.__matrix.getMatrix()
        dimension = self.__matrix.getDimension()
        extended_dimension = self.__matrix.getExtendedDimension()
        for row in range(dimension):
            diagonal_element = matrix[row][row]
            for column in range(extended_dimension):
                if column == extended_dimension - 1:
                    matrix[row][column] /= diagonal_element
                    continue
                if row == column:
                    matrix[row][column] = 0
                    continue
                matrix[row][column] = (-matrix[row][column]) / diagonal_element
        self.__matrix.setConvertedMatrix(matrix)
        print(self.__matrix.createViewStrConvertedMatrix())

    def algorithmGaussZeidel(self):
        converted_matrix = self.__matrix.getConvertedMatrix()
        dimension = self.__matrix.getDimension()
        extended_dimension = self.__matrix.getExtendedDimension()
        k = 0
        eps = self.__matrix.getEpsilon()
        if eps < 1:
            maxIterationNumber = int(100 / eps)
        else:
            maxIterationNumber = int(100 * eps)
        iterations = [[0.0 for x in range(extended_dimension)]
                      for x in range(maxIterationNumber)]
        for row in range(dimension):
            iterations[k][row] = converted_matrix[row][dimension]
        iterations[k][extended_dimension - 1] = 0
        k = k + 1
        for column in range(dimension):
            iterations[k][column] = iterations[k - 1][column]
        try:
            while True:
                for row in range(dimension):
                    s = 0
                    for column in range(extended_dimension):
                        if column == row:
                            continue
                        if column == dimension:
                            s = s + converted_matrix[row][column]
                            break
                        s = s + converted_matrix[row][column] * iterations[k][column]
                    iterations[k][row] = s
                max_accuracy = abs(iterations[k][0] - iterations[k - 1][0])
                for column in range(dimension):
                    if abs(iterations[k][column] - iterations[k - 1][column]) > max_accuracy:
                        max_accuracy = abs(iterations[k][column] - iterations[k - 1][column])
                iterations[k][extended_dimension - 1] = max_accuracy
                k += 1
                if max_accuracy <= eps:
                    break
                for column in range(dimension):
                    iterations[k][column] = iterations[k - 1][column]
        except IndexError as e:
            print(f"Алгоритм не может решить систему с {k} итерациями.")
            k = 20

        print(f"Всего {k} (max={maxIterationNumber}) итераций:")
        for row in range(k):
            if row == 0:
                print(f"№ |", end='')
                for col in range(extended_dimension):
                    if col == extended_dimension - 1:
                        print(f" |epsilon|", end='')
                        break
                    print(f" |x_{(col + 1)}| ", end='')
                print("")
            print(f"{row}| ", end='');
            for var in range(extended_dimension):
                print(f"|{round(iterations[row][var], 6)}| ", end='')
            print()
