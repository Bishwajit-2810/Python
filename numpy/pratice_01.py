# 1 1 1 1 1
# 1 0 0 0 1
# 1 0 9 0 1
# 1 0 0 0 1
# 1 1 1 1 1

import numpy as np

a=np.zeros((5,5))
a[0,:]=1
a[4,:]=1
a[:,0]=1
a[:,4]=1
a[2,2]=9
print(a)


# another way
a=np.ones((5,5))
b=np.zeros((3,3))
b[1,1]=9
a[1:4,1:4]=b
print(a)
