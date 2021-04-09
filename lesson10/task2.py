'''
2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
a) Создать абстрактный класс Clothes (одежда).
OK
b) Сделать в этом классе свойство cloth_size (используя декоратор @property) - размер ткани, необходимый для производства одежды.
Это свойство должно вычислять размерт ткани, вызывая абстрактный метод self.get_size().
c) Сделать два производных класса одежды: Suit (костюм) и Coat (Пальто).
В конструктор Suit должен принимать параметр height (рост), а Coat - size (размер).
Для определения расхода ткани по каждому типу одежды внутри метода get_size() использовать формулы:
для пальто: (size/6.5 + 0.5)
для костюма: (2*height + 0.3)
d) Создать список из 10 единиц одежды случайно выбирая один из двух возможных типов со случайным параметром.
e) Распечатать список одежды: размер требуемой ткани, тип и параметр.
Рассчитать и вывести на экран общий объем ткани, необходимый для пошива всей одежды из этого списка, используя свойство cloth_size. Например:
30.3 - Suit (height: 15)
20 - Coat (size: 3)
13.5 - Coat (size: 2)
4.3 - Suit (seze: 2)
...
Итого: 250.3
'''

from abc import ABC, abstractmethod
class Clothes(ABC):
    @property
    def cloth_size(self):
        # размер ткани, необходимый для производства одежды.
        def get_size(self):
            self.suit = (2 * 'height' + 0.3)
            self.coat = 'size'/6.5 + 0.5
# self.get_size()
class Suit(Clothes):
    def __init__(self, height):
        self.height = height

class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    def __iter__(self):
        return

cloth = Clothes()
clotheth

for c in cloth:
    print(c.cloth_size)
# print(суммарный cloth_size)