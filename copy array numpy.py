from numpy import *

arr=array([1,2,3,4,5])
arr1=array([6,5,4,3,2])
arr=arr+5 #[6,7,8,9,10]
arr2=arr+arr1 #adding (vectorized operation)

sin(arr)
cos(arr)
log(arr)
sqrt(arr)
min(arr)
max(arr)
concatenate(arr,arr1)

#copying
arr3=arr1 #copying (same memory-id)---alaising---
arr3=arr.view() #new id--diff id's

arr1[1]=5 #value changed for both arr, arr1---shallow copy(.view)
arr4=arr.copy() #diff id's
arr1[1]=9 #value doesn't change for arr4---deepcopy(.copy)