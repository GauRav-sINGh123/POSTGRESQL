print("Discover your Spirit Animal! 🐾")
print("Answer a simple question to find out!")
print("What’s your favorite element?")
print("1: Fire 🔥\n2: Water 💧\n3: Earth 🌍\n4: Air 🌬️\n5: Lightning ⚡")

choice = int(input("Enter the number of your choice: "))

match choice:
    case 1:
        print("🔥 Your Spirit Animal is a Phoenix! Rising from the ashes, you are a symbol of resilience.")
    case 2:
        print("💧 Your Spirit Animal is a Dolphin! Playful and wise, you flow effortlessly through challenges.")
    case 3:
        print("🌍 Your Spirit Animal is a Bear! Strong and grounded, you are the protector of the wild.")
    case 4:
        print("🌬️ Your Spirit Animal is an Eagle! With keen vision and grace, you soar above all.")
    case 5:
        print("⚡ Your Spirit Animal is a Dragon! Fierce and powerful, you bring awe wherever you go.")
    case _:
        print("🤔 Hmm... that's not a valid choice! Perhaps you're a mysterious Chimera?")
