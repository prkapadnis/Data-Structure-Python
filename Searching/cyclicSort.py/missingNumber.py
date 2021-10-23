def missingNumber(nums):
    i = 0
    while i < len(nums):
        correct = nums[i]
        if nums[i] < len(nums) and nums[i] != nums[correct]:
            nums[i], nums[correct] = nums[correct], nums[i]
        else:
            i += 1

    for index in range(len(nums)):
        if nums[index] != index:
            return index
    return len(nums)


arr = [3, 0, 1]
print(arr)
print(missingNumber(arr))
print(arr)
