def func(x):
    def func2():
        print(x)
    return func2

print(func(3)())

x= func(3)
x()


def func_ad(*args, **kwargs):
    print(args,kwargs)
    print(*args)



list = [28,True,"hello",False,33.444]
print(list)
print(*list)


def func4(x,y):
    print(x,y)
    
pairs = [(1,2),(3,4)]
for pair in pairs:
    func4(*pair)
    
func_ad(1,2,3,4,5,one=1,two=2)