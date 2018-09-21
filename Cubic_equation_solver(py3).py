
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
        '(Example equation:  x^3 + x^2 + x - 6 = 4)   [Automatically put equal to zero]\n')
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


def find_b(org_x, s, j, j_start, n):

    chars = ''.join([c for c in s[j_start:j] if c != ' '])

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

    else:
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

    else:
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
                '\n!!!!   Error at the values after the "{}", just before the end   !!!!'.format(org_x))

            sys.exit(0)

    else:
        print(
            '\n!!!!   Error at the values after the "{}", just before the end   !!!!'.format(org_x))

        sys.exit(0)


def find_d_with_eq(org_x, s, k, l):    # deals with equals

    d_left = find_d_no_eq(org_x, s, k, l)

    if k == len(s) or (k + 1 == len(s) and s[k + 1] == '='):

        if s[k + 1] == '=':
            p = 2

        else:
            p = 1

        chars = ''.join([c for c in s[k + p:] if c != ' '])

        if len(chars) == 0:
            return d_left

        else:

            try:
                return d_left - float(chars)

            except (ValueError,  SyntaxError):
                if p == 2:
                    print(
                        '\n!!!!   Error at the values after the "==", just at the end   !!!!')

                elif p == 1:
                    print(
                        '\n!!!!   Error at the values after the "=", just at the end   !!!!')

                sys.exit(0)

    else:
        return d_left


def get_a_b_c_d(org_x, x, s):

    #------------------------A--------------------------------
    i = 0
    # find first x
    while i < len(s) and s[i:i + 4] != '{}**3'.format(x) and s[i:i + 3] != '{}^3'.format(x):
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

        a = find_a(org_x, s, i, m)

        #----------------------B-------------------------------
        j = j_start = i + m
        while j < len(s) and s[j:j + 4] != '{}**2'.format(x) and s[j:j + 3] != '{}^2'.format(x):
            j = j + 1

        if j < len(s):

            if s[j:j + 4] == '{}**2'.format(x):
                n = 4

            elif s[j:j + 3] == '{}^2'.format(x):
                n = 3

            else:
                b = 0
                j = j_start
                n = 0

            if n:
                b = find_b(org_x, s, j, j_start, n)

            #   'j' is the position of the second x
            #   'j + n' is the position after the **2/^2

            #--------------------C-------------------------------
            l = l_start = j + n
            while l < len(s) and s[l] != x:  # find third x
                l = l + 1

            if l < len(s):
                #   'l' is the position of the third x

                c = find_c(org_x, s, j, l, n)  # get value for c

            else:
                c = 0
                l = l_start - 1

        else:
            b = 0
            c = 0
            l = j_start - 1

            #--------------------D---------------------------------
        k = l + 1
        while k < len(s) and s[k] != '=':  # find equals sign
            k = k + 1

        if k == len(s):
            d = find_d_no_eq(org_x, s, k, l)  # get value for d

        elif k < len(s):
            d = find_d_with_eq(org_x, s, k, l)  # get value for d

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

    polynomial_discriminant = (18 * a * b * c * d) - (4 * d * (b**3)) + \
        ((b**2) * (c**2)) - (4 * a * (c**3)) - (27 * (a**2) * (d**2))

    pos_cube_root_of_unity = complex((-1 / 2) + (1 / 2j * (3)**(1 / 2)))

    neg_cube_root_of_unity = complex((-1 / 2) - (1 / 2j * (3)**(1 / 2)))

    if polynomial_discriminant == 0:

        if zero == 0:
            # One triple root                      ---- x**3 - 3x**2 + 3x - 1
            root_1 = root_2 = root_3 = -b / (3 * a)

        else:
            # One double root and a single root     ---- x**3 + x**2 - 33x + 63
            root_1 = root_2 = ((9 * a * d) - (b * c)) / (2 * zero)

            root_3 = ((4 * a * b * c) - (9 * d * (a**2)) - b**3) / (a * zero)

    else:
        # 1 real root + 2 complex conjugates        ---- x**3 + x**2 + x + 1
        # OR 3 disict real routes                   ---- x**3 - 6x**2 + 11x - 6
        if one + small_sqr == 0:
            root_1 = -(1 / (3 * a)) * (
                b + big_sqr_minus + (zero / big_sqr_minus))

            root_2 = -(1 / (3 * a)) * (
                b + (pos_cube_root_of_unity * big_sqr_minus) + (zero / big_sqr_minus))

            root_3 = -(1 / (3 * a)) * (
                b + (neg_cube_root_of_unity * big_sqr_minus) + (zero / big_sqr_minus))

        else:

            root_1 = -(1 / (3 * a)) * (
                b + big_sqr_plus + (zero / big_sqr_plus))

            root_2 = -(1 / (3 * a)) * (
                b + (pos_cube_root_of_unity * big_sqr_plus) + (zero / (pos_cube_root_of_unity * big_sqr_plus)))

            root_3 = -(1 / (3 * a)) * (
                b + (neg_cube_root_of_unity * big_sqr_plus) + (zero / (neg_cube_root_of_unity * big_sqr_plus)))

    return [root_1, root_2, root_3]


