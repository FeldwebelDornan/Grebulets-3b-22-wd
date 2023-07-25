class employee:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    def predstavlenie(self):
        print(f'имя {self.name}, возраст:{self.age}, зарплата: {self.salary}')
down = employee('Васёк','45',15000)
down.predstavlenie()
#----------
def simplecheck(a):
    b = 0
    for i in range(2,a-1):
        if a%i==0:
            return 1
    return b
a = int(input())
print('число простое') if simplecheck(a)==0 else print('число непростое')
down.predstavlenie()
#----------
def findcommon(a,b):
    if a<b:
        min = a
    else:
        min = b
    for i in range (2,min):
        if a%i==b%i:
            return i
    return 0
first = 14
second = 10
print(f'наименьший общий делитель: {findcommon(first,second)}') if findcommon(first,second)!=0 else print(f'нет общего делителя')
#---------


#---------
a = input('дай строку')
print(a[::-1])
#---------
a = input()
res=0
x=('а','е','и','о','у','ё','ю','я')
for i in range (len(a)):
    if a[i] in x:
        ++res
print(res)