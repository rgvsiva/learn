
#class: design
#object: instance


class computer:
    #attributes  --variables
    #behaviour --methods (function)
    def config(self):
        print('i5,16gb,1TB')

com1=computer()
com2=computer()
computer.config(com1)
computer.config(com2)
#or
com1.config()
com2.config()

print(type(com1))