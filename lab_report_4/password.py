def pass_maker(string):
    if len(string) < 10:
        print("expected password of 10 length")
        return
    
    
    ascii_str=str(ord(string[0]))
    upper_str=string[-3:].upper()
    lower_str=string[:4].lower()
    special_str="@"
    still_now= ascii_str+upper_str+lower_str
    special_str=special_str*((len(string))-len(still_now))
    return still_now+special_str


string=input()
new_pass = pass_maker(string)
print(new_pass)
