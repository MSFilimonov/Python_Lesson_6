class Car:
    name: str
    color: str
    speed: int
    is_police: bool

    def __init__(self, name, color, speed, is_police):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        return f'начал движение'

    def stop(self):
        return f'остановился'

    def tern_r(self):
        return f'повернул направо'

    def tern_l(self):
        return f'повернул налево'

    def show_speed(self):
        return self.speed


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'превысил скорость'
        else:
            return self.speed


class SportCar(Car):
    def sport_car(self):
        return f'- sport car.'


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'превысил скорость'
        else:
            return self.speed


class PoliceCar(Car):
    def ispolice(self):
        if self.is_police is True:
            return "- police car."


moskvich = TownCar("ИЖ 2141", "Red", 80, False)
gazel = WorkCar("Газель", "Белая", 30, False)
oka = SportCar("ОКА", "Желтая", 120, False)
uaz = PoliceCar("УАЗ", "Синий", 100, True)

print(
    f'Марка городского авто: {moskvich.name}.\nЦвет рабочей машины: {gazel.color}. \nСкорость спортивного авто: {oka.speed}км/ч.\nУАЗ - полицейский автомобиль: {uaz.is_police}.')
print(f'ОКА {oka.sport_car()}\nОКА {oka.go()} и {oka.tern_l()}.')
print(f'ИЖ 2141 {moskvich.show_speed()} и {moskvich.stop()}.')
print(f'Газель {gazel.tern_r()} и его скорость составляет сейчас {gazel.show_speed()}км/ч.')
print(f'УАЗ {uaz.ispolice()}')
