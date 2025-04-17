## 01 - Random Module

### A) How to use it
- Read the docs here: https://docs.python.org/3/library/random.html
- To use it you need to first import it:
~~~python
import random
# This statement imports the random module
~~~

### B) What is a module?
- Modules are responsible for different part of functionalities in your program
- Instead of building all functionalities in 1 page of code, modules can be created/used
- In case of random, it can take months to build the codebase for the functionality
- Therefore, we borrow the functionality from an existing module to make use of it
- Ex:
~~~python
import random

random_integer = random.randint(1, 10)
print(random_integer)
# As per the documentation for this module, randint will randomize choosing 
# between 2 integers. The expectation is that a random integer will be printed.
# This logic can be applied to create your own module.
~~~

### C) How to create a module
- 1st you create a python file in the same directory as your main code
- In the python file, you declare your value/function
- In the main code, you import the python file which you've created
- When declaring, make reference to the file.variable
- file == python file && variable == variable declared in python file
- Ex:
~~~python
# This is the main.py file where we will print my favorite color.
import my_module
# The assumption is that a file call my_module.py was created.
# A variable called 'favorite_color = "Blue"' was declared in it
print(my_module.favorite_color)
# Main code calls the variable 'favorite_color' from the 'my_module.py' file
~~~
- ![image](/Images/04-Module-Creation-Ex.png)
