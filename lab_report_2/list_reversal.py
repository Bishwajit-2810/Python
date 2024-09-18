list=[1,2,3,4,5,6,7,8,9]
reversed_list=[]

for i in range(len(list)-1,-1,-1):
    reversed_list.append(list[i])

print(reversed_list)