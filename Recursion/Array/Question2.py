# Linear search using recusion

def linersearch(arr, index, target):
    if index == len(arr) - 1:
        return False
    return arr[index] == target or linersearch(arr, index+1, target)

arr = [2,3,5,7,3]
# print(linersearch(arr, 0, 5))

def findIndex(arr, target, index):
    if index >= len(arr) - 1:
        return False
    if arr[index] == target:
        return index
    return findIndex(arr, target, index+1)

arr = [2,3,5,7,3]
# print(findIndex(arr, 0, 5))

# Find index of all the occurrences
ans = []
def findAllIndex(arr, target, index):
    if index >= len(arr) - 1:
        return False
    if arr[index] == target:
        ans.append(index)
    return findAllIndex(arr, target, index + 1)

# arr = [1,2,3,4,5,4,2]
# print(findAllIndex(arr, 7, 0))
# print(ans)

def findAllIndex1(arr, target, index):
    ans = []
    if index == len(arr):
        return ans
    if arr[index] == target:
        ans.append(index)
    ans += findAllIndex1(arr, target, index + 1)
    return ans


arr = [1,2,3,4,5,4,2]
print(findAllIndex1(arr, 4, 0))










