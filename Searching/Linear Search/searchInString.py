def search(name, target):
    if len(name) == 0:
        return False
    for i in range(len(name)):
        if name[i].lower() == target:
            return True
    return False


name = 'Pratik'
target = 'p'
print(search(name, target))
