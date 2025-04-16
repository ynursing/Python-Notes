## 04 - Multiple If Statements

### A) How it works
- Multiple conditions are introduced & if all conditions are true, they are all executed
- Ex:
~~~python
if condition1:
    do A
if condition2:
    do B
if condition3:
    do C
~~~
~~~python
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")
    wants_take_photo = input("Do you want a photo taken? It will cost $3 extra.\nY for Yes & N for No. ")
    if wants_take_photo == "y":
        bill += 3

    print(f"Your total is ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
~~~