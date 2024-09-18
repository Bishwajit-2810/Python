length,upper,lower,num=0,0,0,0

password = input()

for i in range(len(password)):
    if len(password)>=8:
        length=1
    if password[i].isupper():
        upper=1
    if password[i].islower():
        lower=1
    if password[i].isnumeric():
        num=1
    
if (length+upper+lower+num)>=4:
    print("password accepted")
else:
    print("password not accepted")
    