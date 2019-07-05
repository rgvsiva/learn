#array means only single datatype, while list is multidatatype
from array import *   #import array as arr

vals=array('i', [4,6,3,4,7,5])
print (vals)
print (vals.buffer_info())
vals.reverse()          #reverse
print (vals)

for i in range(len(vals)):
    print (vals[i])
print ()
for i in vals:
    print (i)

arr=array('u',['a','s','d','f'])    #unicode
newarr=array(vals.typecode,(a for a in vals))  #copying
newarr1=array(vals.typecode,(a*a for a in vals))
print ('newarr:',newarr)
print ('newarr1:', newarr1)
for i in arr:
    print ('arr:',i)
