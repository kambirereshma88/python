#Write A Program Using Function Definition To Print Multiplication Of All The Numbers In A List.
a=[5,2,3,6,4,7,8,9,1]

def listmul(n,x):
    x=x*a[n]
    n+=1
    if n<len(a):
        return  listmul(n,x)
    else:
        return x
print(listmul(0,1))