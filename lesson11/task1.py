'''
. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
'''
# изначально у меня все было проще, но кода было намного больше и не все работало, радует одно, логика была такая же
class Date:

    def __init__(self, date):
        self.day, self.month, self.year = self.on_get_date(date) # до этого точно сама не дошла, сложно, страшно
        self.correct_date(self.day, self.month, self.year)       # хотя подумав понятно, что и откуда остаются вопросы почему так и зачем?

    def __str__(self):
        return f'{self.day:02}.{self.month:02}.{self.year:04}' # чтобы так красиво формат чисел прописать тоже нужна практика и время

    @classmethod
    def on_get_date(cls, date):
        day, month, year = map(int, date.split('-'))
        return day, month, year

    @staticmethod
    def correct_date(day, month, year):
        if not (1 <= month <= 12):
            raise ValueError('формат месяца неверный')
        if month == 2:
            last_day = 29 if year % 4 == 0 and year % 100 != 0 or year % 1000 == 0 else 28
        if month in [1, 3, 5, 7, 8, 10, 12]:
            last_day = 31
        if month in [4, 6, 9, 11]:
            last_day = 30
        if not (1 <= day <= last_day): # вот этот день вообще непонятно как вычислился и откуда взялся
            raise ValueError(f'День должен быть в пределах 1-{last_day}')

dates = ['11-04-2021', '10-24-2021', '32-01-2021', '29-02-2021', '29-02-2020']

for date in dates:
    try:
        dt = Date(date)
        print(dt)
    except ValueError as e:  # и что значит эта e тоже фантастика
        print('Неверный формат:', e)




