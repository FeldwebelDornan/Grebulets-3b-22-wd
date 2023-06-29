a = int(input('Введите длину ряда\n'))
res = [0,1]
i=1
while len(res)<a:
    res.append(res[i]+res[i-1])
    i+=1
print(res)