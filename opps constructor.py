class Data:
    def __init__(self):
        print("I will get call first")

    def show(self):
        print("I am shown,I don't know when i will get a call ")
    
    def __del__(self):
        print("I have destroyed everything......")

obj = Data()
obj.show()




