import random
arr1 = []
sum = 0
for i in range (10):
    arr1.append(random.randrange(1,10))
    sum+=arr1[i]
print(sum)