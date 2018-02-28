import sys

print('(Hearts   = 1\n Diamonds = 2\n Spades   = 3\n Clubs    = 4)\n')
print('(Ace   = 1,\n 2     = 2,\n ..........,\n Jack  = 11,\n Queen = 12,\n King  = 13)\n')
print('Example Input:\n"1,1,2,1,13,4,6,2,3,4" = Ace-Hearts, Two-Hearts, King-Clubs, Six-Diamonds, Three-Clubs\n')
print('\nType out the cards in your hand:\n')

possible_hands = ['a royal flush', 'a straight flush', 'four of a kind',
                  'a full house', 'a flush', 'a straight', 'three of a kind',
                  'two pairs', 'one pair', 'nothing']


def repeat(cards):
    repeat = []

    for i in range(len(cards)):
        for j in range(len(cards)):
            if cards[i] == cards[j] and i != j:
                repeat.append(cards[i])

    return len(repeat)


def royal_flush(suits, cards):
    royals = [1, 13, 12, 11, 10]
    top_cards = []

    if flush(suits):
        for c in cards:
            if int(c) in royals:
                top_cards.append(int(c))

            else:
                return False

    return sorted(top_cards) == sorted(royals)


def straight_flush(suits, cards):
    return straight(cards) and flush(suits)


def four_of_a_kind(cards):
    return repeat(cards) >= 12


def full_house(cards):
    return repeat(cards) == 8


def flush(suits):
    i = 1
    while i < len(suits) and suits[i] == suits[i - 1]:
        i = i + 1

    return i == len(suits)


def straight(cards):
    smallest = int(cards[0])
    cards_wanted = ''

    for c in cards:
        if int(c) < int(smallest):
            smallest = int(c)

    for i in range(5):
        cards_wanted = cards_wanted + str(smallest + i)

    for c in cards:
        if c in cards_wanted:
            cards_wanted = cards_wanted.replace(c, '')

        else:
            return False

    return not cards_wanted


def three_of_a_kind(cards):
    return repeat(cards) == 6


def two_pairs(cards):
    return repeat(cards) == 4


def one_pair(cards):
    return repeat(cards) == 2


def call_functions(suits, cards):
    if royal_flush(suits, cards):
        print('This hand is {}'.format(possible_hands[0]))

    elif straight_flush(suits, cards):
        print('This hand is {}'.format(possible_hands[1]))

    elif four_of_a_kind(cards):
        print('This hand is {}'.format(possible_hands[2]))

    elif full_house(cards):
        print('This hand is {}'.format(possible_hands[3]))

    elif flush(suits):
        print('This hand is {}'.format(possible_hands[4]))

    elif straight(cards):
        print('This hand is {}'.format(possible_hands[5]))

    elif three_of_a_kind(cards):
        print('This hand is {}'.format(possible_hands[6]))

    elif two_pairs(cards):
        print('This hand is {}'.format(possible_hands[7]))

    elif one_pair(cards):
        print('This hand is {}'.format(possible_hands[8]))

    else:
        print('This hand is {}'.format(possible_hands[9]))


def main():
    for line in sys.stdin:
        line = line.strip().split(',')
        suits = line[::2]
        cards = line[1::2]
        call_functions(suits, cards)

if __name__ == '__main__':
    main()
