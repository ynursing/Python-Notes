## 04 - Assignment Operators & F Strings

### A) Assignment Operators
- Assignment operators will increment, depending on the operator, the original value by the value on the right
~~~python
+= 
# increment up by value on right 
-=
# increment down by value on right 
*=
# increment by multiplying by value on right 
/=
# increment by dividing by value on right 
~~~
- Ex:
~~~python
score = 0
score += 10
print(score)
# output will be 10
~~~

### B) F-Strings
- Allows to insert variables or an expression into a string
- (<font color="cyan">f</font>"Any string <font color="cyan">{variable}</font>")
- Ex:
~~~python
score = 3
height = 1.94
is_winning = True

print(f"Your score is {score}, Your height is {height} & you winning is {is_winning}.")
# Output: Your score is 3, Your height is 1.94 & you winning is True.
# All 3 data types were integrated into print function