import random

blank_list = []
num_list = [1, 2, 3, 4]

while num_list != []:
    add = random.choice(num_list)
    blank_list.append(add)
    num_list.remove(add)

transformation_1 = ''
transformation_2 = ''
transformation_3 = ''
transformation_4 = ''

def if_else(saying, num):
    global blank_list, transformation_1, transformation_2, transformation_3, transformation_4
    
    if blank_list[0] == num:
        transformation_1 = saying
    if blank_list[1] == num:
        transformation_2 = f'followed by a {saying}'
    if blank_list[2] == num:
        transformation_3 = f'followed by a {saying}'
    if blank_list[3] == num:
        transformation_4 = f'followed by a {saying}'
    
#horizontal translation

translate = random.randint(2, 15)
way = random.choice(['left', 'right'])
saying_1 = f'Translation {way} {translate} units'
if_else(saying_1, 1)



#vertical translation

translate = random.randint(2, 15)
way = random.choice(['up', 'down'])
saying_2 = f'Translation {way} {translate} units'
if_else(saying_2, 2)

#vertical shift

factor = random.randint(2, 5)
pick = random.randint(1, 2)
if pick == 1:
    factor = f'1/{factor}'
    way = 'shrink'
else:
    way = 'stretch'
    
saying_3 = f'Vertical {way} factor of {factor}'
if_else(saying_3, 3)

#horizontal shift

factor = random.randint(2, 5)
pick = random.randint(1, 2)
if pick == 1:
    factor = f'1/{factor}'
    way = 'shrink'
else:
    way = 'stretch'
    
saying_4 = f'Horizontal {way} factor of {factor}'
if_else(saying_4, 4)
func_list = ['sin(x)', 'cos(x)', 'tan(x)', 'ln(x)', 'x²', '√x']
print('')
print('')
print(f'Given f(x) = {random.choice(func_list)}, what is g(x) if f(x) had a')
print('')
print('')
print(transformation_1)
print('')
print(transformation_2)
print('')
print(transformation_3)
print('')
print(transformation_4)
print('')
print('')