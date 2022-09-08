#!/usr/bin/env python3
import prompt
import random
from brain_games.scripts.brain_games import main


main()


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
        else:
            print(f'''\'{answer}\'is wrong answer ;\'(\'. Correct answer was \'{result}\' ''')
            break
        n = n + 1
