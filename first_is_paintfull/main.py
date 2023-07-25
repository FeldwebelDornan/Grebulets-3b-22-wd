from task1 import hello
x=5
print(x)
t = 'hello'
print(t)
def EvenCheck(a):
    if(a%2==0):
        print(f'чётное {i}')
    else:
        print(f'нечётное {i}')
for i in range(1,10):
    if i != 4 and i !=7:
        EvenCheck(i)
    else:
        continue
def sum(a,b):
    return a+b
def print_sum():
    a=int(input())
    b=int(input())
    print(sum(a,b))
print_sum()
hello()