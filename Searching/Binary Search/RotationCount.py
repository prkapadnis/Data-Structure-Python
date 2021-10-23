# Count the Rotation of the Rotated Array

def findPivot(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        mid = int((start + end) / 2)
        if mid < end and arr[mid] > arr[mid + 1]:
            return mid
        if mid > start and arr[mid] < arr[mid - 1]:
            return mid - 1
        if arr[start] >= arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1


def count(arr):
    return findPivot(arr) + 1

arr = [1,2,3,4,5,0]
print(count(arr), 'times')