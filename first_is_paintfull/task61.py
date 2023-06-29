import math
a = ((1,2),(3,4),(-1,5),(6,-3))
def SortLength(elements):
    return math.dist(elements, (0,0))
a = sorted(a,key=SortLength)
print(a)