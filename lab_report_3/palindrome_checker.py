while True:

    str=input()
    if str=='stop':
        break
    if len(str)<3:
        print("skipped")
        continue

    for i in range(len(str)):
        if str[i]!=str[len(str)-1-i]:
            print("not palindrome")
            break
    print("palindrome")