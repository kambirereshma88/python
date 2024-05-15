
"""
#this is shown by for loop
for row in range(1,6,1):
    for col in range(1,6,1):
        if row==1:
            print('A',end=" ")
        elif col==1 and row!=1:
            print('B',end=" ")
    print()
"""
"""
#this shown by while loop
row=1
while row<=5:
    col=1
    while col<=5:
        if row==1:
            print("A",end=" ")
        elif col==1:
            print("B",end=" ")
        col+=1
    row+=1
    print()

"""
"""
#using for loop:
for row in range(1,6,1):
    for col in range(1,6,1):
        if row==1:
            print('A',end=" ")
        elif col==1 and row==2:
                print('c',end=" ")
        elif col==1 and row!=2:
            print('B',end=" ")        
    print()
"""

#using while loop:

row=1
while row<=5:
    col=1
    while col<=5:
        if row==1:
            print('A',end=" ")
        elif col==1 and row==2:
            print('c',end=" ")
        elif col==1 and row!=2:
            print('B',end=" ")
        col+=1
    row+=1
    print()
        

            
        






                
