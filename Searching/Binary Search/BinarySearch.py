def BinarySearch(arr, target):
    start = 0       # FIRST ELEMENT OF THE RANEG
    end = len(arr) - 1  # LAST ELEMENT OF THE RANGE
    while start <= end:
        mid = int((start + end) / 2)
        if arr[mid] == target:  # check if target elemtn  is equal to mid if yes … then return mid
            return mid
        if arr[mid] < target:   # if number target element is greater than mid … update start value to mid + 1 and recalculate mid value
            start = mid + 1
        if arr[mid] > target:   # if number target element is less than mid … update end value to mid and recalculate mid value
            end = mid - 1
    return False


arr = [1]
print(BinarySearch(arr, 0))
