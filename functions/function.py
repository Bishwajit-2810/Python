def func():
    print("hello")

def func2(x,y,Z=None):
    return x+y,x*y

def func3():
    print("hello")
    def func4():
        print("good morning")
    func4()

func()
print(func2(4,6))
func3()
