def add(*a):
    i=0
    s=0
    while i<len(a):
        s=s+a[i]
        i+=1

    return s
print(add(1,2,3,4,5,6,45,25))