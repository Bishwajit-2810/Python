number=int(input())
prime=True
for i in range(2,number):
    if(number%i==0):
        prime=False
        break
    
if(prime):
    print("prime")
else:
    print("non prime")

