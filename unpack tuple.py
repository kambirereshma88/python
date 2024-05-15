"""
a=('reshma',34,'thane')
(name,age,city)= a
print(name)
print(age)
print(city)


b=[11,22,33,1,2,3,4,5,6,6,7,8]
(a,b,c,*d)=b
print(b)
print(d)


a=(1,2,3,44)
b=list(a)
b[1]=22
b[2]=33
a=tuple(b)
print(a)


"""


a=[153,11,22,24,140,556]
b=[]
c=[]
for i in a:
    if i%2==0:
        b.append(i)
print(b)


for i in a:
    if i%2!=0:
        c.append(i)
print(c)




a=['rahul','rohit','saikilla','onkar','prabhudha','kajol']
b=[]
for i in a:
    if len(i)==5:
        b.append(i)
print(b)


    

























