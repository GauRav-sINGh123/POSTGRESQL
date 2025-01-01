print("🎉 Welcome to the Event App! 🎉")

 
age = int(input("Enter your age: "))
is_registered = input("Are you registered for the event? (yes/no): ").strip().lower()
has_ticket = input("Do you have a ticket? (yes/no): ").strip().lower()

 
if age >= 18 and is_registered == "yes" and has_ticket == "yes":
    print("✅ You are all set! Welcome to the event!")
elif age < 18 and (is_registered == "yes" or has_ticket == "yes"):
    print("⚠️ You need parental consent to attend this event.")
elif not (is_registered == "yes" or has_ticket == "yes"):
    print("❌ Sorry, you cannot attend the event. Please register and get a ticket first.")
else:
    print("🤔 Something's not right. Check your details and try again.")
