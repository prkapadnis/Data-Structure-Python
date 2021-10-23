# https://leetcode.com/problems/rotate-array/
# Given an array, rotate the array to the right by k steps, where k is non-negative
def rotateArray(arr, key):
    ans = [0 for i in range(len(arr))]
    for i in range(len(arr)):
        ans[(i+key) % len(arr)] = arr[i]
    return ans


def rotateArray_1(nums, key):

    # first Approch
    # nums.reverse()
    # swap(nums, 0, key-1)
    # swap(nums, key, len(nums)-1)

    # Second Approch
    key = key % len(nums)
    if key == 0:
        return nums
    else:
        temp = nums[0:len(nums)-key]
        nums[0:key] = nums[len(nums)-key:len(nums)]
        nums[key:len(nums)] = temp


nums = [-1]
key = 2
# print(rotateArray(nums, key))
print(rotateArray_1(nums, key))
print(nums)
