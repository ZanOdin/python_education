profit = float(input("Введите выручку: "))
costs = float(input("Введите издержки: "))

finance_result = profit - costs

if (finance_result > 0):
    print(f"Ваша прибыль составляет: {finance_result:.0f}")
    profitability = (profit / costs) * 100
    print(f"Рентабельность вашей фирмы составляет: {profitability:.0f}%")
    staff = int(input("Введите количество сотрудников вашей фирмы: "))
    everyones_profit = finance_result / staff
    print(f"Прибыль фирмы в расчете на одного сотрудника составляет:{everyones_profit:.0f}")
else:
    print(f"Ваши убытки составляют: {-finance_result:.0f}")
