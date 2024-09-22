import random

num1 = random.randint(1, 12)
num2 = random.randint(1, 12)

degree1 = random.choice(['π/6', 'π/3', 'π/4', 'π/2', '-π/6', '-π/4', '-π/3', '-π/2'])

choice_1 = random.choice(
    [f'arctan({num1}/{num2})', 
     f'arcsin({num1}/{num2})', 
     f'arccos({num1}/{num2})', 
     f'arccsc({num1}/{num2})', 
     f'arcsec({num1}/{num2})', 
     f'arccot({num1}/{num2})', 
     ]
)

choice_2 = random.choice(
    [f'sin({degree1})', 
     f'cos({degree1})', 
     f'tan({degree1})', 
     f'sec({degree1})', 
     f'csc({degree1})', 
     f'cot({degree1})', 
     ]
)

choice_final_1 = random.choice(
    [f'sin({choice_1})', 
     f'cos({choice_1})', 
     f'tan({choice_1})', 
     f'csc({choice_1})', 
     f'sec({choice_1})', 
     f'cot({choice_1})', 
     f'arcsin({choice_2})', 
     f'arccos({choice_2})',
     f'arctan({choice_2})',
     f'arcsec({choice_2})',
     f'arccsc({choice_2})',
     f'arccot({choice_2})',
     ]
)
print()
print()
print(f'find {choice_final_1}')
print()
print()