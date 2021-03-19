"""
Задание 3. * Курс Валюты (расширенный)
Доработать функцию get_currency_rate(): теперь она должна возвращать курс и дату,
на которую этот курс действует (взять из того же файла ЦБ РФ).
Для значения курса используйте тип Decimal (https://docs.python.org/3.8/library/decimal.html) вместо float.
Дата должна быть типа datetime.date.

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
