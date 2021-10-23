# Search for 3 in the range of [1,4]
from _typeshed import StrPath


def searchInRange(arr, start, end, target):
    if len(arr) == 0:
        return False
    for i in range(start, end):
        if arr[i] == target:
            return True
    return False


arr = [18, 12, -7, 3, 14, 28]
start, end = 1, 4
target = 3
print(searchInRange(arr, start, end, target))
