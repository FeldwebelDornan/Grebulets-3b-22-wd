try:
    file = open('list.txt','r')
    str = str(file.readlines()).replace(' ','')
    arr1 = []
    arr2 = []
    for i in str:
        if i not in arr1:
            arr1.append(i)
    for i in arr1:
        arr2.append(str.count(i))
    max = max(arr2)
    for i in range(len(arr2)):
        if arr2[i]== max: print(arr1[i])
    file.close()
except FileNotFoundError:
    print('файл не найден')