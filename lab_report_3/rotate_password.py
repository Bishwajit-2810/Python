m=int(input("Size of String m= "))
str=input("Input String:")
n=int(input("Number of characters to rotate:"))
final=""
if " " in str:
    print("no whitespace plz")
else:
    first_part=str[:n]
    second_part=str[n:]
    final=second_part+first_part
print(final)