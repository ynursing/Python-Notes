import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
user_input = int(input('Welcome to Rock, Paper, Scissors challenge.'
                       'Type 0 for Rock, 1 for Paper, 2 for Scissors.\n'))
moves = [rock, paper, scissors]
if user_input < 0 or user_input >= 3:
    print("Invalid option; Computer wins by default.")
else:
    print(moves[user_input])
    print('The computer chose:')
    computer_choice = random.choice(moves)
    print(computer_choice)
    if user_input == moves.index(computer_choice):
        print("It's a draw.")
    elif (user_input == 0 and computer_choice == moves[2]) or \
          user_input == 1 and computer_choice == moves[0] or \
          user_input == 2 and computer_choice == moves[1]:
        print("You win!")
    else:
        print("You lose!")