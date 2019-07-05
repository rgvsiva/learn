#scope
a=10   #global variable
print(id(a))
def some():
    # global a   # to access global variable
    a = 23       #local variable
    x = globals()['a']
    print(id(x))
    print('inside:',x)
    print('ins:',a)

    globals()['a']=45 #to change the global variable without effecting local variable

some()
print('outside:',a)