data=['name','age','city']
data1=['rohit',30,'thane']
dict={}
for i in range(len(data)):
    dict[data[i]]=data1[i]
print(dict)


#if key and value does not match :

a=['name','age','city','pin']
b=['rohit',30,'thane']
c={}
if len(a)==len(b):
    for i in range(len(a)):
        c[a[i]]=b[i]
        print(c)
else:
    print("key list and value list length should be same")





a=["name","age"]
b=["rohit",50,"thane","maharashtra"]
c={}
for i in range (len(a)):
    for j in range(len(b)):
        if i==j:
            c[a[i]]=b[i]
        elif i>j:
            c[a[i]]="default"
        elif j>(len(a)-1):
            c[j]=b[j]
print(c)


a={"name":"reshma","age":34,"city":"thane"}
print(a.keys())
print(a.values())
print(a.items())


a.pop("city")
print(a)
del a["age"]
print(a)





















            





















