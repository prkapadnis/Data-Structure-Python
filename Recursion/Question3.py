# Sum of digits
def sum(num):
    if num == 0:
        return 0
    remainder = num % 10
    return remainder + sum(int(num/10))

print(sum(45))

# product of digits
def product(num):
    if num <= 1:
        return 1
    remainder = num % 10
    return remainder * product(int(num/10))

print(product(700))