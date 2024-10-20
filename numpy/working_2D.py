import numpy as np

a=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])

print(a.ndim)
print(a.shape)

print("getting value of an index")
print(a[1,5])
print(a[1,-2])

print("get specific row")
print(a[0,:])

print("get specific column")
print(a[:,0])

print("slicing")
print(a[0,1:6:2])
print(a[0,1:-1:2])

print("changing")
a[1,5]=23
print(a)

a[:,5]=23
print(a)

a[:,5]=[6,13]
print(a)