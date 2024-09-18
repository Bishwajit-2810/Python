str='aabbaa'

for i in range(len(str)):
    if str[i]!=str[len(str)-1-i]:
        print("not palindrome")
        break
print("palindrome")