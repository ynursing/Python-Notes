## 02 - Understanding Offsets & Appending Items to a List

### A)What is a List?
- A list can be defined as a data structure
- A way of storing multiple information under 1 variable
- Follows the format: <font color="cyan">variable = [item1, item2, item3, ...]</font>
- Ex:
~~~python
fruits = [item1, item2, ...]
# Allows to store multiple data types in one classification/variable
grocery_list = ["Chicken", 12, True, ...]
# In this case a string, integer & boolean value are being classified for this variable
#######################################################################################
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", ...]

print(states_of_america[1])
# Prints Pennsylvania
states_of_america[1] = "Pencilvania"
# Renames Pennsylvania to Pencilvania
states_of_america.append(["Yashyland", "Poopooland"])
# Appends those items to the list
print(states_of_america)
# Prints all the states after list has been appended
~~~
- You can find the documentation for Python Lists and other List related functions here: 
- https://docs.python.org/3/tutorial/datastructures.html