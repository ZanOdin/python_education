# ==============================================2================================================
# Task_2
print("Для добавления элемента в список введите значение, для остановки нажмите Enter")
new_list = list()
first = list()
second = list()
while True:
    value = input("Введите значение: ")
    if value == "":
        break
    else:
        new_list.append(value)
print(f"Оригинал списка: {new_list}")
elem = 0
while elem < len(new_list):
    first = new_list[elem:elem + 2]
    first.reverse()
    second.append(first)
    elem += 2
print(f"Реверсия двух отдельных элементов списка: {sum(second, [])}")
