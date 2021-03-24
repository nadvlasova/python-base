import os
import shutil
# dir_name = 'second_dir'   # создание одной пустой папки
# if not os.path.exists(dir_name):
#     os.mkdir(dir_name)

# dir_path = os.path.join('data', 'src') # создание папки 'data' с подпапкой в ней папки 'src'
# if not os.path.exists(dir_path):
#     os.makedirs(dir_path)

# dir_name = 'data'     # переименовал папку 'data', а входящую в нее 'src' не захотел???
# new_dir_name = '../new_data_out'
# if os.path.exists(dir_name) and not os.path.exists(new_dir_name):
#     os.rename(dir_name, new_dir_name)

# to_remove_dir_name = 'new_data'     # папку так удалить нельзя remove для удаления файла т.е. 1.py удалить можно
# if os.path.exists(to_remove_dir_name):
#     os.remove(to_remove_dir_name)

# to_remove_dir_name = 'second_dir'     # удаляет ПУСТЫЕ папки
# if os.path.exists(to_remove_dir_name):
#     os.rmdir(to_remove_dir_name)

# в начала файла добавляем импорт модуля : import shutil
# to_remove_dir_name = 'second_dir'       # для удаления папок с содержимым
# if os.path.exists(to_remove_dir_name):
#    shutil.rmtree(to_remove_dir_name)