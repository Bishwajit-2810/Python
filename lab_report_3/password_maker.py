def pass_maker(str):
    if len(str)!=10:
        print("expected password of 10 length")
        return
    
    
    upper_str=str[:3].upper()
    lower_str=str[-3:].lower()
    special_str="!@#$"
    return upper_str+special_str+lower_str


str=input()
new_pass = pass_maker(str)
print(new_pass)
