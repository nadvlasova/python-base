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