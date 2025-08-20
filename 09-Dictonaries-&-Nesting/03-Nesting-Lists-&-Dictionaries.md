## 03 - Nesting Lists & Dictionaries

### A) Syntax
~~~python
Dict = {
    'Key1': 'Item1',
    'Key2': 'Item2',
}

example_nesting = {
    'Key1': ['List'],
    'Key2': {Dict},
}
~~~

### B) Applying context
~~~python
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}
# Print statement will output "Lille"
print(travel_log["France"][1])
###############################################################
###############################################################
###############################################################
# Using this concept, the same can be applied for nested lists:
nested_list = ["A", "B", ["C", "D"]]
# Print statement will output "D"
print(nested_list[2][1])
~~~

### C) Summarizing nesting lists and dictionaries
~~~python
travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}
# Print statement will output "Stuttgart"
print(travel_log["Germany"]["cities_visited"][2])
~~~