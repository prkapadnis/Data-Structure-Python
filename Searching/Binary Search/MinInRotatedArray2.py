# Find the Minimum in rotated array with duplicates

def findMin(arr):
    pivot = findPivot(arr)
    if pivot == -1:
        return arr[0]
    return arr[pivot+1]

def findPivot(arr):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = int((start + end) / 2)
        if mid < end and arr[mid] > arr[mid + 1]:
            return mid
        if mid > start and arr[mid] < arr[mid - 1]:
            return mid - 1
        # If middle start and end are equal
        if arr[mid] == arr[start] and arr[mid] == arr[end]:
            # then just skip the start and end
            if start < end and arr[start] > arr[start + 1]:
                return start
            start += 1
            if end > start and arr[end] < arr[end - 1]:
                return end - 1
            end -= 1
        elif arr[start] <= arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1

print(findMin([1,2,3,4,5]))