n=15346
n1=n
p=len(str(n))
arm=0
for i in range(0,p,1):
     arm=arm+(n%10)**p
     n=n//p

if n1==arm:
    print(n1,"is an armstrong number")

else:
    print(n1,"is not a armstrong number")




#for loop using for

for i in range(1,11,1):
    print(i*2)


for i in range(2,21,2):
    print(i)
