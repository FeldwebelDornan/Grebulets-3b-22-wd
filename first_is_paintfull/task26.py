def findcommon(a,b):
    if a<b:
        min = a
    else:
        min = b
    for i in range (2,min):
        if a%i==b%i:
            return i
    return 0
x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))
print(f'наименьший общий делитель: {findcommon(x,y)}') if findcommon(x,y)!=0 else print(f'нет общего делителя')