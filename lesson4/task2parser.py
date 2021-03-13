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