class First:
    a="class variable"
    print(a)

o=First()
print(o.a)






#static Variable
class Second:
    def show(self,name):
        print(name)

 # def show1(self,name):
  # print(name)

obj= Second()
obj.show('Reshma')





#instance Variable:

class Third:
    def show(self,name):
        self.name = name 
        print(name)

    def show1(self):
        print(self.name)

obj = Third()
obj.show("reshma")
obj.show1()



