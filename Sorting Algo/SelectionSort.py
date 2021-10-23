def getMaxIndex(arr, start, end):
    maxi = start
    for i in range(start, end+1):
        if arr[maxi] < arr[i]:
            maxi = i
    return maxi

def selectionSort(arr):
    """
        The Selection sort algorithm finds the minimum element in the array and putting it at the
        begining.
        It maintains the two array sorted array and unsorted array:
            It finds smallest element in the unsorted array and move them in sorted array.
        The Time complexity is O(n^2)
    """
    for i in range(0, len(arr)):
        last = len(arr) - i - 1
        maxi = getMaxIndex(arr, 0 , last)
        arr[maxi], arr[last] = arr[last], arr[maxi]

arr = [5,14,33,12,61]
selectionSort(arr)
print(arr)