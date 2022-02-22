import random


def random_choice():
    choice_number = random.randint(1, 3)

    if choice_number == 1:
        choice = 'rock'
    elif choice_number == 2:
        choice = 'paper'
    else:
        choice = 'scissors'

    return choice


my_choice = input('Choose rock, paper or scissors: ')
opponent_choice = random_choice()

print('Your opponent chose {}'.format(opponent_choice))

if (my_choice == 'rock' and opponent_choice == 'scissors') or (
        my_choice == 'scissors' and opponent_choice == 'paper') or (my_choice == 'paper' and opponent_choice == 'rock'):
    print('You win!')
elif my_choice == opponent_choice:
    print('You tie!')
else:
    print('Sorry you lose!')

print('Thanks for playing!')
