list=[1,2,3,4,5,5,5,6,6,6,7,8,9]

list2=[]

for i in range(len(list)):
    if list[i] not in list2:
        list2.append(list[i])
        
print(list2)
