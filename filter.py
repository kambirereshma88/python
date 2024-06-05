"""
def fil(n):
    if n%2==0:
        return n
    else:
        return False
    
    a=filter(fill,[1,2,3,4,5,6])

    print(list(a))

"""

b=['rahul','om','reshma','vaibhavi']

def last_a(n):
    if  n[-1]=="a":
           return True
    else:
            return False
        
        
b1=filter(last_a,b)
print(list(b1))

    
b=['rahul','om','reshma','vaibhavi','saikilla','rama','gopa']

def last_a(n):
    if  n[-1]=="a" and len(n)==4:
           return True
    else:
            return False
        
        
b1=filter(last_a,b)
print(list(b1))
