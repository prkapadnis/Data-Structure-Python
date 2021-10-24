# Prints all the Factors of the given number
import math as m
def factors(num):
    for i in range(1,int(m.sqrt(num)+1)):
        if num % i == 0:
            print(i,int(num/i),end=" ")

factors(30)
print()

def factors_1(num):
    myList = list()
    for i in range(1, int(m.sqrt(num)+1)):
        if num % i == 0:
            print(i, end=" ")
            myList.append(int(num/i))
    for i in myList[::-1]:
        print(i, end=" ")

factors_1(30)