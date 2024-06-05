
class Parent:
    def __init__(self,pname):
      self.pname = pname

class Child(Parent):
    def __init__(self,cname,pname):
        #parent.__init__(self,pname)
        super().__init__(pname)
        self.cname = cname
        print(self.cname)
        print(self.pname)

obj = Child("Child","Father")