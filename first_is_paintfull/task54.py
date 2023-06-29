try:
    a = input('Введите целое число ')
    res = 0
    for i in range(int(a)+1):
        res+=i
    print(res)
except ValueError:
    print("Ошибка")