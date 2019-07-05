def update(a):
    print(id(a))
    a=10
    print(id(a))
    print ('a',a)

def update1(a):
    print(id(a))
    a[1]=10
    print(id(a))
    print ('lst',a)
x=8
print(id(x))
update(x)
print ('x',x)   #id's of variables are changing inside and outside of function.

#pass by value, pass by reference---not applicable in python---none of these
lst=[1,4,2,3]
print (id(lst))
update1(lst)
print('ls:',lst)   #list immutable but id doesn't change


