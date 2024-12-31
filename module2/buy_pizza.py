print("Welcom To Fizza Hut")

size=input("What size pizza do you want? S, M, or L: ")
quantity=int(input("How many pizzas do you want? "))
add_pepperoni=input("Do you want pepperoni? Y or N: ")
price=5

match size:
    case "S":
        price=15
    case "M":
        price=20
    case "L":
        price=25

if add_pepperoni=="Y":
    price+=2
    
total_price=quantity*price

print(f"Your final bill is: ${total_price}")

