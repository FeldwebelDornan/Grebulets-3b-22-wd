a = ['apple','orange','banana','pineapple','grape']
for i in range(len(a)-1):
    for j in range(len(a)-1-i):
        if a[j][0] < a[j+1][0]:
            a[j],a[j+1] = a[j+1],a[j]
print(a)