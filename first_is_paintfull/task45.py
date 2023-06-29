try:
    a = input('Введите название файла')
    print(open(f'{str(a)}.TXT','r').readlines())
except FileNotFoundError or OSError:
    print("Ошибка")
finally:
    pass