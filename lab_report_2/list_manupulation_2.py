list1=[1,2,3,4,5,6,7,8,9]
list2=[5,6,7,8,9,10,11,12,13,14]
new_list=[]

for i in range(len(list1)):
    if list1[i] in list2:
        new_list.append(list1[i])
        
print(new_list)