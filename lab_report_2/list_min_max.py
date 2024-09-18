list=[1,2,3,4,5,6,7,8,9]

max=list[0]
min=list[0]
for i in range(len(list)):
    if(list[i]>max):
        max=list[i]
    if(list[i]<min):
        min=list[i]

print(max)
print(min)