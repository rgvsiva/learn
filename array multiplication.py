from numpy import *

arr1=array([1,2,3],[4,5,6])

print (arr1.dtype)
print (arr1.ndim) #dimension ==2 here
print (arr1.shape) #m*n (no.of col and no.of rows) (2,3)--tuple
print (arr1.size)  #no.of elements--6 here

arr2=arr1.flatten()  #converting 2D into 1D array [1,2,3,4,5,6]

arr3=arr1.reshape(3,4)  #(m,n) rows and columns---converting into 2D

arr4=arr1.reshape(2,2,3) # 3D have 2 no.of 2D and each 2D arr have 2no.of 1D array with each 3 elements

m=matrix(arr1) #matrix form ...outpur look similar like array
m=matrix('1,2,3,4 :4,5,6,7') #without array--directly giving the values.
diagonal(m)#diagonal elements
m.min()
m.max()
m=m1+m2 #adding
m=m1*m2 #multiplication

