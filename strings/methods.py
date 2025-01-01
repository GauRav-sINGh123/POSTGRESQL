#Inbuilt string methods in Python

print(help(str)) #Prints all the methods

name=input("Enter your name: ")

print(f"Your name has {len(name)} letters")

 
occurenceOf=input("Enter the letter you want find the occurence of: ")

print(name.find(occurenceOf)) #Finds first occurence

print(name.rfind(occurenceOf)) #Finds last occurence

print(name.count(occurenceOf)) #Counts the number of occurences

 
print(name.capitalize()) #Capitalizes the first letter

print(name.upper()) #Capitalizes all the letters

print(name.lower()) #Lowercases all the letters

print(name.replace(" ", "")) #Removes all the spaces