
i=1
while i<=4:
    j=1
    while j<=i:
        print ('@', end='')
        j+=1
    print()
    i+=1
    
print()


i=1
while i<=4:
    j=1
    while j<=5-i:
        print ('@', end='')
        j+=1
    print()
    i+=1
    
print()

for i in range(4):
    for j in range(4):
        print ('#',end='')
    print ()
print()


for i in range(4):
    for j in range(i+1):
        print ('#',end='')
    print ()
print()

for i in range(4):
    for j in range(4-i):
        print ('#',end='')
    print ()
