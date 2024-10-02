verb_list=["am","going",'enjoying']
reverse_list=[]
str=input().split()

if len(str)<7:
    print("condition doesn't match")
else:
    for i in range(len(str)):
        if str[i].lower() in verb_list:
            reverse_list.append(str[i][::-1])
        else:
            continue
print(str)
print(verb_list)
print(reverse_list)