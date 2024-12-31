num1=2
num2=3

#Arithmetic operations

print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1%num2)


#Concatenation of strings

first_name="John"
last_name="Doe"

full_name=first_name+" "+last_name

print(full_name)



print(f"Hello {first_name} {last_name}") #with f output - Hello John Doe
print("Hello {first_name} {last_name}") #without f output - Hello {first_name} {last_name}

#The f before the string tells Python to evaluate any expressions inside curly braces {} and insert their results into the string.

#{first_name} and {last_name} are placeholders that get replaced with the values of the variables first_name and last_name when the string is printed.
