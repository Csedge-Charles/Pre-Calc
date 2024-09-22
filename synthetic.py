import random


parameters = [0, 1, -1]
obj_range = 2


m = obj_range
n = []
for i in (parameters):
    i *= -1
    n.append(i)


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



print()
print()
# print(f'({a}x + {b})(x + {c})(x + {d})(x + {e})(x + {f})')
# print()
# print(f'({a}x² + {(b + a*c)}x + {b * c})(x + {d})(x + {e})(x + {f})')
# print()
# print(f'({a}x³ + {b + a * c + a * d}x² + {d * (a * c + b) + b * c}x + {b*c*d})(x + {e})(x + {f})')
# print()
# print(f'({a}x⁴ + {b + a * (c + d + e)}x³ + {d * (a * c + b) + b * c + e * (b + a * c + a * d)}x² + {e * d * (a * c + b) + e * b * c + b * c * d}x + {b * c * d * e})(x + {f})')
# print()
print()
print('What are the roots of: ')
print()
input(f'{copy_1}x⁵ {sign_1} {copy_2}x⁴ {sign_2} {copy_3}x³ {sign_3} {copy_4}x² {sign_4} {copy_5}x {sign_5} {copy_6}: ')
print()
print(f'({origin_1}x {ori_sign_1} {origin_2})(x {ori_sign_2} {origin_3})(x {ori_sign_3} {origin_4})(x {ori_sign_4} {origin_5})(x {ori_sign_5} {origin_6})')
print()
print()
