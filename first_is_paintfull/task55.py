try:
    a = input("Введите массив")
    arr = a.split(' ')
    print(min(arr))
except Exception:
    print('ошибка')