num=5
for i in range(num):
    for j in range(i):
        print(" * ",end='')
    print()
    
    
for i in range(num):
    for j in range(num-i):
        print(" * ",end='')
    print()