trig_dict_degree = {
    30 : ['1/2', '√3/2', '√3/3', '2', '2√3/3', '√3'],
    45 : ['√2/2', '√2/2', '1', '√2', '√2', '1'],
    60 : ['√3/2', '1/2', '√3', '2√3/3', '2', '√3/3'],
    90 : ['1', '0', 'undefined', '0', '1', '1'],
    120: ['√3/2', '-1/2', '-√3', '2√3/3', '-2', '-√3/3'],
    135: ['√2/2', '-√2/2', '-1', '√2', '-√2', '-1'],
    150 : ['1/2', '-√3/2', '-√3/3', '2', '-2√3/3', '-√3'],
    180 : ['0', '-1', '0', '-1', '0', 'undefined'],
    210 : ['-1/2', '-√3/2', '√3/3', '-2', '-2√3/3', '√3'],
    225 : ['-√2/2', '-√2/2', '1', '-√2', '-√2', '1'],
    240 : ['-√3/2', '-1/2', '√3', '-2√3/3', '-2', '√3/3'],
    270 : ['-1', '0', 'undefined', '0', '-1', '-1'],
    300 : ['-√3/2', '1/2', '-√3', '-2√3/3', '2', '-√3/3'],
    315 : ['-√2/2', '√2/2', '-1', '-√2', '√2', '-1'],
    330 : ['-1/2', '√3/2', '-√3/3', '-2', '2√3/3', '-√3'],
    360 : ['0', '1', '0', '1', '0', 'undefined'],
}


pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989

e = 2.7182818284590452353602874713526624977572470936999595749669676277240766303535945713821785251664274

radian_list = ['-π/2', '-π/3', '-π/4', '-π/6', '0', 'π/6', 'π/4', 'π/3', 'π/2']
cos_list = ['0', 'π/6', 'π/4', 'π/3', 'π/2', '2π/3', '3/4', '5π/6', 'π']
num_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
trig_dict_radian = {
    'π/6' : ['1/2', '√3/2', '√3/3', '2', '2√3/3', '√3'],
    'π/4' : ['√2/2', '√2/2', '1', '√2', '√2', '1'],
    'π/3' : ['√3/2', '1/2', '√3', '2√3/3', '2', '√3/3'],
    'π/2' : ['1', '0', 'undefined', '0', '1', '1'],
    '2π/3': ['√3/2', '-1/2', '-√3', '2√3/3', '-2', '-√3/3'],
    '3π/4': ['√2/2', '-√2/2', '-1', '√2', '-√2', '-1'],
    '5π/6' : ['1/2', '-√3/2', '-√3/3', '2', '-2√3/3', '-√3'],
    'π' : ['0', '-1', '0', '-1', '0', 'undefined'],
    '7π/6' : ['-1/2', '-√3/2', '√3/3', '-2', '-2√3/3', '√3'],
    '5π/4' : ['-√2/2', '-√2/2', '1', '-√2', '-√2', '1'],
    '4π/3' : ['-√3/2', '-1/2', '√3', '-2√3/3', '-2', '√3/3'],
    '3π/2' : ['-1', '0', 'undefined', '0', '-1', '-1'],
    '5π/3' : ['-√3/2', '1/2', '-√3', '-2√3/3', '2', '-√3/3'],
    '7π/4' : ['-√2/2', '√2/2', '-1', '-√2', '√2', '-1'],
    '11π/6' : ['-1/2', '√3/2', '-√3/3', '-2', '2√3/3', '-√3'],
    '2π' : ['0', '1', '0', '1', '0', 'undefined'],
}








def absval(x):
    if x < 0:
        return x * -1
    return x



def evaluate(x):
    if 'π' in x:
        numerator = ''
        denominator = ''
        sign = 1
        next_up = False
        for i in x:
            if i == 'π':
                next_up = True
            if next_up == False:
                if i == '-':
                    sign = -1
                if i in num_list:   
                    numerator += i
            if next_up:
                if i in num_list:
                    denominator += i
        if numerator == '':
            numerator = '1'
        if denominator == '':
            denominator = '1'
        numerator = int(numerator) * sign
        denominator = int(denominator)
        
        return numerator * pi / denominator
    else:
        numerator = ''
        root = ''
        denominator = ''
        next_up_1 = False
        next_up_2 = False
        negate = 1
        for i in x:
            if next_up_1 == False and next_up_2 == False:
                if i in num_list:
                    numerator += i
                if i == '-':
                    negate *= -1
                if i == '√':
                    next_up_1 = True
                if i == '/':
                    next_up_2 = True
                    next_up_1 = True
            if next_up_1 == True and next_up_2 == False:
                if i == '-':
                    return None
                if i in num_list:
                    root += i
                if i == '/':
                    next_up_2 = True
            if next_up_1 == True and next_up_2 == True:
                if i == '-':
                    negate *= -1
                if i in num_list:
                    denominator += i
        if numerator == '':
            numerator = 1
        if denominator == '':
            denominator = 1
        if root == '':
            root = 1
        
        numerator = float(numerator)
        denominator = float(denominator)
        root = float(root) ** 0.5
        return negate * numerator * root / denominator



