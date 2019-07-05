a=int(input('enter a number for factorial: '))

def fact(a):
    b=1
    for i in range(1,a+1):
        b=b*i
    return b
c=fact(a)
print ('factorial of ',a,'is: ',c)

#using recurrsion
def factorial(a):
    if a==0:
        return 1
    return a*factorial(a-1)

r=factorial(a)
print('factorial:',r)