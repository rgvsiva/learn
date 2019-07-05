#constructor inheritance

class stu:

    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
       # self.lap=self.laptop

    def show(self):
        print(self.name, self.rollno)

    class laptop:         #object of inner class be in outer class
        def __init__(self):
            self.brand='acer'
            self.cpu='i5'
            self.ram='1Tb'
        def show(self):
            print(self.brand, self.cpu,self.ram)

    class lapt(laptop):  # object of inner class be in outer class
        def __init__(self):
            self.brand = 'vivo'
            self.cpu = 'i7'
            self.ram = '2Tb'

        def show(self):
            print(self.brand, self.cpu, self.ram)

s1=stu('gana',34)
s2=stu('siva',44)

s1.show()
#s2.show()

#lap1=s1.lap
#lap2=s2.lap
lap1=stu.laptop()
lap2=stu.laptop()
#print(id(lap1))
#print(id(lap2))
lap1.show()


lap3=stu.laptop.lapt()
lap3.show()