#!/usr/bin/env python3
import prompt
import random


def welcome_user():
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


welcome_user()


def calc():
    n = 1
    while n <= 3: 
        int1 = random.randint(1, 100)
        int2 = random.randint(1, 100)
        list = ['+','-','*']
        oper = random.choice(list)
        result = eval(f'{int1} {oper} {int2}')
        print(f'What is the result of the expression?\nQuestion: {int1} {oper} {int2}')
        answer = prompt.string('Your answer: ')
        if int(answer) == int(result):
            print('Correct!')
            if n == 3:
                print(f"Congratulations, {name}!")
        else:
            print(f'''\'{answer}\'is wrong answer ;(. Correct answer was \'{result}\'.\nLet's try again, {name}!''')
            break
        n = n + 1
