class A:
    def __init__ (self,__name):
        self.__name = __name 
        print(self.__name)

    def __show(self):
        print("i am private method........ ")

    def display(self):
        self.__show()

obj = A("Ram")
obj.display()





#this is another method to acces private method outside class
obj._A__show()       
print(obj._A__name)
    
