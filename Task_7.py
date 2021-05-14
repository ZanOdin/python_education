import json

lines = [line.strip() for line in open('text_7.txt', encoding='utf-8')]
final_dict = {}
average_dict = {}
average = 0
profit_plus = 0
profit = []
for line in lines:
    word = line.split(" ")
    profit = int(word[2]) - int(word[3])
    final_dict.update({word[0]: profit})
    if profit > 0:
        average += profit
        profit_plus += 1
average_dict.update({"average_profit": average / profit_plus})
print([final_dict, average_dict])

with open("my_text_7.json", "w", encoding='utf-8') as f:
    json.dump([final_dict, average_dict], f, indent=4, ensure_ascii=False)

#  Создать (не программно) текстовый файл, в котором каждая строка должна
#  содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
# среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не
# включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить
# ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000},
# {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.
