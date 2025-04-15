## 01 - Print to Console + Take Input from Console 

### A): Printing to console with Python
- Using <u>***print()***</u> function
- Ex:
~~~python
print("Whatever string you want here")
# Will print all strings entered within the quotation marks
~~~

### B) Taking input from console
- Using <u>***input()***</u> function prompts an entry on terminal prior to exiting the code
- Ex:
~~~python
print(input("Typically a question goes here"))
# Input function is treated first. Prompt appears in terminal
# Print function prints out input captured then exits the code
~~~

### C) Subscripting
- Using <u>***[ ]***</u> with <u>***print()***</u> to output a specific char in a string
- <font color="cyan">*Bear in mind that count starts from <u>0</u>*</font>
- If needed, value can also be negative, which starts count from last value
- Ex:
~~~python
print("Hello"[1])
# Outputs the letter "e"
print("Hello"[4])
# Outputs the letter "o"
print("Rainbow"[-1])
# Outputs the letter "w"
print("Rainbow"[-3])
# Outputs the letter "b"
~~~

### D) Counting Length of Data
- Using <u>***len()***</u> to count # of char in a string
- Ex:
~~~python
print(len("Hello"))
# Output will be 5 as there are 5 char in "Hello"