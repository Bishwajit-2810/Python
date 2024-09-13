b = [1,2,3,4,5,6,7,8,9,10]

mp=map(lambda i: i*2,b)
print(list(mp))

fl = filter(lambda i: i<6 or i%2 !=0 ,b)
print(list(fl))