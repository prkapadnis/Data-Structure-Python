# Count the zeros in the number
def count0(num, count):
    if num%10 == num:
        return count
    remainder = num % 10
    if remainder == 0:
       count+=1
    return count0(int(num/10), count)

print(count0(2001010, 0))