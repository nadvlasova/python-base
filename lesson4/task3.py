"""
Задание 3. * Курс Валюты (расширенный)
Доработать функцию get_currency_rate(): теперь она должна возвращать курс и дату,
на которую этот курс действует (взять из того же файла ЦБ РФ).
Для значения курса используйте тип Decimal (https://docs.python.org/3.8/library/decimal.html) вместо float.
Дата должна быть типа datetime.date.

"""

from urllib.request import urlopen
from xml.etree import ElementTree as etree
import datetime
import decimal

cur = ['USD', 'EUR']
def get_currency_rate(cur):
    for i in cur:
        if i == 'USD':
            print(cur_USD, rate_USD)
        elif i == 'EUR':
            print(cur_EUR, rate_EUR)
        elif i != 'USD' and i != 'EUR':
            print(None)

with urlopen("https://www.cbr.ru/scripts/XML_daily.asp") as r:
    el = etree.parse(r)
    root = el.getroot()

    cur_USD = el.findtext('.//Valute[@ID="R01235"]/CharCode')
    rate_USD = el.findtext('.//Valute[@ID="R01235"]/Value')
    rate_USD = decimal.Decimal(rate_USD.replace(',', '.'))

    cur_EUR = el.findtext('.//Valute[@ID="R01239"]/CharCode')
    rate_EUR = el.findtext('.//Valute[@ID="R01239"]/Value')
    rate_EUR = decimal.Decimal(rate_EUR.replace(',', '.'))

    date_rate = el.find('ValCurs/[Date]')
    print(date_rate)

print(get_currency_rate(cur))
# print(date_rate)
