# Print the  number from n to 1 using recursion

def printnumber(num):
    if num == 0:
        return
    print(num)
    printnumber(num-1)

# printnumber(6)


def printNumFromNto1(num):
    if num == 0:
        return
    printNumFromNto1(num-1)
    print(num)

# printNumFromNto1(5)


def fun(num):
    if num == 0:
        return
    print(num, end=" ")
    fun(num-1)
    print(num, end=" ")

fun(5)