def nextGreatestLetter(letters, target):
    start = 0
    end = len(letters) - 1
    while start <= end:
        mid = int((start + end) / 2)
        if letters[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return letters[start % len(letters)]


letters = ["c", "f", "j"]
target = "j"
print(nextGreatestLetter(letters, target))
