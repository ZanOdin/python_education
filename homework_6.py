a = int(input("Количество километров в первый день: "))
b = int(input("Необходимое количество километров: "))
days = 1
print("Результат:\n")
print(f"{days}-й день: {a:.2f}")
while (a <= b):
        a *= 1.1
        days += 1
        print(f"{days}-й день: {a:.2f}")
print(f"\nОтвет: на {days}-й день спортсмен достиг результата - не менее {b} км")