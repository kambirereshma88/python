


#find factorial number
fact=4
i=1

while i<=fact:
    fact=fact*1
    i+=1
    print(fact)



#find armstrong number using while loop

n = 13428
p = len(str(n))
n1=n
arm=0
#arm=152

while n!=0:
    arm=arm+(n%10)**p
    n=n//10

if n1==arm:
    print(n1,"is an armstrong number")

else:
    print(n1,"is not a armstrong number")




        
    
    
