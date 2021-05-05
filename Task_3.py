def my_func(val_1, val_2, val_3):
    """Суммирует два наибольших аргумента"""
    all_sum = sum([val_1, val_2, val_3])
    return (all_sum - min(val_1, val_2, val_3))


print("Введите три числа для получения результата:")
try:
    print(my_func(int(input()), int(input()), int(input())))
except ValueError:
    print("Error")
