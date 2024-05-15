data='my name is khan'
cols=1
for row in range(0,len(data),1):
    for col in range(0,len(data),1):
        if col<len(data)-cols:
            print(data[row],end=" ")

    
    print()
