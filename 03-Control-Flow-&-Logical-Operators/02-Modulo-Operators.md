## 02 - Modulo Operators

### A) What is it?
- Mathematical operation that checks the remainder in a division
- Operator uses "%" between 2 values
- Ex:
~~~python
10 % 3 == 1 # 10 divide by 3 is 3 with 1 remaining
~~~
~~~python
# Putting modulo into practice
user_input = int(input("Enter a value to check if its EVEN or ODD:\n"))
if user_input % 2 == 0:
    print("Number is EVEN")
else:
    print("Number is ODD")
~~~