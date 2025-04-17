## 04 - IndexErrors & Nested Lists

### A) IndexErrors
- Occurs when selecting an item out of range of the list
- In case of states_of_america, there are 50 states
- However machine count starts from 0 to 49 when assigning a position to each item
- In event <font color="cyan">print(states_of_america[50])</font>, we will get an index error

### B) Nested Lists
- Creating a new list by making reference to 2 or more lists in it
- Ex:
~~~python
fruits = ["Cherry", "Apple", "Pear"]
veg = ["Cucumber", "Kale", "Spinnach"]
fruits_and_veg = [fruits, veg]
print(fruits_and_veg)
# The list would look like this: [["Cherry", "Apple", "Pear"], ["Cucumber", "Kale", "Spinnach"]]
print(fruits_and_veg[1][1])
# Output will be "Kale" as [1][1] asks to reference 2nd item in fruits_and_veg
# 2nd item in that variable is the "veg" list
# 2nd item in "veg" is kale
# Bear in mind that count starts from 0
# If there were 3 lists & we needed 2nd item from 3rd list, we would write [2][1]
~~~