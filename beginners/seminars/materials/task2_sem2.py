class Car:
    def __init__(self, max_speed: int = 90, color: str = "red", fuel: int = 40):
        self.__max_speed = max_speed
        self.__color = color
        self.__fuel = fuel

    @staticmethod
    def beep() -> str:
        return "beep"

    def how_fast(self, time: int) -> int:
        return self.__max_speed * time

    def set_max_speed(self, max_speed: int):
        if max_speed < 0 or max_speed > 360:
            raise ValueError("Invalid max speed value")
        self.__max_speed = max_speed
    def get_max_speed(self):
        return self.__max_speed


class Audi(Car):
    def __init__(self, max_speed: int = 200, color: str = "black", fuel: int = 50):
        super().__init__(max_speed, color, fuel)

    @staticmethod
    def beep() -> str:
        return "beep-beep"



my_car = Car()
my_car_2 = Audi(150, "blue", 60)

print(my_car.beep())
print(my_car_2.beep())


print(my_car_2.get_max_speed())

my_car_2.set_max_speed(150)

print(my_car_2.get_max_speed())
