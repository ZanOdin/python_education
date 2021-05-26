# class MyClass:
# #     def __init__(self, name, surname):
# #         self.name = name
# #         self.surname = surname
# #
# #     @staticmethod
# #     def get_fio(obj):
# #         return f"{obj.name} {obj.surname}"
# #
# #     @classmethod
# #     def set_fio(cls, data):
# #         n, s = data
# #         return cls(n, s)
# #
# #
# # my_list = ["Man", "Lo"]
# #
# # one = MyClass.set_fio(my_list)
# # print(MyClass.get_fio(one))

class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def set_numbers(cls, date):
        num, mon, year = date.split('-')
        date = int(num), int(mon), int(year)
        return cls(date)

    @staticmethod
    def validation_date(obj):
        correct_date = False
        if 1 <= obj.date[2] <= 2021:
            if 1 <= obj.date[1] < 8 and obj.date[1] != 2:
                if obj.date[1] % 2 == 0:
                    if 1 <= obj.date[0] <= 30:
                        correct_date = True
                elif obj.date[1] % 2 == 1:
                    if 1 <= obj.date[0] <= 31:
                        correct_date = True
            elif 8 <= obj.date[1] <= 12:
                if obj.date[1] % 2 == 0:
                    if 1 <= obj.date[0] <= 31:
                        correct_date = True
                else:
                    if 1 <= obj.date[0] <= 31:
                        correct_date = True
            elif obj.date[1] == 2:
                if obj.date[2] % 4 == 0 and 1 <= obj.date[0] <= 29:
                    correct_date = True
                elif 1 <= obj.date[0] <= 28:
                    correct_date = True
        if correct_date:
            return f"Your date is correct: {obj.date}"
        else:
            return f"Error. There is no such date... {obj.date}"


my_date = input("Enter the date (day-month-year): ")
first = Date.set_numbers(my_date)
print(Date.validation_date(first))
