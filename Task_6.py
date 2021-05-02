# Структура данных "Товары"
product_type = 0
dictionary = {}
analitic_dict = {}
number = 0
# Вывод меню
products = []
name_values = []
price_values = []
quantity_values = []
type_values = []

print("Добро пожаловать в Вашу базу данных товаров. Для выбора категории введите соответствующую цифру")
while True:
    print("1. Вывести список")
    print("2. Добавить новый товар")
    print("3. Аналитика товаров")
    print("4. Выход")
    choice = int(input("\nВвод: "))

    if choice == 1:
        for elem in products:
            print(elem)

    elif choice == 2:
        number += 1
        dictionary["название"] = input("\nВведите наименование товара: ")
        name_values.append(dictionary["название"])
        dictionary["цена"] = (int(input("Введите цену за единицу товара: ")))
        price_values.append(dictionary["цена"])
        dictionary["количество"] = int(input("Введите количество товара: "))
        quantity_values.append(dictionary["количество"])
        dictionary["ед"] = input("Введите единицу измерения (шт, компл и тд): ")
        type_values.append(dictionary["ед"])
        type_values = set(type_values)
        type_values = list(type_values)
        dict_copy = dictionary.copy()
        analitic_dict = {"название": name_values,
                         "цена": price_values,
                         "количество": quantity_values,
                         "ед" : type_values}
        new_tuple = (number, dict_copy)
        products.append(new_tuple)
        print("Товар успешно добавлен.\n")

    elif choice == 3:
        for key, value in analitic_dict.items():
            print(key, value)

    elif choice == 4:
        break
