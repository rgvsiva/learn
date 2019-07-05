# prime numbers
x=int(input('enter a number: '))
y=0
for i in range(2,x):
      if x%i==0:
            y+=1
if y==0:
      print('prime')
else:
      print ('not prime')


# another method (for-else method)
x=int(input('enter a number: '))
for i in range(2,x):
      if x%i==0:
            print ('not prime')
            break
else:
      print ('prime')
