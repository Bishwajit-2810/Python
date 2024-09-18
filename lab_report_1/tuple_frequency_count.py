tuple=((1,2,3),(4,5,6),(1,2,3))
dict={}
for i in range(len(tuple)):
    for j in range(len(tuple[0])):
        if tuple[i][j] in dict:
            dict[tuple[i][j]]+=1
        else:
            dict[tuple[i][j]]=1
    
    
print(dict)