
"""
row=1
while row<=5:
    col=1
    while col<=5:
        if row==1:
            print("A",end=" ")
        elif col==1 and row==2:
            print("C",end=" ")
        elif col==1 and row!=2:
            print("B",end=" ")
        col+=1
    row+=1
    print()
"""

"""
row=1
while row<=5:
    col=1
    while col<=5:
        if row==1 and col==1:
            print("1",end=" ")
        elif row==2 and col==2:
            print("2",end=" ")
        elif row==3 and col==3:
            print("3",end=" ")
        elif row==4 and col==4:
            print("4",end=" ")
        elif row==5 and col==5:
            print("5",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    print()
    row+=1
"""
row=1
while row<=5:
    col=1
    while col<=5:
        if col>=row:
            print("A",end=" ")
        else:
            print("B",end=" ")
        col+=1
    print()
    row+=1
    




        
