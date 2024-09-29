import random

def capasify(x, y):
    range_list = []
    while x <= y:
        range_list.append(x)
        x += 1
    return  ", ".join(map(str, range_list)) 


para_choice = random.randint(1, 100)
if para_choice <= 80:
    parameters = [-1, 0, 1]
if para_choice > 80:
    parameters = [0]
obj_range = 3



m = obj_range
n = []
for i in (parameters):
    i *= -1
    n.append(i)
    
case = random.randint(1, 5)

#quadratic 1
a1 = random.randint(-2, 2)
b1 = random.randint(-4, 4)
c1 = random.randint(-2, 2)
d1 = random.randint(-5, 5)

while a1 == 0:
    a1 = random.randint(-2, 2)
while c1 == 0:
    c1 = random.randint(-2, 2)
while d1 == 0:
    d1 = random.randint(-5, 5)
while b1 == 0:
    b1 = random.randint(-5, 5)

first_coeff = a1 * c1
second_coeff = a1 * d1 + c1 * b1
third_coeff = b1 * d1

first_sign_1 = ' + '
first_sign_2 = '+'
if first_coeff == 1:
    first_coeff = ''
if first_coeff == -1:
    first_coeff = '-'
if second_coeff < 0:
    second_coeff *= -1
    first_sign_1 = ' - '
if third_coeff < 0:
    third_coeff *= -1
    first_sign_2 = '-'
if second_coeff == 1:
    second_coeff = ''

x = 'x'

if second_coeff == 0:
    first_sign_1 = ''
    second_coeff = ''
    x = ''
first_quadratic = f'{first_coeff}x²{first_sign_1}{second_coeff}{x} {first_sign_2} {third_coeff}'


#quadratic 2

a2 = random.randint(-2, 2)
b2 = random.randint(-4, 4)
c2 = random.randint(-2, 2)
d2 = random.randint(-5, 5)

while a2 == 0:
    a2 = random.randint(-2, 2)
while c2 == 0:
    c2 = random.randint(-2, 2)
while d2 == 0:
    d2 = random.randint(-5, 5)
while b2 == 0:
    b2 = random.randint(-5, 5)

first_coeff_2 = a2 * c2
second_coeff_2 = a2 * d2 + c2 * b2
third_coeff_2 = b2 * d2

second_sign_1 = ' + '
second_sign_2 = '+'
if first_coeff_2 == 1:
    first_coeff_2 = ''
if first_coeff_2 == -1:
    first_coeff_2 = '-'
if second_coeff_2 < 0:
    second_coeff_2 *= -1
    second_sign_1 = ' - '
if third_coeff_2 < 0:
    third_coeff_2 *= -1
    second_sign_2 = '-'
if second_coeff_2 == 1:
    second_coeff_2 = ''

x = 'x'

if second_coeff_2 == 0:
    second_sign_1 = ''
    second_coeff_2 = ''
    x = ''

second_quadratic = f'{first_coeff_2}x²{second_sign_1}{second_coeff_2}{x} {second_sign_2} {third_coeff_2}'


#cubic

a = random.randint(-3, 3)
b = random.randint(-m, m)
c = random.randint(-m, m)
d = random.randint(-m, m)
e = random.randint(-m, m)


while a == 0 or a == 1 or a == -1:
    a = random.randint(-3, 3)
while b == 0:
    b = random.randint(-m, m)
while c in n:
    c = random.randint(-m, m)
while d in n:
    d = random.randint(-m, m)
while e in n:
    e = random.randint(-m, m)


while b / a == 1 or b / a == -1:
    a = random.randint(-3, 3)
    while a == 0 or a == 1 or a == -1:
        a = random.randint(-3, 3)
    while b in n:
        b = random.randint(-m, m)

        

coefficient_1 = a
coefficient_2 = b + a * c + a * d
coefficient_3 = d * (a * c + b) + b * c
coefficient_4 = b * c * d



copy_1 = coefficient_1
copy_2 = coefficient_2 
copy_3 = coefficient_3
copy_4 = coefficient_4 


sign_1 = '+' 
sign_2 = '+' 
sign_3 = '+' 



if copy_2 < 0:
    copy_2 *= -1
    sign_1 = '-'
if copy_3 < 0:
    copy_3 *= -1
    sign_2 = '-'
if copy_4 < 0:
    copy_4 *= -1
    sign_3 = '-'



if copy_1 == -1:
    copy_1 = '-'

if copy_1 == 1:
    copy_1 = ''
if copy_2 == 1:
    copy_2 = ''
if copy_3 == 1:
    copy_3 = ''
if copy_4 == 1:
    copy_4 = ''


origin_1 = a
origin_2 = b
origin_3 = c
origin_4 = d



ori_sign_1 = '+'
ori_sign_2 = '+'
ori_sign_3 = '+'



if origin_2 < 0:
    origin_2 *= -1
    ori_sign_1 = '-'
if origin_3 < 0:
    origin_3 *= -1
    ori_sign_2 = '-'
if origin_4 < 0:
    origin_4 *= -1
    ori_sign_3 = '-'



extra = ''
if a < 0 and b < 0:
    origin_1 *= -1
    extra = '-'
    ori_sign_1 = '+'
    
if a < 0 and b > 0:
    origin_1 *= -1
    extra = '-'
    ori_sign_1 = '-'
    



cubic = f'{copy_1}x³ {sign_1} {copy_2}x² {sign_2} {copy_3}x {sign_3} {copy_4}'


#binomial

a = random.randint(-2, 2)
b = random.randint(-3, 3)

while a == 0:
    a = random.randint(-2, 2)

if a == 1:
    a = ''
if a == -1:
    a = '-'
    
sign_1 = ' + '
if b < 0:
    b *= -1
    sign_1 = ' - '

if b == 0:
    sign_1 = ''
    b = ''

binomial = f'{a}x{sign_1}{b}'

#intiger

num = random.randint(-5, 5)
while num == 0:
    num = random.randint(-5, 5)

if case == 1:
    print()
    print()
    print(f'({first_quadratic}) / ({second_quadratic})')
    print()
    print()
    
if case == 2:
    print()
    print()
    print(f'({cubic}) / ({random.choice([first_quadratic, second_quadratic])})')
    print()
    print()
    
if case == 3:
    print()
    print()
    print(f'({random.choice([first_quadratic, second_quadratic])}) / ({binomial})')
    print()
    print()

if case == 4:
    print()
    print()
    print(f'({random.choice([first_quadratic, second_quadratic])}) / ({cubic})')
    print()
    print()
    
if case == 5:
    print()
    print()
    print(f'({num}) / ({random.choice([first_quadratic, cubic])})')
    print()
    print()
    
    