list = [28,True,"hello",False,33.444]
print(list)
print(len(list))
list.append("world")
print(list)
list.extend(["no","yes",33.33])
print(list)
print(list.pop())
list.pop()
print(list)
print(list.pop(4))
list.pop(4)
print(list)
print(list[2])
list[2]="hi"
print(list)

# reference copy
list2=list
list[1]=420
print(list,list2)

# value copy
list2=list[:]
list[1]=400
print(list,list2)
