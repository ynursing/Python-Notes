## 03 - Math Operations in Python

### A) Add, Subtract, Multiply, Divide, Exponents
- Python will use PEDMAS rule when evaluating math operations
- Operations will be treated from LEFT to RIGHT
~~~python
# Add: 
print(1 + 2)
# Subtract:
print(2 - 1)
# Multiply:
print(3 * 3)
# Divide:
print(3 / 3)
## Data output will be a float
## To output as an int, use:
print(3 // 4)
## Output will erase all values after the decimal
# Exponent:
print(2**3)
~~~

### B) Rounding values
- Using <u>***round(value, ndigits)***</u>
- ndigits representing how many values to keep after the decimal
- Ex:
~~~python
bmi = 84 / 1.65 ** 2
print(bmi)
print(round(bmi, 5))
# bmi == 30.85399449035813
# round(bmi, 5) == 30.85399
~~~