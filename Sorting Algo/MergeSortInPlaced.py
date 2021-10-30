# Merge Sort In Placed sort
# Didn't Work

def mergeSort(arr, start, end):
    if (end - start) == 1:
        return
    mid = int((start + end) / 2)
    mergeSort(arr, start, mid)
    mergeSort(arr, mid, end)
    merge(arr, start, mid, end)

def merge(arr, start, mid, end):
    ans = list()
    i = start
    j = mid
    k = 0
    while i < mid and j < end:
        if arr[i] < arr[j]:
            ans.insert(k, arr[i])
            i += 1
        else:
            ans.insert(k, arr[j])
            j += 1
        k += 1

    while i < start:
        ans.insert(k, arr[i])
        i += 1
        k += 1

    while j < end:
        ans.insert(k, arr[j])
        j += 1
        k += 1

    for i in range(0,end-start):
        arr[start + i] = ans[i]


arr = [5,4,3,2,1]
mergeSort(arr, 0, len(arr)-1)
print(arr)