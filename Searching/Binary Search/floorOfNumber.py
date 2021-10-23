# FLOOR OF NUMBER
# floor Of Number is the greatest number in an array that is smaller than or equal to the target number
def floorOfNumber(arr, target):
    if target < arr[0]:
        return -1
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = int((start + end) / 2)
        if arr[mid] == target:
            return arr[mid]
        if arr[mid] < target:
            start = mid + 1
        if arr[mid] > target:
            end = mid - 1
    return arr[end]


def array(arr):
    return arr[-1]


arr = [2, 3, 5, 9, 14, 16, 18]
target = 1
# print(floorOfNumber(arr, target))
print(array(arr))
