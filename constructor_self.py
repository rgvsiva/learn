

class computer:

    def __init__(self):
        self.name='siva'
        self.age=24
    def update(self):
        self.age=12
    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False
c1=computer()    #heap memory  (objects take some memory)
c2=computer()   #constructor (calculate memory)  ---called init method internally

c1.name='gana'

print(c1.name)
print(c2.name)

c1.update()     #c1 is the variable for update(self=c1)
#if c1.age==c2.age:
if c1.compare(c2):
    print("they are same")
else:
    print('not same')


print(c1.age)
print(id(c1))
print(id(c2))