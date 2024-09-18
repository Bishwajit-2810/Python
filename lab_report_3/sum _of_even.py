x=[3,4,5,7,8,10,'dghf','cbxgc',3.5, 6.2]
sum=0
for i in range(len(x)):
    if type(x[i]) == int and x[i]%2==0:
        sum=sum+x[i]

print(sum)