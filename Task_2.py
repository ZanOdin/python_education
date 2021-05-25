from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def cons(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size
        self.result = 0

    @property
    def cons(self):
        self.result = round(float(self.size / 6.5 + 0.5), 2)
        return self.result

    def __add__(self, other):
        return self.result + other.result


class Costume(Clothes):
    def __init__(self, height):
        self.height = height
        self.result = 0

    @property
    def cons(self):
        self.result = round(float((2 * self.height + 0.3) / 100), 2)
        return self.result

    def __add__(self, other):
        return self.result + other.result


class Clothes:

    @staticmethod
    def main_cons(*sizes):
        result = 0
        for size in sizes:
            result += size
        return result


coat_1 = Coat(15)
coat_2 = Coat(24)
costume_1 = Costume(182)
costume_2 = Costume(178)

clothes = Clothes()

print(f"Расход ткани для пальто: {coat_1.cons + coat_2.cons}")
print(f"Расход ткани для костюма: {costume_1.cons + costume_2.cons}")
print(f"Общий расход ткани для производства: "
      f"{round(clothes.main_cons((coat_1 + coat_2), (costume_1 + costume_2)), 2)}")
