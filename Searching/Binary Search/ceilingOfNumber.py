# Ceiling of a number:
# The ceiling of a number is the number which is the smaller number in the array which greater than or eqaul to the
# target number
def CeilingOfNumber(arr, target):
    # What if target is greater than the greatest number of an array
    if target > arr[len(arr) - 1]:
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
    return start


arr = [2, 3, 5, 9, 14, 16, 18]
target = 13
print(CeilingOfNumber(arr, target))
