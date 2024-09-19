list_size=int(input("size of list: "))
set_of_char=set()
for i in range(list_size):
    new_string=input()
    for char in new_string:
        if char not in set_of_char:
            set_of_char.add(char)
    
print(sorted(set_of_char))
