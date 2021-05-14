def read_sum(txt_file):
    with open(txt_file, "r", encoding='utf-8') as file:
        numbers = []
        for elem in file.read().split(" "):
            try:
                numbers.append(float(elem))
            except ValueError:
                print("Ошибка. Введите только числа")
        print(sum(numbers))


with open("task_5.txt", "w", encoding='utf-8') as new_file:
    string = input("Введите числа через пробел: ")
    new_file.write(string)

read_sum("task_5.txt")
