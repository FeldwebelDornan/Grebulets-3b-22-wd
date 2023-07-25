import random
#----------------
list1 = []
for i in range (5):
    a = int(input())
    list1.append(a)
print(list1)
#----------------
list2 = []
for i  in range (10):
    list2.append(random.randrange(1,100))
min = max = list2[0]
for i in range (10):
    if min > list2[i]:
        min = list2[i]
for i in range (10):
    if max < list2[i]:
        max = list2[i]
#----------------
mas1 = [1,23,3,5]
mas2 = [43,2,1,5,9]
mas3 = mas1 + mas2
#----------------
arr1 = []
sum = 0
for i in range (10):
    arr1.append(random.randrange(1,10))
    sum+=arr1[i]
#----------------
arr2 = [1,2,4,5,6]
a = int(input('введи число, паскудина '))
print ('это число есть в массиве') if a in arr2 else print('этого числа нет в массиве')
#----------------
a = input()
res=0
x=('а','е','и','о','у','ё','ю','я')
for i in range (len(a)):
    if a[i] in x:
        res+=1
print(res)
#----------------
class schoolboy:
    def __init__(self,name,clas):
        self.name = name
        self.clas = clas
    def ucheba(self):
        print(f'{self.name} из {self.clas} учится')
vasya = schoolboy('вася','11А')
vasya.ucheba()
#---------------
a = input()
