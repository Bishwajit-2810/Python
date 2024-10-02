def vowel_counter(str):
    vowel_count=0
    consonant_count=0
    str=str.lower()
    for i in range(len(str)):
        if str[i]=='a' or str[i]=='e' or str[i]=='i' or str[i]=='o' or str[i]=='u':
            vowel_count+=1
        else:
            consonant_count+=1
    return vowel_count,consonant_count
    
    

str=input().split()
list_of_not_allowed=[]
list_of_allowed=[]
print(str)
for i in range(len(str)):
    if len(str[i]) < 5:
        list_of_not_allowed.append(str[i])
    else:
        list_of_allowed.append(str[i])
        
vowel=[]
non_vowel=[]
for i in range(len(list_of_allowed)):
    vow,con = vowel_counter(list_of_allowed[i])
    vowel.append(vow)
    non_vowel.append(con)

print(f"list of words: {list_of_allowed}")
print(f"list of vowel: {vowel}")
print(f"list of consonants: {non_vowel}")
