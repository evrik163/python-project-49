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


def prime_factor(n):
    i = n
    lits = []
    while n != 1:
        if i == 0:
            break
        elif n%i == 0:
            lits.append(i)
            i = i - 1
        else:
            i = i - 1
    return lits


def gcd():
    print('Find the greatest common divisor of given numbers.')
    n = 1
    while n <= 3:
        int1 = random.randint(2, 100)
        int2 = random.randint(2, 100)
        print(f'Question: {int1} {int2}')
        a = prime_factor(int1)
        b = prime_factor(int2)
        c = (set(a).intersection(b))
        my_list = list(c)
        result = my_list[-1]
        answer = prompt.string('Your answer: ')
        if int(answer) == int(result):
            print("Correct!")
            if n == 3:
                print(f"Congratulations, {name}!")
            n = n + 1
        else:
            print(f'''\'{answer}\'is wrong answer ;(. Correct answer was \'{result}\'\nLet's try again, {name}!''')
            break
