class Trafficlight:
    def __init__(self):
        self.__color = ["red", "yellow", "green"]

    def running(self):
        from time import sleep
        i = 0
        while i < 1:
            print(self.__color[0])
            sleep(7)
            print(self.__color[1])
            sleep(2)
            print(self.__color[2])
            sleep(7)
            print(self.__color[1])
            sleep(2)
            i += 1


light = Trafficlight()
light.running()
