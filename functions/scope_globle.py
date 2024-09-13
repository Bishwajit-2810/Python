x = "Bk"

def func(name):
    global x
    x=name
    
print(x)
func("changed")
print(x)