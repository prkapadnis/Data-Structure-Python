# https: // leetcode.com/problems/find-in-mountain-array/

def peakIndex(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        mid = int((start + end) / 2)
        if arr[mid] < arr[mid + 1]:
            start = mid + 1
        else:
            end = mid
    return start


def binarySearch(arr, target, start, end):
    isAsc = arr[start] < arr[end]
    while start <= end:
        mid = int((start + end) / 2)
        if arr[mid] == target:
            return mid
        if(isAsc):
            if target < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if target < arr[mid]:
                start = mid + 1
            else:
                end = mid - 1
    return -1


def ans(arr, target):
    peakind = peakIndex(arr)
    firstSlot = binarySearch(arr, target, 0, peakind)
    if firstSlot == -1:
        return binarySearch(arr, target, peakind+1, len(arr)-1)
    return firstSlot


arr = [0, 5, 3, 1]
target = 1
print(ans(arr, target))
