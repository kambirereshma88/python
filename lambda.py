a=lambda name,age,city:f"My name is {name}.My age is {age} and i live in {city}."
print(a("reshma",35,"Thane"))

#
a=lambda name,age,city="Badlapur":f"My name is {name}.My age is {age} and i live in {city}."
print(a("reshma",35))

a=lambda a,b:(a+b)
print(a(10,15))

a=lambda a,b:(a*b)
print(a(12,12))

a=lambda a,b:(a%b)
print(a(15,3))

a=lambda x,y:(x-y)
result=a(20,5)
print (result)

a=lambda x,y:(x-y)
print(a(50,25))