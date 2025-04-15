## 05 - Bill Splitter Calculator Project

print("Welcome to the bill split calculator!")
bill = float(input("What is the total of the bill?\n$"))
tip = int(input("How much would you like to give? 10, 12, or 15?\n"))
people = int(input("How many people to split the bill with?\n"))
total_bill = tip / 100 * bill + bill
split_total_bill = round((total_bill / people), 2)
formatted_split = "%.2f" % split_total_bill # Forces 2 decimal points to display
print(f"Each person should pay: ${formatted_split}")
#######################################################################
# Welcome to the bill split calculator!
# What is the total of the bill?
# $150
# How much would you like to give? 10, 12, or 15?
# 12
# How many people to split the bill with?
# 5
# Each person should pay: $33.60