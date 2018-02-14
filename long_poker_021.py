import sys


total = {'rf_total': 0,
         'sf_total': 0,
         'foac_total': 0,
         'fh_total': 0,
         'f_total': 0,
         's_total': 0,
         'toac_total': 0,
         'tp_total': 0,
         'op_total': 0,
         'nothing_total': 0}


def royal_flush(suit, card):
    top_cards = [14, 13, 12, 11, 10]

    i = 1
    while i < len(suit) and suit[i] == suit[i - 1]:
        i = i + 1

    for c in card:
        if c in top_cards:
            top_cards.replace(c, '')

        else:
            return False

    return not top_cards


def straight_flush(suit, card):
     i = 1
    while i < len(suit) and suit[i] == suit[i - 1]:
        i = i + 1

    smallest = card[0]
    j = 1
    while j < len(card):
        if card[i] < smallest:
            smallest = card[i]

        j = j + 1

    cards_wanted = [smallest, smallest + 1, smallest + 2, smallest + 3, smallest + 4]

    for c in card:
        if c in cards_wanted:
            cards_wanted.replace(c, '')

        else:
            return False

    return not top_cards


def four_of_a_kind(suit, card):
    possible_cards = []
    i = 0
    while i < len(card) and len(possible_cards) <= 2:
        if card[i] not in possible_cards:
                possible_cards.append(c)
        i = i + 1

    if len(possible_cards) > 2:
        return False

    j = 0
    while j < len(possible_cards):
        l = 0
        while l < 4:
            if possible_cards[j] in card:
                card.replace(cards[j], '', 1)

            l = l + 1

        j = j + 1


def full_house(suit, card):
    possible_cards = []
    i = 0
    while i < len(card) and len(possible_cards) <= 2:
        if card[i] not in possible_cards:
                possible_cards.append(c)
        i = i + 1

    return len(possible_cards) > 2


def flush(suit, card):


def straight(suit, card):


def three_of_a_kind(suit, card):


def two_pairs(suit, card):


def one_pair(suit, card):


def call_functions(suit, card):
    if royal_flush(suit, card):
        total['rf_total'] = total['rf_total'] + royal_flush(suit, card)

    elif straight_flush(suit, card):
        total['sf_total'] = total['sf_total'] + straight_flush(suit, card)

    elif four_of_a_kind(suit, card):
        total['foac_total'] = total['foac_total'] + four_of_a_kind(suit, card)

    elif full_house():
        total['fh_total'] = total['fh_total'] + full_house(suit, card)

    elif flush(suit, card):
        total['f_total'] = total['f_total'] + flush(suit, card)

    elif straight(suit, card):
        total['s_total'] = total['s_total'] + straight(suit, card)

    elif three_of_a_kind(suit, card):
        total['toac_total'] = total['toac_total'] + three_of_a_kind(suit, card)

    elif two_pairs(suit, card):
        total['tp_total'] = total['tp_total'] + two_pairs(suit, card)

    elif one_pair(suit, card):
        total['op_total'] = total['op_total'] + one_pair(suit, card)

    else:
        total['nothing_total'] = total['nothing_total'] + 1

    return total


def main():
    for line in sys.stdin:
        line = line.strip().split(',')
        suits = line[::2]
        cards = line[1::2]
        totals = call_functions(suits, cards)


if __name__ == '__main__':
