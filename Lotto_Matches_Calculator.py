import sys
import random


def put_in_commas(num):
    if len(num) < 4:
        return num

    return str(put_in_commas(num[:-3])) + ',' + str(num[-3:])

print('\nHow many lotto simulations do you want to take place? (Input Below)')

itterations = int(input())

print('\nFrom a simulation of {} Lotto Draws, You got:'.format(
    put_in_commas(str(itterations))))

matches = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

numbers = sys.argv[1:]
lucky_nums = set()

for number in numbers:
    lucky_nums.add(int(number))

for i in range(itterations):
    lotto_numbers = set(random.sample(range(1, 48), 6))

    match = lotto_numbers & lucky_nums

    if len(match) > 1:
        matches[len(match)] += 1

prob = []
new_matches = []
for i in range(2, 7):
    try:
        prob.append(put_in_commas(str(itterations // matches[i])))

    except ZeroDivisionError:
        prob.append('?')

    finally:
        new_matches.append(put_in_commas(str(matches[i])))

        print('   {} Matches {:>{}} times => You have a 1 in {} chance of winning'.format(
            i, new_matches[i - 2], len(new_matches[0]), prob[i - 2]))
