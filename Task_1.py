class Matrix:
    def __init__(self, matrix):
        self.new_matrix = ""
        self.other_matrix = ""
        self.matrix = matrix

    def __str__(self):
        for elem in self.matrix:
            for el in elem:
                self.new_matrix += f"{str(el)} "
            self.new_matrix += "\n"
        return self.new_matrix

    def __add__(self, other):
        try:
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    self.other_matrix += f"{str(self.matrix[i][j] + other.matrix[i][j])} "
                self.other_matrix += "\n"
            return self.other_matrix
        except IndexError:
            return "ERROR: Your matrices must be same."


matrix_1 = Matrix([[1, 3], [6, 7], [6, 3]])
matrix_2 = Matrix([[3, 2], [5, 3], [2, 4]])
print(matrix_1)
print(matrix_2)
print(matrix_1 + matrix_2)

# self.new_matrix += [[f"{str(el)} " for el in elem] for elem in self.matrix]
# self.new_matrix += [[f"{str(self.matrix[i])}" for i in range(r)] for r in range(len(self.matrix))]
