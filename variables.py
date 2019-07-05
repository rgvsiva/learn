#two types:: instance varaibles & class(static) variables
#if we define a variable inside the init method--instance variable
#if we define a variable outside the init method --class variable

#namespace==is an area where we create and store objects/varibale
#class namespace  & object\instance namespace
class car:
    wheels=4      #class variable...(namespace)
    def __init__(self):
        self.milage=10          #instance variables--- (namespace)
        self.company='BMW'

c1=car()
c2=car()

c1.milage=15

car.wheels=5

print(c1.company , c1.milage , c1.wheels)
print(c2.company , c2.milage , c2.wheels)