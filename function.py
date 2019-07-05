def greet():
    print  ('hellooo \ngood morning')


def addsub(a,b):
    c=a+b
    d=a-b
    return c,d



greet()
r1,r2 = addsub(5,4)
addsub(6,7)
print (r1,r2)