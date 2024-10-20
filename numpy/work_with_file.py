import numpy as np

a=np.genfromtxt('numpy/data.txt',delimiter=",")
print(a)

print(a > 50)

print(a[a > 50])

print(np.any(a>50,axis=0))
print(np.all(a>50,axis=0))
