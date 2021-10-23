def BinarySearch(arr, target, start, end):
    if start > end:
        return -1
    mid = int((start + end) / 2)
    if arr[mid] == target:
        return mid
    if arr[mid] > target:
        return BinarySearch(arr, target, start, mid-1)
    return BinarySearch(arr, target, mid+1, end)


arr = [1, 2, 3, 4, 5]
target = 7
print(BinarySearch(arr, target, 0, len(arr)-1))