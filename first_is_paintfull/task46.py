import os
try:
    open('test.TXT','w').write('Hello, world!')
except FileNotFoundError or OSError:
    print("Ошибка")
finally:
    pass