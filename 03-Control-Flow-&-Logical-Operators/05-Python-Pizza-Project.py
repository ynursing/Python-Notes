print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
pizza_price = 0
if size == "L":
    pizza_price = 25
    if pepperoni == "Y":
        pizza_price += 3
elif size == "M":
    pizza_price = 20
    if pepperoni == "Y":
        pizza_price += 3
elif size == "S":
    pizza_price = 15
    if pepperoni == "Y":
        pizza_price += 2
if extra_cheese == "Y":
    pizza_price += 1
print(f"Your final bill is: ${pizza_price}.")