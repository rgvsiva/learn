
x=int(input("how many fibonacci no's u want: "))
def fib(x):
    a=0
    b=1
    if x<=0:
          print('please enter possitive number')
    elif x==1:
          print(a)
    elif x>=2:
          print(a)
          print(b)
          for i in range(2,x):
              c=a+b
              print(c)
              a=b
              b=c
fib(x)
#my method
def fibo(x):
    fib=[0,1]
    n,m=0,1
    for i in range(x-2):
          d=n+m
          n=m
          m=d
          fib.append(m)
    return(fib)
a=fibo(x)
print(a)
y=int(input('which fibonacci number you want: '))
if y<=0 or y>x:
    print("list does't have it")
else:
    print(a[y-1])