def degree_main(degree):
    if degree <= 0:
        while degree < 0:
            degree += 360
    else:
        while degree > 360:
            degree -= 360
    return degree

def factorial(x):
    num = x
    if x == 0:
        return 1
    for i in range(1, x):
        num *= i
    return num




def radian_main(radian):
    numerator = ''
    denominator = ''
    slash = '/'
    sign = 1
    next_up = False
    for i in radian:
        if i == 'π':
            next_up = True
        if next_up == False:
            if i == '-':
                sign = -1
            if i in num_list:   
                numerator += i
        if next_up:
            if i in num_list:
                denominator += i
    if numerator == '':
        numerator = '1'
    if denominator == '':
        denominator = '1'
    combined = sign * int(numerator) / int(denominator)
    if combined > 0:
        while combined > 2:
            combined -= 2
    if combined <= 0:
        while combined <= 0:
            combined += 2
    if absval(int(combined)) == combined:
        denominator = 1
        numerator = combined
        numerator = round(numerator)
    else:
        if absval(int(combined) + 0.5) == combined:
            denominator = 2
            numerator = combined * denominator
            numerator = round(numerator)
        else:
            if absval(int(combined) + 0.33333 - combined) <= 0.001:
                denominator = 3
                numerator = combined * 3
                numerator = round(numerator)
            else:
                if absval(int(combined) + 0.66666 - combined) <= 0.001:
                    denominator = 3
                    numerator = combined * 3
                    numerator = round(numerator)
                else:
                    
                    if absval(int(combined) + 0.166666 - combined )<= 0.001:
                        denominator = 6
                        numerator = combined * 6
                        numerator = round(numerator)
                    else:
                        if absval(int(combined) + 0.833333 - combined) <= 0.001:
                            denominator = 6
                            numerator = combined * 6
                            numerator = round(numerator)

                        else:
                            if absval(int(combined) + 0.75 - combined) == 0:
                                denominator = 4
                                numerator = combined * 4
                                numerator = round(numerator)

                            else:
                                if absval(int(combined) + 0.25 - combined) <= 0.001:
                                    denominator = 4
                                    numerator = combined * 4
                                    numerator = round(numerator)

            
    
    if numerator == 1 or numerator == '1':
        numerator = ''
    else:
        numerator = int(numerator)
    
    if denominator == 1 or numerator == '1':
        denominator = ''
        slash = ''
    else:
        denominator = int(denominator)
        
    return f'{numerator}π{slash}{denominator}'


def convert(x):
    if 'π' in str(x):
        numerator = ''
        denominator = ''
        sign = 1
        next_up = False
        for i in x:
            if i == 'π':
                next_up = True
            if next_up == False:
                if i == '-':
                    sign = -1
                if i in num_list:   
                    numerator += i
            if next_up:
                if i in num_list:
                    denominator += i
        if numerator == '':
            numerator = '1'
        if denominator == '':
            denominator = '1'
        numerator = int(numerator) * sign
        denominator = int(denominator)
        
        return int(numerator * 180 / denominator)
    else:
        slash = '/'
        combined = x / 180
        if absval(int(combined)) == combined:
            denominator = 1
            numerator = combined
            numerator = round(numerator)
        else:
            if absval(int(combined) + 0.5) == combined:
                denominator = 2
                numerator = combined * denominator
                numerator = round(numerator)
            else:
                if absval(int(combined) + 0.33333 - combined) <= 0.001:
                    denominator = 3
                    numerator = combined * 3
                    numerator = round(numerator)
                else:
                    if absval(int(combined) + 0.66666 - combined) <= 0.001:
                        denominator = 3
                        numerator = combined * 3
                        numerator = round(numerator)
                    else:
                        
                        if absval(int(combined) + 0.166666 - combined )<= 0.001:
                            denominator = 6
                            numerator = combined * 6
                            numerator = round(numerator)
                        else:
                            if absval(int(combined) + 0.833333 - combined) <= 0.001:
                                denominator = 6
                                numerator = combined * 6
                                numerator = round(numerator)
        if numerator == 1:
            numerator = ''
        else:
            numerator = int(numerator)
        
        if denominator == 1:
            denominator = ''
            slash = ''
        else:
            denominator = int(denominator)
            
        return f'{numerator}π{slash}{denominator}'
    
        
            



def sin(theta):
    if 'π' in str(theta):
        theta = radian_main(theta)
        if theta in trig_dict_radian.keys():
            return trig_dict_radian[theta][0]
        else:
            return None
    else:
        if theta in trig_dict_degree.keys():     
            return trig_dict_degree[degree_main(theta)][0]
        else:
            return None

def cos(theta):
    if 'π' in str(theta):
        theta = radian_main(theta)
        if theta in trig_dict_radian.keys():
            return trig_dict_radian[radian_main(theta)][1]
        else:
            return None
    else:
        if theta in trig_dict_degree.keys():     
            return trig_dict_degree[degree_main(theta)][1]
        else:
            return None

