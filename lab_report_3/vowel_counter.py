str=input()
str=str.lower()
vowel_list=['a','e','i','o','u']
vowel_count=0
for i in range(len(str)):
    if str[i] not in vowel_list:
        continue
    else:
        vowel_count+=1
        
print(vowel_count)