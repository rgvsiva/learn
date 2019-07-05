#reverse of array withour built in func (swapping)

from array import *

arr=array('i',[])
x=int(input('enter the length'))
for i in range(1,x+1):
    y=int(input('enter the next val:'))
    arr.append(y)

print (arr)

#reverse of array withour built in func (swapping)
l=x #input for user
for i in range(x//2):
        temp=arr[i]
        arr[i]=arr[l-1]
        arr[l-1]=temp
        l-=1
print ('reverse:',arr)
print()

#arr.reverse()  # inbuilt func

#another method by takind new array
rev=array(arr.typecode,[])
for i in range(len(arr)-1,-1,-1):
    rev.append(arr[i])
print ('REV:',rev)

print(arr)
#efficient method
r=array(arr.typecode,[])
for i in range(len(arr)-1,-1,-1):
    r=r+array(arr.typecode,[arr[i]])
print ('r:',r)