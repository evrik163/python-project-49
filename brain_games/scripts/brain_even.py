#!/usr/bin/env python3
import prompt
import random
from brain_games.scripts.brain_games import main


def welcome_user():
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


welcome_user()


def even_check():
    n = 1
    while n <= 3:
        random_number = random.randint(1, 100)
        print(f'''Answer "yes" if the number is even, otherwise answer "no".\nQuestion: {random_number}''')
        answer = prompt.string('Your answer: ')
        if random_number % 2 == 0 and answer == 'yes':
            print('Correct!')
        elif random_number % 2 != 0 and answer == 'no':
            print('Correct!')
        else:
            print(f'''\'yes\' is wrong answer ;\'(\'. Correct answer was 'no'.\n Let's try again, {name}!''')
            break
        n = n + 1
