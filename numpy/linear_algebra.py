import numpy as np

a=np.ones((2,3))
b=np.full((3,2),1)

print(np.matmul(a,b))

c=np.identity(3)
print(np.linalg.det(c))