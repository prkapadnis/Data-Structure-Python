import math


def isPrime(num):
    count = 2
    while count * count <= num:
        if num % count == 0:
            return False
        count += 1
    return True

# for i in range(2, 40):
#     print(isPrime(i))


# Optimised way

def isPrime_1(arr):
    i = 2
    while i != int(math.sqrt(arr[-1])):
        for j in arr[i:]:
            if j % i == 0:
                arr.remove(j)
        i += 1


arr = [i for i in range(2, 41)]
# print(arr[3::])
# print(int(math.sqrt(arr[-1])))
isPrime_1(arr)
print(arr)
