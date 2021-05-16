class Road:

    def __init__(self, lenght, width):
        self._lenght = int(lenght)
        self._width = int(width)

    def mass_result(self):
        return f"{int(self._lenght * self._width * 25 * 5 / 1000)} т"


new_road = Road(2000, 20)
print(new_road.mass_result())
