import numpy as np

a=np.array([1,2,3])
b=np.array([[1,2,3],[1,2,3]])

print(a,b,sep='\n\n')

print("dimension of numpy array")

print(a.ndim)
print(b.ndim)

print("shape of numpy array")

print(a.shape)
print(b.shape)

print("data type of numpy array")

print(a.dtype)
print(b.dtype)

print("item size of numpy array")

print(a.itemsize)
print(b.itemsize)

print("total size of numpy array")

print(a.nbytes)
print(b.nbytes)


print("elements of numpy array")
a=np.array([1,2,3,4,5,6,7,8,9,10])
print(a[[1,5,6,8]])


