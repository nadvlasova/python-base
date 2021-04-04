'''
5. Реализуйте базовый класс Car. при создании класса должны быть переданы атрибуты: color (str), name (str).
---OK---
реализовать в классе методы: go(speed), stop(), turn(direction), которые должны изменять состояние машины -
для хранения этих свойств вам понадобятся дополнительные атрибуты - придумайте какие.
!!!!!!!!!!С этим не разобралась, не хватило времени и логики
добавьте метод is_police() - который возвращает True/False, в зависимости от того является ли этот автомобиль
полицейским (см.дальше)
---OK---
Сделайте несколько производных классов: TownCar, SportCar, WorkCar, PoliceCar;
---OK---
Добавьте в базовый класс метод get_status(), который должен возвращать в виде строки название, цвет,
текущую скорость автомобиля и направление движения (в случае если автомобиль едет), для полицейских автомобилей
перед названием автомобиля должно идти слово POLICE;
---OK---
Для классов TownCar и WorkCar в методе get_status() рядом со значением скорости должна выводиться фраза "ПРЕВЫШЕНИЕ!",
если скорость превышает 60 (TownCar) и 40 (WorkCar).
---OK---
Создайте по одному экземпляру каждого производного класса. В цикле из 10 итераций, для каждого автомобиля
сделайте одно из случайных действий: go, stop, turn со случайными параметрами. После каждого действия показывайте статус автомобиля.
!!!!!!!!!! Не выполненный пункт 2 подтянул невыполнение этого пункта
'''

class Car:
    def __init__(self, color = 'black', name = 'Ford'):
        self.color = color
        self.name = name

    def __str__(self):
        return f'{self.color} {self.name}'

    def go(self, speed):
        if speed <= self.speed_limit:
            self.speed = speed
        else:
            raise ValueError("ПРЕВЫШЕНИЕ!")


    def stop(self, speed):
        if self.speed == 0:
           print('This car is stop!')
        else:
            self.speed = speed

    def turn(self, direction):
        if self.direction == 'right':
            print('Turn right')
        elif self.direction  == 'left':
            print('Turn left')
        elif self.direction == 'straight':
            print('Go straight')

    def is_police(self, name):
        if self.name == 'police':
            return True
        else:
            False

    def get_status(self):
        return f'{self.name}, {self.color}, {self.speed}, {self.direction}'

class TownCar(Car):
    speed_limit = 60
    def __init__(self, color, name, speed, direction):
        super().__init__(color, name)
        self.speed = speed
        self.direction = direction

    def __str__(self):
        if self.speed > self.speed_limit:
            self.speed = self.speed,'ПРЕВЫШЕНИЕ!'
        return f'{self.color} {self.name} {self.speed} {self.direction} '

class SportCar(Car):
    def __init__(self, color, name, speed, direction):
        super().__init__(color, name)
        self.speed = speed
        self.direction = direction

    def __str__(self):
        return f'{self.color} {self.name} {self.speed} {self.direction} '

class WorkCar(Car):
    speed_limit = 40
    def __init__(self, color, name, speed,  direction):
        super().__init__(color, name)
        self.speed = speed
        self.direction = direction

    def __str__(self):
        if self.speed > self.speed_limit:
            self.speed = self.speed,'ПРЕВЫШЕНИЕ!'
        return f'{self.color} {self.name} {self.speed} {self.direction} '

class PoliceCar(Car):
    def __init__(self, color, name, speed, direction):
        super().__init__(color, name)
        self.speed = speed
        self.direction = direction

    def __str__(self):
        return f'police: {self.color} {self.name} {self.speed} {self.direction} '


# car = Car('black', 'Ford')
# print(car)
car1 = TownCar('blue', 'BMW', 160, 'left')
car2 = SportCar('red', 'Porshe', 160, 'left')
car3 = WorkCar('white', 'Kamaz', 60, 'right')
car4 = PoliceCar('yellow', 'police', 0, 'None')
print(car1)
print(car2)
print(car3)
print(car4)

print(car4.is_police(car4))

print(car1.get_status())
print(car2.get_status())
print(car3.get_status())
print(car4.get_status())

print(car1.get_status())