class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"Worker full name: {self.name} {self.surname}"

    def get_total_income(self):
        return f"Worker wage: {self._income['wage']}," \
               f" bonus: {self._income['bonus']}," \
               f" total: {sum(self._income.values())}"


person = Position("Peter", "Pen", "Pirate Slayer", 500, 100)
print(person.get_full_name())
print(f"Woker position is: {person.position}")
print(person.get_total_income())
