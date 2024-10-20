import numpy as np

a=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])

print(a)

b=a.reshape(14,1)
print(b)
b=a.reshape(1,14)
print(b)
b=a.reshape(7,2)
print(b)

a=np.ones(3)
b=np.zeros(3)
c=np.vstack((a,b,a,b))
print(c)
c=np.hstack((a,b,a,b))
print(c)