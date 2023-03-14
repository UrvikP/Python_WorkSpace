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

# Start of program
hand = [rock, paper, scissors]
user_choice = int(input(
    'What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scizors'))
computer_choice = random.randint(0, 2)

if user_choice == 0 and computer_choice == 2:
    print(f'You:\n{hand[user_choice]} \n Com:\n{hand[computer_choice]}')
    print('Rock beats Scizors. You win!')
elif user_choice == 1 and computer_choice == 0:
    print(f'You:\n{hand[user_choice]} \n Com:\n{hand[computer_choice]}')
    print('Paper beats Rock. You win!')
elif user_choice == 2 and computer_choice == 1:
    print(f'You:\n{hand[user_choice]} \n Com:\n{hand[computer_choice]}')
    print('Scizors beats Paper. You win!')
elif computer_choice == 0 and user_choice == 2:
    print(f'You:\n{hand[user_choice]} \n Com:\n{hand[computer_choice]}')
    print('Rock beats Scizors. You Lose.')
elif computer_choice == 1 and user_choice == 0:
    print(f'You:\n{hand[user_choice]} \n Com:\n{hand[computer_choice]}')
    print('Paper beats Rock. You Lose')
elif computer_choice == 2 and user_choice == 1:
    print(f'You:\n{hand[user_choice]} \n Com:\n{hand[computer_choice]}')
    print('Scizor beats Paper. You Lose')
elif user_choice == computer_choice:
    print(f'You:\n{hand[user_choice]} \n Com:\n{hand[computer_choice]}')
    print("It's a draw.")
else:
    print("You typed an invalid number, you lose.")
