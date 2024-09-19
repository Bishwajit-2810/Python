number_of_string=int(input("enter how many string: "))
size_of_string=int(input("enter size of string: "))

compressed=[]

for i in range(number_of_string):
    string=input()
    if len(string)>size_of_string:
        string=string[:size_of_string]
    
    new_compressed=''
    count=1
    for i in range(1,len(string)):
        if string[i]==string[i-1]:
            count+=1
        else:
            if count >= 1:
                new_compressed+= str(count)+string[i-1]
            else:
                 new_compressed+=string[i-1]
            
            count=1
    if count>=1:
        new_compressed+=str(count)+string[-1]
    else:
        new_compressed+=string[-1]
    
    compressed.append(new_compressed)
print(compressed)
             