a = input("Введите строку").lower()
arr1 = []
for i in range(len(a)):
    if a[i] not in arr1:
        arr1.append(a[i])
arr2 = [a.count(arr1[i]) for i in range(len(arr1)) ]
print (arr2)


