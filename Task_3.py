class Cell:
    def __init__(self, cell):
        self.cell = cell

    def make_order(self, row):
        for _ in range(self.cell // row):
            print("|" * row)
        print("|" * (self.cell % row) + "\n")

    def __add__(self, other):
        return f"|" * (self.cell + other.cell)

    def __sub__(self, other):
        result = self.cell - other.cell
        if result > 0:
            return f"|" * result
        else:
            return "Result is less then zero."

    def __mul__(self, other):
        return f"|" * (self.cell * other.cell)

    def __truediv__(self, other):
        try:
            return f"|" * round(self.cell / other.cell)
        except ZeroDivisionError:
            return "Can't be divided by zero"


cell_1 = Cell(7)
cell_2 = Cell(3)
print(cell_1 + cell_2)
print(cell_1 * cell_2)
print(cell_1 - cell_2)
print(cell_1 / cell_2)
print()
cell_1.make_order(5)
cell_2.make_order(3)

