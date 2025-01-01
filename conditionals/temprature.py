
unit=input("Enter the temperature unit Celsius or Fahrenheit \n Type C or F: ")
temp=float(input("Enter the temperature: "))

if unit=="C":
    temp=(temp*9/5)+32
    print(f"The temperature in Fahrenheit is {round(temp,2)}")
elif unit=="F":
    temp=(temp-32)*5/9
    print(f"The temperature in Celsius is {round(temp,2)}")
else:
    print("Invalid unit")