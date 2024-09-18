def reverse(str):
    new_str=""

    for i in range(len(str)):
        new_str+=str[len(str)-1-i]
        
    return new_str

str="hello world"
new_str= reverse(str)
print(new_str)