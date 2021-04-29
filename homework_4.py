number = int(input("Введите число: "))
high_number = number % 10
while number:
    number = number // 10
    if high_number < number % 10:
        high_number = number % 10
print(high_number)
