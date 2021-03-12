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

cur = ['USD', 'EUR']
def get_currency_rate(cur):
    for i in cur:
        if i == 'USD':
            print(cur_USD, rate_USD)

        elif i == 'EUR':
            print(cur_EUR, rate_EUR)
    else:
        print(None)

with urlopen("https://www.cbr.ru/scripts/XML_daily.asp") as r:
    el = etree.parse(r)
    root = el.getroot()

    cur_USD = el.findtext('.//Valute[@ID="R01235"]/CharCode')
    rate_USD = el.findtext('.//Valute[@ID="R01235"]/Value')
    rate_USD = float(rate_USD.replace(',','.'))

    cur_EUR = el.findtext('.//Valute[@ID="R01239"]/CharCode')
    rate_EUR = el.findtext('.//Valute[@ID="R01239"]/Value')
    rate_EUR = float(rate_EUR.replace(',', '.'))

print(get_currency_rate(cur))



