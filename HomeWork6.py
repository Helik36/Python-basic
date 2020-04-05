# Задание 1
from time import sleep

class TraficLight:

    __colors = ['Красный', 'Жёлтый', 'Зелённый', 'Жёлтый']

    def running(self):
        while True:
            for w in TraficLight.__colors:
                print(f"Сейчас: {w}")
                if w == TraficLight.__colors[0]:
                    sleep(7)
                elif w == TraficLight.__colors[1]:
                    sleep(2)
                elif w == TraficLight.__colors[2]:
                    sleep(7)
                elif w == TraficLight.__colors[3]:
                    sleep(2)

traf = TraficLight()
traf.running()

# Задание 2 ___________________________________________________________________________________________________________

class Road:
   def __init__(self, length, width, volume, w):
       self._length = length
       self._width = width
       self.volume = volume
       self.w = w


   def mass(self):
       return self._length * self._width * self.volume * self.w

ram = Road(20, 5000, 25, 5)
print(ram.mass())

# Задание 3 ___________________________________________________________________________________________________________

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print("Имя сотрудника:", self.name, self.surname)

    def get_total_income(self):
        print("Зп состовляет:", self._income["wage"] + self._income["bonus"])

a = Position("Гера", "Майер", "Крутой", 20000, 10000)
a.get_full_name()
print("Должность:", a.position)
a.get_total_income()

# Задание 4 ___________________________________________________________________________________________________________

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_poice = is_police

    def show_speed(self):
        print(f"Текущая скорость: {self.speed}")

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self, directuon):
        self.direction = directuon
        print(f"Машина повернула {self.direction}")

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print(f"Обыная машина. speed: {speed}, color: {color}, name: {name}, is police: {is_police}")
        if self.speed > 60:
            print("please, slow!!!\n")
        else:
            print("Speed is normal!\n")

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print(f"Спортивная машина. speed: {speed}, color: {color}, name: {name}, is police: {is_police}\n")

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print(f"Рабочая Машина. speed: {speed}, color: {color}, name: {name}, is police: {is_police}")
        if self.speed > 40:
            print("please, slow!!!\n")
        else:
            print("Speed is normal!\n")

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print(f"Полицейская Машина. speed: {speed}, color: {color}, name: {name}, is police: {is_police}")

my_car = TownCar(59, "Синий", "Audi", False)
my_car.go()
my_car.turn("налево")
print()
sport_car = SportCar(120, "Black", "Rolf", False)
sport_car.go()
sport_car.show_speed()
print()
work_car = WorkCar(55, "Gray", "Vaz", False)
work_car.stop()
print()
police = PoliceCar(70, "Red", "Ford", True)

# Задание 5 ___________________________________________________________________________________________________________

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки: {self.title}")

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Рисуем {self.title}ой")

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Рисуем {self.title}ом")

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Рисуем {self.title}ом")

j = Stationery("Ручка")
j.draw()

pen = Pen("Ручк")
pen.draw()

p = Pencil("Карандаш")
p.draw()

h = Handle("Маркер")
h.draw()
