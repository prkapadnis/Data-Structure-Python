def linearSearch(myList, key):
    for i in range(len(myList)):
        if myList[i] == key:
            return i + 1
    return -1

myList = [1,2,3,4,5]
elementToSearch = int(input("Enter the Element to search: "))
# index = linearSearch(myList, elementToSearch)
# print(index)
print(f"The element {elementToSearch} is found at {linearSearch(myList, elementToSearch)}")
