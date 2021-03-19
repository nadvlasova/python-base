"""
Задание 2. Курс Валюты
Написать функцию get_currency_rate(), принимающую в качестве аргумента код валюты
(например, USD, EUR, GBP, ...) в виде строки и возвращающую курс этой валюты по отношению к рублю.
Код валюты может быть в произвольном регистре.
Функция должна возвращать результат числового типа, например float.
Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
Используйте библиотеку requests, чтобы забрать актуальные данные из ЦБ РФ по адресу
http://www.cbr.ru/scripts/XML_daily.asp.
Выведите на экран курсы для доллара и евро, используя написанную функцию.
Рекомендация: выполнить предварительно запрос к этой странице в обычном браузере, посмотреть содержимое ответа.
"""

from urllib.request import urlopen
from xml.etree import ElementTree as etree

def get_currency_rate(cur):
    return rates.get(cur)

cur = ['USD', 'EUR']

rates = {}
with urlopen("https://www.cbr.ru/scripts/XML_daily.asp") as r:
    el = etree.parse(r)
    root = el.getroot()

    for currency in cur:
        rate = el.findtext('.//Valute[CharCode="'+currency+'"]/Value')
        rate = float(rate.replace(',','.'))
        rates[currency] = rate

for c in cur:
    print(c, get_currency_rate(c))



