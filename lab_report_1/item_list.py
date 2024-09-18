anime_names = ["Attack on Titan","Death Note","One Punch Man","My Hero Academia","Naruto","Bleach","Dragon Ball Z","Sword Art Online"]

length_list=[]

for i in range(len(anime_names)):
    length_list.append(len(anime_names[i]))

print(length_list)




new_anime_names=[]
for i in range(len(anime_names)):
    new_anime_names.append(anime_names[i].swapcase())
    
print(new_anime_names)



