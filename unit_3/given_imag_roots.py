import random

option_zeros = 2 #random.randint(1, 2)

def absval(x):
    if x < 0:
        return -1 * x
    else:
        return x

if option_zeros == 1:
    #imaginary
    #a + bi
    a = random.randint(-2, 2)
    b = random.randint(-3, 3)
    
    while b == 0:
        b = random.randint(-3, 3)
        
    i_sign = ' + '
    a_copy = a 
    b_copy = b
    if a == 0:
        a_copy = ''
    if b < 0 and a != 0:
        b_copy *= -1
        i_sign = ' - '
    if b < 0 and a == 0:
        b_copy *= -1
        i_sign = '-'
    if b > 0 and a == 0:
        i_sign = ''
    if b_copy == 1:
        b_copy = ''
        
    zero = f'{a_copy}{i_sign}{b_copy}i'

    
if option_zeros == 2:
    #imaginary
    #a + bi√c

    a = random.randint(-2, 2)
    b_1 = random.randint(-2, 2)
    b_2 = random.choice([2, 3]) 
    while b_1 == 0:
        b_1 = random.randint(-2, 2)
        
    b = absval(b_1 * (b_2 ** (0.5)))

    i_sign = ' + '
    a_copy = a 
    b_1_copy = b_1
    b_2_copy = b_2
    if a == 0:
        a_copy = ''
    if b_1 < 0 and a != 0:
        b_1_copy *= -1
        i_sign = ' - '
    if b_1 < 0 and a == 0:
        b_1_copy *= -1
        i_sign = '-'
    if b_1 > 0 and a == 0:
        i_sign = ''
    if b_1_copy == 1:
        b_1_copy = ''
        
    zero = f'{a_copy}{i_sign}{b_1_copy}i√{b_2_copy}'




c = random.randint(-3, 3)
d = random.randint(-2, 2)
e = random.randint(-3, 3)
f = random.randint(-2, 2)


while c == 0 or c == 1 or c == -1:
    c = random.randint(-3, 3)
while d == 0:
    d = random.randint(-2, 2)
while e == 0:
    e = random.randint(-3, 3)
while f == 0:
    f = random.randint(-2, 2)

quadratic_coefficient_2 = -2 * a
quadratic_constant = round(a ** 2 + b ** 2)

cubic_coefficient_1 = round(c)
cubic_coefficient_2 = round(d - (2 * a * c))
cubic_coefficient_3 = round((c * (a ** 2 + b ** 2)) - (2 * a * d))
cubic_constant = round(d * (a ** 2 + b ** 2))

quartic_coefficient_1 = c
quartic_coefficient_2 = cubic_coefficient_2 + e * cubic_coefficient_1 
quartic_coefficient_3 = cubic_coefficient_3 + e * cubic_coefficient_2
quartic_coefficient_4 = cubic_constant + e * cubic_coefficient_3
quartic_constant = cubic_constant * e

fifth_coefficient_1 = c
fifth_coefficient_2 = quartic_coefficient_2 + f * quartic_coefficient_1
fifth_coefficient_3 = quartic_coefficient_3 + f * quartic_coefficient_2
fifth_coefficient_4 = quartic_coefficient_4 + f * quartic_coefficient_3
fifth_coefficient_5 = quartic_constant + f * quartic_coefficient_4
fifth_constant = f * quartic_constant

sign_1 = ' + '
sign_2 = ' + '
sign_3 = ' + '
sign_4 = ' + '
sign_5 = ' + '

x_1 = 'x'
x_2 = 'x²'
x_3 = 'x³'
x_4 = 'x⁴'
x_5 = 'x⁵'
if fifth_coefficient_2 < 0:
    fifth_coefficient_2 *= -1
    sign_1 = ' - '
if fifth_coefficient_3 < 0:
    fifth_coefficient_3 *= -1
    sign_2 = ' - '
if fifth_coefficient_4 < 0:
    fifth_coefficient_4 *= -1
    sign_3 = ' - '
if fifth_coefficient_5 < 0:
    fifth_coefficient_5 *= -1
    sign_4 = ' - '
if fifth_constant < 0:
    fifth_constant *= -1
    sign_5 = ' - '
    
if fifth_coefficient_2 == 1:
    fifth_coefficient_2 = ''
if fifth_coefficient_3 == 1:
    fifth_coefficient_3 = ''
if fifth_coefficient_4 == 1:
    fifth_coefficient_4 = ''
if fifth_coefficient_5 == 1:
    fifth_coefficient_5 = ''

if fifth_coefficient_2 == 0:
    fifth_coefficient_2 = ''
    sign_1 = ''
    x_4 = ''

if fifth_coefficient_3 == 0:
    fifth_coefficient_3 = ''
    sign_2 = ''
    x_3 = ''

if fifth_coefficient_4 == 0:
    fifth_coefficient_4 = ''
    sign_3 = ''
    x_2 = ''

if fifth_coefficient_5 == 0:
    fifth_coefficient_5 = ''
    sign_4 = ''
    x_1 = ''
    
polynomial = f'{fifth_coefficient_1}{x_5}{sign_1}{fifth_coefficient_2}{x_4}{sign_2}{fifth_coefficient_3}{x_3}{sign_3}{fifth_coefficient_4}{x_2}{sign_4}{fifth_coefficient_5}{x_1}{sign_5}{fifth_constant}'

quadratic_sign_1 = '+'
quadratic_sign_2 = '+'

if quadratic_coefficient_2 < 0:
    quadratic_coefficient_2 *= -1
    quadratic_sign_1 = '-'

if quadratic_constant < 0:
    quadratic_constant *= -1
    quadratic_sign_2 = '-'

if quadratic_coefficient_2 == 1:
    quadratic_coefficient_2 = ''
    
main = ''
d_sign = '+'
e_sign = '+'
f_sign = '+'
if c < 0:
    main = '-'
    c *= -1
    d *= -1

if d < 0:
    d_sign = '-'
    d *= -1

if e < 0:
    e_sign = '-'
    e *= -1

if f < 0:
    f_sign = '-'
    f *= -1
    

print()
print()
print(f'If one of the zeros is {zero}, ')
print()
print(f'What are the other zeros of: ')
print()
print(polynomial)
input(f'')
print(f'{main}(x² {quadratic_sign_1} {quadratic_coefficient_2}x {quadratic_sign_2} {quadratic_constant})({c}x {d_sign} {d})(x {e_sign} {e})(x {f_sign} {f})')
print()