def tan(theta):
    if 'π' in str(theta):
        theta = radian_main(theta)
        if theta in trig_dict_radian.keys():
            return trig_dict_radian[radian_main(theta)][2]
        else:
            return None
    else:
        if theta in trig_dict_degree.keys():     
            return trig_dict_degree[degree_main(theta)][2]
        else:
            return None

def csc(theta):
    if 'π' in str(theta):
        theta = radian_main(theta)
        if theta in trig_dict_radian.keys():
            return trig_dict_radian[radian_main(theta)][3]
        else:
            return None
    else:
        if theta in trig_dict_degree.keys():     
            return trig_dict_degree[degree_main(theta)][3]
        else:
            return None
        

def sec(theta):
    if 'π' in str(theta):
        theta = radian_main(theta)
        if theta in trig_dict_radian.keys():
            return trig_dict_radian[radian_main(theta)][4]
        else:
            return None
    else:
        if theta in trig_dict_degree.keys():     
            return trig_dict_degree[degree_main(theta)][4]
        else:
            return None

def cot(theta):
    if 'π' in str(theta):
        theta = radian_main(theta)
        if theta in trig_dict_radian.keys():
            return trig_dict_radian[radian_main(theta)][5]
        else:
            return None
    else:
        if theta in trig_dict_degree.keys():     
            return trig_dict_degree[degree_main(theta)][5]
        else:
            return None

def arcsin(ratio):
    for i in radian_list:
        if sin(i) == ratio:
            return i
    return None

def arccos(ratio):
    for i in cos_list:
        if cos(i) == ratio:
            return i
    return None

def arctan(ratio):
    for i in radian_list:
        if tan(i) == ratio:
            return i
    return None

def arccsc(ratio):
    for i in radian_list:
        if csc(i) == ratio:
            return i
    return None

def arcsec(ratio):
    for i in cos_list:
        if sec(i) == ratio:
            return i
    return None

def arctan(ratio):
    for i in radian_list:
        if tan(i) == ratio:
            return i
    return None

def l(x, base):
    digit_1 = 0
    digit_2 = 0
    digit_3 = 0
    digit_4 = 0
    digit_5 = 0
    digit_6 = 0
    digit_7 = 0
    digit_8 = 0
    digit_9 = 0
    digit_10 = 0
    
    if x <= 0:
        return None
    
    while base ** digit_1 < x:
        digit_1 += 1
    digit_1 -= 1
    while base ** (digit_1 + digit_2 / 10) < x:
        digit_2 += 1
    digit_2 -= 1
    while base ** (digit_1 + digit_2 / 10 + digit_3 / 100) < x:
        digit_3 += 1
    digit_3 -= 1
    while base ** (digit_1 + digit_2 / 10 + digit_3 / 100 + digit_4 / 1000) < x:
        digit_4 += 1
    digit_4 -= 1
    while base ** (digit_1 + digit_2 / 10 + digit_3 / 100 + digit_4 / 1000 + digit_5 / 10000) < x:
        digit_5 += 1
    digit_5 -= 1
    while base ** (digit_1 + digit_2 / 10 + digit_3 / 100 + digit_4 / 1000 + digit_5 / 10000 + digit_6 / 100000) < x:
        digit_6 += 1
    digit_6 -= 1
    while base ** (digit_1 + digit_2 / 10 + digit_3 / 100 + digit_4 / 1000 + digit_5 / 10000 + digit_6 / 100000 + digit_7 / 1000000) < x:
        digit_7 += 1
    digit_7 -= 1
    while base ** (digit_1 + digit_2 / 10 + digit_3 / 100 + digit_4 / 1000 + digit_5 / 10000 + digit_6 / 100000 + digit_7 / 1000000 + digit_8 / 10000000) < x:
        digit_8 += 1
    digit_8 -= 1
    while base ** (digit_1 + digit_2 / 10 + digit_3 / 100 + digit_4 / 1000 + digit_5 / 10000 + digit_6 / 100000 + digit_7 / 1000000 + digit_8 / 10000000 + digit_9 / 100000000) < x:
        digit_9 += 1
    digit_9 -= 1
    while base ** (digit_1 + digit_2 / 10 + digit_3 / 100 + digit_4 / 1000 + digit_5 / 10000 + digit_6 / 100000 + digit_7 / 1000000 + digit_8 / 10000000 + digit_9 / 100000000 + digit_10 / 1000000000) < x:
        digit_10 += 1
    digit_10 -= 1
    
    exponent = digit_1 + digit_2 / 10 + digit_3 / 100 + digit_4 / 1000 + digit_5 / 10000 + digit_6 / 100000 + digit_7 / 1000000 + digit_8 / 10000000 + digit_9 / 100000000 + digit_10 / 1000000000
    
    if absval(round(exponent) - exponent) <= 0.0001:
        return round(exponent)
    return exponent

def log(x, base=None):
    if base is not None:
        return l(x, base)
    else:
        return l(x, 10)

def ln(x):
    return log(x, e)

