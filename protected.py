class A:
    def __init__(self, _name):
        self. _name= _name

class B(A):
    def _show1(self):
        print(self. _name)


obj = B("Reshma")
obj._show1()
print(obj. _name)