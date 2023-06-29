import statistics
arr1 = [5,7,11,13,15,20,25]
arr2 = [i for i in arr1 if i>10]
print(statistics.mean(arr2))