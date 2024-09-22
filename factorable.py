import random

a = random.randint(-2, 2)
b = random.randint(-2, 2)
c = random.randint(-4, 4)
d = random.randint(-4, 4)

while a == 0:
    a = random.randint(-2, 2)
while b == 0:
    b = random.randint(-2, 2)
while c == 0:
    c = random.randint(-4, 4)
while d == 0:
    d = random.randint(-4, 4)

while a * b == 1 or a * b == -1:
    a = random.randint(-2, 2)

sign1 = '+'
sign3 = '+'

n1 = c * b + a * d
n2 = c * d


if c * b + a * d < 0:
    n1 *= -1
    sign1 = '-'
if c * d < 0:
    n2 *= -1
    sign3 = '-'

print()
print()
input(f'{a * b}x² {sign1} {n1}x {sign3} {n2}')
print()
print()
print()