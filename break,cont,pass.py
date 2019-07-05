
x=int(input('how many u want: '))

i = 1
av=5
while i<=x:
    if i>=av:
        print ('out of stock')
        break
    print ('biryani')
    i+=1
print ('bye')
print ()


for i in range(1,31):
    if i%3==0 or i%5==0:
        continue
    print (i)
print()

for i in range(1,16):
    if i%2!=0:
        pass
    else:
        print(i)
