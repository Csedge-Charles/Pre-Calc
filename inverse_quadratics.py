import random

n1 = random.randint(-2, 2)
n2 = random.randint(-7, 7)
while n1 == 0:
    n1 = random.randint(-2, 2)
while n2 == 0:
    n2 = random.randint(-7, 7)
n1 *= 2

sign_1 = '+'
sign_2 = '+'

if n1 < 0:
    sign_1 = '-'
    n1 *= -1
    
if n2 < 0:
    sign_2 = '-'
    n2 *= -1
print()
print()
input(f'Graph: 1 / (x² {sign_1} {n1}x {sign_2} {n2}): ')
print()
print()
