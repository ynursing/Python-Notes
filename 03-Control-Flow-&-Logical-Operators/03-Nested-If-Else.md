## 03 - Nested If/Else & Elif Statements

### A) How does it work?
- When an initial condition is met, a 2nd condition is introduced
- When there is a 3rd or more condition <font color="cyan">***"Elif"***</font> is used in between to add the conditions
- Ex:
~~~python
# Coding exercise code
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("How old are you?\n"))
    if age <= 12:
        print("Please pay $5")
    elif age <= 18:
        print("Please pay $7")
    else:
        print("Please pay $12")
else:
    print("Sorry you have to grow taller before you can ride.")
################################################################
weight = 85
height = 1.85

bmi = weight / (height ** 2)
👇
if bmi >= 25:
    print("overweight")
elif bmi >= 18.5:
    print("normal weight")
else:
    print("under weight")
# Take note on how to order the checks
~~~