# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

def evenDigit(arr):
    count = 0
    for ele in arr:
        if len(str(ele)) % 2 == 0:
            count += 1
    return count


nums = [12, 345, 21, 6, 7896]
print(evenDigit(nums))
