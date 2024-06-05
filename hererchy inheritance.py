class parent:
    def __init__ (self,land,car,tractor,house):
        self.land=land
        self.car=car
        self.tractor=tractor
        self.house=house


class child1(parent):
    def show(self):
        a=self.land/2
        print(f"My parent gave me {a}acr land and {self.tractor} tractor")


class child2(parent):
    def show(self,home):
        a=self.land/2
        print(f"My parent gave me {a} acr land and {self.car }car and i have my own {home}")




ch1 = child1(10,'nexon','mahindra 445','bunglow')
ch1.show()

ch2=child2(10,'nexon','mahindra 445','bunglow')
ch2.show("parent niwas")

