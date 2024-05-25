

def outer(row):
    def inner(col):
        print("*",end=" ")
        col+=1
        if col<=row:
            return inner(col)
    inner(1)
    row+=1
    print()
    if row<=4:
        return outer(row)
    
outer(1)




def outer(row):
    def inner(col):
        print ("*",end=" ")
        col+=1
        if col<=row:
            return inner(col)
    inner(1)
    row+=1
    print()
    if row<=6:
        return outer(row)
    
outer(1)




def outer(row):
    def inner(col):
        print("5",end=" ")
        col+=1
        if col<=row:
            return inner(col)
    inner(1)
    row+=1
    print()
    if row<=5:
        return outer(row)
    
outer(1)





