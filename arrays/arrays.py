import array

arr = array.array('i',[1, 2, 3])

for i in arr:
  print(i,end=" ")
print("\r")

arr.append(4)

for i in arr:
  print(i,end=" ")
print("\r")
  
arr.insert(2,5)

for i in arr:
  print(i,end=" ")

print("\r")

arr.pop(0)

for i in arr:
  print(i,end=" ")

print("\r")

arr.append(2)
for i in arr:
  print(i,end=" ")

print("\r")

print(arr.index(2))

arr.reverse()

for i in arr:
  print(i,end=" ")

print("\r")