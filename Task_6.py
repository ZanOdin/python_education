lines = [line.strip() for line in open("text_6.txt", encoding='utf-8')]
digits = []
lessons = []
lesson_dict = {}
x = 0
for line in lines:
    word = line.split(" ")
    for elem in word[1:4]:
        digits = [el for el in elem if el.isdigit()]
        digits = ''.join(digits)
        if digits != "":
            lessons.append(int(digits))
    lesson_dict.update({word[0]: sum(lessons)})
    lessons.clear()
for key, value in lesson_dict.items():
    print(key, value)


#  Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}