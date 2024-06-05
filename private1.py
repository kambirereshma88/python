class A:
    def __init__(self,__name):
        self.__name = __name

    def show1(self):
        print(self.__name)

class B(A):
        def show(self):
            print(self.__name)

    
obj = B('i am learning python ')
obj.show1()
#obj.show()