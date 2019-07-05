import math
x=int(input('Enter maximum number: '))
x=math.sqrt(x)
x=math.floor(x)
for i in range(x+1):
    print (i*i)
print()
print()

#another method
for i in range(501):
    if i*i<=500:
        print (i*i)
        


    
