## 02 - Highest Score Exercise
~~~python
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

max_score = 0
# First create a variable
# Variable will store the scores for checking
for score in student_scores:
# For loop will run through list
    if score > max_score:
# If statement will check if "score" is greater than "max_score"
        max_score = score
# In event that "max_score" is greater, store into variable "score"

print(max_score)
# Once for loop has checked the list, it will print out the final
# "max_score" value.
~~~