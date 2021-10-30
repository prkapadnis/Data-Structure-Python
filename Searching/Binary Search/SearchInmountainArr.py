# https://leetcode.com/problems/peak-index-in-a-mountain-array/

def peakIndexInMountainArray(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        mid = int((start + end) / 2)
        if arr[mid] < arr[mid + 1]:
            start = mid + 1
        else:
            end = mid
    return start


arr = [0, 10, 5, 2]
print(peakIndexInMountainArray(arr))
