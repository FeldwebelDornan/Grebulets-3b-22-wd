try:
    print(open('test.TXT','r').readlines())
except FileNotFoundError:
    print("Файл не найден")
finally:
    pass