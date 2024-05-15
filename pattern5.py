"""
row=1
while row<=5:
    col=1
    while col<=5:
        if  row==1:
            print('*',end=" ")
        elif col==row:
            print('*',end=" ")
        else:
            print(" ",end=" ")
        col+=1
    print()
    row+=1



row=1
while row<=4:
    col=1
    while col<=4:
        if col==2 and row==1 or col==2 and row==3:
            print('B',end=" ")
        elif col==1 and row==2 or col==3 and row==2:
            print('A',end=" ")
        elif col==1 and row==3:
            print('A',end=" ")
        elif col==3 and row==3:
            print('A',end=" ")
        elif col==3 and row==4:
            print('A',end=" ")
        elif col==1 and row==4:
            print('A',end=" ")
        else:
            print(' ',end=" ")
        col+=1
    print()
    row+=1

"""

"""
for row in range(0,4,1):
    for col in range(0,3,1):
        if col%2==0:
            print("A",end=" ")
        elif row==0 and col%2==0:
            print(" ",end=" ")
        elif col==1 and row%2==0:
            print("B",end=" ")
        else:
            print(" ",end=" ")   
    print()
    
   """  

for row in range(0,4,1):
    for col in range(0,3,1):
        if row == 0 and col % 2 == 0:
            print(" ", end=" ")
        elif col == 1 and row % 2 == 0:
            print("B",end=" ")
        elif col%2==0:
            print("A",end=" ")
        else:
            print(" ", end=" ")
    print()












            
            

