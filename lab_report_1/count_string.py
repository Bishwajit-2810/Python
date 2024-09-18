list=['abc', 'xyz', 'aba', '1221']

count=0
for i in range(len(list)):
    if list[i][0]==list[i][len(list[i])-1]:
        count+=1

print(count)