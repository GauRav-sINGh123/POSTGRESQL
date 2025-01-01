
name="John Doe"
age=25
gpa=2.5

print(gpa)
print(type(gpa)) #gpa is a float

gpa=int(2.5)  #type casted from float to int

print(gpa)
print(type(gpa)) #gpa is now an int
 
age=str(age) #type casted from int to strings

print(type(age))

age += 1 #Error cannot add int to str

age+="1" #251

print(age)

name=bool(name) #type casted from str to bool

print(name) #True because name is not empty if it would've been empty it would have been false