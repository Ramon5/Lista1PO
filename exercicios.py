import random


class HelloWorld:
    def __init__(self):
        print("Olá mundo!")


class VectorStorage:
    """
        This class provide vector to numbers inserted by users
    """

    def __init__(self):
        self._vector = []

    def _populate(self):
        for i in range(1, 11):
            number = input(f"Insira o {i}º número: ")
            self._vector.append(int(number))

    def _show(self):
        print("Numbers on vector \n")
        for number in self._vector:
            print(f"{number} ", end="")

    def execute(self):
        self._populate()
        self._show()


class MatrixNumbers:
    """
        This class provide a read numbers and storage in matrix
    """

    def __init__(self):
        self._matrix = []
        self._lines = 10
        self._columns = 10

    def _generate_matrix(self):
        for i in range(self._lines):
            column = []
            for j in range(self._columns):
                number = random.randint(0, 50)
                column.append(int(number))
            self._matrix.append(column)

    def _show(self):
        print("\nMatriz \n")
        for i in range(self._lines):
            for j in range(self._columns):
                print(f"{self._matrix[i][j]} \t", end="")
            print("\n")

    def execute(self):
        self._generate_matrix()
        self._show()


class MaxMinAverage:
    """
        this class provide methods to calculate max, min and average
        from list data
    """

    def __init__(self):
        self._vector = []

    def _read_numbers(self):
        for i in range(1, 11):
            print(f"Informe o {i}º número: ", end="")
            number = input()
            self._vector.append(int(number))

    def _average(self):
        return sum(self._vector) / len(self._vector) if len(self._vector) > 0 else 0

    def execute(self):
        self._read_numbers()
        print(f"\nMáx value: {max(self._vector)}")
        print(f"Min value: {min(self._vector)}")
        print(f"Average: {self._average()}")


class MatrixReader:
    def __init__(self):
        self._matrixA = []
        self._matrixB = []
        self._lines = 10
        self._columns = 10

    def _read_file(self):
        second_matrix = False
        with open("matrix.txt") as source:
            for line in source:
                data = line.split(" ")
                if len(data) == 1:
                    second_matrix = True
                    continue
                self._matrixA.append(
                    list(map(int, data))
                ) if not second_matrix else self._matrixB.append(list(map(int, data)))

    def _sum_matrix(self):
        matrix = []
        for i in range(self._lines):
            line = []
            for j in range(self._columns):
                sum_value = self._matrixA[i][j] + self._matrixB[i][j]
                line.append(sum_value)
            matrix.append(line)

        return matrix

    def _show(self):
        matrix = self._sum_matrix()
        print("\nMatriz Resultante\n")
        for i in range(self._lines):
            for j in range(self._columns):
                print(f"{matrix[i][j]} \t", end="")
            print("\n")

    def execute(self):
        self._read_file()
        self._show()
