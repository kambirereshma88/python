#1.instance method

class Instance:
    def show(self):
        return "This is instance methods"
    
obj = Instance()
print(obj.show())


#2.class method:

class Class:
    @classmethod
    def show(cls):
        return cls   
print(Class.show())




#3.static method:

class Static:
    @staticmethod
    def show(name,age):
        print(name)
        print(age)
        return()
    
Static.show("reshma",35)









