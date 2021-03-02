# 2. * (вместо задачи 1) Доработать предыдущую функцию num_translate_adv():
# реализовать корректную работу с числительными, начинающимися с заглавной буквы.
# Например:
# >>> >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"

rus = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять', ]
english = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', ]
lib_tr = dict(zip(english, rus))
lib_tr_up = dict([[k.capitalize(), v.capitalize()] for k, v in lib_tr.items()])

def num_translate():
    for i in lib_tr:
        if world == i:
            return (lib_tr[world])
    for i in lib_tr_up:
        if world == i:
            return (lib_tr_up[world])

world = input('Введите слово ')
print(num_translate())
