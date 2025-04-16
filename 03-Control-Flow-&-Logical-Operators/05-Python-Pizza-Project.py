print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
pizza_price = 0
if size == "L":
    pizza_price = 25
elif size == "M":
    pizza_price = 20
elif size == "S":
    pizza_price = 15
else:
    print("You chose the wrong input for size.")
if pepperoni == "Y":
    if size == "S":
        pizza_price += 2
    else:
        pizza_price += 3
else:
    print("No pepperoni for you.")
if extra_cheese == "Y":
    pizza_price += 1
else:
    print("No extra cheese.")
print(f"Your final bill is: ${pizza_price}.")