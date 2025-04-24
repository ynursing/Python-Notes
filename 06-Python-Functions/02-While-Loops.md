## 02 - While Loop Function

### A) Compared to For Loop
- Ex:
~~~python
# FOR LOOP
for item in list_of_items:
    #Do something

for number in range (a, b):
    #Do something

# WHILE LOOP
while something_is_true:
    # Do something repeatedly
~~~
- ![image](/Images/06-While-Function-Game.png)
- ![image](/Images/06-While-Function-Game-1.png)
- ![image](/Images/06-While-Function-Game-2.png)
~~~python
# SOLUTION FOR ALL POSSIBLE CASES FOR REEBORG'S WORLD MAZE
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
~~~