# Chooses a random name in the list friends
import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# OPTION 1
# Number of items start from 0 to 4
random_index = random.randint(0, 4)
# Using random.randint(a, b) function, I can randomize between int 0 & int 4
print(friends[random_index])
# random_integer randomly selects between 0 & int 4
# Print function prints an item from the list friends & selects the name
# based on the items position

# OPTION 2
print(random.choice(friends))
# random.choice function allows picking from a sequence of items