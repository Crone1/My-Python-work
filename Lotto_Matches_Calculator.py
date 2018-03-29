import sys
import random

itterations = 100000000
matches = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

numbers = sys.argv[1:]
lucky_nums = []

for number in numbers:
    lucky_nums.append(int(number))

numbers = set(lucky_nums)

for i in range(itterations):
    lotto_numbers = random.sample(range(1,48), 6)

    draw = set(lotto_numbers)

    match = draw & numbers

    if len(match) > 1:
        matches[len(match)] += 1

try:
    prob_6 = str(itterations // matches[6])
    if len(prob_6) == 8:
        prob_6 = prob_6[:2] + ',' + prob_6[2:5] + ',' + prob_6[5:]

    if len(prob_6) == 7:
        prob_6 = prob_6[0] + ',' + prob_6[1:4] + ',' + prob_6[4:]

    elif len(prob_6) == 6:
        prob_6 =  prob_6[0:3] + ',' + prob_6[3:]

except ZeroDivisionError:
    prob_6 = '?'

try:
    prob_5 = str(itterations // matches[5])
    if len(prob_5) == 7:
        prob_5 = prob_5[0] + ',' + prob_5[1:4] + ',' + prob_5[4:]

    elif len(prob_5) == 6:
        prob_5 =  prob_5[0:3] + ',' + prob_5[3:]

    elif len(prob_5) == 5:
        prob_5 =  prob_5[0:2] + ',' + prob_5[2:]

except ZeroDivisionError:
    prob_5 = '?'

print('Number of times you got 2 Matches : {:>{}} => You have a 1 in {} chance'.format(
    matches[2], len(str(matches[2])), itterations // matches[2]))
print('Number of times you got 3 Matches : {:>{}} => You have a 1 in {} chance'.format(
    matches[3], len(str(matches[2])), itterations // matches[3]))
print('Number of times you got 4 Matches : {:>{}} => You have a 1 in {} chance'.format(
    matches[4], len(str(matches[2])), itterations // matches[4]))
print('Number of times you got 5 Matches : {:>{}} => You have a 1 in {} chance'.format(
    matches[5], len(str(matches[2])), prob_5))
print('Number of times you got 6 Matches : {:>{}} => You have a 1 in {} chance'.format(
    matches[6], len(str(matches[2])), prob_6))