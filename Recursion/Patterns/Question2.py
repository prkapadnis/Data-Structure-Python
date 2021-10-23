#Bubble sort with recursion

def bubbleSort(arr, row, col):
   if row == 0:
      return
   if col < row:
      if arr[col] > arr[col+1]:
         arr[col], arr[col+1] = arr[col+1], arr[col]
      bubbleSort(arr, row, col+1)
   else:
      bubbleSort(arr, row-1, 0)

arr = [5,4,3,2,1]
bubbleSort(arr, len(arr)-1, 0)
print(arr)