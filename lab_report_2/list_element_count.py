list=[1,2,3,4,5,5,5,6,6,6,7,8,9,10,11,12,13,14]

dict={}

for i in range(len(list)):
    if list[i] in dict:
        dict[list[i]]+=1
    else:
        dict[list[i]]=1
    
print(dict)