from functools import reduce
f=lambda a:a*a
d=lambda a,b:a+b

print (f(9))
print(d(8,5))

nums=[3,8,6,4,3,2,9,8,1]
eve=lambda n : n%2==0
evens=list(filter(eve,nums))    # filter give sequence
print(evens)

d=list(map(lambda m:m*2,evens))
print(d)

e=reduce(lambda x,y:x+y,evens)
print(e)