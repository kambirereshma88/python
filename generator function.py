def abc():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    yield 6 
    yield 7 
    yield 8
    yield 9
    yield 10

obj = abc()
#print(next(obj))
#print(next(obj))
#print(next(obj))


for i in range(10):
    print(next(obj))






