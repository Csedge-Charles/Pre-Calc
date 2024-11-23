import random
import os
import sys
sys.path.append(os.path.abspath('/Users/charlesshao/Pre-Calc'))
import functions

radian_list = ['π/6', 'π/4', 'π/3', 'π/2', '2π/3', '3π/4', '5π/6', 'π']
determinate = [1, -1]
sign_list = ['+', '-']
trans = [1, 2, 3, 4]
trig_list = ['sin', 'cos', 'tan', 'csc', 'sec', 'cot']

a = random.choice(trans) * random.choice(determinate)
b = random.choice(trans) * random.choice(determinate)
c = random.choice(radian_list)
d = random.choice(trans)

sign_1 = random.choice(sign_list)
sign_2 = random.choice(sign_list)

if b == 1 or b == -1:
    b = random.choice(['', '-'])

trig_function = random.choice(trig_list)

print()
print()
print(f'{a}{trig_function}({b}x {sign_1} {c}) {sign_2} {d}')
print()
print()
