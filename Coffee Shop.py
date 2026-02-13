#lets build a simple python 
# Coffe shop program
print("=====================================")
print ("Hello, welcome to DanCoffee Shop")
print("=====================================\n")

print("Whats your name?")
name = input ("Name: ")

print("Hello buddies " + name + ", how can I help you today?")
print("======================================")

print("Are you want order our coffee menu?")
order = input("Yes or No: ")
if order.lower() == "yes":
    print("Great! Let's see our menu.")
    print(""" 
_____________________________
|       DanCoffee Shop      |
|This is our menu:          |
|1. Espresso                |
|2. Cappuccino              |
|3. Latte                   |
|4. Americano               |
|5. Premium Java Coffee     |
|___________________________|
\n""")
    print("Please select a number from the menu above.\n")
    choice = input("Please enter the number of your choice: \n")
    
    if choice == "1":
        print("You have ordered an Espresso.Wait a minute, we will prepare it for you.\n")
    elif choice == "2":
        print("You have ordered a Cappuccino.Wait a minute, we will prepare it for you.")
    elif choice == "3":
        print("You have ordered a Latte.Wait a minute, we will prepare it for you.")
    elif choice == "4":
        print("You have ordered an Americano.Wait a minute, we will prepare it for you.")
    elif choice == "5":
        print("You have ordered a Premium Java Coffee.Wait a minute, we will prepare it for you.")
    else:
        print("Invalid choice, please try again.")
    print("=======================================================================\n")
    print("Thank you for ordering at DanCoffee Shop, " + name + ".")
    print("We hope you enjoy your coffee!\n") 
    print("=======================================================================")

    