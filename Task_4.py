# =============================================Вариант 1==========================================
def my_func(x, y):
    """Возведение числа x в степень y"""
    try:
        x = float(x)
    except ValueError:
        print("x - Действительное число")
    if y < 0:
        try:
            y = int(y)
            return x ** y
        except ValueError:
            print("y - Целое отрицательное число")
    else:
        print("y - Целое отрицательное число")


try:
    print(round(my_func(15, -3), 8))
except TypeError:
    print()


# =============================================Вариант 2==========================================

def my_func_2(x, y):
    """Возведение числа x в степень y внутри цикла"""
    if y < 0 and x > 0:
        result = 1
        for i in range(abs(y)):
            result *= x
        return 1 / result
    else:
        print("x - действительное положительное число, y - Целое отрицательное число")


try:
    print(my_func_2(float(input()), int(input())))
except TypeError:
    print("x - действительное положительное число, y - целое отрицательное число..")
