list=[9,8,7,6,5,4,3,2,1]

for i in range(len(list)):
    for j in range(len(list)-1-i):
        if list[j]>list[j+1]:
            temp=list[j]
            list[j]=list[j+1]
            list[j+1]=temp
            
print(list)