student_number=int(input())

for i in range(student_number):
    name=input()
    name=name.strip()
    if(len(name)>20):
        print("name has more than 20 char")
        continue
    lower=name.lower()
    length=len(name)
    first_char_ascii=ord(name[0])
    
    email=f'{lower}_{length}_{first_char_ascii}'
    print(email)
    