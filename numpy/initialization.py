import numpy as np

print("zero array")
a=np.zeros(5)
print(a)
a=np.zeros((3,5))
print(a)
a=np.zeros((3,5,4))
print(a)

print("\none array")
a=np.ones(5)
print(a)

print("\nany array")
a=np.full((2,4),22)
print(a)

print("\nany array using previous")
a=np.full_like(a,25)
print(a)

print("\nrandom array")
a=np.random.rand(4,4)
print(a)
print()
a=np.random.random_sample(a.shape)
print(a)
print("\nrandom int")
a=np.random.randint(22,size=(4,4))
print(a)

print("\nidentity matrix")
a=np.identity(6)
print(a)

print("\nrepeat row")
a=np.array([[1,2,3,4]])
r1=np.repeat(a,4,axis=0)
print(r1)
