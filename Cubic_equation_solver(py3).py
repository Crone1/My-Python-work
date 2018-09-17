
#!usr/bin/env python3

import sys


def set_up():

    print('What is your variable name?  (only one letter)')
    org_x = input()

    if len(org_x) != 1:
        print('\n!!!!   This variable is not of length one   !!!!')
        sys.exit(0)

    x = org_x.lower()

    print('\nWhat is your equation?')
    print(
        '(Example equation:  x**3 + x**2 + x - 6 = 4)   [Automatically put equal to zero]\n')
    s = sys.stdin.readline().strip().lower()
    return (org_x, x, s)


def find_a(org_x, s, i, m):

    if s[:i] == '':
        return 1

    else:
        try:
            return float(s[:i])

        except (ValueError,  SyntaxError):
            if m == 4:
                print(
                    '\n!!!!   Error at the values before the "{}**3"   !!!!'.format(org_x))

            elif m == 3:
                print(
                    '\n!!!!   Error at the values before the "{}^3"   !!!!'.format(org_x))

        sys.exit(0)


def find_b(org_x, s, i, j, m, n):

    chars = ''.join([c for c in s[i + m:j] if c != ' '])

    if chars == '+':
        return 1

    elif chars == '-':
        return -1

    if chars[0] == '+' or chars[0] == '-':
        try:
            return float(chars)

        except (ValueError,  SyntaxError):

            if n == 4:
                print(
                    '\n!!!!   Error at the values before the "{}**2"   !!!!'.format(org_x))

            elif n == 3:
                print(
                    '\n!!!!   Error at the values before the "{}^2"   !!!!'.format(org_x))

            sys.exit(0)


def find_c(org_x, s, j, l, n):

    chars = ''.join([c for c in s[j + n:l] if c != ' '])

    if chars == '+':
        return 1

    elif chars == '-':
        return -1

    if chars[0] == '+' or chars[0] == '-':
        try:
            return float(chars)

        except (ValueError,  SyntaxError):
            print('\n!!!!   Error at the values before the "{}"   !!!!'.format(org_x))

            sys.exit(0)


def find_d_no_eq(org_x, s, k, l):

    chars = ''.join([c for c in s[l + 1:k] if c != ' '])

    if s[l + 1:k] == '' or len(chars) == 0:
        return 0

    if chars[0] == '+' or chars[0] == '-':
        try:
            return float(chars)

        except (ValueError,  SyntaxError):
            print(
                '\n!!!!   Error at the values just after the "{}", just before the end   !!!!'.format(org_x))

            sys.exit(0)


def find_d_with_eq(org_x, s, k, l):    # deals with equals

    d_left = find_d_no_eq(org_x, s, k, l)

    if s[k + 1] == '=':
        p = 2

    else:
        p = 1

    chars = ''.join([c for c in s[k + p:] if c != ' '])

    try:
        return float(d_left) - float(chars)

    except (ValueError,  SyntaxError):
        if p == 2:
            print('\n!!!!   Error at the values after the "==", just at the end   !!!!')

        elif p == 1:
            print('\n!!!!   Error at the values after the "=", just at the end   !!!!')

        sys.exit(0)


def get_a_b_c_d(org_x, x, s):

    #------------------------A--------------------------------
    i = 0
    while i < len(s) and s[i] != x:  # find first x
        i = i + 1

    if i < len(s):

        if s[i:i + 4] == '{}**3'.format(x):
            m = 4

        elif s[i:i + 3] == '{}^3'.format(x):
            m = 3

        else:
            print('\n!!!!   Error, This is not a cubic equation  !!!!')
            sys.exit(0)

        #   'i' is the position of the first x
        #   'i + m' is the position after the 3

        a = find_a(org_x, s, i, m)  # get value for a

        #----------------------B-------------------------------
        j = i + 1
        while j < len(s) and s[j] != x:  # find second x
            j = j + 1

        if j < len(s):

            if s[j:j + 4] == '{}**2'.format(x):
                n = 4

            elif s[j:j + 3] == '{}^2'.format(x):
                n = 3

            else:
                b = 0
                l = i + m

            #   'j' is the position of the second x
            #   'j + n' is the position after the 2

            b = find_b(org_x, s, i, j, m, n)  # get value for b

            #--------------------C-------------------------------
            l = j + 1
            while l < len(s) and s[l] != x:  # find third x
                l = l + 1

            if l < len(s):

                #   'l' is the position of the third x

                c = find_c(org_x, s, j, l, n)  # get value for c

                k = l + 1

            else:
                c = 0
                k = j + n

            #--------------------D---------------------------------

        while k < len(s) and s[k] != '=':  # find equals sign
            k = k + 1

        if k == len(s):
            d = find_d_no_eq(org_x, s, k, l)  # get value for c

        elif k < len(s):
            d = find_d_with_eq(org_x, s, k, l)

    else:
        print('\n!!!!   Error, Wrong variable name given   !!!!')
        sys.exit(0)

    return (a, b, c, d)


def get_roots(a, b, c, d):

    zero = (b**2) - (3 * a * c)

    one = (2 * (b**3)) - (9 * a * b * c) + (27 * d * (a**2))

    small_sqr = ((one**2) - (4 * (zero**3)))**(1 / 2)

    big_sqr_plus = ((one + small_sqr) / 2)**(1 / 3)

    big_sqr_minus = ((one - small_sqr) / 2)**(1 / 3)

    if zero != 0 and one != 0:

        root_1 = '{:.4f}'.format(-(1 / (3 * a)) *
                                 (b + big_sqr_plus + (zero / big_sqr_plus)))

        root_2 = '{:.4f}'.format(-(1 / (3 * a)) * (b + (-1 / 2 + (
            1 / 2 * complex((3)**(1 / 2)))) * big_sqr_plus + (zero / big_sqr_plus)))

        root_3 = '{:.4f}'.format(-(1 / (3 * a)) * (b + (-1 / 2 - (
            1 / 2 * complex((3)**(1 / 2)))) * big_sqr_plus + (zero / big_sqr_plus)))

    elif zero = one = 0:
        root_1 = -b / (3 * a)

    elif one = 0 and zero != 0:
        root_1 = ((9 * a * d) - (b * c)) / (2 * zero)

        root_2 = ((4 * a * b * c) - (9 * d * (a**2)) - b**3) / (a * zero)

    return (root_1, root_2, root_3)


def print_solution(org_x, root_1, root_2, root_3):

    roots = set([root_1, root_2, root_3])

    for r in roots:
        j = r.rstrip('0').rstrip('.')
        if j == '':
            root_list.append('0')

        root_list.append(j)

    if len(root_list) == 3:
        print('{} = {} AND {} = {} AND {} = {}'.format(
            org_x, root_list[0], org_x, root_list[1], org_x, root_list[2]))

    elif len(root_list) == 1:
        print('{} = {}'.format(org_x, root_list[0]))

    elif len(root_list) == 2:
        print('{} = {} AND {} = {}'.format(
            org_x, root_list[0], org_x, root_list[1]))


def main():

    org_x, x, s = set_up()
    a, b, c, d = get_a_b_c_d(org_x, x, s)

    #print('A = {}, B = {}, C = {}, D = {}'.format(a, b, c, d))

    (r1, r2, r3) = get_roots(a, b, c, d)

    print_solution(org_x, r1, r2, r3)

if __name__ == '__main__':
    main()
