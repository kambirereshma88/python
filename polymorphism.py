class A:
    def math(self):
        return f'performing addition'
    
    def math(self):
        return f'performing subtraction'
    
obj = A()
print(obj.math())




#method overriding with inheritance

class A:
    def Flying(request):
        return f'Birds are flying'
    
class B(A):
    def Flying(request):
        return f'planes are flying'
    
obj = B()
print(obj.Flying())

