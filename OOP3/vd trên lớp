import math
class Point:
    x = int
    y = int
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return"(%d,%d)" % (self.x,self.y)
    
    def read (self):
        self.x = int(input("Nhapx: "))
        self.y = int(input("Nhapy: "))
    
    def distance (self, point):
        d = math.sqrt ((self.x - point.x)**2 + (self.y - point.y)**2)
        return d


diemA = Point(3,4)
print(diemA)

diemB = Point()
diemB.read()
print(diemB)

diemC = Point(-diemB.x , -diemB.y)
print(diemC)

diem0 = Point()
print(diemB.distance(diem0))
print(diemA.distance(diemB))
