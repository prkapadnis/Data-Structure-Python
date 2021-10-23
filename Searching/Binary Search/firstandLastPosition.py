def search(arr, target, findFirstIndex):
    start = 0
    ans = -1
    end = len(arr) - 1
    while start <= end:
        mid = int((start + end) / 2)
        if target > arr[mid]:
            start = mid + 1
        elif target < arr[mid]:
            end = mid - 1
        else:
            ans = mid
            if(findFirstIndex):
                end = mid - 1
            else:
                start = mid + 1
    return ans


def searchRange(nums, target):
    ans = [-1, -1]
    first = search(nums, target, True)
    last = search(nums, target, False)
    ans[0] = first
    ans[1] = last
    return ans


arr = [4, 5, 6, 6, 7, 7, 10]
print(searchRange(arr, target=7))
