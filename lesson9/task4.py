'''
4. Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw() (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три производных класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе переопределить метод draw(). Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры каждого класса и положить их в список. Проитерироваться по этому списку и вызвать метод draw()
для каждого элемента.
'''

class Stationery:
    title = ['pen', 'pencil', 'handle']
    def draw(self):
        return ('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        return ('i am a pen')

class Pencil(Stationery):
    def draw(self):
        return ('i am a pencil')

class Handle(Stationery):
    def draw(self):
        return ('i am a handle')

pen = Pen()
pencil = Pencil()
handle = Handle()
all =  [pen, pencil, handle]
for i in all:
    print(i.draw())
#print(pen.draw(),pencil.draw(),handle.draw())