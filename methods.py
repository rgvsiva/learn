#variables---store data
#methods---behaviour
'''instance---
class---
static---
'''
class student:
    school='sch'
    def __init__(self,m1,m2,m3):   #self--instance varaiable
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return(self.m1+self.m2+self.m3)/3
    def get_m1(self):    #getters---accessors---fetching the value
        return self.m1
    def set_m1(self,value): #setters---mutators---changing the value
        self.m1=value
    @classmethod    #decorators
    def sch_name(cls):   #class variable
        cls.school='jaffa'
        return cls.school
    @staticmethod     #decorators
    def info():    #static method ---nothoing to do with class and instance variables
        print('affafdffas')

s1=student(45,4,65)
s2=student(5,89,36)

print(s1.avg())
print(student.sch_name())
#print(s1.info())
print(s2.avg())
