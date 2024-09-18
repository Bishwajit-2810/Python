list=[1,2,3,4,5,6,7,8,9]
list2=[]

for i in range(len(list)):
    if list[i]%2==0:
        list2.append(list[i])

print(list2)