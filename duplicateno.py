
"""
#gives duplicate number:
a=[1,2,1,2,33,44,55,33]
i=0
for i in range(len(a)):
    for j in range(i+1,len(a),1):
        if a[i]==a[j]:
            print(a[i])
"""

a=[1,55,33,55,65,65,88,2,2,33,99,77,99,88]
i=0
for i in range(len(a)):
    for j in range(i+1,len(a),1):
        if a[i]== a[j]:
            print(a[i])
        
    
        
    
