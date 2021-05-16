class Stationery:
    title = ""

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    title = "Ручка"

    def draw(self):
        print(f"({Pen.title}) Напишем что-нибудь ручкой")


class Pencil(Stationery):
    title = "Карандаш"

    def draw(self):
        print(f"({Pencil.title}) Нарисуем что-нибудь карандашом")


class Handle(Stationery):
    title = "Маркер"

    def draw(self):
        print(f"({Handle.title}) Обведем рисунок маркером")


pen = Pen()
pen.draw()
pencil = Pencil()
pencil.draw()
handle = Handle()
handle.draw()
