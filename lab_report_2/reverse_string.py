str="hello world"
new_str=""

for i in range(len(str)):
    new_str+=str[len(str)-1-i]

print(new_str)