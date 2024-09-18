tuple=(2,4,7,5,3,1,0)
list=[]

for i in range(len(tuple)):
    list.append(tuple[len(tuple)-1-i])

print(list)