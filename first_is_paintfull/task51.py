from math import gcd
from functools import reduce
arr1 = [24,36,48,60]
arr2 = [12,18,24,36,72]
arr1.extend(arr2)
print(f'Наибольший общий делитель {reduce(gcd,arr1)}')