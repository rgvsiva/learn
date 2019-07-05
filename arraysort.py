from array import *

arr=array('i',[])
x=int(input('enter the length'))
for i in range(1,x+1):
    y=int(input('enter the next val:'))
    arr.append(y)
print (arr)

#by using min&max and creating new array
sortnew=array(arr.typecode,[])
for m in range(len(arr)):
    sortnew.append(min(arr))
    arr.remove(min(arr))

print('sortnew:', sortnew)


#sorting of an array (swapping)
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]>=arr[j]:
            temp=arr[j]
            arr[j]=arr[i]
            arr[i]=temp
print ('sort:',arr)

