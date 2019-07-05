
x=int(input("upto which fibonacci no's u want: "))
def fib(x):
    a=0
    b=1
    if x<=0:
          print('not possible')
    elif x==1:
          print(a)
    elif x>=2:
          print(a)
          print(b)
          for i in range(2,x):
              c=a+b
              if c<=x:
                print(c)
              else:
                  break
              a=b
              b=c
fib(x)