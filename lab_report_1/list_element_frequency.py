list=[[1,2,3],[4,5,6],[1,2,3]]
dict={}
for i in range(len(list)):
    for j in range(len(list[0])):
        if list[i][j] in dict:
            dict[list[i][j]]+=1
        else:
            dict[list[i][j]]=1
    
    
print(dict)