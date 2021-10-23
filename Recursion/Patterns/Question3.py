# Selection Sort
def getMaxIndex(arr, start, end):
    maxi = start
    for i in range(start, end+1):
        if arr[maxi] < arr[i]:
            maxi = i
    return maxi


def selectionSort(arr, lastIndex):
    if lastIndex == 1:
        return
    maxi = getMaxIndex(arr, 0, lastIndex)
    arr[maxi], arr[lastIndex] = arr[lastIndex], arr[maxi]
    selectionSort(arr, lastIndex-1)


# arr = [5,2,5,7,89,1,2,12]
# selectionSort(arr, len(arr)-1)
# print(arr)

def selection(arr, row, col, maxi):
    if row == 0:
        return
    if col < row:
        if arr[col] > arr[maxi]:
            selection(arr, row, col+1, col)
        else:
            selection(arr, row, col+1, maxi)
    else:
        arr[maxi], arr[row-1] = arr[row-1], arr[maxi]
        selection(arr, row-1, col=0, maxi=0)

arr = [5,2,5,7,89,1,2,12]
selection(arr, len(arr), col = 0, maxi = 0)
print(arr)