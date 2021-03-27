import os

names_folders = ('settings', 'mainapp', 'adminapp', 'authapp')
for i in names_folders:
    tmp_file_name = os.path.join('my_project', str(i))
    if not os.path.exists(tmp_file_name):
        os.makedirs(tmp_file_name)

