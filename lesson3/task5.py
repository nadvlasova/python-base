# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из двух случайных слов,
# взятых из трёх списков:
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#         Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)?
# Сможете ли вы сделать аргументы именованными?

import random
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_joke():
    '''
    Функция формирует шутку из трех случайных слов взятых из предложенных списков
    :return: шутку с типом строка
    '''
    a = random.choice(nouns)
    b = random.choice(adverbs)
    c = random.choice(adjectives)
    joke = [a, b, c]
    return (' ' .join(joke))

def get_jokes(n):
    '''
    Функция создает список из запрошенного количества шуток
    :param n: количество
    :return: список шуток в виде строк
    '''
    jokes_list = []
    for i in range(n):
        jokes_list.append(get_joke())
    return jokes_list

print(get_jokes(2))

def get_jokes_uniq(n):
    '''
    Функция формирования шуток из неповторяющихся слов
    :param n: количество шуток
    :return: список строк в виде шуток
    '''

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    n = min(n, len(nouns),len(adverbs),len(adjectives))
    jokes = []
    for i in range(n):
        a = random.choice(nouns)
        b = random.choice(adverbs)
        c = random.choice(adjectives)
        joke = f'{a} {b} {c}'
        jokes.append(joke)

        nouns.remove(a)
        adverbs.remove(b)
        adjectives.remove(c)
    return jokes
print(get_jokes_uniq(5))