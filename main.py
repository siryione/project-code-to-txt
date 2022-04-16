import os
from os import listdir
from os.path import isfile, join

dir_path = os.path.dirname(os.path.realpath(__file__))
files = [f for f in listdir(dir_path) if isfile(join(dir_path, f))]

result = ''
for file in files:
    if file.endswith('.cpp') | file.endswith('.hpp'):
        with open(file, 'r') as f:
            file_read = f.read()
        result += file.upper() + '\n'*2 + file_read + '\n'*3
        with open("result.txt", 'w') as f:
            f.write(result)


