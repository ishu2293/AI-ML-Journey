class shape:
    def area(self):
        print("The area is calculated")

class circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = 3.14*self.radius*self.radius
        print(f"The area of circle with radius {self.radius} is {area}")    

class rectangle(shape):
     def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        
     def area(self):
        area = self.length*self.breadth
        print(f"The area of rectangle is {area}")        

class triangle(shape):
     def __init__(self, base, height):
        self.base = base
        self.height = height

     def area(self):
        area = 0.5*self.base*self.height
        print(f"The area of triangle is {area}")       

# s1 = circle(4)
# s1.area()         

# s1 = rectangle(4, 5)
# s1.area()  

s1 = triangle(8, 3)
s1.area()  
