# Checking array is sorted or not

def isSorted(arr, index):
    if index == len(arr)-1:
        return True
    return arr[index] < arr[index + 1] and isSorted(arr, index + 1)


arr = [1,3,5,7,8,10]
# print(arr[-1])
print(isSorted(arr, 0))
