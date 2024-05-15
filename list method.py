"""
a=[1,2,1,1,2,3]
a.append(11)
a.append(12)
print(a)

#insert
a.insert(1,"xyz")
print(a)

b=[1]
b.extend(a)
print(b)
print(b+a)


#remove
a.remove("xyz")
a.remove(1)
print(a)

#del
del a
del a[1]
print(a)


a.clear()
print(a)
"""

a=['rahul','rohit','saikilla','onkar','prabhudha','kajol']
b=[]
"""
for i in a:
    if 'k' in i:
        b.append(i)
    print(b)

"""
"""
for i in a:
    if 'a'==i[1]:
        b.append(i)
    print(b)
"""
 
a=['rahul','raj','rajesh','kajol','anju','shweta']
b=[]

for i in a:
    if 'j' in i:
        b.append(i)
    print(b)



for i in a:
    if 's'==i[0]:
        b.append(i)
    print(b)



























