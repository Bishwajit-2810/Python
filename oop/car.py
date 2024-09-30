class Car:
    def __init__(self,name,price,reg_id):
        self.name=name
        self.price=price
        self.__reg_id=reg_id
    
    def reg_getter(self):
        return self.__reg_id
        
    def show_car(self):
        print(self.name , self.price ,sep="\n")

my_car = Car("Bugatti", "200million",1001)
my_car.show_car()
# print(my_car.__reg_id)
print(my_car.reg_getter())