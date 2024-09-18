list=[ True,False,["hello","good morning"],5,1414,["bk","kg"]]
flat_list=[]
for i in range(len(list)):
    if type(list[i])==type(list):
        for j in range(len(list[i])):
            flat_list.append(list[i][j])
    else:
        flat_list.append(list[i])
        
print(flat_list)       
           