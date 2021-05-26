class ComplexNumber:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sign = ["+", "-"]

    def __add__(self, other):

        return f"Addition of two complex numbers: " \
               f"{self.x + other.x} " \
               f"{self.sign[0] if (self.y + other.y) > 0 else self.sign[1]} " \
               f"{abs(self.y + other.y)}i"

    def __mul__(self, other):
        return f"Multiple of two complex numbers: " \
               f"{self.x * other.x - self.y * other.y} " \
               f"{self.sign[0] if (self.y * other.y - self.x * other.y) > 0 else self.sign[1]} " \
               f"{abs((self.y * other.y - self.x * other.y))}i"


first = ComplexNumber(5, -4)
second = ComplexNumber(3, -1)
print(first + second)
print(first * second)