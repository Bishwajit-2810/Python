str=input()
str_set=set()
break_=False
index=0
for i in range(len(str)):
    if str[i] not in str_set:
        str_set.add(str[i])
    else:
        index=i
        break_=True
        break
    
if break_:
    print("repeat found at index",index)
else: 
    print('repeat not found')