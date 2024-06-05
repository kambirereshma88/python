row=1
while row<=6:
    col=1
    while col<=6:
        if col==6 or row==1:
            print("A",end=" ")
        if col==5 or col==6 or row==2:
            print("B",end=" ")