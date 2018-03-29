#!usr/bin/env python

import sys


def minus_b_formula(in_sqr_root):
    equation = []
    sqr_root = (int(in_sqr_root)) ** (0.5)

    equation.append(str((-b + sqr_root) / (2 * a)))

    equation.append(str((-b - sqr_root) / (2 * a)))

    return equation


print('What is Your Variable Name?')
x = input()

print('\nWhat is Your Equation?')
print('(Example equation:  x**2 + x - 6 = 0)\n')
s = sys.stdin.readline().strip()

a = ''
b = ''
c = ''

# RULES:
# print '(Use Two Asctriscs To Indicate To The Power Of)'
# variable name can only be one letter
# solution must not be complex

i = 0
while i < len(s) and s[i] != x:
    i = i + 1

if s[i + 3] == '2':

    if i < len(s):
        try:
            a = float(int(s[:i]))

        except (ValueError,  SyntaxError):
            a = 1

        j = i + 1
        while j < len(s) and s[j] != x:
            j = j + 1

        if j < len(s):
            try:
                b = float(int(s[i + 4:j]))

            except (ValueError,  SyntaxError):
                b = 1

            l = j + 1
            while l < len(s) and s[l] != '=':
                l = l + 1

            if l == len(s):
                try:
                    c = float(int(s[j + 1:l]))

                except (ValueError,  SyntaxError):
                    c = 0

            elif l < len(s):
                c = float(int(s[j + 1:l])) - float(int(s[l + 1:]))

        elif j == len(s):
            b = 0
            try:
                c = float(int(s[i + 4:]))

            except (ValueError,  SyntaxError):
                c = 0

        else:
            print('\n!!!!   Error, This is not a Quadratic   !!!!')

    else:
        print('\n!!!!   Error, Wrong Variable Name Given   !!!!')

else:
    print('\n!!!!   Error, This is not a Quadratic   !!!!')


if (a or a == 0) and (b or b == 0) and (c or c == 0):

    in_sqr_root = (b ** 2) - (4 * a * c)

    if in_sqr_root >= 0:
        [equation_plus, equation_minus] = minus_b_formula(in_sqr_root)

        if equation_minus != equation_plus:
            print('{} = {} AND {} = {}'.format(
                x, equation_plus, x, equation_minus))

        else:
            print('{} = {}'.format(x, equation_plus))

    else:
        print('\n!!!!   Error, This Equation has a Complex Solution   !!!!')
