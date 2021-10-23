# Find the Minimum in rotated array with No duplicates

def findMin(arr):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = int((start + end) / 2)
        if mid < end and arr[mid] > arr[mid + 1]:
            return arr[mid + 1]
        if mid > start and arr[mid] < arr[mid - 1]:
            return arr[mid]
        if arr[start] >= arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return arr[0]

print(findMin([1,2,3,4,5]))