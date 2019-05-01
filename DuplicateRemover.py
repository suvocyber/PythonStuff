import easygui
import os
import hashlib

dir_path = easygui.diropenbox()
print(dir_path)
files = os.listdir(dir_path)

files = (file for file in files if os.path.isfile(path=os.path.join(dir_path, file)))
files = sorted(files, key=lambda fn: os.path.getatime(os.path.join(dir_path, fn)))

hash_table = dict()
duplicates =[]


for filename in files:
    file_path = os.path.join(dir_path, filename)

    with open(file_path, 'rb') as filepointer:
        content = filepointer.read()


    hasher = hashlib.sha256()
    hasher.update(content)
    _hash = hasher.hexdigest()

    if _hash in hash_table.keys():
        duplicates.append(file_path)
    else:
        hash_table[_hash] = file_path


for dup in duplicates:
    filename = os.path.split(dup)[1]
    selection = easygui.choicebox(title="Delete Duplicates?", msg="Delete file permanently {FILENAME}?".format(FILENAME=filename), choices=['delete-it', 'keep-it'])
    if selection == 'delete-it':
        os.remove(dup)