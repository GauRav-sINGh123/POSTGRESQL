#User Validation

username=input("Enter your username: ")

if len(username)>12:
    print("Username must be less than 12 characters")
elif not username.find(" ") == -1:
    print("Username cannot contain spaces")
elif not username.isalpha():
    print("Username cannot contain digits")
else:
    print("Username is valid ")