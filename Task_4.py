import random

import self as self


class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.direction = \
            random.choice(["West", "East", "North", "South"])

    def go(self):
        print(f"{self.name} went")

    def stop(self):
        print(f"{self.name} stop")

    def turn(self):
        print(f"The {self.name} turn to the {self.direction}")

    def show_speed(self):
        print(f"Now speed is {self.speed}")


class TownCar(Car):
    type = "TownCar"

    def show_speed(self):
        if self.speed > 60:
            print(f"Caution. Over speed! ({self.speed}) "
                  f"Drop speed up to 60")
        else:
            print("Speed is normally.")


class WorkCar(Car):
    type = "WorkCar"

    def show_speed(self):
        if self.speed > 40:
            print(f"Caution. Over speed! ({self.speed}) "
                  f"Drop speed up to 40")
        else:
            print("Speed is normally.")


class SportCar(Car):
    type = "SportCar"

    def show_speed(self):
        if self.speed > 70:
            print(f"Caution. Over speed! ({self.speed}) "
                  f"Drop speed up to 70")
        else:
            print("Speed is normally.")


class PoliceCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed, is_police=True)

    def find_intruder(self, car_name, speed, car_color, car_type):
        if speed > 60 and car_type == "TownCar":
            print(f"Police car goes to arrest {car_color} {car_name} for "
                  f"over speed. ({speed})")
        elif car_type == "WorkCar" and speed > 40:
            print(f"Police car goes to arrest {car_color} {car_name} for "
                  f"over speed. ({speed})")
        elif car_type == "SportCar" and speed > 70:
            print(f"Police car goes to arrest {car_color} {car_name} for "
                  f"over speed. ({speed})")
        else:
            print(f"{car_color} {car_name} speed is normally ({speed}).")


car_town = TownCar("Jiguli", "orange", 60)
car_town.go()

car_town.turn()
car_town.show_speed()
car_town.stop()
print()

car_work = WorkCar("Gazelle", "grey", 50)
car_work.go()

car_work.turn()
car_work.show_speed()
car_work.stop()
print()

car_sport = SportCar("Chevrolette Corvette", "yellow", 95)

car_sport.go()

car_sport.turn()
car_sport.show_speed()
car_sport.stop()
print()
car_police = PoliceCar("Toyota Camry", "white", "80")
car_police.find_intruder(car_town.name, car_town.speed,
                         car_town.color, car_town.type)
car_police.find_intruder(car_work.name, car_work.speed,
                         car_work.color, car_work.type)
car_police.find_intruder(car_sport.name, car_sport.speed,
                         car_sport.color, car_sport.type)
