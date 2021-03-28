'''
3. Создать структуру файлов и папок, как написано в задании 2
(при помощи скрипта или «руками» в проводнике).
Написать скрипт, который собирает все шаблоны в одну папку
templates, например:
|--my_project
   ...
  |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html
Примечание: исходные файлы необходимо оставить; обратите внимание,
что html-файлы расположены в родительских папках
(они играют роль пространств имён); предусмотреть возможные
исключительные ситуации; это реальная задача, которая решена,
например, во фреймворке django.
'''

import os
import shutil


g_path = r'C:/Users/nadvl/PycharmProjects/python-base/lesson7/my_project_task3'
project_path = os.path.join(g_path, 'templates')
try:
    os.mkdir(project_path)
except:
    pass

for dirname in os.listdir(g_path):
    #print(dirname)
    folders_dir = os.path.join(g_path, dirname, 'templates', dirname)
    #print(folders_dir)
    if os.path.isdir(folders_dir):
         #shutil.copytree(g_path, dirname,  os.path.join(project_path, 'templates', dirname))
         shutil.copytree(folders_dir, os.path.join(project_path, dirname))
    #print(dirname)

# def copytree(src, dst, symlinks=False, ignore=None, copy_function=copy2,
#              ignore_dangling_symlinks=False, dirs_exist_ok=False):


# for root, dirs, files in os.walk('.'):
#     app_dir = os.path.join(root, dirs, files, 'templates', root, dirs, files)
#     if not os.path.isdir(app_dir):
#         continue
#     shutil.copytree(root, 'folder', 'dirs_exist_ok=True', os.path.join(project_path, root, dirs, files , ))

