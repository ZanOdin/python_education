def number_list():
    """Суммирует набор чисел, введенных пользователем"""
    final = 0
    while True:
        numbs = input("Введите числа через пробел: ")
        numbs = numbs.split()
        numbs_int = []
        interim = 0
        for numb in numbs:
            if numb.isdigit() == True:
                numbs_int.append(int(numb))
            elif numb.lower() == "q":
                final += sum(numbs_int)
                return print(f"{final}")
            else:
                print("Error")
        interim = sum(numbs_int)
        final += interim
        if final == interim:
            print(f"Результат: {interim}")
        else:
            print(f"{interim} ({final})")


number_list()
