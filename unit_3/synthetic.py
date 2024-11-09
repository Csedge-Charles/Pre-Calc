import random

odd_1 = 40
odd_2 = 20
odd_3 = 3

# odd_1 : odd_2 : odd_3 = 5th degree : quartic : cubic

total = odd_1 + odd_2 + odd_3

my_num = random.randint(1, total)

if my_num <= odd_1:
    decider = 1
if my_num > odd_1 and my_num <= odd_1 + odd_2:
    decider = 2
if my_num > odd_1 + odd_2 and my_num <= total:
    decider = 3



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

if decider == 1:
    a = random.randint(-3, 3)
    b = random.randint(-m, m)
    c = random.randint(-m, m)
    d = random.randint(-m, m)
    e = random.randint(-m, m)
    f = random.randint(-m, m)

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
    while f in n:
        f = random.randint(-m, m)

    while b / a == 1 or b / a == -1:
        a = random.randint(-3, 3)
        while a == 0 or a == 1 or a == -1:
            a = random.randint(-3, 3)
        while b in n:
            b = random.randint(-m, m)

            

    coefficient_1 = a
    coefficient_2 = b + a * (c + d + e + f)
    coefficient_3 = d * (a * c + b) + b * c + e * (b + a * c + a * d) + (f * (b + a * (c + d + e)))
    coefficient_4 = (e * d * (a * c + b) + e * b * c + b * c * d) + (f * (d * (a * c + b) + b * c + e * (b + a * c + a * d)))
    coefficient_5 =  (b * c * d * e) + (f * (e * d * (a * c + b) + e * b * c + b * c * d))
    constant = b * c * d * e * f


    copy_1 = coefficient_1
    copy_2 = coefficient_2 
    copy_3 = coefficient_3
    copy_4 = coefficient_4 
    copy_5 = coefficient_5
    copy_6 = constant

    sign_1 = '+' 
    sign_2 = '+' 
    sign_3 = '+' 
    sign_4 = '+' 
    sign_5 = '+' 

    if copy_2 < 0:
        copy_2 *= -1
        sign_1 = '-'
    if copy_3 < 0:
        copy_3 *= -1
        sign_2 = '-'
    if copy_4 < 0:
        copy_4 *= -1
        sign_3 = '-'
    if copy_5 < 0:
        copy_5 *= -1
        sign_4 = '-'
    if copy_6 < 0:
        copy_6 *= -1
        sign_5 = '-'

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
    if copy_5 == 1:
        copy_5 = ''
    if copy_6 == 1:
        copy_6 = ''

    origin_1 = a
    origin_2 = b
    origin_3 = c
    origin_4 = d
    origin_5 = e
    origin_6 = f

    ori_sign_1 = '+'
    ori_sign_2 = '+'
    ori_sign_3 = '+'
    ori_sign_4 = '+'
    ori_sign_5 = '+'

    if origin_2 < 0:
        origin_2 *= -1
        ori_sign_1 = '-'
    if origin_3 < 0:
        origin_3 *= -1
        ori_sign_2 = '-'
    if origin_4 < 0:
        origin_4 *= -1
        ori_sign_3 = '-'
    if origin_5 < 0:
        origin_5 *= -1
        ori_sign_4 = '-'
    if origin_6 < 0:
        origin_6 *= -1
        ori_sign_5 = '-'

    extra = ''
    if a < 0 and b < 0:
        origin_1 *= -1
        extra = '-'
        ori_sign_1 = '+'
        
    if a < 0 and b > 0:
        origin_1 *= -1
        extra = '-'
        ori_sign_1 = '-'
        


    print()
    print()
    print('What are the roots of: ')
    print()
    input(f'{copy_1}x⁵ {sign_1} {copy_2}x⁴ {sign_2} {copy_3}x³ {sign_3} {copy_4}x² {sign_4} {copy_5}x {sign_5} {copy_6}: ')
    print()
    print(f'{extra}({origin_1}x {ori_sign_1} {origin_2})(x {ori_sign_2} {origin_3})(x {ori_sign_3} {origin_4})(x {ori_sign_4} {origin_5})(x {ori_sign_5} {origin_6})')
    print()
    print()

if decider == 2:
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
    coefficient_2 = b + a * (c + d + e)
    coefficient_3 = d * (a * c + b) + b * c + e * (b + a * c + a * d)
    coefficient_4 = e * d * (a * c + b) + e * b * c + b * c * d
    coefficient_5 =  b * c * d * e


    copy_1 = coefficient_1
    copy_2 = coefficient_2 
    copy_3 = coefficient_3
    copy_4 = coefficient_4 
    copy_5 = coefficient_5

    sign_1 = '+' 
    sign_2 = '+' 
    sign_3 = '+' 
    sign_4 = '+' 


    if copy_2 < 0:
        copy_2 *= -1
        sign_1 = '-'
    if copy_3 < 0:
        copy_3 *= -1
        sign_2 = '-'
    if copy_4 < 0:
        copy_4 *= -1
        sign_3 = '-'
    if copy_5 < 0:
        copy_5 *= -1
        sign_4 = '-'


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
    if copy_5 == 1:
        copy_5 = ''


    origin_1 = a
    origin_2 = b
    origin_3 = c
    origin_4 = d
    origin_5 = e


    ori_sign_1 = '+'
    ori_sign_2 = '+'
    ori_sign_3 = '+'
    ori_sign_4 = '+'


    if origin_2 < 0:
        origin_2 *= -1
        ori_sign_1 = '-'
    if origin_3 < 0:
        origin_3 *= -1
        ori_sign_2 = '-'
    if origin_4 < 0:
        origin_4 *= -1
        ori_sign_3 = '-'
    if origin_5 < 0:
        origin_5 *= -1
        ori_sign_4 = '-'


    extra = ''
    if a < 0 and b < 0:
        origin_1 *= -1
        extra = '-'
        ori_sign_1 = '+'
        
    if a < 0 and b > 0:
        origin_1 *= -1
        extra = '-'
        ori_sign_1 = '-'
        


    print()
    print()
    print('What are the roots of: ')
    print()
    input(f'{copy_1}x⁴ {sign_1} {copy_2}x³ {sign_2} {copy_3}x² {sign_3} {copy_4}x {sign_4} {copy_5}: ')
    print()
    print(f'{extra}({origin_1}x {ori_sign_1} {origin_2})(x {ori_sign_2} {origin_3})(x {ori_sign_3} {origin_4})(x {ori_sign_4} {origin_5})')
    print()
    print()

if decider == 3:
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
        


    print()
    print()
    print('What are the roots of: ')
    print()
    input(f'{copy_1}x³ {sign_1} {copy_2}x² {sign_2} {copy_3}x {sign_3} {copy_4}: ')
    print()
    print(f'{extra}({origin_1}x {ori_sign_1} {origin_2})(x {ori_sign_2} {origin_3})(x {ori_sign_3} {origin_4})')
    print()
    print()
# print(f'({a}x + {b})(x + {c})(x + {d})(x + {e})(x + {f})')
# print()
# print(f'({a}x² + {(b + a*c)}x + {b * c})(x + {d})(x + {e})(x + {f})')
# print()
# print()
# print()

