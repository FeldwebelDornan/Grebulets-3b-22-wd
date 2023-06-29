def simplecheck(a):
    b = 0
    for i in range(2,a):
        if a%i==0:
            return 1
    return b
a = int(input())
print('число простое') if simplecheck(a)==0 else print('число непростое')