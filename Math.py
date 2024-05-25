def Math(x,y,op):
    if op=="+":
        a=x+y
    elif op=="*":
        a=x*y
    elif op=="-":
        a=x-y
    else:
        a="something went wrong"
    return a

print(Math(1,2,"+"))

print(Math(1,2,"*"))
print(Math(1,2,"-"))
print(Math(1,2,"/"))


