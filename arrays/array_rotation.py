def printArray(arr):
  for i in arr:
    print(i,end = " ")
  print("\r")

def reverseArray(arr, start, end):
  while(start < end):
    temp = arr[start]
    arr[start] = arr[end]
    arr[end] = temp
    start += 1
    end -= 1



def rotateArray(arr, d):
  if d == 0:
    return
  n = len(arr)
  reverseArray(arr, 0, d-1) 
  reverseArray(arr, d, n-1) 
  reverseArray(arr, 0, n-1) 

arr = [1,2,3,4,5,6,7]
d = 2
rotateArray(arr, d)
printArray(arr)
