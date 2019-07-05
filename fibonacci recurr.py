#mY method
x=int(input("'how many fib no's you want"))

def fib(a,b,x):
    for i in range(x):
        c = a + b
        print(c)
        return fib(b,c,x-1)
a,b=0,1
if x<=0:
    x=int(input('please enter a possitive number: '))
elif x==1:
    print (a)
else:
    print(a)
    print(b)
    r=fib(a,b,x-2)
print()
#anohter method
def fibo(x):
    if x<=1:
        return x
    else:
        a=fibo(x-1)
        b=fibo(x-2)
        return a+b

if x<=0:
    print(0)
else:
    for i in range(x):
        print (fibo(i))