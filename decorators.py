def div(a,b):
    print(a/b)

def smart_div(func):

    def inner(a,b):
        a,b=b,a
        print('df')
        return func(a,b)
    print('sd')
    return inner

div1=smart_div(div)

div1(2,4)