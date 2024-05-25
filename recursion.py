def abc(n):
    print(n)
    n+=1
    if n<=10:
        return abc(n)
abc(1)







#factorial of 15:

def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)
    
result= factorial(6)

print("The factorial is", result)

