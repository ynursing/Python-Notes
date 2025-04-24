## 01 - Defining & Calling Python Functions

### A) How to define a function
- Start line with <font color="cyan">"def"</font> followed by a <font color="cyan">function_name()</font> and a colon such as <font color="cyan">":"</font>.
- Ex:
~~~python
## DEFINING THE FUNCTION
def my_function():
    print("Hello")
    print("Bye")
    
## CALLING THE FUNCTION
my_function()
################################################
# Output:
# Hello
# Bye
################################################
~~~
- Using For Loop with function can shorten code:
- ![image](/Images/06-Python-Functions-Game.png)
~~~python
# ALTERNATIVE SOLUTION:
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
for hurdles in range(6):
    jump()
~~~