

def person(name,**data): # keyword variale length arguments  (multiple data with keywords--**)
    print(name)
    print(data)
    for i,j in data.items():
        print(i,j)

person('gana',age=24,city='hyd',mob=9491143589) # wil get set