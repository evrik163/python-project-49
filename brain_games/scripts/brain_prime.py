#!/usr/bin/env python3
import prompt
import random


def welcome_user():
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

welcome_user()

def fin():
    print(f'''Answer "yes" if given number is prime. Otherwise answer "no".''')
    n = 1
    while n <= 3:
        random_number = random.randint(1, 100)
        print(f'Question: {random_number}')
        answer = prompt.string('Your answer: ')
        i = 2
        lits = [1]
        while i != random_number:
            if random_number % i == 0:
                lits.append(i)
                random_number = random_number / i
            elif random_number % i != 0:
                i = i + 1
        lits.append(int(random_number))
        right_answer = ''
        if len(lits) == 2:
            right_answer = 'yes'
        elif len (lits) > 2:
            right_answer = 'no'
        if len(lits) == 2 and answer == 'yes':
            print('Correct!')
            if n == 3:
                print(f"Congratulations, {name}!")
        elif len(lits) > 2 and answer == 'no':
            print('Correct!')
        else:
            print(f'''\'{answer}\'is wrong answer ;(. Correct answer was \'{right_answer}\'.\nLet's try again, {name}!''')
            break
        n = n + 1
