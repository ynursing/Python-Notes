## 02 - Verify & Change Data Types

### A) Verifying Data Types
- Use function <u>***type()***</u> to verify data type
- Ex:
~~~python
print(type(12345))
# print function used to output info from type() function
~~~

### B) Changing Data Types
- To treat a string as an integer, use function  <u>***int()***</u>
- Same can be applied using functions <u>***float(), bool(), str()***</u> 
- Ex:
~~~python
print(int("123") + int("456"))
# print() outputs the result as a string while int() treats the strings as int,
# Math operation performed & thus output will be "579"
###################################################################################
print("Number of letters in your name: " + str(len(input("Enter your name"))))
# input() prompts user to enter their name, which is a string
# len() counts the # of char, outputs as an integer
# str() converts the integer to a string
# print() outputs the 1st string, then concatenates with string from str() function
###################################################################################
name_of_user = input("Enter your name")
length_of_name = len(name_of_user)
print(type("Number of char in your name: ")) #str
print(type(length_of_name)) #int
print("Number of char in your name: " + str(length_of_name))
# Same way to represent the previous code using variables & checks
~~~