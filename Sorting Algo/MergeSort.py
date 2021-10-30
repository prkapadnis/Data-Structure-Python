# Merge Sort

def mergeSort(arr):
    if len(arr) == 1:
        return arr
    mid = int(len(arr) / 2)
    firstHalf = mergeSort(arr[0:mid])
    secondHalf = mergeSort(arr[mid:])

    return merge(firstHalf, secondHalf)

def merge(first, second):
    ans = list()
    i, j, k = 0, 0, 0
    while i < len(first) and j < len(second):
        if first[i] < second[j]:
            ans.insert(k, first[i])
            i += 1
        else:
            ans.insert(k, second[j])
            j += 1
        k += 1

    while i < len(first):
        ans.insert(k, first[i])
        i += 1
        k += 1

    while j < len(second):
        ans.insert(k, second[j])
        j += 1
        k += 1
    return ans

arr = [5,4,3,2,1]
arr = mergeSort(arr)
print(arr)