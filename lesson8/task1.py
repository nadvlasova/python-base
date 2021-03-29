'''
1. Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя и почтовый домен
из email адреса и возвращает их в виде словаря. Если адрес не валиден, выбросить исключение ValueError. Пример:
#>>> email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
#>>> email_parse('someone@geekbrainsru')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
    raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru
Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении;
имеет ли смысл в данном случае использовать функцию re.compile()?
'''
# 1 - разбить на объекты
# 2 - вытащить имя пользователя и почтовый домен
# 3 - создать словарь и закинуть данные в словарь
# 4 - проверка валидности адреса
# 5 - исключение при невалидности

import re

# email = 'someone@geekbrains.ru'
def email_parse (email):
    res2 = re.split('', email)
    if '@' and '.' not in res2:
        raise ValueError('wrong email:', email)  # выбросили исключение
    res = re.split(r'[@]', email)
    username = res[0]
    domain = res[1]
    res_dict = {'username': username, 'domain': domain}
    return res_dict



print(email_parse('someone@geekbrains.ru'))
