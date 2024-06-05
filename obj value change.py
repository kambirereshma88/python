class A:
    def __init__(self,name,age):
        self.name= name
        self.age= age

    def show(self):
        return f"My name is {self.name} and my age is {self.age}"
    
obj = A('reshma',35)

obj =A('resh',35)

print (obj.show())

        
