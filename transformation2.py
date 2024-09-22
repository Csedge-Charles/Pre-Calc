import random

#vertical changes:

vertical_stretch = random.randint(1, 5)
Operator = random.choice([f"1/{vertical_stretch}", vertical_stretch])

Vertical_movement = random.randint(1, 5)
Operator_2 = random.choice(['-', '+'])

Reflection = random.choice(['-', ''])

#horizontal changes: 

horizontal_stretch = random.randint(1, 5)
Operator_3 = random.choice([f'1/{horizontal_stretch}', horizontal_stretch])

horizontal_movement = random.randint(1, 5)
Operator_4 = random.choice(['-', '+'])

Reflection_2 = random.choice(['-', ''])

#functions

Sin = f'{Reflection}{vertical_stretch}sin({Reflection_2}{horizontal_stretch}x {Operator_2} {horizontal_movement}) {Operator_4} {Vertical_movement}'

Tan = f'{Reflection}{vertical_stretch}tan({Reflection_2}{horizontal_stretch}x {Operator_2} {horizontal_movement}) {Operator_4} {Vertical_movement}'

Cos = f'{Reflection}{vertical_stretch}cos({Reflection_2}{horizontal_stretch}x {Operator_2} {horizontal_movement}) {Operator_4} {Vertical_movement}'

Ln = f'{Reflection}{vertical_stretch}ln({Reflection_2}{horizontal_stretch}x {Operator_2} {horizontal_movement}) {Operator_4} {Vertical_movement}'

Squared = f'{Reflection}{vertical_stretch}({Reflection_2}{horizontal_stretch}x {Operator_2} {horizontal_movement})² {Operator_4} {Vertical_movement}'

Function = random.choice([Sin, Tan, Cos, Ln, Squared])

print()
print()
print('Describe the transformation:')
print()
print(Function)
print()
print()








