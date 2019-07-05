from array import *

arr=array('i',[])
x=int(input('enter the length'))
for i in range(1,x+1):
    y=int(input('enter the next val:'))
    arr.append(y)

print (arr)

val=int(input('enter the val for search: '))
a,k=0,0
for e in arr:
    if e==val:
        print ('found at:',k)
        a+=1
    k += 1
if a==0:
    print('not found')
print()
#print(arr.index(val))



#create an array with 5 values and delete the value at index number 2 without using builtin func

new=array(arr.typecode,[])
for i in range(len(arr)):
    if i==2:
        continue
    new.append(arr[i])
print (new)