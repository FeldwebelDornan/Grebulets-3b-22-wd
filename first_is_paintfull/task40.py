import os
try:
    file = open('test.TXT','r')
except FileNotFoundError:
    print('Файл не найден')
else:
    print('Файл найден')
    file.close()