def checkPrime(n=6):
    for i in range(2,n,1):
        r=n%i

        if r == 0:
            print(f"{n} is not a prime number")
            break

    else:
        print(f"{n} is a prime number")

checkPrime(8)