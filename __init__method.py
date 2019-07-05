class computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
        print('in init')
    #attributes  --variables
    #behaviour --methods (function)
    def config(self):
        print ('config is : ', self.cpu,',',self.ram)

com1=computer('i5','16gb')
com2=computer('ryen','8gb')
com1.config()
com2.config()

print(type(com1))