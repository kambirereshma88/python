
from abstractfile import Math

class cal(Math):
    def __init__(self,*a):
        self.a=a

    def add(self):
        s=0
        for i in self.a:
            s=s+i
        return s

