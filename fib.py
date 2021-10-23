def fib(number):
    first_num = 0
    second_num = 1
    i = 2
    while i < number:
        value = first_num + second_num
        first_num = second_num
        second_num = value
        i += 1
    return second_num


print(fib(5))
# write a program to print the fibonacci series
