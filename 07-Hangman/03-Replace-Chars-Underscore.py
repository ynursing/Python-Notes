import random
word_list = ["aardvark", "baboon", "camel"]

placeholder = ""

chosen_word = random.choice(word_list)

print(chosen_word)
# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word

word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

guess = input("Guess a letter: ").lower()

# TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.

display = ""
for letter in chosen_word:
    if letter == guess:
#        print(letter)
        display += letter
    else:
#        print(placeholder)
        display += "_"

print(display)
