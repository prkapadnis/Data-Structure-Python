def findMedianSortedArrays(num1, num2):
    mergeArray = num1+num2
    mergeArray.sort()
    start = 0
    end = len(mergeArray) - 1
    mid = int((start + end) / 2)
    if len(mergeArray) % 2 == 0:
        return float((mergeArray[mid] + mergeArray[mid+1]) / 2)
    return mergeArray[mid]


num1 = [0, 0]
num2 = [0, 0]
print(findMedianSortedArrays(num1, num2))
