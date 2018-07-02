#!usr/bin/env python3

import sys


def set_up():
    print('What is your variable name?  (only one letter)')
    org_x = input()
    x = org_x.lower()

    print('\nWhat is your equation?')
    print('(Example equation:  x**2 + x - 6 = 0)\n')
    s = sys.stdin.readline().strip().lower()
    return (x, s)


def find_a(s, i, m):
    if s[:i] == '':
        return 1

    else:
        try:
            return float(s[:i])

        except (ValueError,  SyntaxError):
            if m == 4:
                print(
                    '\n!!!!   Error at the values before the "{}**2"   !!!!'.format(org_x))

            elif m == 3:
                print(
                    '\n!!!!   Error at the values before the "{}^2"   !!!!'.format(org_x))

        sys.exit(0)


def find_b(s, i, j, m):

    chars = ''.join([c for c in s[i + m:j] if c != ' '])

    if chars == '+':
        return 1

    elif chars == '-':
        return -1

    if chars[0] == '+' or chars[0] == '-':
        try:
            return float(chars[1:])

        except (ValueError,  SyntaxError):
            print('\n!!!!   Error at the values before the "{}"   !!!!'.format(org_x))

            sys.exit(0)


def find_c_no_eq(s, l, j):

    chars = ''.join([c for c in s[j + 1:l] if c != ' '])

    if s[j + 1:l] == '' or len(chars) == 0:
        return 0

    if chars[0] == '+' and chars[0] == '-':
        try:
            return float(chars[1:])

        except (ValueError,  SyntaxError):
            print(
                '\n!!!!   Error at the values just after the "{}", just before the end   !!!!'.format(org_x))

            sys.exit(0)


def find_c_with_eq(s, l, j):    # deals with equals

    c_left = find_c_no_eq(s, l, j)

    if s[l + 1] == '=':
        n = 2

    else:
        n = 1

    chars = ''.join([c for c in s[l + n:] if c != ' '])

    try:
        return c_left - float(chars)

    except (ValueError,  SyntaxError):
        if n == 2:
            print('\n!!!!   Error at the values after the "==", just at the end   !!!!')

        elif n == 1:
            print('\n!!!!   Error at the values after the "=", just at the end   !!!!')

        sys.exit(0)


def get_a_b_c(x, s):
    i = 0
    while i < len(s) and s[i] != x:  # find first x
        i = i + 1

    if i < len(s):

        if s[i:i + 4] == '{}**2'.format(x):
            m = 4

        elif s[i:i + 3] == '{}^2'.format(x):
            m = 3

        else:
            print('\n!!!!   Error, This is not a quadratic equation  !!!!')
            sys.exit(0)

        a = find_a(s, i, m)  # get value for a

        j = i + 1
        while j < len(s) and s[j] != x:  # find second x
            j = j + 1

        if j < len(s):

            b = find_b(s, i, j, m)  # get value for b

            l = j + 1

        else:
            b = 0
            l = i + m

        while l < len(s) and s[l] != '=':  # find equals sign
            l = l + 1

        if l == len(s):
            c = find_c_no_eq(s, l, j)  # get value for c

        elif l < len(s):
            c = find_c_with_eq(s, l, j)

    else:
        print('\n!!!!   Error, Wrong variable name given   !!!!')
        sys.exit(0)

    return (a, b, c)


def get_and_print_solution_quadratic(x, a, b, c):
    in_sqr_root = (b ** 2) - (4 * a * c)    #minus b formula
    sqr_root = (int(in_sqr_root)) ** (0.5)

    equation_plus = str((-b + sqr_root) / (2 * a))
    equation_minus = str((-b - sqr_root) / (2 * a))

    if equation_minus != equation_plus:
        print('{} = {} AND {} = {}'.format(
            org_x, equation_plus, org_x, equation_minus))

    else:
        print('{} = {}'.format(org_x, equation_plus))


def main():
    # RULES:
    # variable name can only be one letter

    x, s = set_up()
    a, b, c = get_a_b_c(x, s)
    get_and_print_solution_quadratic(x, a, b, c)

if __name__ == '__main__':
    main()
