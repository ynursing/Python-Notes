## 01 - Functions With Inputs

### A) Basics of Functions
- You use "def" following by a name to define a function as seen below:
~~~python
def greet():
    print("Hello everyone.")
    print("I am under the water.")
    print("I am drowning.")

greet()
~~~
- Inputs can be defined when added to the parentheses as seen below:
- Parameter: Name of the data
- Argument: Value of the data
~~~python
def greet_with_name(name):
    print(f"Hello {name}.") 
    # 'name' becomes a parameter
    print(f"I am under the water, {name}")
    print(f"I am drowning, {name}")

greet_with_name("Hans")
# 'Hans' becomes the argument for the parameter 
~~~

### B) Multiple Parameters in Functions
- Example of positional argument:
~~~python
def greet_with(name,location):
    print(f"My name is {name}.")
    print(f"I live in {location}.")

greet_with("Hans","Quatre-Bornes")
# Uses positional argument to determine which parameter to associate with
# Fills out parameters based on position of arguments
~~~
- Example of keyword argument:
~~~python
def greet_with(name,location):
    print(f"My name is {name}.")
    print(f"I live in {location}.")

greet_with(location="Quatre-Bornes", name="Hans")
# Unlike positional arguements, keyword arguments allow for parameters to be
# in any order
~~~