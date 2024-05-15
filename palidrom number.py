
n=1221
n1=n
s=0
while n!=0:
    s=s*10+n%10
    print(s)
    n=n//10
if n1==s:
    print(s,"This is a palindrom number")
else:
    print(s,"This is not a palindrom number")


"""
step1
n=1234
s=0*10+1234%10
s=0+4
s=4
n=1234//10
n=123


step2
n=123
s=4
s=4*10+123%10
s=40+3
s=43
n=123//10
n=3

step3
n=12
s=43
s=43*10+12%10
s=430+2
s=432
n=12//10
n=2

step4
n=1
s=432
s=432*10+1%10
s=4320+1
s=4321
n=1//10
n=0

"""

