# 3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников
# и возвращающую словарь, в котором ключи — первые буквы имен,
# а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# Например:
# >>> >>> thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"], "П": ["Петр"]
# }
# Подумайте: полезен ли будет вам оператор распаковки? Сможете ли вы вернуть отсортированный по ключам словарь?

employee = ["Иван", "Мария", "Петр", "Илья"]
organized = {}
def thesaurus(employee):
    for i in employee:
        first_letter = i[0]
        if first_letter in organized:
            organized[first_letter].append(i)
        else:
            organized[first_letter] = [i]
    return(organized)

print(thesaurus(employee))


