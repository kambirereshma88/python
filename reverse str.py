
"""
# with negative str 
a="my name is khan"
i=-1
l=-(len(a))
s="  "


while i>=l:
    s=s+a[i]
    i=i-1
print(s)

"""


#with positive str

"""
a="my name is khan"
i=0
l=(len(a))
s=" "  #empty str

while i>=l:
    s=s+a[i]
    i=i-1
print(s)
"""



a="my name is reshma"
i=0
l=(len(a))
print(l)
s=""
for i in range(len(a)-1,-1,-1):
    s=s+a[i]
print(s)

a="i am studying in itvedant institute"
i=0
l=len(a)
print(l)
s=""
for i in range(len(a)-1,-1,-1):
    s=s+a[i]
print(s)


a="i am studying python"
i=0
l=len(a)
print(l)
s=""
for i in range(0,len(a),1):
    s=s+a[i]
print(s)
    






