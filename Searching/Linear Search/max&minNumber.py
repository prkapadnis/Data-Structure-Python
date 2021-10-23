def max(arr):
    max = 0
    for i in range(len(arr)):
        max = arr[0]
        if arr[i] > max:
            max = arr[i]
    return max


def min(arr):
    min = arr[0]
    for i in range(len(arr)):
        if min > arr[i]:
            min = arr[i]
    return min


arr = [100, 222, 24, 63, 89]
print(max(arr))
print(min(arr))
