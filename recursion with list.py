a=[1,2,3,5,8,101]
def listmul(n,s):
    s=s*a[n]
    n+=1
    if n<len(a):
        return listmul(n,s)
    else:
        return s
    
print(listmul(0,1))