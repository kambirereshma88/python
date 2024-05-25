import functools
a= functools.reduce(lambda x,y:x+y,[1,2,3,4,5,6])
print(a)

a= functools.reduce(lambda x,y:x*y,[1,2,3,4,5,6])
print(a)

a= functools.reduce(lambda x,y:x-y,[55,22,33,66,55,44,99])
print(a)

a=functools.reduce(lambda x,y:x%y,[666/2])
print(a)