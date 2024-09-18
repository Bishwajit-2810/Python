list=[0,1]
number=int(input())
for i in range(number):
    list.append(list[i]+list[i+1])
print(list)