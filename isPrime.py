def isPrime(num):
    count = 2
    while count * count <= num:
        if num % count == 0:
            return False
        count += 1
    return num

for i in range(2, 40):
    print(isPrime(i))
