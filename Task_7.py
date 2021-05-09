# ------------------------Factorial with yield------------------------------------
from math import factorial
from itertools import count, takewhile


def fact(number):
    number_list = [elem for elem in takewhile(lambda x: x <= number, count(1, 1))]
    for item in number_list:
        yield factorial(item)


n = int(input("Введите натуральное число: "))
print(f"\nФакториал {n} равен:")
for el in fact(n):
    print(f"{el}", end=" ")
