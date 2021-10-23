# Given an integer num, return the number of steps to reduce it to zero.


def helper(num, count):
    if num == 0:
        return count
    if num % 2 == 0:
        return helper(num/2, count+1)
    return helper(num-1, count+1)

def numberOfSteps(num):
    return helper(num, 0)

print(numberOfSteps(8))