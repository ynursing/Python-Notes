## 03 - Using For Loops with Range Function

### A) Range Function:
~~~python
for number in range(1, 10):
    print(number)
# Outputs 1,2,3,4,5,6,7,8,9
############################################
# How to add all numbers between 1 & 100
total = 0
for number in (range(1, 101)):
    total += number
# "+=" allows the addition of all var in the range then 
# stores the value as "total"
print(total)
~~~