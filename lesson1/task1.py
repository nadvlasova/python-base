# #1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
# до минуты: <s> сек;
# * до часа: <m> мин <s> сек;
# * до суток: <h> час <m> мин <s> сек;
# * *до месяца, до года, больше года: по аналогии.
print('Введите число: ')
a = int(input())
if a < 60:
    print(a, 'сек.')
elif a > 60 and a < 3600: #min
    m = a // 60
    s = a % 60
    print(m,  'мин.', s,  'сек.')
elif a > 3600 and a < 86400: #hour
    h = a // 3600
    m = (a % 3600) // 60
    s = (a % 3600) % 60
    print(h, 'час.', m, 'мин.', s,'сек.')
elif a > 86400 and a < 2629743: #day
    d = a // 86400
    h = (a % 86400) // 3600
    m = ((a % 86400) % 3600) // 60
    s = (a % 86400) % 60
    print(d, 'дн.' ,h, 'час.', m, 'мин.', s, 'сек.')
elif a > 2629743 and a < 31556926: #month
    month = a // 2629743
    day = (a % 2629743) // 86400
    hour = ((a % 2629743) % 86400) // 3600
    min = (((a % 2629743) % 86400) % 3600) // 60
    sec = (a % 2629743) % 60
    print(month, 'мес.', day, 'дн.', hour, 'час.', min, 'мин.', sec, 'сек.')
elif a > 31556926: #years
    year = a // 31556926
    month = (a % 31556926) //2629743
    day = ((a % 31556926) % 2629743) // 86400
    hour = (((a % 31556926) % 2629743) % 86400) //3600
    min = ((((a % 31556926) % 2629743) % 86400) % 3600) // 60
    sec = (((((a % 31556926) % 2629743) % 86400) % 3600) %60) %60
    print(year, 'год', month, 'мес.', hour, 'час.', min, 'мин.', sec,'сек.')
