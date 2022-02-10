# https://leetcode.com/problems/rotate-array/
# Given an array, rotate the array to the right by k steps, where k is non-negative
def rotateArray(arr, key):
    ans = [0 for i in range(len(arr))]
    for i in range(len(arr)):
        ans[(i+key) % len(arr)] = arr[i]
        print(ans)
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
        # suppose the array is [1,2,3,4,5,6] and key is [2]
        temp = nums[0:len(nums)-key]  # [1,2,3,4]
        nums[0:key] = nums[len(nums)-key:len(nums)] # nums[4:6] = [5,6]
        nums[key:len(nums)] = temp # [5,6,1,2,3,4]


nums = [1,2,3,4,5,6]
key = 2
print(rotateArray(nums, key))
# print(rotateArray_1(nums, key))
print(nums)
