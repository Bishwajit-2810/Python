list=[1,2,3,3,2,1,5,6,7,4,9,7,8]

min= min(list)
max= max(list)

list[list.index(max)]=min
list[list.index(min)]=max

print(list)