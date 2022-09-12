#!/usr/bin/env python3
import prompt
import random


def welcome_user():
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


welcome_user()


def even_check():  # noqa: C901
    n = 1
    while n <= 3:
        random_number = random.randint(1, 100)
        print('''Answer "yes" if the number is even, otherwise answer "no".\n'''
              f'Question: {random_number}')
        answer = prompt.string('Your answer: ')
        right_result = ''
        if random_number % 2 == 0:
            right_result = 'yes'
        elif random_number % 2 != 0:
            right_result = 'no'
        if random_number % 2 == 0 and answer == 'yes':
            print('Correct!')
            if n == 3:
                print(f"Congratulations, {name}!")
        elif random_number % 2 != 0 and answer == 'no':
            print('Correct!')
            if n == 3:
                print(f"Congratulations, {name}!")
        else:
            print(f'\'{answer}\' is wrong answer ;(.'
                  f''' Correct answer was '{right_result}'.\n'''
                  f'''Let's try again, {name}!''')
            break
        n = n + 1