def strip_string(s):

    t = s.rstrip('0').rstrip('.')
    if t == '':
        return '0'

    else:
        return t


def tidy_roots(l):

    strings = []

    for r in l:
        comp = []

        if not isinstance(r, complex):

            a = str(r)

            j = 0
            while j < len(a) and a[j] != '.':
                j = j + 1

            if j + 4 < len(a):
                strings.append(strip_string('{:.4f}'.format(r)))

            else:
                strings.append(strip_string(a))

        else:
            if r.real != 0:
                a = str(r.real)

                j = 0
                while j < len(a) and a[j] != '.':
                    j = j + 1

                if j + 4 < len(a):
                    if strip_string('{:.4f}'.format(r.real)) != '0' and strip_string('{:.4f}'.format(r.real)) != '-0':
                        comp.append(strip_string('{:.4f}'.format(r.real)))

                else:
                    comp.append(strip_string(a))

            if r.imag != 0:

                b = str(abs(r.imag))

                i = 0
                while i < len(b) and b[i] != '.':
                    i = i + 1

                if i + 4 < len(b):
                    if strip_string('{:.4f}'.format(r.imag)) != '0' and strip_string('{:.4f}'.format(r.imag)) != '-0':
                        if r.imag > 0:
                            comp.append(strip_string(
                                '+ {:.4f}'.format(abs(r.imag))))

                        elif r.imag < 0:
                            comp.append(strip_string(
                                '- {:.4f}'.format(abs(r.imag))))

                else:
                    if r.imag > 0:
                        comp.append('+ ' + strip_string(b))

                    elif r.imag < 0:
                        comp.append('- ' + strip_string(b))

            if len(comp) == 2:
                strings.append('{} {}j'.format(comp[0], comp[1]))

            elif len(comp) == 1:
                if strip_string('{:.4f}'.format(r.real)) == '0' or strip_string('{:.4f}'.format(r.real)) == '-0':
                    strings.append('{}j'.format(comp[0]))

                else:
                    strings.append(str(comp[0]))

            elif len(comp) == 0:
                strings.append('0')

    return strings


def sign(n):
    return n >= 0


def print_solution(org_x, root_list, a):

    new = []
    for r in root_list:
        try:
            if sign(int(r)):
                new.append('- {}'.format(abs(int(r))))

            else:
                new.append('+ {}'.format(abs(int(r))))

        except ValueError:
            break

    if len(new) == len(root_list):
        if a == 1:

            print('\nThe factors are:')
            print('({} {})({} {})({} {})'.format(org_x, new[
                  0], org_x, new[1], org_x, new[2]))

    print('\nThe roots are approximately:')

    no_duplicute_roots = list(set(root_list))

    if len(no_duplicute_roots) == 3:
        print('{} = {} AND {} = {} AND {} = {}'.format(
            org_x, no_duplicute_roots[0], org_x, no_duplicute_roots[1], org_x, no_duplicute_roots[2]))

    elif len(no_duplicute_roots) == 2:
        print('{} = {} AND {} = {}'.format(
            org_x, no_duplicute_roots[0], org_x, no_duplicute_roots[1]))

    elif len(no_duplicute_roots) == 1:
        print('{} = {}'.format(org_x, no_duplicute_roots[0]))


def main():

    org_x, x, s = set_up()

    a, b, c, d = get_a_b_c_d(org_x, x, s)

    list_of_roots = get_roots(a, b, c, d)

    tidied_roots = tidy_roots(list_of_roots)

    print_solution(org_x, tidied_roots, a)

if __name__ == '__main__':
    main()
