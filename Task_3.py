cash = 0
lines = 0
print("Оклад менее 20 тыс у сотрудников: ", end="")
with open("text_3.txt", "r", encoding="utf-8") as file:
    for line in file:
        words = line.split()
        if float(words[1]) < 20000:
            print(words[0], end=" ")
        lines += 1
        cash += float(words[1])
    print(f"\nСредняя зарплата: {cash / lines}")
