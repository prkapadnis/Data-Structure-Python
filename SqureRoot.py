# How to find the if the number is perfect square or not

def isPerfectSquare(num):
    start = 2
    end = num
    while start <= end:
        mid = int((start + end) / 2)
        if mid * mid == num:
            return mid
        if mid * mid > num:
            end = mid - 1
        else:
            start = mid + 1
    incr = 0.1
    for i in range(0,3):
        while end * end <= num:
            end += incr
        incr /= 10
    return end

print("%.2f"%isPerfectSquare(50))


def isPerfectSquare(num):
