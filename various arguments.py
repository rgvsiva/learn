def add(a,b): #(formal arguments--a,b
    c=a+b
    print(c)

add(5,6)  #actual arguments---5,6
#actual arguments---4 types--postion, keyword, default,variable length
print()

def person(name,age=18):
    print(name)
    print(age-5)
person('siva', 24)           #position
person(age=24,name='siva')   #keyword
person ('siva',34)              #default

def sum(a,*b):  #varialbe length (*b)---wil create tuple
    c=a
    for i in b: # for tuple elements
        c=c+i
    print(c)
sum(5,6,7,8,9)