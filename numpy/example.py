a=[1,3,5]
b=[1,2,3]

# print(a*b) #error
import numpy as np

a=np.array([1,3,5])
b=np.array([1,2,3])

c=np.array(a*b)

print(c)