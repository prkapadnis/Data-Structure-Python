# Reverse a number
import math
sum = 0
def reverse(num):
    global sum
    if num <= 0:
       return
    remainder = (num%10)
    sum = sum * 10 + remainder
    reverse(int(num/10))

# reverse(5739)
# print(sum)
# print(int(math.log10(sum) + 1))

# -----------------------------------------------------------------------------

def helper(num, base):
    if num%10 == num:
        return num
    remainder = num % 10
    return remainder * int(math.pow(10, base-1)) + helper(int(num/10), base-1)


def reverse_1(num):
    digits = int(math.log10(num) + 1)
    return helper(num, digits)

print(reverse_1(3456))