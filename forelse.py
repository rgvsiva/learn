n=[5,34,34,44,41]

for i in n:
    if i%5==0:
        print (i)
        break    #compulsory, if not we wil find not found in output
else:
    print ('not found')