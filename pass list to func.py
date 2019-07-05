

def count(ls):
    even=0
    odd=0
    for i in ls:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd

lst=[2,5,7,6,8,9,5,10,14,8]
even,odd=count(lst)
print ('even:',even,'\n''odd: ',odd)
print('Even : {} and Odd : {}'.format(even,odd))