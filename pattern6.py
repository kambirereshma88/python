
row=1
while row<=4:
    col=1
    while col<=4:
        if col==2 and row==1 or col==2 and row==3:
            print("B",end=" ")
        elif col==1 and row==2 or col==3 and row==2:
            print("A",end=" ")
        elif col==1 and row==3:
            print("A",end=" ")
        elif col==3 and row==3:
            print("A",end=" ")
        elif col==3 and row==4:
            print("A",end=" ")
        elif col==1 and row==4:
            print("A",end=" ")
        else:
            print(' ',end=" ")
        
        col+=1
    print()
    row+=1

