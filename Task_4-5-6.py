# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
# в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также
# других данных, можно использовать любую подходящую структуру, например словарь.
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
# для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных
# на уроках по ООП.
from abc import ABC, abstractmethod


class Warehouse:
    def __init__(self):
        self.capacity = 2500
        self.warehouse_dict = {}
        self.subdivision_dict = {}

    def accept_goods(self, name, quantity, size_type, appointment):
        self.capacity -= quantity * size_type
        if self.capacity > 0:
            self.warehouse_dict[name.lower()] = {'quantity': quantity, 'size_type': size_type, 'appointment': appointment}
        else:
            print(f"You haven't more place for new equipment")

    def show_goods(self):
        for key, elem in self.warehouse_dict.items():
            print(f"{key} -- {elem}")
        print(f"Free space is: {self.capacity}")

    def transfer_of_goods(self):
        new_list = []

        for num, value in enumerate(self.warehouse_dict, 1):
            new_list.append([num, value])
            print(num, value)
        try:
            choice = int(input('Enter the item number for transfer: '))
            for elem in new_list:
                if elem[0] == choice:
                    name = (" ".join(self.warehouse_dict[elem[1]].keys()).split(" "))
                    quantity_choice = int(input(f'Quantity of {elem[1]} is: {self.warehouse_dict[elem[1]][name[0]]} Enter the quantity: '))
                    self.capacity += quantity_choice * self.warehouse_dict[elem[1]][name[1]]
                    if self.warehouse_dict[elem[1]][name[0]] - quantity_choice <= 0:
                        value = self.warehouse_dict.pop(elem[1])
                        self.subdivision_dict = {value['appointment']: {elem[1]: value['quantity']}}
                    else:
                        self.warehouse_dict[elem[1]][name[0]] -= quantity_choice
                        value = self.warehouse_dict[elem[1]]
                        self.subdivision_dict = {value['appointment']: {elem[1]: value['quantity']}}
                    Warehouse.show_goods(self)
                    return self.subdivision_dict
        except ValueError:
            print(f"Incorrect. Enter the list item number.")

    @classmethod
    def get_subdivision(cls, list_s):
        return f"Equipment confirmed: {list_s}"


class OfficeEquipment:
    def __init__(self, quantity):
        try:
            self.quantity = int(quantity)
        except ValueError:
            print("Need only Numbers!")
        self.name = ""
        self.tech_types = [1, 2, 3, 4, 5]
        self.subdivision = ['Administration', 'Workshop', 'Warehouse', 'Main Office', 'Security']

    def __str__(self):
        return f"{self.name} in the amount of {self.quantity} pieces."


class Printer(OfficeEquipment):
    def __init__(self, quantity):
        super().__init__(quantity)
        self.name = "Printer"
        self.size = self.tech_types[3]
        self.subdivision = self.subdivision[1]


class Scanner(OfficeEquipment):
    def __init__(self, quantity):
        super().__init__(quantity)
        self.name = "Scanner"
        self.size = self.tech_types[2]
        self.subdivision = self.subdivision[3]


class Xerox(OfficeEquipment):
    def __init__(self, quantity):
        super().__init__(quantity)
        self.name = "Xerox"
        self.size = self.tech_types[2]
        self.subdivision = self.subdivision[3]


class Computer(OfficeEquipment):
    def __init__(self, quantity):
        super().__init__(quantity)
        self.name = "Computer"
        self.size = self.tech_types[4]
        self.subdivision = self.subdivision[0]


class Camera(OfficeEquipment):
    def __init__(self, quantity):
        super().__init__(quantity)
        self.name = "Camera"
        self.size = self.tech_types[0]
        self.subdivision = self.subdivision[-1]


try:
    printer = Printer(100)
    scanner = Scanner(100)
    xerox = Xerox(100)
    comp = Computer(100)
    camera = Camera(60)
    warehouse = Warehouse()

    warehouse.accept_goods(printer.name, printer.quantity, printer.size, printer.subdivision)
    warehouse.accept_goods(scanner.name, scanner.quantity, scanner.size, scanner.subdivision)
    warehouse.accept_goods(xerox.name, xerox.quantity, xerox.size, xerox.subdivision)
    warehouse.accept_goods(comp.name, comp.quantity, comp.size, comp.subdivision)
    warehouse.accept_goods(camera.name, camera.quantity, camera.size, camera.subdivision)
    warehouse.show_goods()
    subd = warehouse.transfer_of_goods()
    show = warehouse.get_subdivision(subd)
    print(show)
except AttributeError:
    print("Incorrect Enter.")