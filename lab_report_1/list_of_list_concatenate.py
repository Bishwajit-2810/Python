list=[[1,2,3],[4,5,6]]
list2=[5,6,7,8,9,10]

for i in range(len(list)):
    if type(list[i])==type(list):
        
        list2.append(list[i])
    else:
        list2.append(list[i])
        
print(list2)    
