def cyclicSort(arr):
    i = 0
    while i < len(arr):
        correctIndex = arr[i] - 1
        if arr[i] != arr[correctIndex]:
            arr[i], arr[correctIndex] = arr[correctIndex], arr[i]
        else:
            i += 1

arr = [1,3,4,2,2]
print(arr)
cyclicSort(arr)
print(arr) 