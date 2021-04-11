'''
3. Реализовать базовый класс Employee (сотрудник).
определить атрибуты: name (имя), surname (фамилия), которые должны передаваться при создании экземпляра Employee;
---OK---
создать класс Position (должность) с аттрибутами employee (сотрудник/Employee), position (должность/str),
income (вознаграждение/dict) - атрибуты также задаются при создании экземпляра класса;
---OK---
последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus};
!!!!!!!!!! Создание словаря ввело в страх, делала пока все, что понимала, без доп. разборок(все эти строки, словари,
множества, кортежи, их методы, циклы ещё плохо отложились в голове, буду отрабатывать)
в классе Position реализовать методы получения полного имени сотрудника get_full_name() и дохода
с учётом премии get_total_income() (wage + bonus);
---OK---
проверить работу примера на реальных данных: создать экземпляры классов Employee, Position,
вывести на экран имя сотрудника, его должность и вознаграждение сотрудника, используя методы класса Position.
!!!!!!!!!!!! По отдельности выводить получается, а вот как прописать, чтобы все вместе выводилось пока не помню, надо
пересмотреть вебинар, но уже следующую тему пора разбирать, а то домашку следующую не успею сделать.
'''

class Employee:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{self.name} {self.surname}'


class Position:

    def __init__(self, employee, position, wage):
        self.employee = employee
        self.position = position
        self.wage = wage


    # def __str__(self):
    #     return f'{self.employee} - {self.position} {self.income}'

    def get_full_name(self, employee ):
        return  employee #f'{self.name} {self.surname}'


    def get_total_income(self, wage):
        bonus = wage / 100 * 25
        income = wage + bonus
        return income



    def __str__(self):
        return f'{self.employee} - {self.position} - {self.wage}'


employee1 = Employee('Vasy', 'Pupkin')
employee2 = Employee('Kat', 'Braun')
employee3 = Employee('Nik', 'Klaus')
employee4 = Employee('Santa', 'Dru')
position1 = Position( employee1, 'director', 50000)
position2 = Position( employee2, 'manager', 25000)
position3 = Position( employee3, 'worker', 35000)
position4 = Position( employee4, 'cleaner', 15000)

#print(employee)
print(position1)
print(position2)
print(position3)
print(position4)

print(position1.get_full_name(employee1))
print(position2.get_full_name(employee2))

print(position1.get_total_income(30000))
# print(position2.get_total_income())
