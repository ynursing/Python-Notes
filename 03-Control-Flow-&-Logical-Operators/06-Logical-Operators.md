## 06 - Logical Operators

### A) How it works
- A <font color="cyan">***and***</font> B #Both conditions need to be true
- C <font color="cyan">***or***</font> D #Only one condition needs to be true
- <font color="cyan">***not***</font> E #The condition must be false
- Ex:
~~~python
choice = input("left or right?")
if choice == "left" or choice == "Left" or choice == "LEFT"
# Variable is allowing for multiple ways to type left
# Same principle applies for and & not functions