try:
    a = input('Введите число: ')
    print(int(a)**2)
except ValueError:
    print('Ошибка')
finally:
    pass