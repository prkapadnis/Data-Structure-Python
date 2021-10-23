# https://www.geeksforgeeks.org/find-position-element-sorted-array-infinite-numbers/

def binarySearch(arr, target, start, end):
    while(start <= end):
        mid = int((start + end) / 2)
        if target > arr[mid]:
            start = mid + 1
        elif target < arr[mid]:
            end = mid - 1
        else:
            return mid
    return -1


def ans(arr, target):
    start = 0
    end = 1
    while target > arr[end]:
        newstart = end + 1
        end = end + (end - start + 1) * 2
        start = newstart
    return binarySearch(arr, target, start, end)

arr = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170, 190, 230, 250]
target = 100
print(ans(arr, target))
    