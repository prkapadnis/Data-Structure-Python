def quickSort(lst, low, high):
    if low >= high:
        return
    start = low
    end = high
    mid = int((start + end) / 2)
    pivot = lst[mid]
    while start <= end:
        while lst[start] < pivot:
            start += 1
        while lst[end] > pivot:
            end -= 1
        if start <= end:
            lst[start], lst[end] = lst[end], lst[start]
            start += 1
            end -= 1
    quickSort(lst, low, end)
    quickSort(lst, start, high)


arr = [6, 9, 2, 4, 5, 1]
quickSort(arr, 0, len(arr)-1)
print(arr)
