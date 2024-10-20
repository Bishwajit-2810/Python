import numpy as np

a=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(a)

print("getting value of an index")
print(a[0,1,1])

print("changing")
a[:,1,:]=2
print(a)
a[:,1,:]=[[8,8],[9,9]]
print(a)