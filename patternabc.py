cols=1
for row in range(65,71,1):
    for col in range(65,71,1):
        if col<=70-cols:
            print(" ",end=" ")
        else:
            print(chr(row),end=" ")
    cols+=1
    print()
    
