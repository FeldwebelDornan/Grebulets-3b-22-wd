import random
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
print(f'минимальное значение: {min}\nмаксимальное значение: {max}')