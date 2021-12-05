def findSquare(num):
    ans = 0
    while num > 0:
        rem = int(num % 10)
        ans += rem * rem
        num = int(num / 10)
    return ans

def happyNumber(num):
    slow = num
    fast = num
    slow = findSquare(slow)
    fast = findSquare(findSquare(fast))

    while slow != fast:
        slow = findSquare(slow)
        fast = findSquare(findSquare(fast))
    
    if slow == 1:
        return True
    return False

print(happyNumber(12))
    