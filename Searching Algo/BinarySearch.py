def binarySearch(myList, key):
    low = 0
    high = len(myList) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if myList[mid] == key:
            return mid
        if myList[mid] > key:
            high = mid 
        if myList[mid] < key:
            low = mid
    return -1

myList = [1,2,3,4,5]
elementToSearch = 3
print(f"the element {elementToSearch} is at index: {binarySearch(myList, elementToSearch)}")