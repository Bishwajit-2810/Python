name_list=["Umme","Eity","Esrat"]

dict={}
asc_list=[]

for i in range(len(name_list)):
    sum=0
    for j in range(len(name_list[i])):
        asc_value=ord(name_list[i][j])
        sum=sum+asc_value
    dict[name_list[i]]=sum
    asc_list.append(sum)
    
print(asc_list)