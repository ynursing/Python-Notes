## 01 - Python Dictionaries Deep Dive

### A) Dictionaries
- Works similarly to a real dictionary
  - A word/key has an associated explanation/value
- Ex:

| Key      | Value                                                                     |
|----------|---------------------------------------------------------------------------|
| Bug      | An error in a program that prevents the program from running as expected. |
| Function | A piece of code that you can easily call over and over again.             |
| Loop     | The action of doing something over and over again.                        |
~~~python
example_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
}

print(example_dictionary["Function"])
~~~

### B) Wipe an existing dictionary
~~~python
example_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}
empty_dictionary = {} #Adding curly brackets and nothing inside can clear an existing dictionary

example_dictionary["Loop"] = "The action of doing something over and over again."

example_dictionary = {}
print(example_dictionary)
~~~

### C) Edit value of a key in a dictionary
~~~python
example_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
}
print(example_dictionary)

example_dictionary["Loop"] = "The action of doing something repeatedly without end."

print(example_dictionary["Loop"])
~~~

### D) Loop through a dictionary
~~~python
example_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
}

for key in example_dictionary:
    print(key)
    print(example_dictionary[key])
~~~