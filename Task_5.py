# Raiting structure
raiting_list = [8, 7, 6, 5, 5, 5, 4, 4, 4, 3, 3]
print(f"Текущий рейтинг: {raiting_list}")
new_raiting = int(input("Введите новый элемент рейтинга (1-9): "))
if new_raiting > raiting_list[0]:
    raiting_list = raiting_list[::-1]
    raiting_list.append(new_raiting)
    raiting_list = raiting_list[::-1]

elif new_raiting < raiting_list[-1]:
    raiting_list.append(new_raiting)
else:
    for elem in raiting_list:
        if new_raiting == elem:
            raiting_list = raiting_list[::-1]
            index = raiting_list.index(elem)
            raiting_list.insert(index, str(new_raiting))  # для проверки в str
            raiting_list = raiting_list[::-1]
            break

print(raiting_list)
