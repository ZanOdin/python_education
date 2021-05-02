string = input("Введите слова через пробел: ").split()
for ind, s in enumerate(string, 1):
    print(ind, s[:10])
