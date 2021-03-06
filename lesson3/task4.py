# 4. * (вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки
# в формате «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий,
# а значения — словари, реализованные по схеме предыдущего задания и содержащие записи,
# в которых фамилия начинается с соответствующей буквы.
# Например:
# >>> >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# {
#     "А": {
#         "П": ["Петр Алексеев"]
#     },
#     "С": {
#         "И": ["Иван Сергеев", "Инна Серова"],
#         "А": ["Анна Савельева"]
#     }
# }
# Сможете ли вы вернуть отсортированный по ключам словарь?

employee = ("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
organized = {}
def thesaurus(employee):
    for i in employee:
        first_letter = i[0]
        if first_letter in organized:
            organized[first_letter].append(i)
        else:
            organized[first_letter] = [i]
    return(organized)
import pprint
pprint.pprint(thesaurus(employee))

for first_letter in sorted(organized.keys(), reverse=True):
    print(first_letter, organized[first_letter])