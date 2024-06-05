stdata='ABCDEF'
cols=1
for row in range(0,len(stdata),1):
    for col in range(0,len(stdata),1):
        if col< len(stdata)-cols:
            print(" ",end=" ")
        else:
            print(stdata[row],end=" ")
    cols+=1
    print()


"""
step1:-1 for outer loop 
cols=1
row=65
inner loop will run

"""
