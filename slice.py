a = "my nAme is khan"
data='aeiou'
v=0
c=0
s=0
for i in range(len(a)):
    if a[i].lower()in data:
        v=v+1
    elif (a[i]not in data)and (a[i]!=" "):
        c=c+1
    else:
        s=s+1
print(f"vowels are {v}")
print(f"consonants are {c}")
print(f"spaces are {s}")
        
