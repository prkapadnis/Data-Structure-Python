# The number is a palindrome or not
import math

def helper(num, base):
    if num%10 == num:
        return num
    remainder = num % 10
    return remainder * int(math.pow(10, base-1)) + helper(int(num/10), base-1)


def reverse(num):
    digits = int(math.log10(num)) + 1
    return helper(num, digits)


def palindrome(num):
    return num == reverse(num)

print(palindrome(121))