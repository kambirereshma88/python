def abc(name,age ,city):
    a=f"my name is {name} my age is {age} and my city is {city}"
    return a

b=abc("Rohit",50,"Thane")
print(b)

#function with keyword argument
def abc(name,age ,city):
    a=f"my name is {name} my age is {age} and my city is {city}"
    return a

b=abc(name="Rohit",age=50,city="Thane")
print(b)


def abc(name,age ,city):
    a=f"my name is {name} my age is {age} and my city is {city}"
    return a

b=abc(age=50,city="Thane",name="Rohit")
print(b)


