# Rotated Binary Search with distinct values

def RotatedBinarySearch(arr, target):
    pivot = findPivot(arr)
    if pivot == -1:
        return BinarySearch(arr, target, 0, len(arr)-1)
    if arr[pivot] == target:
        return True
    if arr[0] <= target:
        return BinarySearch(arr, target, 0, pivot-1)
    return BinarySearch(arr, target, pivot+1, len(arr)-1)


def BinarySearch(arr, target, start, end):
    while start <= end:
        mid = int((start + end) / 2)
        if arr[mid] == target:
            return True
        if arr[mid] > target:
            end = mid - 1
        if arr[mid] < target:
            start = mid + 1
    return False


def findPivot(arr):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = int((start + end) / 2)
        if mid < end and arr[mid] > arr[mid+1]:
            return mid
        if mid > start and arr[mid] < arr[mid-1]:
            return mid-1
        if arr[start] >= arr[mid]:
            end = mid - 1
        if arr[start] < arr[mid]:
            start = mid + 1
    return -1


arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1]
print(findPivot(arr))
print(RotatedBinarySearch(arr, 2))
