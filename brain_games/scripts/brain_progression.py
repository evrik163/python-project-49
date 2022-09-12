#!/usr/bin/env python3
import prompt
import random


def welcome_user():
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


welcome_user()


def prog():
    print('What number is missing in the progression?')
    n = 1
    while n <= 3:
        i = 1
        my_list = []
        int1 = random.randint(1, 100)
        int2 = random.randint(1, 10)
        int3 = random.randint(0, 5)
        while i <= 6:
            my_list.append(int1)
            int1 = int1 + int2
            i = i + 1
        result = my_list[int3]
        my_list[int3] = '..'
        string = ' '.join(str(x) for x in my_list)
        print(f'Question: {string}')
        answer = prompt.string('Your answer: ')
        if int(result) == int(answer):
            print('Correct!')
            if n == 3:
                print(f"Congratulations, {name}!")
            n = n + 1
        else:
            print(f'''\'{answer}\'is wrong answer ;(. Correct answer was \'{result}\'.
Let's try again, {name}!''')
            break
