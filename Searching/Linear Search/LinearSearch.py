def LinearSearch(arr, key):
    for i in range(0, len(arr)):
        if arr[i] == key:
            return i
    return 0


arr = [18, 12, 9, 14, 77, 50]
print(LinearSearch(arr, 14))
