#List is a collection which is ordered and changeable. Allows duplicate members.

names=["John", "Jane", "Jill", "Jenny"]
names.append("Lily")
names.pop() # Removes the last item
names.remove("Jill") #Removes the specified item
names.insert(1, "Jill") #Inserts the specified item at the specified index
names.count("Jill") #Returns the number of occurences of the specified value
names.index("John") #Returns the index of the first element with the specified value
names.clear() #Removes all the elements