def searchIn2d(arr, target):
    for row in range(len(arr)):
        for col in range(len(arr[row])):
            if arr[row][col] == target:
                return row, col


def maxIn2D(arr):
    max = arr[0][0]
    for row in range(len(arr)):
        for col in range(len(arr[row])):
            if arr[row][col] > max:
                max = arr[row][col]
    return max


def minIn2D(arr):
    min = arr[0][0]
    for row in range(len(arr)):
        for col in range(len(arr[row])):
            if min > arr[row][col]:
                min = arr[row][col]
    return min


arr = [
    [23, 4, 11],
    [18, 12, 3, 9],
    [78, 99, 34, 56],
    [18, 122]
]
target = 34
print(searchIn2d(arr, target))
print(maxIn2D(arr))
print(minIn2D(arr))
