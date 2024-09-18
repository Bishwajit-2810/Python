list=[1,2,3,4,5,6,7,8,9]

for i in range(0,len(list)-1,2):
    temp=list[i]
    list[i]=list[i+1]
    list[i+1]=temp

print(list)