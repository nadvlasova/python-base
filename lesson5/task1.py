"""
Задание 1. Функция-генератор rand_nums
Написать функцию-генератор rand_nums, генерирующую N случайных целых чисел в
диапазоне 1 до 100 (включительно). Количество чисел N, которое выдаст генератор
передается в функцию через параметр:
"""
import random

def rand_nums(n):

    counter = 0
    while True:
        if counter >= n:
            return
        a = (random.randint(1, 100))
        yield a
        counter += 1

rand5 = rand_nums(5)
print(type(rand5))
print(next(rand5))
print(next(rand5))
print(next(rand5))
print(next(rand5))
print(next(rand5))
print(next(rand5))
print(next(rand5))

