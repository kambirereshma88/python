"""row=1
while row<=5:
    col=1
    while col<=5:
        if col==1 or col==3 or col==5 or row==1 or row==5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1

        
    print()
    row+=1
"""

for row in range(1,6,1):
   for col in range(1,6,1):
       if (row==1 or row==5 or col==1 or col==3 or col==5):
           print("*",end=" ")
       else:
           print(" ",end=" ")


   print()
       




















            
