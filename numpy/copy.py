import numpy as np

a=np.array([1,2,3,4,5])

b=a        # shallow copy / reference copy

print(a,b,sep="\n")
print()

b[3]=69

print(a,b,sep="\n")
print()


b=a.copy()   # Deep copy

print(a,b,sep="\n")
print()


b[3]=96

print(a,b,sep="\n")
print()

