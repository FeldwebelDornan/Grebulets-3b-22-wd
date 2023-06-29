arr = [1,2,3,2,1]
def polindrom(arr):
    if len(arr)//2<1: return True
    if arr[0]!=arr[len(arr)-1]: return False
    return polindrom(arr[1:len(arr)-1])
print('полиндром') if polindrom(arr) else print('не полиндром')

