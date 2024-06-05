class Parent:
    def __init__(self,iphone):
     self.iphone = iphone

class Child(Parent):
   def show(self):
      return f"My parent gifted me {self.iphone}"
   
obj = Child("iphone 15 pro")
print(obj.show())


class Parameters:
   def __init__(self,radius,base,height):
      self.radius = radius
      self.base = base 
      self.height = height

class Circle(Parameters):
   def Areaofcircle(self):
      self.a = 3.14*(self.radius)**2
      return f"Area of Cirlce is {self.a}"
   
class Semicircle(Circle):
   def semicircle(self):
      s= self.a/2
      return f"Area of semicircle is {s}"
   

obj = Semicircle(20,30,15)
print(obj.Areaofcircle())
print(obj.semicircle())