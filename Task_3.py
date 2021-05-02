while True:
    month = int(input("Введите номер месяца (1-12): "))
    if month > 0 and month <= 12:
        break

# -----------------------------------------------list----------------------------------------------

seasons = ["spring", "summer", "autumn", "winter"]
for season in seasons:
    if month >= 2 and month <= 4:
        season = seasons[0]
    elif month >= 5 and month <= 8:
        season = seasons[1]
    elif month >= 9 and month <= 11:
        season = seasons[2]
    else:
        season = seasons[3]
print(season)

# -----------------------------------------------dict----------------------------------------------

season_dict = {'winter': [12, 1, 2],
               'spring': [3, 4, 5],
               'summer': [6, 7, 8],
               'autumn': [9, 10, 11]}
for value, month_1 in season_dict.items():  # Поиск пары ключ-значение
    for m in month_1:  # Поиск переменной внутри списка значения
        if m == month:  # Сравнения значения с вводом пользователя
            season = value  # Присваивание значения месяца в переменную для вывода
print(season)
