try:
    a = input("Введите первое число")
    b = input("Введите второе число")
    res = int(a) / int(b)
    print(f'результат деления: {res}')
except Exception as e:
    print(f"ошибка {e}")
finally:
    print('завершение программы')