def palindrome(str):
    for i in range(len(str)):
        if str[i]!=str[len(str)-1-i]:
            return False
    return True


palindrome_list=[]
list_str=input().split()
for i in range(len(list_str)):
    if palindrome(list_str[i]):
        palindrome_list.append(list_str[i])
    else:
        continue

print(palindrome_list)