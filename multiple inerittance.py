class Time:   #parent 1
    def __init__(self,time):
        self.time = time

class distance:   #parent 2
    def __init__(self,distance):
        self.distance = distance


class speed(distance,Time):  # child 1
    def __init__(self,distance,time):
        Time.__init__(self,time)
        distance.__init__(self,distance)

        s=distance/time
        print(f"speed of car is {s} km/hr")

obj = speed(120,20)
print(obj)