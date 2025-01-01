#Circumference of Circle

import math

radius=float(input("Enter the radius of the circle:"))

circumference=2*math.pi*radius

print(f"The circumference of the circle is {round(circumference,3)}")
 

#Area of Circle

area=math.pi*radius**2

print(f"The area of the circle is {round(area,3)}")