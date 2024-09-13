# it's a python only thing (one line initialization)(same for list sets dicts tuples)

list = [ list for list in range(10)]
print(list)

list = [ list+10 for list in range(10)]
print(list)

list = [ list*10 for list in range(10)]
print(list)

list = [ 0 for list in range(10)]
print(list)

list = [ [0 for list in range(10)] for list in range(10)]
print(list)

list = [ i for i in range(100) if i%5 ==0 ]
print(list)