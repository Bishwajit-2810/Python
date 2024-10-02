input = list(map(int,input("enter numbers: ").split()))
list2=[]
for i in range(len(input)):
    if (len(str(input[i])))<3:
        print(f"{input[i]} not possible")
    else:
        
        sum=0
        val=input[i]
        while val>0:
            curr=val%10
            sum=sum+curr
            val=val//10
        list2.append(sum)
print(list2)