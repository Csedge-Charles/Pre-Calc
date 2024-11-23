import functions as trig

import random
for i in range(10):
    denominator = random.choice([1, 2, 3, 4, 6])
    slash = '/'
    pi = 'π'

    choice = random.choice(['radian', 'ratio'])

    if denominator == 6:
        numerator = random.randint(-25, 25)
        while numerator % 2 == 0 or numerator % 3 == 0:
            numerator = random.randint(-25, 25)
    elif denominator == 4:
        numerator = random.randint(-20, 20)
        while numerator % 2 == 0:
            numerator = random.randint(-25, 25)

    elif denominator == 3:
        numerator = random.randint(-15, 15)
        while numerator % 3 == 0:
            numerator = random.randint(-15, 15)

    elif denominator == 2:
        numerator = random.randint(-10, 10)
        while numerator % 2 == 0:
            numerator = random.randint(-10, 10)
    else:
        slash = ''
        denominator = ''
        numerator = random.randint(-5, 5)

    if numerator == 0:
        denominator = ''
        slash = ''
        numerator = ''
        pi = ''

    radian = f'{numerator}{pi}{slash}{denominator}'

    operator_list = ['sin', 'cos', 'tan', 'csc', 'sec', 'cot']
    chose = random.randint(0, 5)
    function_list = [trig.sin(radian), trig.cos(radian), trig.tan(radian), trig.csc(radian), trig.sec(radian), trig.cot(radian)]

    print()
    print()
    input(f'What is {operator_list[chose]}({radian}): ')
    print()
    print(function_list[chose])
    print()
    print()