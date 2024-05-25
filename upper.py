def upper(a):
    tx=" "
    for i in a:
        if i!=" ":
            asc = ord(i)-32
            asc1 = chr(asc)
            tx=tx+asc1
        else:
            tx=tx+" "
    return tx
print(upper("my name is "))
            

def lower(a):
    tx=" "
    for i in a:
        if i>="A":
            asc=ord(i)+32
            asc1=chr(asc)
            tx=tx+asc1
        else:
            tx=tx+" "
    return tx
print(lower("MY NAME IS KHAN"))