# Check if the array is mountain array or not

def is_mountainArr(lst):
    start = 0
    end = len(lst) - 1
    while start < len(lst) - 1 and lst[start] < lst[start + 1]:
        start += 1
    while end > 0 and lst[end] < lst[end-1]:
        end -= 1
    if start > 0 and start == end and end < len(lst) - 1:
        return True
    return False


arr = [1, 2, 3, 4, 5, 3, 2, 1]
print(is_mountainArr(arr))
