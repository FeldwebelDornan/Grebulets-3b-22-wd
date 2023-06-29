a = input('Введите слово:\n').replace(' ','')
res=[0,0]
x=('а','е','и','о','у','ё','ю','я')
for i in range (len(a)):
    if a[i] in x: res[0] += 1
    else: res[1]+=1
print(res)