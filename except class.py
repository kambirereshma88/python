class A:
    def div(self,a,b):
        try:
            d=a/b
        except Exception as e:
            return e
        else:
            return d
        finally:
            print("Always Running")

obj = A()
print(obj.div(1,2))