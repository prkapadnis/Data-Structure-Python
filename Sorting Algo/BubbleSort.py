def bubbleSort(arr):
    """
        This is a bubble sort algorithm which sort the array.
        The worst time complexity is O(n^2)
        The space complexity is O(1) because there is no extra space is required we just swap 
            the values in array.
    """
    for i in range(len(arr)):
        for j in range(1, len(arr) - i):
            if(arr[j] < arr[j - 1]):
                arr[j], arr[j-1] = arr[j-1], arr[j]

arr = [5,4,3,2,1]
print(arr)
bubbleSort(arr)
print(arr)
# print("The sorted array is: ", end=" ")
# for i in arr:
#     print(i, end=" ")
# print(help(bubbleSort))