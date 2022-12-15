arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
d = 1 # how much to rotate

newArr = [0] * len(arr)

for i in range(len(arr)):
    if arr[i + d] <= len(arr) - 1:
        newArr[i] = arr[i + d]
    else:
        newArr[i] = arr[i - d]

print(newArr)