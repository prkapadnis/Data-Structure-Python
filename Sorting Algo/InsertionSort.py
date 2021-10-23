def insertionSort(arr):
    """
        In Insertion Sort the array is virtually split into sorted and unsorted array and picked
        a element from unsorted array and placed it at a correct position in sorted array.
        The Time complexity is O(n^2)
    """
    for i in range(1, len(arr)):
        elementToSort = arr[i]
        while arr[i - 1] > elementToSort and i > 0:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i = i - 1

arr = [5,4,3,2,1]
insertionSort(arr)
print(arr)