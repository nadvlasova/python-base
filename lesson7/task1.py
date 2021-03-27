# import os
#
# names_folders = ('settings', 'mainapp', 'adminapp', 'authapp')
# for i in names_folders:
#     tmp_file_name = os.path.join('my_project', str(i))
#     if not os.path.exists(tmp_file_name):
#         os.makedirs(tmp_file_name)


import os
path = r'C:\Users\nadvl\PycharmProjects\python-base\lesson7' # путь к папке, где будет создаваться папка пректа
project_name = 'project1' # назначение имени папке проекта
folders = ['setting', 'mainapp', 'adminapp', 'authapp'] # список из наименований вложенных папок в папке проекта
fullPath = os.path.join(path, project_name) # полный путь к папке пректа join соединяет путь и название папки пректа
if not os.path.exists(fullPath): # проверяем есть ли такая папка, чтобы не было ошибки если такая папка уже есть
    os.mkdir(fullPath) # создание самой папки проекта

for f in folders:
    folder = os.path.join(fullPath, f) # создали путь к вложенным папкам проекта
    if not os.path.exists(folder):
        os.mkdir(folder)

