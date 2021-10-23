# Find the factorial

def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num-1)

print(factorial(15))

# Sum of N number
def sum(num):
    if num == 1:
        return 1
    return num + sum(num-1)

print(sum(25))

